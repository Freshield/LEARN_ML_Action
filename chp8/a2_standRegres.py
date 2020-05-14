# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_standRegres.py
@Time: 2020-05-14 17:16
@Last_update: 2020-05-14 17:16
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
import numpy as np


def standRegres(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    xTx = xMat.T * xMat
    if np.linalg.det(xTx) == 0.0:
        print('This matrix is singular, cannot do inverse')
        return None
    ws = xTx.I * (xMat.T * yMat)

    return ws


if __name__ == '__main__':
    from a1_loadDataSet import loadDataSet
    import matplotlib.pyplot as plt
    filename = 'data/ex0.txt'
    dataMat, labelMat = loadDataSet(filename)
    print(dataMat)
    print(labelMat)
    ws = standRegres(dataMat, labelMat)
    print(ws)
    xMat = mat(dataMat)
    yMat = mat(labelMat)
    yHat = xMat * ws

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten().A[0])
    xCopy = xMat.copy()
    xCopy.sort(0)
    yHatp = xCopy*ws
    ax.plot(xCopy[:,1], yHatp)
    plt.show()

    print(corrcoef(yHat.T, yMat))