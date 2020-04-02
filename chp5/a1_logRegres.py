#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_logRegres.py
@Time: 2020-04-02 10:25
@Last_update: 2020-04-02 10:25
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
import random


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('data/Ch05/testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))

    return dataMat, labelMat


def sigmoid(inX):
    return 1.0 / (1+np.exp(-inX))


def gradAscent(dataMatIn, classLabels):
    # 100, 3
    dataMatrix = np.mat(dataMatIn)
    # 100, 1
    labelMat = np.mat(classLabels).transpose()
    m, n = dataMatrix.shape
    alpha = 0.001
    maxCycles = 500
    # 3, 1
    weights = np.ones((n, 1))
    for k in range(maxCycles):
        # 100, 1
        h = sigmoid(dataMatrix * weights)
        # 100, 1
        error = (labelMat - h)
        # 3, 1
        weights = weights + alpha * dataMatrix.transpose() * error

    return weights


def stocGradAscent0(dataMatrix, classLabels):
    dataMatrix = np.array(dataMatrix)
    m, n = dataMatrix.shape
    alpha = 0.01
    weights = np.ones(n)
    for i in range(m):
        h = sigmoid(np.sum(dataMatrix[i] * weights))
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]

    return weights


def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    dataMatrix = np.array(dataMatrix)
    m, n = np.shape(dataMatrix)
    weights = np.ones(n)
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4 / (1.0+j+i) + 0.01
            randIndex = int(random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(dataMatrix[randIndex] * weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del dataIndex[randIndex]

    return weights


def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat, labelMat = loadDataSet()
    dataArr = np.array(dataMat)
    n = dataArr.shape[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')

    x = np.arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    y = np.transpose(y)
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()
    plt.close()


if __name__ == '__main__':
    dataMat, labelMat = loadDataSet()
    # weights = gradAscent(dataMat, labelMat)
    # plotBestFit(weights)
    # weights = stocGradAscent0(dataMat, labelMat)
    # plotBestFit(weights)
    weights = stocGradAscent1(dataMat, labelMat)
    plotBestFit(weights)

    # data = np.array(dataMat[0])
    # label = labelMat[0]
    # weight1 = np.ones((3))
    # h1 = np.sum(sigmoid(data * weight1))
    # error1 = label - h1
    # grad1 = data * error1
    #
    #
    # weight2 = np.array([4.12,0.48,-0.61])
    # h2 = np.sum(sigmoid(data * weight2))
    # error2 = label - h2
    # grad2 = data * error2
    #
    # print(data)
    # print(label)
    # print(h1)
    # print(error1)
    # print(grad1)
    # print()
    # print(data)
    # print(label)
    # print(h2)
    # print(error2)
    # print(grad2)
