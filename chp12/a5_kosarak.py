# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a5_kosarak.py
@Time: 2020-06-18 17:49
@Last_update: 2020-06-18 17:49
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a4_mineTree import *

parseDat = [line.split() for line in open('data/kosarak.dat').readlines()]

initSet = createInitSet(parseDat)

myFPtree, myHeaderTab = createTree(initSet, 100000)

myFreqList = []

mineTree(myFPtree, myHeaderTab, 100000, set([]), myFreqList)

print(myFreqList)
print(len(myFreqList))