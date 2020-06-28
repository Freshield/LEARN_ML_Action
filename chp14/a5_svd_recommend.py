# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a5_svd_recommend.py
@Time: 2020-06-28 14:59
@Last_update: 2020-06-28 14:59
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a4_recommend import *


def loadExData2():
    return[[0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
           [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
           [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
           [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
           [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
           [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
           [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
           [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
           [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
           [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
           [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]]


def svdEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]
    simTotal = 0.0
    ratSimTotal = 0.0
    U, Sigma, VT = la.svd(dataMat)
    Sig4 = mat(eye(4) * Sigma[:4])
    xformedItems = dataMat.T * U[:, :4] * Sig4.I
    for j in range(n):
        userRating = dataMat[user, j]

        if userRating == 0 or j == item:
            continue

        similarity = simMeas(xformedItems[item, :].T, xformedItems[j, :].T)

        print(f'the {item} and {j} similarity is: {similarity}')
        simTotal += similarity
        ratSimTotal += similarity * userRating

    if simTotal == 0:
        return 0
    else:
        return ratSimTotal / simTotal


if __name__ == '__main__':
    U, Sigma, VT = la.svd(mat(loadExData2()))
    print(Sigma)
    Sig2 = Sigma ** 2
    print(sum(Sig2))
    print(sum(Sig2)*0.9)
    print(sum(Sig2[:3]))
    myMat = mat(loadExData())
    print(recommend(myMat, 1, estMethod=svdEst))