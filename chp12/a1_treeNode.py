# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_treeNode.py
@Time: 2020-06-15 18:00
@Last_update: 2020-06-15 18:00
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class treeNode(object):
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode
        self.children = {}

    def inc(self, numOccur):
        self.count += numOccur

    def disp(self, ind=1):
        print('    ' * ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind+1)