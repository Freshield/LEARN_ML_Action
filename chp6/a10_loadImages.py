#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a10_loadImages.py
@Time: 2020-04-09 16:19
@Last_update: 2020-04-09 16:19
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
from a11_img2vector import img2vector

def loadImages(dirName):
   from os import listdir
   hwLables = []
   trainingFileList = listdir(dirName)
   m = len(trainingFileList)
   trainingMat = zeros((m, 1024))
   for i in range(m):
       fileNameStr = trainingFileList[i]
       fileStr = fileNameStr.split('.')[0]
       classNumStr = int(fileStr.split('_')[0])
       if classNumStr == 9:
           hwLables.append(-1)
       else:
           hwLables.append(1)

       trainingMat[i, :] = img2vector('%s/%s' % (dirName, fileNameStr))

   return trainingMat, hwLables