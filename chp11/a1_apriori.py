# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_apriori.py
@Time: 2020-06-10 17:15
@Last_update: 2020-06-10 17:15
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def loadDataSet():
    return [[1,3,4], [2,3,5], [1,2,3,5], [2,5]]


def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if [item] not in C1:
                C1.append([item])

    C1.sort()

    return list(map(frozenset, C1))


def scanD(D, Ck, minSupport):
    """
    D: dataset, Ck: 项集, minSupport: 最小支持度
    """
    ssCnt = {}
    # 遍历每条
    for tid in D:
        # 遍历项集
        for can in Ck:
            # 看是否是当前这条数据的子项
            if can.issubset(tid):
                # 字典相应的索引加1
                if can not in ssCnt:
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1

    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support

    return retList, supportData


def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            L1 = list(Lk[i])[:k-2]
            L2 = list(Lk[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])

    return retList


def apriori(dataSet, minSupport=0.5):
    C1 = createC1(dataSet)
    D = list(map(set, dataSet))
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        L.append(Lk)

        print(k)
        print(Lk)
        k += 1

    return L, supportData


if __name__ == '__main__':
    dataSet = loadDataSet()
    print(dataSet)
    C1 = createC1(dataSet)
    print(C1)
    retList, supportData = apriori(dataSet, 0.5)
    print()
    print(retList)
    print(supportData)