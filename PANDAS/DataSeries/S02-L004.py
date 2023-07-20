import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math
import random as rnd

dataAsFloatList = []
for i in range(0, 100000):
    dataAsFloatList.append(i * rnd.random())

dataAsFloatSeries = pd.Series(dataAsFloatList)
print(dataAsFloatSeries)

print('size: \t', dataAsFloatSeries.size)
print('nbytes:\t', dataAsFloatSeries.nbytes)
print('shape:\t', dataAsFloatSeries.shape)
print('axes:\t', dataAsFloatSeries.axes)
print('dtype:\t', dataAsFloatSeries.dtype)
print('index:\t', dataAsFloatSeries.index)
print('unique:\t', dataAsFloatSeries.is_unique)
print('monotonic:\t', dataAsFloatSeries.is_monotonic_increasing)

print('\n================================\n')

dataAsStringList = []
for i in range(0, 100000):
    dataAsStringList.append(str(i * rnd.random()))

dataAsStringListSeries = pd.Series(dataAsFloatList)
print(dataAsStringListSeries)

print('size: \t', dataAsStringListSeries.size)
print('nbytes:\t', dataAsStringListSeries.nbytes)
print('dtype:\t', dataAsStringListSeries.dtype)

print('\n=============== DOKŁANA ZAJĘTOŚĆ PAMIĘCI =================\n')
print(dataAsFloatSeries.memory_usage(deep=True))
print(dataAsStringListSeries.memory_usage(deep=True))
