#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_adaBoostTrainDS.py
@Time: 2020-04-10 16:48
@Last_update: 2020-04-10 16:48
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
from a2_stump import buildStump


def adaBoostTrainDS(dataArr, classLabels, numIt=40):
    """
    adaBoost的训练代码
    整体流程：
    1. 按照最大迭代数进行遍历
    2. 得到弱分类器
    3. 计算当前弱分类器的alpha值，alpha=0.5 * log((1-error) / error)
    4. 更新数据的权重D，D=D * exp(alpha) / sum(D)或D=D * exp(-alpha) / sum(D)
    5. 计算多个分类器的合并预测结果和错误率
    """
    weakClassArr = []
    m = shape(dataArr)[0]
    D = mat(ones((m, 1)) / m)
    aggClassEst = mat(zeros((m, 1)))
    # 1. 按照最大迭代数进行遍历
    for i in range(numIt):
        # 2. 得到弱分类器
        bestStump, error, classEst = buildStump(dataArr, classLabels, D)
        # print('D:', D.T)
        # 3. 计算当前弱分类器的alpha值，alpha=0.5 * log((1-error) / error)
        alpha = float(0.5 * log((1.0 - error) / max(error, 1e-16)))
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)
        # print('classEst: ', classEst.T)
        # 4. 更新数据的权重D，D=D * exp(alpha) / sum(D)或D=D * exp(-alpha) / sum(D)
        # 这里用-1 * alpha * label * predict是因为这样可以自动计算是否为正确分类
        # 如果label=1，pred=1或label=-1，pred=-1，-1 * label * pred * alpha = -alpha
        # 如果label=1，pred=-1或label=-1，pred=1，-1 * label * pred * alpha = alpha
        expon = multiply(-1 * alpha * mat(classLabels).T, classEst)
        D = multiply(D, exp(expon))
        D = D / D.sum()
        # 5. 计算多个分类器的合并预测结果和错误率
        aggClassEst += alpha * classEst
        # print('aggClassEst: ', aggClassEst.T)
        aggError = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m, 1)))
        errorRate = aggError.sum() / m
        print('total error: ', errorRate, '\n')
        if errorRate == 0.0:
            break

    return weakClassArr, aggClassEst


if __name__ == '__main__':
    from a1_loadSimpData import loadSimpData

    datMat, classLabels = loadSimpData()
    classifierArray = adaBoostTrainDS(datMat, classLabels, 9)