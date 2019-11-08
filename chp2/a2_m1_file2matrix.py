#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_m1_file2matrix.py
@Time: 2020-03-11 14:42
@Last_update: 2020-03-11 14:42
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


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = np.zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(listFromLine[-1])
        index += 1

    return returnMat, classLabelVector


if __name__ == '__main__':
    file_path = 'data/datingTestSet2.txt'
    file2matrix(file_path)