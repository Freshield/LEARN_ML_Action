# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_clusterClubs.py
@Time: 2020-06-09 16:54
@Last_update: 2020-06-09 16:54
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a2_biKmeans import *


def distSLC(vecA, vecB):
    a = sin(vecA[0, 1] * pi / 180) * sin(vecB[0, 1] * pi / 180)
    b = cos(vecA[0, 1] * pi / 180) * cos(vecB[0, 1] * pi / 180) * cos((vecB[0, 0] - vecA[0, 0]) / 180)

    return arccos(a + b) * 6371.0


import matplotlib
import matplotlib.pyplot as plt


def clusterClubs(numClust=5):
    datList = []
    for line in open('data/places.txt').readlines():
        lineArr = line.split('\t')
        datList.append([float(lineArr[4]), float(lineArr[3])])
    dataMat = mat(datList)
    myCentroids, clustAssing = biKmeans(dataMat, numClust, distMeas=distSLC)

    fig = plt.figure()
    rect = [0.1, 0.1, 0.8, 0.8]
    scatterMarkers = ['s', 'o', '^', '8', 'p',
                      'd', 'v', 'h', '>', '<']
    axprops = dict(xticks=[], yticks=[])
    ax0 = fig.add_axes(rect, label='ax0', **axprops)
    imgP = plt.imread('data/Portland.png')
    ax0.imshow(imgP)
    ax1 = fig.add_axes(rect, label='ax1', frameon=False)
    for i in range(numClust):
        ptsInCurrCluster = dataMat[nonzero(clustAssing[:, 0].A == i)[0], :]
        markerStyle = scatterMarkers[i % len(scatterMarkers)]
        ax1.scatter(ptsInCurrCluster[:, 0].flatten().A[0],
                    ptsInCurrCluster[:, 1].flatten().A[0],
                    marker=markerStyle, s=90)

    ax1.scatter(myCentroids[:, 0].flatten().A[0],
                myCentroids[:, 1].flatten().A[0], marker='+', s=300)
    plt.show()


if __name__ == '__main__':
    clusterClubs(5)