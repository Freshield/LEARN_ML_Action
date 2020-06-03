# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: tkinter_tree.py
@Time: 2020-06-02 16:35
@Last_update: 2020-06-02 16:35
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from tkinter import *

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from compare import *


def reDraw(tolS, tolN):
    reDraw.f.clf()
    reDraw.a = reDraw.f.add_subplot(111)
    if chkBtnVar.get():
        if tolN < 2:
            tolN = 2
        myTree = createTree(reDraw.rawDat, modelLeaf, modelErr, (tolS, tolN))
        yHat = createForecast(myTree, reDraw.testDat, modelTreeEval)
    else:
        myTree = createTree(reDraw.rawDat, ops=(tolS, tolN))
        yHat = createForecast(myTree, reDraw.testDat)

    reDraw.a.scatter(array(reDraw.rawDat[:, 0].T)[0], array(reDraw.rawDat[:, 1].T)[0], s=5)
    reDraw.a.plot(reDraw.testDat, yHat, linewidth=2.0)
    reDraw.canvas.draw()

def getInputs():
    try:
        tolN = int(tolNentry.get())
    except:
        tolN = 10
        print('enter Integer for tolN')
        tolNentry.delete(0, END)
        tolNentry.insert(0, '10')

    try:
        tolS = float(tolSentry.get())
    except:
        tolS = 1.0
        print('enter Float for tolS')
        tolSentry.delete(0, END)
        tolSentry.insert(0, '1.0')

    return tolN, tolS


def drawNewTree():
    tolN, tolS = getInputs()
    reDraw(tolS, tolN)


root = Tk()

reDraw.f = Figure(figsize=(5, 4), dpi=100)
reDraw.canvas = FigureCanvasTkAgg(reDraw.f, master=root)
reDraw.canvas.draw()
reDraw.canvas.get_tk_widget().grid(row=0, columnspan=3)

# Label(root, text='Plot Place Holder').grid(row=0, columnspan=3)

Label(root, text='tolN').grid(row=1, column=0)
tolNentry = Entry(root)
tolNentry.grid(row=1, column=1)
tolNentry.insert(0, '10')

Label(root, text='tolS').grid(row=2, column=0)
tolSentry = Entry(root)
tolSentry.grid(row=2, column=1)
tolSentry.insert(0, '1.0')

Button(root, text='ReDraw', command=drawNewTree).grid(row=1, column=2, rowspan=3)

chkBtnVar = IntVar()
chkBtn = Checkbutton(root, text='Model Tree', variable=chkBtnVar)
chkBtn.grid(row=3, column=0, columnspan=2)

reDraw.rawDat = mat(loadDataSet('data/sine.txt'))
reDraw.testDat = arange(float(min(reDraw.rawDat[:, 0])[0, 0]), float(max(reDraw.rawDat[:, 0])[0, 0]), 0.01)
reDraw(1.0, 10)

root.mainloop()