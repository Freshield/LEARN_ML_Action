#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: test_feedparse.py
@Time: 2020-03-18 10:23
@Last_update: 2020-03-18 10:23
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import feedparser
nasa = feedparser.parse('http://www.nasa.gov/rss/dyn/image_of_the_day.rss')
yahoo = feedparser.parse('http://sports.yahoo.com/nba/teams/hou/rss.xml')

print(yahoo['entries'])