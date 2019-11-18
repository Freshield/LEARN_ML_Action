#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_handwritingClassTest.py
@Time: 2019-11-17 15:55
@Last_update: 2019-11-17 15:55
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import os
import numpy as np
from a3_m1_img2vector import img2vector
from a1_kNN import classify0


def handwritingClassTest(file_dir, test_dir):
    hwLabels = []
    trainingFileList = os.listdir(file_dir)
    m = len(trainingFileList)
    trainingMat = np.zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector(os.path.join(file_dir, fileNameStr))

    testFileList = os.listdir(test_dir)
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector(os.path.join(test_dir, fileNameStr))
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print('the classifier came back with: %d, the real answer is: %d' % (classifierResult, classNumStr))
        if (classifierResult != classNumStr):
            errorCount += 1.0

    print('\nthe total number of errors is : %d' % errorCount)
    print('\nthe total error rate is: %f' % (errorCount/float(mTest)))


if __name__ == '__main__':
    train_dir = '/media/freshield/SSD_1T/LEARN_ML_Action/chp2/data/trainingDigits'
    test_dir = '/media/freshield/SSD_1T/LEARN_ML_Action/chp2/data/testDigits'
    handwritingClassTest(train_dir, test_dir)