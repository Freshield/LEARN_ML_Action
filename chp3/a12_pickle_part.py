#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a12_pickle_part.py
@Time: 2019-12-05 10:05
@Last_update: 2019-12-05 10:05
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import pickle


def storeTree(inputTree, filename):
    fw = open(filename, 'wb')
    pickle.dump(inputTree, fw)
    fw.close()


def grabTree(filename):
    fr = open(filename, 'rb')
    return pickle.load(fr)


if __name__ == '__main__':
    from a11_classify import retrieveTree
    tree = retrieveTree(0)
    storeTree(tree, 'data/classifierStorage.txt')
    tree = grabTree('data/classifierStorage.txt')
    print(tree)