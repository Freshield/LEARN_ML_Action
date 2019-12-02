#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a6_createTree.py
@Time: 2019-12-01 14:52
@Last_update: 2019-12-01 14:52
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a5_majorityCnt import majorityCnt
from a4_chooseBestFeatureToSplit import chooseBestFeatureToSplit
from a3_splitDataSet import splitDataSet


def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    # 如果类别全部相同, 返回类别
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # 如果遍历完所有特征，这里是1是label
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    # 得到最好的feature
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    # 构造树
    myTree = {bestFeatLabel: {}}
    # 去除label，否则顺序会对不上
    del labels[bestFeat]

    # 遍历feature所有的值，来构建子树
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)

    return myTree


if __name__ == '__main__':
    from a2_createDataSet import createDataSet
    myDat, labels = createDataSet()
    print(myDat)
    myTree = createTree(myDat, labels)
    print(myTree)