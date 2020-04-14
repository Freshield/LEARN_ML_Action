#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a6_plotROC.py
@Time: 2020-04-14 15:38
@Last_update: 2020-04-14 15:38
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


def plotROC(predStrengths, classLabels):
    """
    画ROC曲线
    这里predStrengths是预测的结果，classLabels为标签的值列表

    """
    import matplotlib.pyplot as plt
    cur = (1.0, 1.0)
    # 计算auc用
    ySum = 0.0
    # 一共有多少正例
    numPosClas = sum(array(classLabels) == 1.0)
    # y轴的步长，也就是正例的个数
    yStep = 1 / float(numPosClas)
    # x轴的步长，也就是反例的个数
    xStep = 1 / float(len(classLabels) - numPosClas)

    # 得到预测值的从小到大排序顺序索引
    sortedIndicies = predStrengths.argsort()


    # 画线是从右往左画的
    fig = plt.figure()
    fig.clf()
    ax = plt.subplot(111)
    # 遍历从小到大的索引
    for index in sortedIndicies.tolist()[0]:
        # 这里由于是从小到大，代表从反例到正例
        # 如果全都预测对应该是先全部走完反例的步数
        # 然后到达0,1后直线下降
        # 每分错一个相当于y轴下降一步
        # 代表有一个是反例的预测为正例
        # 所以真阳率则下降了

        # 每得到一个正例则往下走一步
        if classLabels[index] == 1.0:
            delX = 0
            delY = yStep
        # 每得到一个反例则往左走一步
        else:
            delX = xStep
            delY = 0
            # 相当于得到所有的高度和
            ySum += cur[1]

        ax.plot([cur[0], cur[0]-delX], [cur[1], cur[1]-delY], c='b')
        cur = (cur[0]-delX, cur[1]-delY)

    ax.plot([0,1], [0,1], 'b--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC curve for AdaBoost Horse Colic Detection System')
    ax.axis([0,1,0,1])
    plt.show()
    # ySum是所有小矩形的高，宽都为xStep，所有可以直接得到面积
    print('The area under the Curve is: ', ySum * xStep)


if __name__ == '__main__':
    from a5_loadDataSet import loadDataSet
    from a3_adaBoostTrainDS import adaBoostTrainDS

    datArr, labelArr = loadDataSet('data/horseColicTraining2.txt')
    classifierArray, aggClassEst = adaBoostTrainDS(datArr, labelArr, 50)
    # plotROC(expand_dims(array(labelArr),0), labelArr)
    plotROC(aggClassEst.T, labelArr)