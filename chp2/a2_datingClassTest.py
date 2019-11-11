#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_datingClassTest.py
@Time: 2019-11-10 15:18
@Last_update: 2019-11-10 15:18
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a1_kNN import classify0
from a2_m1_file2matrix import file2matrix
from a2_m3_auto_norm import autoNorm


def datingClassTest(filename):
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix(filename)
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print('the classifier came back with: %d, the real answer is: %d' % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0

    print('the total error rate is: %f' % (errorCount/float(numTestVecs)))


if __name__ == '__main__':
    filename = 'data/datingTestSet2.txt'
    datingClassTest(filename)