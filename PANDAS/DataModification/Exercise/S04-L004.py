import pandas as pd

fortune = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Fortune_500_2017.csv")
print(fortune.head())

fortune.set_index('Rank', inplace=True)
print(fortune.head())

print(fortune[99:105])

print(fortune.loc[100:105][["Title", "Employees"]])

fortune.reset_index()
fortune.set_index('Title', inplace=True)
fortune.sort_index(inplace=True)

print(fortune.loc['X':'Y'])