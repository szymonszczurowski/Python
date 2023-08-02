x

print(fortune.head())

fortune['RankByEmployee'] = fortune['Employees'].rank(ascending=False)
fortune['RankByProfits'] = fortune['Profits'].rank(ascending=False)

isEmployeesRankFirst10 = fortune['RankByEmployee'] <= 10
print(isEmployeesRankFirst10)

isProfitRankFirst10 = fortune['RankByProfits'] <= 10

print(fortune[isProfitRankFirst10 & isEmployeesRankFirst10])


