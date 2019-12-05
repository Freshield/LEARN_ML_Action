#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a11_classify.py
@Time: 2020-03-17 09:54
@Last_update: 2020-03-17 09:54
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def classify(inputTree, featLabels, testVec):
    # 得到判断点
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    # 得到判断点的label索引
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        # 得到判断点索引的值
        if testVec[featIndex] == key:
            # 如果不是叶节点
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]

    return classLabel


def retrieveTree(i):
    listOfTrees =[{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                  {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                  ]
    return listOfTrees[i]


if __name__ == '__main__':
    from a2_createDataSet import createDataSet
    myDat, labels = createDataSet()
    tree = retrieveTree(0)
    print(classify(tree, labels, [1,0]))
    print(classify(tree, labels, [1,1]))
