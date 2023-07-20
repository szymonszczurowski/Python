import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math


cites = ['Shanghai', 'Beijing', 'Istanbul']
population = [24183300, 20794100, 15030000]

citypopSeries = pd.Series(index=cites, data=population)
print(citypopSeries)

print('population all:', citypopSeries.sum())
print('mean:', citypopSeries.mean())
print('index:', citypopSeries.index)
print(citypopSeries.tolist())
print('index:', citypopSeries.keys())
print('value:', citypopSeries.values)
