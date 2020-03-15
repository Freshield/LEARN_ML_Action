#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a7_treePlotter.py
@Time: 2020-03-16 17:13
@Last_update: 2020-03-16 17:13
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle='sawtooth', fc='0.8')
leafNode = dict(boxstyle='round4', fc='0.8')
arrow_args = dict(arrowstyle='<-')

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    """
    绘制节点
    :param nodeTxt: 绘制的信息
    :param centerPt: bbox的位置
    :param parentPt: 箭头的尾巴位置
    :param nodeType: bbox的样式
    :return:
    """
    createPlot.ax1.annotate(
        nodeTxt, xy=parentPt, xycoords='axes fraction', xytext=centerPt, textcoords='axes fraction',
        va='center', ha='center', bbox=nodeType, arrowprops=arrow_args)

def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode('decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()


if __name__ == '__main__':
    createPlot()

