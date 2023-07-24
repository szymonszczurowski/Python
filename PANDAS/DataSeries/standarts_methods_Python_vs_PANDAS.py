import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math


obj = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Name']).squeeze()

#PYTHON
print(type(obj), '\n')
print(len(obj), '\n')
print(sorted(obj), '\n')
print(type(sorted(obj)), '\n')
print(list(obj), '\n')
print(type(list(obj)), '\n')
print(dict(obj))
print(type(dict(obj)), '\n')
print(min(obj), '\n')
print(max(obj), '\n')
print(obj.name, '\n')
obj.name = 'Name of pokemon'
print(obj.name, '\n')

obj2 = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Name']).squeeze()
print(obj2.name, '\n')
obj2.name = 'Spped of pokemon'
print(obj2.name, '\n')
