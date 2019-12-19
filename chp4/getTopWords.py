#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: getTopWords.py
@Time: 2020-03-18 11:05
@Last_update: 2020-03-18 11:05
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import operator
import feedparser
from rss_test import localWords


def getTopWords(ny, sf):
    vocbList, p0V, p1V = localWords(ny, sf)
    topNY = []
    topSF = []
    for i in range(len(p0V)):
        if p0V[i] > -6.0:
            topSF.append((vocbList[i], p0V[i]))
        if p1V[i] > -6.0:
            topNY.append((vocbList[i], p1V[i]))
    sortedSf = sorted(topSF, key=lambda pair: pair[1], reverse=True)
    print('SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**')
    for item in sortedSf[:30]:
        print(item)
    sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)
    print('NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**')
    for item in sortedNY[:30]:
        print(item)


if __name__ == '__main__':
    feed0 = feedparser.parse('http://www.nasa.gov/rss/dyn/image_of_the_day.rss')
    feed1 = feedparser.parse('http://sports.yahoo.com/nba/teams/hou/rss.xml')
    getTopWords(feed1, feed0)