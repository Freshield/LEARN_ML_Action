# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_ascendTree.py
@Time: 2020-06-18 17:18
@Last_update: 2020-06-18 17:18
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a2_createTree import *


def ascendTree(leafNode: treeNode, prefixPath: list):
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)


def findPrefixPath(basePat, treeNode):
    condPats = dict()
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink

    return condPats


if __name__ == '__main__':
    dataSet = loadSimpDat()
    dataSet = createInitSet(dataSet)
    print(dataSet)
    retTree, headerTable = createTree(dataSet, minSup=3)
    print(headerTable)
    print(findPrefixPath('x', headerTable['r'][1]))