# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_mrmean.py
@Time: 2020-06-30 15:54
@Last_update: 2020-06-30 15:54
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


class MRmean(MRJob):
    def __init__(self, *args, **kwargs):
        super(MRmean, self).__init__(*args, **kwargs)
        self.inCount = 0
        self.inSum = 0
        self.inSqSum = 0

    def mapper(self, key, value):
        if False:
            yield

        inVal = float(value)
        self.inCount += 1
        self.inSum += inVal
        self.inSqSum += inVal * inVal

    def mapper_final(self):
        mn = self.inSum / self.inCount
        mnSq = self.inSqSum / self.inCount
        yield (1, [self.inCount, mn, mnSq])

    def reducer(self, key, values):
        cumVal = 0.0
        cumSumSq = 0.0
        cumN = 0.0
        for valArr in values:
            nj = float(valArr[0])
            cumN += nj
            cumVal += nj * float(valArr[1])
            cumSumSq += nj * float(valArr[2])

        mean = cumVal / cumN
        var = (cumSumSq - 2 * mean * cumVal + cumN * mean * mean) / cumN
        yield (mean, var)

    def steps(self):
        return ([MRStep(mapper=self.mapper, reducer=self.reducer, mapper_final=self.mapper_final)])


if __name__ == '__main__':
    MRmean.run()