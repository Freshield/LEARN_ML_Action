#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a9_getTreeDepth.py
@Time: 2020-03-14 17:30
@Last_update: 2020-03-14 17:30
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1

        if thisDepth > maxDepth:
            maxDepth = thisDepth

    return maxDepth


if __name__ == '__main__':
    tree = {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
    print(getTreeDepth(tree))
