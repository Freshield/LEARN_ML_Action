#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_m1_img2vector.py
@Time: 2019-11-16 15:48
@Last_update: 2019-11-16 15:48
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import numpy as np


def img2vector(filename):
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])

    return returnVect


if __name__ == '__main__':
    filename = '/media/freshield/SSD_1T/LEARN_ML_Action/chp2/data/trainingDigits/0_13.txt'
    data_array = img2vector(filename)
    print(data_array[0,0:31])