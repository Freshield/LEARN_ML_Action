# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_test_svd.py
@Time: 2020-06-28 10:39
@Last_update: 2020-06-28 10:39
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from numpy import *

U, Sigma, VT = linalg.svd([[1, 1], [7, 7]])

print(U)
print(Sigma)
print(VT)