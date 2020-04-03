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
    dataMatrix = np.mat(np.random.randn(m, n))
    labelMat = np.mat(np.random.randn(m, 1))
    alphas = np.mat(np.random.randn(m, 1))
    # 2. 按照迭代数迭代
    while iter < maxIter:
        alphaPairsChanged = 0
        # 3. 遍历所有数据
        for i in range(m):
            print(np.multiply(alphas, labelMat).T.shape)
            print(dataMatrix.shape)
            print(dataMatrix[i,:].shape)
            # np.multiply(alphas, labelMat).T：alphas中的每个值和label的值相乘(1, 100)
            # dataMatrix*dataMatrix[i, :].T：当前第i个数据数据和所有的训练数据分别相乘(100, 1)
            # 把前两个矩阵相乘再加上b
            # 相当于dataMatrix所有数据都乘以dataMatrix[i]然后再乘以自己对应的label再乘alpha加b，最后求和
            fXi = float(np.multiply(alphas, labelMat).T * (dataMatrix*dataMatrix[i, :].T)) + b

            # 等同
            # dataMatrix = np.array(dataMatrix)
            # labelMat = np.array(labelMat)
            # labelMat = np.squeeze(labelMat)
            # alphas = np.array(alphas)
            # alphas = np.squeeze(alphas)
            # fXi = np.sum(np.sum(dataMatrix * dataMatrix[i], axis=1) * alphas * labelMat) + b
            # 把得到的fXi和label进行相减对比
            Ei = fXi - float(labelMat[i])

            # 当这个数据的label*Ei小于负的容错率且这个数据的alpha小于C 或者
            # 当这个数据的label*Ei大于正的容错率且这个数据的alpha大于0时
            if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or \
                    ((labelMat[i]*Ei > toler) and (alphas[i]>0)):
                pass



if __name__ == '__main__':
    data_path = 'data/Ch06/testSet.txt'
    from a1_svmMLiA import loadDataSet

    dataMat, labelMat = loadDataSet(data_path)
    smoSimple(dataMat, labelMat, 1, 1, 100)