#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a12_testDigits.py
@Time: 2020-04-09 16:33
@Last_update: 2020-04-09 16:33
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
from a10_loadImages import loadImages
from a6_kernelTrans import kernelTrans
from a8_smoK import smoP


def testDigits(kTup=('rbf', 10)):
    dataArr, labelArr = loadImages('data/Ch06/trainingDigits')
    b, alphas = smoP(dataArr, labelArr, C=200, toler=0.0001, maxIter=10000, kTup=kTup)
    datMat = mat(dataArr)
    labelMat = mat(labelArr).transpose()
    svInd = nonzero(alphas.A > 0)[0]
    sVs = datMat[svInd]
    labelSv = labelMat[svInd]
    print('there are %d Support Vectors' % shape(sVs)[0])
    m, n = shape(datMat)
    errorCount = 0
    for i in range(m):
        kernelEval = kernelTrans(sVs, datMat[i, :], kTup)
        predict = kernelEval.T * multiply(labelSv, alphas[svInd]) + b
        if sign(predict) != sign(labelArr[i]):
            errorCount += 1
    print('the training error rate is: %f' % (float(errorCount) / m))
    dataArr, labelArr = loadImages('data/Ch06/testDigits')
    errorCount = 0
    datMat = mat(dataArr)
    labelMat = mat(labelArr).transpose()
    m, n = shape(datMat)
    for i in range(m):
        kernelEval = kernelTrans(sVs, datMat[i, :], kTup)
        predict = kernelEval.T * multiply(labelSv, alphas[svInd]) + b
        if sign(predict) != sign(labelArr[i]):
            errorCount += 1
    print('the test error rate is: %f' % (float(errorCount) / m))


if __name__ == '__main__':
    testDigits(('rbf', 50))