# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a7_searchForSet.py
@Time: 2020-05-15 11:08
@Last_update: 2020-05-15 11:08
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
from bs4 import BeautifulSoup
import random


def scrapePage(retX, retY, inFile, yr, numPce, origPrc):
    """
    函数说明:从页面读取数据，生成retX和retY列表
    Parameters:
        retX - 数据X
        retY - 数据Y
        inFile - HTML文件
        yr - 年份
        numPce - 乐高部件数目
        origPrc - 原价
    Returns:
        无
    Website:
        http://www.cuijiahua.com/
    Modify:
        2017-12-03
    """
    # 打开并读取HTML文件
    with open(inFile, encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html)

    i = 1
    # 根据HTML页面结构进行解析
    currentRow = soup.find_all('table', r = "%d" % i)

    while(len(currentRow) != 0):
        currentRow = soup.find_all('table', r = "%d" % i)
        title = currentRow[0].find_all('a')[1].text
        lwrTitle = title.lower()
        # 查找是否有全新标签
        if (lwrTitle.find('new') > -1) or (lwrTitle.find('nisb') > -1):
            newFlag = 1.0
        else:
            newFlag = 0.0

        # 查找是否已经标志出售，我们只收集已出售的数据
        soldUnicde = currentRow[0].find_all('td')[3].find_all('span')
        if len(soldUnicde) == 0:
            print("商品 #%d 没有出售" % i)
        else:
            # 解析页面获取当前价格
            soldPrice = currentRow[0].find_all('td')[4]
            priceStr = soldPrice.text
            priceStr = priceStr.replace('$','')
            priceStr = priceStr.replace(',','')
            if len(soldPrice) > 1:
                priceStr = priceStr.replace('Free shipping', '')
            sellingPrice = float(priceStr)

            # 去掉不完整的套装价格
            if  sellingPrice > origPrc * 0.5:
                print("%d\t%d\t%d\t%f\t%f" % (yr, numPce, newFlag, origPrc, sellingPrice))
                retX.append([yr, numPce, newFlag, origPrc])
                retY.append(sellingPrice)
        i += 1
        currentRow = soup.find_all('table', r = "%d" % i)


def setDataCollect(retX, retY):
    scrapePage(retX, retY, 'data/setHtml/lego8288.html', 2006, 800, 49.99)
    scrapePage(retX, retY, 'data/setHtml/lego10030.html', 2002, 3096, 269.99)
    scrapePage(retX, retY, 'data/setHtml/lego10179.html', 2007, 5195, 499.99)
    scrapePage(retX, retY, 'data/setHtml/lego10181.html', 2007, 3428, 199.99)
    scrapePage(retX, retY, 'data/setHtml/lego10189.html', 2008, 5922, 299.99)
    scrapePage(retX, retY, 'data/setHtml/lego10196.html', 2009, 3263, 249.99)


if __name__ == '__main__':
    from a2_standRegres import standRegres
    retX = []
    retY = []
    setDataCollect(retX, retY)
    print(retX)
    print(shape(retX))
    lgX1 = mat(ones((63, 5)))
    lgY = mat(retY)
    print(shape(lgY))

    lgX1[:, 1:] = mat(retX)
    print(lgX1[0])
    ws = standRegres(lgX1, lgY)
    print(ws)
    print(lgX1[0] * ws)
    print(lgY[0, 0])
    print(lgX1[-1] * ws)
    print(lgY[0, -1])
    print(lgX1[43] * ws)
    print(lgY[0, 43])