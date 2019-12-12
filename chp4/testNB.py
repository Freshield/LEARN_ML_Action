#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: testNB.py
@Time: 2019-12-11 17:20
@Last_update: 2019-12-11 17:20
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
from bayes import loadDataSet, createVocabList, setOfWords2Vec
from trainNB0 import trainNB0


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    # 通过log把乘法问题变成了加法问题
    # 通过相乘去除了不存在的词
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    tesDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(tesDoc, p0V, p1V, pAb))
    testEntry = ['stupid', 'garbage']
    tesDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(tesDoc, p0V, p1V, pAb))



if __name__ == '__main__':
    testingNB()