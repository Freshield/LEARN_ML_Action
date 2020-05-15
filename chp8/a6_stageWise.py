# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a6_stageWise.py
@Time: 2020-05-15 10:46
@Last_update: 2020-05-15 10:46
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
from a4_abalone import rssError


def stageWise(xArr, yArr, eps=0.01, numIt=100):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    yMat = yMat - yMean
    xMeans = mean(xMat, 0)
    xVar = var(xMat, 0)
    xMat = (xMat - xMeans) / xVar
    m, n = shape(xMat)
    returnMat = zeros((numIt, n))
    ws = zeros((n, 1))
    wsMax = ws.copy()
    for i in range(numIt):
        print(ws.T)
        lowestError = inf
        for j in range(n):
            for sign in [-1, 1]:
                wsTest = ws.copy()
                wsTest[j] += eps*sign
                yTest = xMat * wsTest
                rssE = rssError(yMat.A, yTest.A)
                if rssE < lowestError:
                    lowestError = rssE
                    wsMax = wsTest

        ws = wsMax.copy()
        returnMat[i, :] = ws.T

    return returnMat


if __name__ == '__main__':
    from a1_loadDataSet import loadDataSet
    from a2_standRegres import standRegres
    from a3_lwlr import lwlrTest
    import matplotlib.pyplot as plt

    filename = 'data/abalone.txt'
    xArr, yArr = loadDataSet(filename)
    weights = stageWise(xArr, yArr, 0.001, 5000)
    print(weights)

    xMat = mat(xArr)
    yMat = mat(yArr).T
    xMeans = mean(xMat, 0)
    xVar = var(xMat, 0)
    xMat = (xMat - xMeans) / xVar
    yM = mean(yMat, 0)
    yMat = yMat - yM
    weights = standRegres(xMat, yMat.T)
    print(weights.T)