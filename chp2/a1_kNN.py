#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: kNN.py
@Time: 2020-03-11 11:36
@Last_update: 2020-03-11 11:36
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
import operator

def createDataSet():
    group = array([[1., 1.1], [1., 1.], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    #计算距离
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5

    # 得到排序索引
    sortedDistIndicies = distances.argsort()
    # 得到前k个数据的索引字典
    classCount = dict()
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # 进行排序并转换为tuple的list
    sortedClassCount = sorted(classCount.items(), key=lambda x: x[1], reverse=True)

    return sortedClassCount[0][0]


if __name__ == '__main__':
    group, labels = createDataSet()
    print(group)
    print(labels)
    value = classify0([0,0], group, labels, 3)
    print(value)