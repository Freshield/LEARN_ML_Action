#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_calcShannonEnt.py
@Time: 2020-03-12 11:23
@Last_update: 2020-03-12 11:23
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from math import log


def calcShannonEnt(dataSet):
    # 一共有多少数据
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1

    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)

    return shannonEnt


if __name__ == '__main__':
    from a2_createDataSet import createDataSet
    dataSet, labels = createDataSet()
    # dataSet[0][-1] = 'maybe'
    print(dataSet)
    print(labels)
    shannonEnt = calcShannonEnt(dataSet)
    print(shannonEnt)