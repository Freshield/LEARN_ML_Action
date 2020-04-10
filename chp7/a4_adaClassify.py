#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a4_adaClassify.py
@Time: 2020-04-10 17:43
@Last_update: 2020-04-10 17:43
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
from a2_stump import stumpClassify


def adaClassify(datToClass, classifierArr):
    dataMatrix = mat(datToClass)
    m = shape(dataMatrix)[0]
    aggClassEst = mat(zeros((m, 1)))
    for i in range(len(classifierArr)):
        classEst = stumpClassify(dataMatrix, classifierArr[i]['dim'],
                                 classifierArr[i]['thresh'],
                                 classifierArr[i]['ineq'])
        aggClassEst += classifierArr[i]['alpha'] * classEst
        print(aggClassEst)

    return sign(aggClassEst)


if __name__ == '__main__':
    from a1_loadSimpData import loadSimpData
    from a3_adaBoostTrainDS import adaBoostTrainDS

    datArr, labelArr = loadSimpData()
    classifierArr = adaBoostTrainDS(datArr, labelArr, numIt=30)
    pred = adaClassify([[5, 5], [0, 0]], classifierArr)
    print(pred)