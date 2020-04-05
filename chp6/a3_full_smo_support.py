#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_full_smo_support.py
@Time: 2020-04-07 17:09
@Last_update: 2020-04-07 17:09
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
from a1_svmMLiA import selectJrand


class optStruct:
    def __init__(self, dataMatIn, classLabels, C, toler):
        self.X = dataMatIn
        self.labelMat = classLabels
        self.C = C
        self.tol = toler
        self.m = np.shape(dataMatIn)[0]
        self.alphas = np.mat(np.zeros((self.m, 1)))
        self.b = 0
        self.eCache = np.mat(np.zeros((self.m, 2)))


def calcEk(oS: optStruct, k):
    """计算Ek的值"""
    fXk = float(np.multiply(oS.alphas, oS.labelMat).T * (oS.X * oS.X[k, :].T)) + oS.b
    Ek = fXk - float(oS.labelMat[k])

    return Ek


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


def updateEk(oS, k):
    Ek = calcEk(oS, k)
    oS.eCache[k] = [1, Ek]


if __name__ == '__main__':
    a = np.array([[0,1],[1,0],[2,0],[3,2]])
    print(a)
    print(a.shape)
    print(np.nonzero(a[:, 0]))