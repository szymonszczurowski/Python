import pandas as pd

programmers = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\StackOverflowDeveloperSurvey2018.csv", low_memory=False, usecols=['ConvertedSalary']).squeeze()

print(programmers.mean())
print(programmers.median())
print(programmers.std())

print(programmers.max())

fortune500 = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Fortune_500_2017.csv", usecols=['Title', 'Employees'], index_col='Title').squeeze()
print(fortune500.idxmax())
print(fortune500.loc[fortune500.idxmax()])

print(fortune500.idxmin())
print(fortune500.loc[fortune500.idxmin()])