# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a4_recommend.py
@Time: 2020-06-28 14:39
@Last_update: 2020-06-28 14:39
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a3_svd_filter import *


def standEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]
    simTotal = 0.0
    ratSimTotal = 0.0

    for j in range(n):
        userRating = dataMat[user, j]
        if userRating == 0:
            continue

        overLap = nonzero(logical_and(dataMat[:, item].A > 0, dataMat[:, j].A > 0))[0]
        if len(overLap) == 0:
            similarity = 0
        else:
            similarity = simMeas(dataMat[overLap, item], dataMat[overLap, j])

        simTotal += similarity
        ratSimTotal += similarity * userRating

    if simTotal == 0:
        return 0
    else:
        return ratSimTotal / simTotal


def recommend(dataMat, user, N=3, simMeas=cosSim, estMethod=standEst):
    unratedItems = nonzero(dataMat[user, :].A == 0)[1]
    if len(unratedItems) == 0:
        return 'you rated everything'

    itemScores = []
    for item in unratedItems:
        estimatedScore = estMethod(dataMat, user, simMeas ,item)
        itemScores.append((item, estimatedScore))

    return sorted(itemScores, key=lambda jj: jj[1], reverse=True)[: N]


if __name__ == '__main__':
    myMat = mat(loadExData())
    myMat = mat([
        [4,4,0,2,2],
        [4,0,0,3,3],
        [4,0,0,1,1],
        [1,1,1,2,0],
        [2,2,2,0,0],
        [1,1,1,0,0],
        [5,5,5,0,0]
    ])
    print(myMat)
    print(recommend(myMat, 2))
    print(recommend(myMat, 2, simMeas=ecluidSim))
    print(recommend(myMat, 2, simMeas=pearsSim))