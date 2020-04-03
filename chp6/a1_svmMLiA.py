#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_svmMLiA.py
@Time: 2020-04-03 15:25
@Last_update: 2020-04-03 15:25
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import random


def loadDataSet(fileName):
    # 读取数据，x0, x1, label
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))

    return dataMat, labelMat


def selectJrand(i, m):
    # 从0, m中选出一个不等于i的数值
    # i为alpha的下标, m为alpha的数目
    j = i
    while j == i:
        print(j)
        j = int(random.uniform(0, m))
        print(j)

    return j


def clipAlpha(aj, H, L):
    # 用H, L来限定aj的值
    # 让aj小于H且大于L
    if aj > H:
        aj = H

    if L > aj:
        aj = L

    return aj


if __name__ == '__main__':
    data_path = 'data/Ch06/testSet.txt'
    dataMat, labelMat = loadDataSet(data_path)
    print(labelMat)