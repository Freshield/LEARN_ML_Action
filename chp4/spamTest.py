#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: spamTest.py
@Time: 2019-12-13 17:45
@Last_update: 2019-12-13 17:45
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import re
import random
from numpy import *
from bayes import createVocabList, setOfWords2Vec
from trainNB0 import trainNB0
from testNB import classifyNB
import traceback
from bagOfWords2Vec import bagOfWords2Vec


def textParse(bigString):
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


def spamTest():
    docList = []
    classList = []
    fullText = []
    for i in range(1, 26):
        try:
            wordList = textParse(open('data/Ch04/email/spam/%d.txt' % i).read())
            docList.append(wordList)
            fullText.extend(wordList)
            classList.append(1)
            wordList = textParse(open('data/Ch04/email/ham/%d.txt' % i).read())
            docList.append(wordList)
            fullText.extend(wordList)
            classList.append(0)
        except Exception as e:
            print(str(e))
            traceback.print_exc()
            print(i)
            exit()
    vocabList = createVocabList(docList)
    trainingSet = list(range(50))
    testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del trainingSet[randIndex]
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
            print(docList[docIndex])
    print('the error rate is: ', float(errorCount)/len(testSet))


if __name__ == '__main__':
    spamTest()