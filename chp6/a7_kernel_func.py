#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: kernel_func.py
@Time: 2020-04-09 13:34
@Last_update: 2020-04-09 13:34
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import numpy as np
from a1_svmMLiA import clipAlpha, selectJrand
from a6_kernelTrans import optStruct


def calcEk(oS: optStruct, k):
    """计算Ek的值"""
    fXk = float(np.multiply(oS.alphas, oS.labelMat).T * oS.K[:, k]) + oS.b
    Ek = fXk - float(oS.labelMat[k])

    return Ek


def updateEk(oS, k):
    Ek = calcEk(oS, k)
    oS.eCache[k] = [1, Ek]


def selectJ(i, oS: optStruct, Ei):
    """
    这里是选择J的函数，通过选择具有最大步长的j来进行返回
    a2new = a2old + (y2(E1 - E2)) / eta
    这里找的就是最大的E1 - E2
    """
    maxK = -1
    maxDeltaE = 0
    Ej = 0
    # 设置为有效
    oS.eCache[i] = [1, Ei]
    # 得到eCache中还没有设置为有效的值
    validEcacheList = np.nonzero(oS.eCache[:, 0].A)[0]
    # 6. 选择对应的j元素，计算fx和Ej
    if (len(validEcacheList)) > 1:
        for k in validEcacheList:
            if k == i:
                continue
            Ek = calcEk(oS, k)
            deltaE = abs(Ei - Ek)
            if deltaE > maxDeltaE:
                maxK = k
                maxDeltaE = deltaE
                Ej = Ek
        return maxK, Ej
    else:
        j = selectJrand(i, oS.m)
        Ej = calcEk(oS, j)

    return j, Ej


def innerL(i, oS: optStruct):
    # 4. 计算i的fx和Ei
    Ei = calcEk(oS, i)
    # 5. 判断KKT条件是否满足，如果不满足则继续优化
    if ((oS.labelMat[i]*Ei < -oS.tol) and (oS.alphas[i] < oS.C)) or \
            ((oS.labelMat[i]*Ei > oS.tol) and (oS.alphas[i] > 0)):
        # 6. 选择对应的j元素，计算fx和Ej
        j, Ej = selectJ(i, oS, Ei)
        alphaIold = oS.alphas[i].copy()
        alphaJold = oS.alphas[j].copy()
        # 7. 得到L和H

        if oS.labelMat[i] != oS.labelMat[j]:
            L = max(0, oS.alphas[j] - oS.alphas[i])
            H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
        else:
            L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
            H = min(oS.C, oS.alphas[j] + oS.alphas[i])
        if L == H:
            print('L==H')
            return 0

        eta = 2.0 * oS.K[i, j] - oS.K[i, i] - oS.K[j, j]
        if eta >= 0:
            print('eta>=0')
            return 0
        # 8. 更新a2的值
        oS.alphas[j] -= oS.labelMat[j] * (Ei - Ej)/eta
        oS.alphas[j] = clipAlpha(oS.alphas[j], H, L)
        updateEk(oS, j)

        if (abs(oS.alphas[j]) - alphaJold) < 0.00001:
            print('j not moving enough')
            return 0
        # 9. 更新a1
        oS.alphas[i] += oS.labelMat[j] * oS.labelMat[i] * (alphaJold - oS.alphas[j])
        updateEk(oS, i)
        # 10. 更新b
        b1 = oS.b - Ei - \
             oS.labelMat[i] * (oS.alphas[i]-alphaIold) * oS.K[i, i] - \
             oS.labelMat[j] * (oS.alphas[j]-alphaJold) * oS.K[i, j]
        b2 = oS.b - Ej - \
             oS.labelMat[i] * (oS.alphas[i]-alphaIold) * oS.K[i, j] - \
             oS.labelMat[j] * (oS.alphas[j]-alphaJold) * oS.K[j, j]
        if (0 < oS.alphas[i]) and (oS.C > oS.alphas[i]):
            oS.b = b1
        elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[j]):
            oS.b = b2
        else:
            oS.b = (b1 + b2) / 2.0

        return 1
    else:
        return 0
