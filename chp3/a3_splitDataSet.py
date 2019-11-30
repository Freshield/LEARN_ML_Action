#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_splitDataSet.py
@Time: 2019-11-26 14:01
@Last_update: 2019-11-26 14:01
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def splitDataSet(dataSet, axis, value):
    """
    axis是哪个feature，value是这个feature的数值
    这里相当于把目标feature的所有数值都单独分离出来
    :param dataSet:
    :param axis:
    :param value:
    :return:
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            # 得到去除第axis的feature之后的所有值
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)

    return retDataSet


if __name__ == '__main__':
    from a2_createDataSet import createDataSet
    dataSet, labels = createDataSet()
    print(dataSet)
    print(splitDataSet(dataSet, 0, 1))
    print(splitDataSet(dataSet, 0, 0))