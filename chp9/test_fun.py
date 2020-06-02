# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: test_fun.py
@Time: 2020-06-02 16:48
@Last_update: 2020-06-02 16:48
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def test_fun():
    print('here')
    print(test_fun.test)


def test_fun2():
    print('here1')
    print(test_fun2.test)


if __name__ == '__main__':
    test_fun.test = 1
    test_fun()
    print(test_fun2())