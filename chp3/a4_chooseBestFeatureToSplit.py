#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a4_chooseBestFeatureToSplit.py
@Time: 2019-11-28 14:12
@Last_update: 2019-11-28 14:12
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a1_calcShannonEnt import calcShannonEnt
from a3_splitDataSet import splitDataSet


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        # 得到某个feature的所有出现的值
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            # 计算每个切分后的子集的熵
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i

    return bestFeature




if __name__ == '__main__':
    from a2_createDataSet import createDataSet
    myDat, labels = createDataSet()
    print(myDat)
    bestFeature = chooseBestFeatureToSplit(myDat)
    print(bestFeature)