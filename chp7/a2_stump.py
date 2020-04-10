#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_stump.py
@Time: 2020-04-10 14:28
@Last_update: 2020-04-10 14:28
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


def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
    """
    把dataMatrix的dimen维，进行threshIneq比较方法和threshVal比较后的值都设置为-1
    """
    retArray = ones((shape(dataMatrix)[0], 1))
    if threshIneq == 'lt':
        retArray[dataMatrix[:, dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:, dimen] > threshVal] = -1.0

    return retArray


def buildStump(dataArr, classLabels, D):
    """
    建立树桩，得到最好的树桩
    整体流程：
    1. 遍历所有的特征
    2. 因为是数值型数据，所以要在最大值和最小值中间按步长切分开
    3. 遍历所有步长的值，这里的步长的值相当于是分割的阈值
    4. 根据阈值遍历大于小于两种分割逻辑来把数据分为正反例
    5. 根据特征索引，步长阈值，分割逻辑得到所有预测的结果
    6. 根据数据的权重D计算错误率，并更新来得到错误率最小的树桩
    """
    dataMatrix = mat(dataArr)
    labelMat = mat(classLabels).T
    m, n = shape(dataMatrix)
    numSteps = 10.0
    bestStump = {}
    bestClasEst = mat(zeros((m, 1)))
    minError = inf
    # 1. 遍历所有的特征
    for i in range(n):
        # 2. 因为是数值型数据，所以要在最大值和最小值中间按步长切分开
        rangeMin = dataMatrix[:, i].min()
        rangeMax = dataMatrix[:, i].max()
        stepSize = (rangeMax - rangeMin) / numSteps
        # 3. 遍历所有步长的值，这里的步长的值相当于是分割的阈值
        for j in range(-1, int(numSteps) + 1):
            # 4. 根据阈值遍历大于小于两种分割逻辑来把数据分为正反例
            for inequal in ['lt', 'gt']:
                threshVal = (rangeMin + float(j) * stepSize)
                # 5. 根据特征索引，步长阈值，分割逻辑得到所有预测的结果
                predictedVals = stumpClassify(dataMatrix, i, threshVal, inequal)
                # 6. 根据数据的权重D计算错误率，并更新来得到错误率最小的树桩
                errArr = mat(ones((m, 1)))
                errArr[predictedVals == labelMat] = 0
                weightedError = D.T * errArr
                # print('split: dim %d, thresh %.2f, thresh inequal: %s, the weighted error is %.3f' % (
                #     i, threshVal, inequal, weightedError))

                if weightedError < minError:
                    minError = weightedError
                    bestClasEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal

    # print('bestone: split: dim %d, thresh %.2f, thresh inequal: %s, the weighted error is %.3f' % (
    #     bestStump['dim'], bestStump['thresh'], bestStump['ineq'], minError))

    return bestStump, minError, bestClasEst


if __name__ == '__main__':
    from a1_loadSimpData import loadSimpData

    datMat, classLabels = loadSimpData()
    D = mat(ones((5, 1))/ 5)
    bestStump, minError, bestClasEst = buildStump(datMat, classLabels, D)