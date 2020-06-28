# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_svdRec.py
@Time: 2020-06-28 10:40
@Last_update: 2020-06-28 10:40
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


def loadExData():
    return [[1,1,1,0,0],
            [2,2,2,0,0],
            [1,1,1,0,0],
            [5,5,5,0,0],
            [1,1,0,2,2],
            [0,0,0,3,3],
            [0,0,0,1,1]]


if __name__ == '__main__':
    Data = loadExData()
    U, Sigma, VT = linalg.svd(Data)

    print(Sigma)
    Sig3 = mat([[Sigma[0],0,0],
                  [0,Sigma[1],0],
                  [0,0,Sigma[2]]])
    rst = U[:, :3] * Sig3 * VT[:3, :]
    print(rst)