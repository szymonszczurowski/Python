import pandas as pd
import numpy as np

fortune = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Fortune_500_2017.csv", low_memory=False,
                   usecols=['Rank','Title','Employees','Profits','Assets'],
                   index_col='Rank')

print(fortune.head())

fortune['RankByEmployee'] = fortune['Employees'].rank(ascending=False)
fortune['RankByProfits'] = fortune['Profits'].rank(ascending=False)

isEmployeesRankFirst10 = fortune['RankByEmployee'] <= 10
print(isEmployeesRankFirst10)

isProfitRankFirst10 = fortune['RankByProfits'] <= 10

print(fortune[isProfitRankFirst10 & isEmployeesRankFirst10])


