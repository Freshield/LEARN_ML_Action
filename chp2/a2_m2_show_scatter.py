#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_m2_show_scatter.py
@Time: 2019-11-08 14:49
@Last_update: 2019-11-08 14:49
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def show_scatter(datingDataMat, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1],
               15.0 * np.array(labels), 15.0 * np.array(labels))
    plt.show()
    plt.close()


if __name__ == '__main__':
    from a2_m1_file2matrix import file2matrix
    file_path = 'data/datingTestSet2.txt'
    datingDataMat, labels = file2matrix(file_path)
    print(datingDataMat.shape)
    print(len(labels))
    print(datingDataMat[0])
    print(labels[0])
    show_scatter(datingDataMat, labels)