# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: model.py
@Time: 2020-06-02 14:49
@Last_update: 2020-06-02 14:49
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from prune import *


def linearSolve(dataSet):
    m, n = shape(dataSet)
    X = mat(ones((m, n)))
    Y = mat(ones((m, 1)))
    X[:, 1: n] = dataSet[:, 0: n-1]
    Y = dataSet[:, -1]
    xTx = X.T * X
    if linalg.det(xTx) == 0.0:
        raise NameError('This matrix is singular, cannot do inverse, \n try increasing the second value of ops')
    ws = xTx.I * (X.T * Y)
    return ws, X, Y


def modelLeaf(dataSet):
    ws, X, Y = linearSolve(dataSet)

    return ws


def modelErr(dataSet):
    ws, X, Y = linearSolve(dataSet)
    yHat = X * ws

    return sum(power(Y - yHat, 2))


if __name__ == '__main__':
    myMat2 = mat(loadDataSet('data/exp2.txt'))
    tree = createTree(myMat2, modelLeaf, modelErr)

    print(tree)