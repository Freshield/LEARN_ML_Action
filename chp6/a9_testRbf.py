#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a9_testRbf.py
@Time: 2020-04-09 13:38
@Last_update: 2020-04-09 13:38
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
from a1_svmMLiA import loadDataSet
from a6_kernelTrans import kernelTrans
from a8_smoK import smoP
# from data.Ch06.svmMLiA import smoP


def testRbf(k1=1.3):
    # 得到原始数据dataArr, labelArr
    dataArr, labelArr = loadDataSet('data/Ch06/testSetRBF.txt')
    # 训练网络
    b, alphas = smoP(dataArr, labelArr, C=200, toler=0.0001, maxIter=10000, kTup=('rbf', k1))
    datMat = np.mat(dataArr)
    labelMat = np.mat(labelArr).transpose()
    # 得到alphas中非零部分，也就是支持向量
    svInd = np.nonzero(alphas.A > 0)[0]
    # 得到数据中的支持向量
    # k, n
    sVs = datMat[svInd]
    # k
    labelSV = labelMat[svInd]
    print('there are %d Support Vectors' % np.shape(sVs)[0])
    m, n = np.shape(datMat)
    errorCount = 0
    for i in range(m):
        # 进行核化
        kernelEval = kernelTrans(sVs, datMat[i,:], ('rbf', k1))
        # ki * yi * alpha + b
        predict = kernelEval.T * np.multiply(labelSV, alphas[svInd]) + b
        if np.sign(predict) != np.sign(labelArr[i]):
            errorCount += 1
    print('the training error rate is: %f' % (float(errorCount) / m))

    dataArr, labelArr = loadDataSet('data/Ch06/testSetRBF2.txt')
    datMat = np.mat(dataArr)
    labelMat = np.mat(labelArr).transpose()
    errorCount = 0
    for i in range(m):
        # 进行核化
        kernelEval = kernelTrans(sVs, datMat[i, :], ('rbf', k1))
        # ki * yi * alpha + b
        predict = kernelEval.T * np.multiply(labelSV, alphas[svInd]) + b
        if np.sign(predict) != np.sign(labelArr[i]):
            errorCount += 1
    print('the test error rate is: %f' % (float(errorCount) / m))


if __name__ == '__main__':
    testRbf(0.1)