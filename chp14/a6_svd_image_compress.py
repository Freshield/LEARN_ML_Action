# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a6_svd_image_squeeze.py
@Time: 2020-06-28 16:47
@Last_update: 2020-06-28 16:47
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a5_svd_recommend import *


def printMat(inMat, thresh=0.8):
    for i in range(32):
        for k in range(32):
            if float(inMat[i,k]) > thresh:
                print(1, end='')
            else:
                print(0, end='')
        print('')


def imgCompress(numSV=3, thresh=0.8):
    myl = []
    for line in open('data/0_5.txt').readlines():
        newRow = []
        for i in range(32):
            newRow.append(int(line[i]))
        myl.append(newRow)

    myMat = mat(myl)
    print('****original matrix******')
    printMat(myMat, thresh)
    U, Sigma, VT = la.svd(myMat)

    SigRecon = mat(zeros((numSV, numSV)))
    for k in range(numSV):
        SigRecon[k,k] = Sigma[k]

    reconMat = U[:, :numSV] * SigRecon * VT[:numSV, :]

    print(f'****reconstructed matrix using {numSV} singular values******')
    printMat(reconMat, thresh)


if __name__ == '__main__':
    imgCompress(2)