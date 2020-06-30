# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_reducer.py
@Time: 2020-06-30 15:29
@Last_update: 2020-06-30 15:29
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import sys
from numpy import mat, mean, power


def read_input(file):
    for line in file:
        yield line.rstrip()


input = read_input(sys.stdin)
mapperOut = [line.split('\t') for line in input]
cumVal = 0.0
cumSumSq = 0.0
cumN = 0.0
for instance in mapperOut:
    nj = float(instance[0])
    cumN += nj
    cumVal += nj * float(instance[1])
    cumSumSq += nj * float(instance[2])

mean = cumVal / cumN
varSum = (cumSumSq - 2 * mean * cumVal + cumN * mean * mean) / cumN
print('%d\t%f\t%f' % (cumN, mean, varSum))
print('report: still alive', file=sys.stderr)