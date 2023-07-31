import pandas as pd
import numpy as np

fortune = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Fortune_500_2017.csv", low_memory=False,
                   usecols=['Rank','Title','Employees','Profits','Assets'],
                   index_col='Rank')

print(fortune.head())

print(fortune['Employees'].rank(ascending=False).head())

fortune['RankByEmployee'] = fortune['Employees'].rank(ascending=False)
print(fortune.head())

print(fortune['Profits'].rank().head())

fortune['RankByProfits'] = fortune['Profits'].rank()


print(fortune.nlargest(n=3, columns='Assets'))
print(fortune.nsmallest(n=3, columns='Assets')
)