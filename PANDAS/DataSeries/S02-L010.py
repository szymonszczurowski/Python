import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

stack = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\StackOverflowDeveloperSurvey.csv", usecols=['Salary']).squeeze().dropna()
print(stack.head(), '\n')

print(stack.sort_values(ascending=False).head(), '\n')
print(stack.sort_values().head(), '\n')

stackCopy = stack.copy()
stackCopy2 = stack.copy()
print(stackCopy, '\n')
stackCopy.sort_values(ascending=False, inplace=True)
print(stackCopy.head(), '\n')
stackCopy2.sort_values(inplace=True)
print(stackCopy2.head(), '\n')

print(stack.sort_index(ascending=False), '\n')


maxSalaries = stack.sort_values(ascending=False).head(100)
minSalaries = stack.sort_values().head(100)

print(maxSalaries, '\n')
print(minSalaries, '\n')

print(maxSalaries.mean(), '\n')
print(minSalaries.mean(), '\n')