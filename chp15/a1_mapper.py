# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_mapper.py
@Time: 2020-06-30 15:23
@Last_update: 2020-06-30 15:23
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
input = [float(line) for line in input]
numInputs = len(input)
input = mat(input)
sqInput = power(input, 2)

print('%d\t%f\t%f' % (numInputs, mean(input), mean(sqInput)))
print('report: still alive', file=sys.stderr)