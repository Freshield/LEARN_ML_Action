# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_createTree.py
@Time: 2020-06-18 16:30
@Last_update: 2020-06-18 16:30
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a1_treeNode import *


def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat


def createInitSet(dataSet):
    retDict = dict()
    for trans in dataSet:
        retDict[frozenset(trans)] = 1

    return retDict


def createTree(dataSet, minSup=1):
    headerTable = dict()
    # 遍历每条
    for trans in dataSet:
        # 遍历每个元素
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]

    # 去除小于最小支持度的
    for k in list(headerTable.keys()):
        if headerTable[k] < minSup:
            del(headerTable[k])

    freqItemSet = set(headerTable.keys())
    if len(freqItemSet) == 0:
        return None, None

    for k in headerTable:
        headerTable[k] = [headerTable[k], None]

    reTree = treeNode('Null Set', 1, None)
    for tranSet, count in dataSet.items():
        localD = dict()
        for item in tranSet:
            if item in freqItemSet:
                localD[item] = headerTable[item][0]

        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(
                localD.items(), key=lambda p: p[1], reverse=True)]

            updateTree(orderedItems, reTree, headerTable, count)

    return reTree, headerTable


def updateTree(items, inTree: treeNode, headerTable, count):
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count)
    # 如果当前元素不在children中
    else:
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None:
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])

    if len(items) > 1:
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)


def updateHeader(nodeToTest, targetNode):
    while nodeToTest.nodeLink != None:
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode


if __name__ == '__main__':
    dataSet = loadSimpDat()
    dataSet = createInitSet(dataSet)
    print(dataSet)
    retTree, headerTable = createTree(dataSet, minSup=3)