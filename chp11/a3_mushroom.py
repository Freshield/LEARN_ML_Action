# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_mushroom.py
@Time: 2020-06-11 14:52
@Last_update: 2020-06-11 14:52
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a2_rules import *


mushDatSet = [line.split() for line in open('data/mushroom.dat').readlines()]

L, supportData = apriori(mushDatSet, minSupport=0.3)

for item in L[3]:
    if item.intersection('2'):
        print(item)