#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_calcShannonEnt.py
@Time: 2020-03-12 11:23
@Last_update: 2020-03-12 11:23
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from math import log


def calcShannonEnt(dataSet):
    numEntries = len(dataSet)