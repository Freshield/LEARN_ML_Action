# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_loadDataSet.py
@Time: 2020-05-14 17:10
@Last_update: 2020-05-14 17:10
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
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))

    return dataMat, labelMat


if __name__ == '__main__':
    filename = 'data/ex0.txt'
    dataMat, labelMat = loadDataSet(filename)
    print(dataMat)
    print(labelMat)