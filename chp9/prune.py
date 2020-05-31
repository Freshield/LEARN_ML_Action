# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: prune.py
@Time: 2020-06-02 12:17
@Last_update: 2020-06-02 12:17
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from regTrees import *


def isTree(obj):
    return type(obj) is dict


def getMean(tree):
    if isTree(tree['right']): tree['right'] = getMean(tree['right'])
    if isTree(tree['left']): tree['left'] = getMean(tree['left'])

    return (tree['left'] + tree['right']) / 2.0


def prune(tree, testData):
    if shape(testData)[0] == 0: return getMean(tree)

    if isTree(tree['right']) or isTree(tree['left']):
        lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])

    if isTree(tree['left']): tree['left'] = prune(tree['left'], lSet)
    if isTree(tree['right']): tree['right'] = prune(tree['right'], rSet)

    if (not isTree(tree['left'])) and (not isTree(tree['right'])):
        lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])

        errorNoMerge = sum(power(lSet[:, -1] - tree['left'], 2) + sum(
            power(rSet[:, -1] - tree['right'], 2)))
        treeMean = (tree['left'] + tree['right']) / 2.0
        errorMerge = sum(power(testData[:, -1] - treeMean, 2))

        if errorMerge < errorNoMerge:
            print('merging')
            return treeMean
        else:
            return tree
    else:
        return tree


if __name__ == '__main__':
    myDat2 = loadDataSet('data/ex2.txt')
    print(myDat2)
    myMat2 = mat(myDat2)
    tree2 = createTree(myMat2, ops=(0, 1))
    print(tree2)

    myDatTest = loadDataSet('data/ex2test.txt')
    myDatTest = mat(myDatTest)
    tree2 = prune(tree2, myDatTest)
    print(tree2)