#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_createDataSet.py
@Time: 2020-03-12 11:27
@Last_update: 2020-03-12 11:27
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def createDataSet():
    dataSet = [
        [1,1,'yes'],
        [1,1,'yes'],
        [1,0,'no'],
        [0,1,'no'],
        [0,1,'no']
    ]
    lables = ['no surfacing', 'flippers']

    return dataSet, lables
