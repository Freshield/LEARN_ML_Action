# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a5_ridgeRegres.py
@Time: 2020-05-14 22:28
@Last_update: 2020-05-14 22:28
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from numpy import *


def ridgeRegres(xMat, yMat, lam=0.2):
    xTx = xMat.T * xMat
    denom = xTx + eye(shape(xMat)[1]) * lam
    if linalg.det(denom) == 0.0:
        print('This matrix is singular, cannot do inverse')
        return None

    ws = denom.I * (xMat.T * yMat)
    return ws


def ridgeTest(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    yMat = yMat - yMean
    xMeans = mean(xMat, 0)
    xVar = var(xMat, 0)
    xMat = (xMat - xMeans) / xVar
    numTestPts = 30
    wMat = zeros((numTestPts, shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRegres(xMat, yMat, exp(i-10))
        wMat[i, :] = ws.T

    return wMat


if __name__ == '__main__':
    from a1_loadDataSet import loadDataSet
    from a2_standRegres import standRegres
    from a3_lwlr import lwlrTest
    import matplotlib.pyplot as plt

    filename = 'data/abalone.txt'
    abX, abY = loadDataSet(filename)
    ridgeWeights = ridgeTest(abX, abY)
    print(ridgeWeights)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(ridgeWeights)
    # ax.plot([[1,2,3],[1,2,3],[2,3,4],[1,2,3]])
    plt.show()