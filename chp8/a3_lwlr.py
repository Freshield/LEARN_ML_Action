# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_lwlr.py
@Time: 2020-05-14 17:58
@Last_update: 2020-05-14 17:58
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


def lwlr(testPoint, xArr, yArr, k=1.0):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye(m))
    for j in range(m):
        diffMat = testPoint - xMat[j, :]
        weights[j, j] = exp(diffMat*diffMat.T / (-2.0*k**2))

    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:
        print('This matrix is singular, cannot do inverse')
        return None

    ws = xTx.I * (xMat.T * (weights * yMat))

    return testPoint * ws


def lwlrTest(testArr, xArr, yArr, k=1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)

    return yHat


if __name__ == '__main__':
    from a1_loadDataSet import loadDataSet

    filename = 'data/ex0.txt'
    xArr, yArr = loadDataSet(filename)
    print(xArr)
    print(yArr)
    print(yArr[0])
    print(lwlr(xArr[0], xArr, yArr, 1.0))
    print(lwlr(xArr[0], xArr, yArr, 0.01))
    
    yHat = lwlrTest(xArr, xArr, yArr, 0.01)
    xMat = mat(xArr)
    srtInd = xMat[:, 1].argsort(0)
    xSort = xMat[srtInd][:, 0, :]

    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xSort[:, 1], yHat[srtInd])
    ax.scatter(xMat[:, 1].flatten().A[0], mat(yArr).T.flatten().A[0], s=2, c='red')
    plt.show()
    