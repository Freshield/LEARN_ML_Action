# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a5_mrjob_pegasos.py
@Time: 2020-06-30 16:55
@Last_update: 2020-06-30 16:55
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from mrjob.job import MRJob
from mrjob.step import MRStep
from typing import NewType

import pickle
from numpy import *

new_int = NewType('new_int', int)

class MRsvm(MRJob):
    DEFAULT_INPUT_PROTOCOL = 'json_value'

    def __init__(self, *args, **kwargs):
        super(MRsvm, self).__init__(*args, **kwargs)
        with open('/media/freshield/SSD_1T/LEARN_ML_Action/chp15/data/testSet.txt') as f:
            self.data = [line.replace('\n', '').split('\t') for line in f.readlines()]
        self.data = mat(self.data)
        self.w = 0
        self.eta = 0.69
        self.dataList = []
        self.k = 100
        self.iterations = 50
        self.numMappers = 1
        self.t = 1

    def mapper(self, mapperId, inVals):
        if False:
            yield

        if inVals[0] == 'w':
            self.w = [float(i) for i in inVals[1]]
        elif inVals[0] == 'x':
            self.dataList.append(int(inVals[1]))
        elif inVals[0] == 't':
            self.t = inVals[1]

    def mapper_final(self):
        labels = self.data[:, -1].astype(float64)
        X = self.data[:, 0:-1]
        if self.w == 0:
            self.w = [0.001] * shape(X)[1]

        for index in self.dataList:
            p = mat(self.w).astype(float64) * X[index, :].T.astype(float64)
            if labels[index] * p < 1.0:
                yield (1, ['u', index])

        yield (1, ['w', self.w])
        yield (1, ['t', self.t])

    def reducer(self, _, packedVals):
        for valArr in packedVals:
            if valArr[0] == 'u':
                self.dataList.append(valArr[1])
            elif valArr[0] == 'w':
                self.w = valArr[1]
            elif valArr[0] == 't':
                self.t = valArr[1]

        labels = self.data[:, -1]
        X = self.data[:, 0: -1]

        wMat = mat(self.w)
        wDelta = mat(zeros(len(self.w)))
        for index in self.dataList:
            wDelta += float(labels[index]) * X[index, :].astype(float64)

        eta = 1.0 / (2.0 * self.t)
        wMat = (1.0 - 1.0 / self.t) * wMat + (eta / self.k) * wDelta

        for mapperNum in range(1, self.numMappers+1):
            yield (mapperNum, ['w', wMat.tolist()[0]])
            if self.t < self.iterations:
                yield (mapperNum, ['t', self.t + 1])
                for j in range(self.k // self.numMappers):
                    yield (mapperNum, ['x', random.randint(shape(self.data)[0])])

    def steps(self):
        return ([MRStep(mapper=self.mapper, mapper_final=self.mapper_final,
                        reducer=self.reducer,)] * self.iterations)


if __name__ == '__main__':
    MRsvm.run()