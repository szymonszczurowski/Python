import pandas as pd

salary = pd.read_csv('C:\\Users\\szczu\\Desktop\\data\\course-files\\StackOverflowDeveloperSurvey.csv', usecols=['Salary']).squeeze().dropna()
print(salary.head(), '\n')

print(salary.count())
print(salary.min())
print(salary.max(), '\n')

print(salary.head().to_list())
print(salary.head().to_dict(), '\n')

listSalarySorted = salary.sort_values(ascending=False).to_list()
print(listSalarySorted[:5])

salary.name = 'Salary of a person'
print(salary.head())