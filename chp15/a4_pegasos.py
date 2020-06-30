# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a4_pegasos.py
@Time: 2020-06-30 16:34
@Last_update: 2020-06-30 16:34
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from numpy import *


def predict(w, x):
    return w * x.T


def batchPegasos(dataSet, labels, lam, T, k):
    m, n = shape(dataSet)
    w = zeros(n)

    dataIndex = list(range(m))

    for t in range(1, T+1):
        wDelta = mat(zeros(n))
        eta = 1.0 / (lam * t)
        random.shuffle(dataIndex)
        for j in range(k):
            i = dataIndex[j]
            p = predict(w, dataSet[i, :])
            if labels[i] * p < 1:
                wDelta += labels[i] * dataSet[i, :].A

        w = (1.0 - 1/t) * w + (eta / k) * wDelta

    return w