import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

fortune500 = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Fortune_500_2017.csv", usecols=['Rank', 'Title'], index_col='Rank').squeeze()
print(fortune500.head(), '\n')
print(fortune500.sort_index().head(10), '\n')
print(fortune500.sort_index(ascending=False).head(20), '\n')

fortune500 = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Fortune_500_2017.csv", usecols=["Title", "Employees"], index_col="Title").squeeze()

print(fortune500.head(), '\n')
print(fortune500['IBM'])
print(fortune500['Apple'])