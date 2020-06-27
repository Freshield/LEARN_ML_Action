# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_svg_filter.py
@Time: 2020-06-28 11:59
@Last_update: 2020-06-28 11:59
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a2_svdRec import *
from numpy import linalg as la


def ecluidSim(inA, inB):
    return 1.0 / (1.0 + la.norm(inA - inB))


def pearsSim(inA, inB):
    if len(inA) < 3:
        return 1.0

    return 0.5 + 0.5 * corrcoef(inA, inB, rowvar=0)[0][1]


def cosSim(inA, inB):
    num = float(inA.T * inB)
    denom = la.norm(inA) * la.norm(inB)

    return 0.5 + 0.5 * (num / denom)


if __name__ == '__main__':
    myMat = mat(loadExData())
    print(ecluidSim(myMat[:, 0], myMat[:, 4]))
    print(ecluidSim(myMat[:, 0], myMat[:, 0]))

    print(cosSim(myMat[:, 0], myMat[:, 4]))
    print(cosSim(myMat[:, 0], myMat[:, 0]))

    print(pearsSim(myMat[:, 0], myMat[:, 4]))
    print(pearsSim(myMat[:, 0], myMat[:, 0]))
