# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: compare.py
@Time: 2020-06-02 15:04
@Last_update: 2020-06-02 15:04
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from model import *


def regTreeEval(model, inDat):
    return float(model)


def modelTreeEval(model, inDat):
    n = shape(inDat)[1]
    X = mat(ones((1, n+1)))
    X[:, 1: n+1] = inDat

    return float(X * model)


def treeForeCast(tree, inData, modelEval=regTreeEval):
    if not isTree(tree):
        return modelEval(tree, inData)

    if inData[tree['spInd']] > tree['spVal']:
        if isTree(tree['left']):
            return treeForeCast(tree['left'], inData, modelEval)
        else:
            return modelEval(tree['left'], inData)
    else:
        if isTree(tree['right']):
            return treeForeCast(tree['right'], inData, modelEval)
        else:
            return modelEval(tree['right'], inData)


def createForecast(tree, testData, modelEval=regTreeEval):
    m = len(testData)
    yHat = mat(zeros((m, 1)))
    for i in range(m):
        yHat[i, 0] = treeForeCast(tree, mat(testData[i]), modelEval)

    return yHat


if __name__ == '__main__':
    trainMat = mat(loadDataSet('data/bikeSpeedVsIq_train.txt'))
    testMat = mat(loadDataSet('data/bikeSpeedVsIq_test.txt'))
    myTree = createTree(trainMat, regLeaf, regErr, (1, 20))
    yHat = createForecast(myTree, testMat[:, 0], regTreeEval)
    print(corrcoef(yHat, testMat[:, 1], rowvar=0)[0, 1])

    myTree = createTree(trainMat, modelLeaf, modelErr, (1, 20))
    yHat = createForecast(myTree, testMat[:, 0], modelTreeEval)
    print(corrcoef(yHat, testMat[:, 1], rowvar=0)[0, 1])

    ws, X, Y = linearSolve(trainMat)
    for i in range(shape(testMat)[0]):
        yHat[i] = testMat[i, 0] * ws[0, 0]
    print(corrcoef(yHat, testMat[:, 1], rowvar=0)[0, 1])