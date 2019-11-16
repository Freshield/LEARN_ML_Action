#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_classify_person.py
@Time: 2019-11-11 15:30
@Last_update: 2019-11-11 15:30
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import numpy as np
from a2_m1_file2matrix import file2matrix
from a2_m3_auto_norm import autoNorm
from a1_kNN import classify0


def classifyPerson(filename):
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input('percentage of time spend playing video games?'))
    ffMiles = float(input('frequent flier miles earned per year?'))
    iceCream = float(input('liters of ice cream consumed per year?'))
    datingDataMat, datingLabels = file2matrix(filename)
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = np.array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)
    print('You will probably like this person: ', resultList[classifierResult - 1])



if __name__ == '__main__':
    filename = 'data/datingTestSet2.txt'
    classifyPerson(filename)