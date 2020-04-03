#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_smoSimple.py
@Time: 2020-04-03 15:38
@Last_update: 2020-04-03 15:38
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
from a1_svmMLiA import selectJrand, clipAlpha


def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    """
    smo的优化过程
    :param dataMatIn: 输入的特征的矩阵
    :param classLabels: 输入的label的矩阵
    :param C: 松弛变量
    :param toler: 容错率
    :param maxIter: 最大的迭代数
    :return:
    整体流程：
    1. 准备相关矩阵和值
    2. 按照迭代数迭代
    3. 遍历所有数据

    """
    # 1. 准备相关矩阵和值
    # 特征数据(m, n)
    dataMatrix = np.mat(dataMatIn)
    # label数据(m, 1)
    labelMat = np.mat(classLabels).transpose()
    b = 0
    m, n = np.shape(dataMatrix)
    # alphas(m, 1)
    alphas = np.mat(np.zeros((m, 1)))
    iter = 0
    # 2. 按照迭代数迭代
    while iter < maxIter:
        # 看alpha的值是否变化
        alphaPairsChanged = 0
        # 3. 遍历所有数据
        for i in range(m):
            # np.multiply(alphas, labelMat).T：alphas中的每个值和label的值相乘(1, 100)
            # dataMatrix*dataMatrix[i, :].T：当前第i个数据数据和所有的训练数据分别相乘(100, 1)
            # 把前两个矩阵相乘再加上b
            # 相当于dataMatrix所有数据都乘以dataMatrix[i]然后再乘以自己对应的label再乘alpha加b，最后求和
            # 是第i个数据预测的类别
            fXi = float(np.multiply(alphas, labelMat).T * (dataMatrix*dataMatrix[i, :].T)) + b

            # 等同
            # dataMatrix = np.array(dataMatrix)
            # labelMat = np.array(labelMat)
            # labelMat = np.squeeze(labelMat)
            # alphas = np.array(alphas)
            # alphas = np.squeeze(alphas)
            # fXi = np.sum(np.sum(dataMatrix * dataMatrix[i], axis=1) * alphas * labelMat) + b
            # 把得到的fXi和label进行相减对比
            # 得到的是误差Ei
            Ei = fXi - float(labelMat[i])

            # 当这个数据的label*Ei小于负的容错率且这个数据的alpha小于C 或者
            # 当这个数据的label*Ei大于正的容错率且这个数据的alpha大于0时
            # 用来判别此数据是否可以被优化
            # label*Ei是为了调整正负，这里是说如果误差很大，那么开始对alpha进行优化
            # 同时还要保证alpha不在0或者C上
            if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or \
                    ((labelMat[i]*Ei > toler) and (alphas[i]>0)):
                # 随机选择另一个数据向量，得到这个向量的误差Ej
                j = selectJrand(i, m)
                fXj = float(np.multiply(alphas, labelMat).T * (dataMatrix*dataMatrix[j, :].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                # 开始计算L和H，用于浆alpha[j]调整到0到C之间
                # 保证alpha在0，C之间
                if (labelMat[i] != labelMat[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] -C)
                    H = min(C, alphas[j] + alphas[i])

                if L == H:
                    print('L==H')
                    continue

                # eta是alpha[j]的最优修改量
                eta = 2.0 * dataMatrix[i, :] * dataMatrix[i, :].T - \
                      dataMatrix[j, :] * dataMatrix[j, :].T
                if eta >= 0:
                    print('eta>=0')
                    continue

                # 得到新的alpha[j]，如果变化太小则退出
                alphas[j] -= labelMat[j] * (Ei - Ej) / eta
                alphas[j] = clipAlpha(alphas[j], H, L)
                if (np.abs(alphas[j] - alphaJold) < 0.00001):
                    print('j not moving enough')
                    continue

                # 对alpha[i]同样进行修改，不过方向相反
                alphas[i] += labelMat[j] * labelMat[i] * (alphaJold - alphas[j])
                b1 = b - Ei - \
                     labelMat[i] * (alphas[i] - alphaIold) * dataMatrix[i, :] * dataMatrix[i, :].T - \
                     labelMat[j] * (alphas[j] - alphaJold) * dataMatrix[i, :] * dataMatrix[j, :].T
                b2 = b - Ej - \
                     labelMat[i] * (alphas[i] - alphaIold) * dataMatrix[i, :] * dataMatrix[j, :].T - \
                     labelMat[j] * (alphas[j] - alphaJold) * dataMatrix[j, :] * dataMatrix[j, :].T

                if (0 < alphas[i]) and (C > alphas[i]):
                    b = b1
                elif (0 < alphas[j]) and (C > alphas[j]):
                    b = b2
                else:
                    b = (b1 + b2) / 2.0

                alphaPairsChanged += 1
                print('iter: %d i: %d, pairs changed %d' % (iter, i, alphaPairsChanged))

        if alphaPairsChanged == 0:
            iter += 1
        else:
            iter = 0
        print('iteration number: %d' % iter)

    return b, alphas





if __name__ == '__main__':
    data_path = 'data/Ch06/testSet.txt'
    from a1_svmMLiA import loadDataSet

    dataMat, labelMat = loadDataSet(data_path)
    b, alphas = smoSimple(dataMat, labelMat, 0.6, 0.001, 40)