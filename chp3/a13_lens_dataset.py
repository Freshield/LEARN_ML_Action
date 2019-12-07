#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a13_lens_dataset.py
@Time: 2019-12-06 10:44
@Last_update: 2019-12-06 10:44
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a6_createTree import createTree
from a10_plotTree import createPlot

data_path = 'data/lenses.txt'

with open(data_path, 'r') as fr:
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]

lesesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = createTree(lenses, lesesLabels)

print(lensesTree)
createPlot(lensesTree)