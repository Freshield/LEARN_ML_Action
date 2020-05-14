# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a4_abalone.py
@Time: 2020-05-14 22:03
@Last_update: 2020-05-14 22:03
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


def rssError(yArr, yHatArr):
    return ((yArr-yHatArr)**2).sum()


if __name__ == '__main__':
    from a1_loadDataSet import loadDataSet
    from a2_standRegres import standRegres
    from a3_lwlr import lwlrTest
    filename = 'data/abalone.txt'
    abX, abY = loadDataSet(filename)
    yHat01 = lwlrTest(abX[:99], abX[:99], abY[:99], 0.1)
    yHat1 = lwlrTest(abX[:99], abX[:99], abY[:99], 1)
    yHat10 = lwlrTest(abX[:99], abX[:99], abY[:99], 10)
    print(rssError(abY[:99], yHat01.T))
    print(rssError(abY[:99], yHat1.T))
    print(rssError(abY[:99], yHat10.T))
    yHat01 = lwlrTest(abX[100:199], abX[:99], abY[:99], 0.1)
    yHat1 = lwlrTest(abX[100:199], abX[:99], abY[:99], 1)
    yHat10 = lwlrTest(abX[100:199], abX[:99], abY[:99], 10)
    print(rssError(abY[100:199], yHat01.T))
    print(rssError(abY[100:199], yHat1.T))
    print(rssError(abY[100:199], yHat10.T))

    ws = standRegres(abX[:99], abY[:99])
    yHat = mat(abX[100:199]) * ws
    print(rssError(abY[100:199], yHat.T.A))