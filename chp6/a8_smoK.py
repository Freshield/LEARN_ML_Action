#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a8_smoK.py
@Time: 2020-04-09 13:36
@Last_update: 2020-04-09 13:36
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
from a6_kernelTrans import optStruct
from a7_kernel_func import innerL


def smoP(dataMatIn, classLabels, C, toler, maxIter, kTup=('lin', 0)):
    oS = optStruct(np.mat(dataMatIn), np.mat(classLabels).transpose(), C, toler, kTup)
    iter = 0
    entireSet = True
    alphaPairsChanged = 0
    # 推出条件：iter大于maxIter 或者 遍历整个集合都未对任意alpha对进行修改
    while (iter < maxIter) and ((alphaPairsChanged > 0) or (entireSet)):
        alphaPairsChanged = 0
        if entireSet:
            for i in range(oS.m):
                alphaPairsChanged += innerL(i, oS)
                print('fullSet, iter: %d i:%d, pairs changed %d' % (iter, i, alphaPairsChanged))
            iter += 1
        else:
            # 找到所有大于0小于C的值，也就是非边界值
            nonBoundIs = np.nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
            for i in nonBoundIs:
                alphaPairsChanged += innerL(i, oS)
                print('non-bound, iter: %d i:%d, pairs changed %d' % (iter, i, alphaPairsChanged))
            iter += 1
        # 如果遍历过一遍所有的值则换回遍历非边界值模式
        if entireSet:
            entireSet = False
        # 如果没有更改alpha则换回遍历所有的值
        elif alphaPairsChanged == 0:
            entireSet = True
            print('iteration number: %d' % iter)

    return oS.b, oS.alphas


if __name__ == '__main__':
    data_path = 'data/Ch06/testSet.txt'
    from a1_svmMLiA import loadDataSet
    from a6_kernelTrans import kernelTrans

    dataMat, labelMat = loadDataSet(data_path)
    b, alphas = smoP(dataMat, labelMat, C=0.6, toler=0.001, maxIter=40, kTup=('rbf', 1.3))
    datMat = np.mat(dataMat)
    labelMat = np.mat(labelMat).transpose()
    # 得到alphas中非零部分，也就是支持向量
    svInd = np.nonzero(alphas.A > 0)[0]
    # 得到数据中的支持向量
    # k, n
    sVs = datMat[svInd]
    # k
    labelSV = labelMat[svInd]
    print('there are %d Support Vectors' % np.shape(sVs)[0])
    m, n = np.shape(datMat)
    i = 1
    # 进行核化
    kernelEval = kernelTrans(sVs, datMat[i, :], ('rbf', 1.3))
    # ki * yi * alpha + b
    predict = kernelEval.T * np.multiply(labelSV, alphas[svInd]) + b

    print(predict)
    print(labelMat[i])
