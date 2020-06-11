# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_rules.py
@Time: 2020-06-11 11:10
@Last_update: 2020-06-11 11:10
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a1_apriori import *


def generateRules(L, supportData, minConf=0.7):
    bigRuleList = []
    # 从1开始是因为0为单个元素的
    for i in range(1, len(L)):
        # 遍历所有集合
        for freqSet in L[i]:
            # 得到所有的单独的元素
            H1 = [frozenset([item]) for item in freqSet]
            if i > 1:
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calConf(freqSet, H1, supportData, bigRuleList, minConf)

    return bigRuleList


def rulesFromConseq(freqSet, H, supportData, br1, minConf=0.7):
    """
    freqSet: 规律集, H: 规律集中的item, supportData: 支持度的字典
    br1: 关联规则的总列表, minConf: 最小可信度
    """
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        Hmp1 = aprioriGen(H, m + 1)
        Hmp1 = calConf(freqSet, Hmp1, supportData, br1, minConf)
        if len(Hmp1) > 1:
            rulesFromConseq(freqSet, Hmp1, supportData, br1, minConf)


def calConf(freqSet, H, supportData, br1, minConf=0.7):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if conf >= minConf:
            print(f'{freqSet-conseq} --> {conseq}, conf: {conf}')
            br1.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)

    return prunedH

if __name__ == '__main__':
    dataSet = loadDataSet()
    print(dataSet)
    C1 = createC1(dataSet)
    print(C1)
    retList, supportData = apriori(dataSet, 0.5)
    print(retList)
    rules = generateRules(retList, supportData, minConf=0.5)
    print(rules)