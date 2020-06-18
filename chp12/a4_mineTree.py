# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a4_mineTree.py
@Time: 2020-06-18 17:26
@Last_update: 2020-06-18 17:26
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a3_ascendTree import *


def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    bigL = [v[0] for v in sorted(
        headerTable.items(), key=lambda p: p[0])]

    for basePat in bigL:
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headerTable[basePat][1])
        myCondTree, myHead = createTree(condPattBases, minSup)

        if myHead != None:
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)


if __name__ == '__main__':
    dataSet = loadSimpDat()
    dataSet = createInitSet(dataSet)
    print(dataSet)
    retTree, headerTable = createTree(dataSet, minSup=3)
    print(headerTable)
    freqItems = []
    mineTree(retTree, headerTable, 3, set([]), freqItems)
    print(freqItems)