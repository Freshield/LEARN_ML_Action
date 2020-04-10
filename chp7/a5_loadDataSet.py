#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a5_loadDataSet.py
@Time: 2020-04-10 18:01
@Last_update: 2020-04-10 18:01
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


def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t'))
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat - 1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))

    return dataMat, labelMat


if __name__ == '__main__':
    from a3_adaBoostTrainDS import adaBoostTrainDS
    from a4_adaClassify import adaClassify

    datArr, labelArr = loadDataSet('data/horseColicTraining2.txt')
    classifierArray = adaBoostTrainDS(datArr, labelArr, 50)

    testArr, testLabelArr = loadDataSet('data/horseColicTest2.txt')
    prediction10 = adaClassify(testArr, classifierArray)
    errArr = mat(ones((67, 1)))
    print(errArr[prediction10 != mat(testLabelArr).T].sum())