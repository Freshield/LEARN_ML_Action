#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: rss_test.py
@Time: 2020-03-18 10:33
@Last_update: 2020-03-18 10:33
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import random
import operator
import feedparser
from spamTest import textParse
from bayes import createVocabList
from bagOfWords2Vec import bagOfWords2Vec
from trainNB0 import trainNB0
from testNB import classifyNB


def calcMostFreq(vocabList, fullText):
    freqDict = {}
    for token in vocabList:
        freqDict[token] = fullText.count(token)
    sortedFreq = sorted(freqDict.items(), key=operator.itemgetter(1), reverse=True)

    return sortedFreq[: 30]


def localWords(feed1, feed0):
    docList = []
    classList = []
    fullText = []
    minLen = min(len(feed1['entries']), len(feed0['entries']))

    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    top30Words = calcMostFreq(vocabList, fullText)
    for pairW in top30Words:
        if pairW[0] in vocabList:
            vocabList.remove(pairW[0])

    trainingSet = list(range(2*minLen))
    testSet = []
    for i in range(20):
        randomIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randomIndex])
        del trainingSet[randomIndex]
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(trainMat, trainClasses)
    errorCount = 0
    for docIndex in testSet:
        wordVector = bagOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(wordVector, p0V, p1V, pSpam) != classList[docIndex]:
            print(docList[docIndex])
            errorCount += 1
    print('the error rate is: ', float(errorCount)/len(testSet))
    return vocabList, p0V, p1V



if __name__ == '__main__':
    feed0 = feedparser.parse('http://www.nasa.gov/rss/dyn/image_of_the_day.rss')
    feed1 = feedparser.parse('http://sports.yahoo.com/nba/teams/hou/rss.xml')

    localWords(feed1, feed0)
