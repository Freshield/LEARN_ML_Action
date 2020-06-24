# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_real_world_test.py
@Time: 2020-06-24 14:36
@Last_update: 2020-06-24 14:36
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a1_pca import *


def replaceNanWithMean():
    datMat = loadDataSet('data/secom.data', ' ')
    numFeat = shape(datMat)[1]
    for i in range(numFeat):
        meanVal = mean(datMat[nonzero(~isnan(datMat[:, i].A))[0], i])
        datMat[nonzero(isnan(datMat[:, i].A))[0], i] = meanVal

    return datMat


if __name__ == '__main__':
    dataMat = replaceNanWithMean()

    meanVals = mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals

    covMat = cov(meanRemoved, rowvar=0)

    eigvals, eigVects = linalg.eig(mat(covMat))

    print(eigvals)
