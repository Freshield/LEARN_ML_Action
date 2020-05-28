# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: regTrees.py
@Time: 2020-05-28 17:55
@Last_update: 2020-05-28 17:55
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
    """读取数据集"""
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)
        dataMat.append(fltLine)

    return dataMat


def binSplitDataSet(dataSet, feature, value):
    mat0 = dataSet[nonzero(dataSet[:, feature] > value)[0], :]
    mat1 = dataSet[nonzero(dataSet[:, feature] <= value)[0], :]

    return mat0, mat1


def regLeaf():
    pass

def regErr():
    pass

def chooseBestSplit(dataSet, leafType, errType, ops):
    pass

def createTree(dataSet, leafType=regLeaf, errType=regErr, ops=(1, 4)):
    feat, val = chooseBestSplit(dataSet, leafType, errType, ops)
    if feat is None:
        return val
    retTree = dict()
    retTree['spInd'] = feat
    retTree['spVal'] = val
    lSet, rSet = binSplitDataSet(dataSet, feat, val)
    retTree['left'] = createTree(lSet, leafType, errType, ops)
    retTree['right'] = createTree(rSet, leafType, errType, ops)

    return retTree


if __name__ == '__main__':
    testMat = mat(eye(4))
    print(testMat)
    mat0, mat1 = binSplitDataSet(testMat, 1, 0.5)
    print(mat0)
    print(mat1)