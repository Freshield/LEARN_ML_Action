# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a8_crossValidation.py
@Time: 2020-05-15 13:11
@Last_update: 2020-05-15 13:11
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
from numpy import *
from a6_stageWise import rssError
from a5_ridgeRegres import ridgeTest


def crossValidation(xArr, yArr, numVal=10):
    m = len(yArr)
    indexList = list(range(m))
    errorMat = zeros((numVal, 30))
    print(xArr.shape)
    print(yArr.shape)
    # valid的次数
    for i in range(numVal):
        trainX = []
        trainY = []
        testX = []
        testY = []
        random.shuffle(indexList)
        # for j in range(m):
        #     if j < m * 0.9:
        #         trainX.append(xArr[indexList[j]][0])
        #         trainY.append(yArr[indexList[j]][0])
        #     else:
        #         testX.append(xArr[indexList[j]][0])
        #         testY.append(yArr[indexList[j]][0])
        trainX = xArr[indexList[:int(m*0.9)]]
        trainY = yArr[indexList[:int(m*0.9)]].T
        testX = xArr[indexList[int(m*0.9):]]
        testY = yArr[indexList[int(m*0.9):]].T
        wMat = ridgeTest(trainX, trainY)
        # 遍历所有30次的岭回归的结果参数
        for k in range(30):
            matTestX = mat(testX)
            matTrainX = mat(trainX)
            meanTrain = mean(matTrainX, 0)
            varTrain = var(matTrainX, 0)
            matTestX = (matTestX - meanTrain) / varTrain
            yEst = matTestX * mat(wMat[k, :]).T + mean(trainY)
            errorMat[i, k] = rssError(yEst.T.A, array(testY))

    meanErrors = mean(errorMat, 0)
    minMean = float(min(meanErrors))
    bestWeights = wMat[nonzero(meanErrors==minMean)]
    xMat = mat(xArr)
    yMat = mat(yArr).T
    meanX = mean(xMat, 0)
    varX = var(xMat, 0)
    unReg = bestWeights/varX
    print('the best model from Ridge Regression is:\n', unReg)
    print('with constanct term: ', -1*sum(multiply(meanX, unReg)) + mean(yMat))



if __name__ == '__main__':
    from a7_searchForSet import setDataCollect

    retX = []
    retY = []
    setDataCollect(retX, retY)
    # lgX1 = mat(ones((63, 5)))
    # lgX1[:, 1:] = mat(retX)
    lgX1 = mat(retX)
    lgY = mat(retY).T
    crossValidation(lgX1, lgY, 10)