#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: trainNB0.py
@Time: 2019-12-10 16:20
@Last_update: 2019-12-10 16:20
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


def trainNB0(trainMatrix, trainCategory):
    """
    :param trainMatrix: 训练集, (6, 32)
    :param trainCategory: labels, (6,)
    :return:
    """
    # 训练集的数量
    numTrainDocs = len(trainMatrix)
    # 字典的长度
    numWords = len(trainMatrix[0])
    # 得到辱骂的概率, 也就是为1的概率
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    # 初始化数值
    # (32,)
    # 为了解决乘0问题, 初始化为1和2
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.
    p1Denom = 2.

    # 遍历每个训练集
    for i in range(numTrainDocs):
        # 如果label为1, 也就是是辱骂的数据
        if trainCategory[i] == 1:
            # 向量进行累加
            p1Num += trainMatrix[i]
            # 分母加上本条数据出现的字符数量
            p1Denom += sum(trainMatrix[i])
        # 如果label为0, 也就是正常的数据
        else:
            # 向量进行累加
            p0Num += trainMatrix[i]
            # 分母加上本条数据出现的字符数量
            p0Denom += sum(trainMatrix[i])
    # 相应字符在相应类别中出现的概率
    # 为了解决下溢出的问题, 这里使用log
    p1Vect = log(p1Num/p1Denom)
    p0Vect = log(p0Num/p0Denom)

    return p0Vect, p1Vect, pAbusive


if __name__ == '__main__':
    from bayes import loadDataSet, createVocabList, setOfWords2Vec
    # 数据
    listOposts, listClasses = loadDataSet()
    # 词典
    myVocabList = createVocabList(listOposts)

    # 把数据的词转换为向量
    trainMat = []
    for postinDoc in listOposts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))

    print(len(myVocabList))
    print(len(trainMat[0]))
    print()
    p0V,p1V,pAb = trainNB0(trainMat, listClasses)
    print()
    print(len(p0V))
    print(len(p1V))
    print(pAb)
    print(p0V)
    print(p1V)
    print(sum(p0V))
    print(sum(p1V))