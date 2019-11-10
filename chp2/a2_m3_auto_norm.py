#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_m3_auto_norm.py
@Time: 2019-11-09 15:02
@Last_update: 2019-11-09 15:02
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


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(dataSet.shape)
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals




if __name__ == '__main__':
    from a2_m1_file2matrix import file2matrix
    file_path = 'data/datingTestSet2.txt'
    datingDataMat, labels = file2matrix(file_path)
    datingDataMat, ranges, minVals = autoNorm(datingDataMat)
    print(ranges)
    print(minVals)

    print(datingDataMat)