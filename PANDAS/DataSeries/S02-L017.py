import pandas as pd

surveys = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\StackOverflowDeveloperSurvey2018.csv", low_memory=False, usecols=['Salary']).squeeze().dropna()
print(surveys.head(), '\n')
print(surveys.count(), '\n')

surveys = pd.to_numeric(surveys, errors='coerce')
surveys = surveys.dropna()
surveysIncrease = surveys * 0.03
print(surveysIncrease.head(), '\n')

surveysAfterIncrease = surveys + surveysIncrease
print(surveysAfterIncrease.head(), '\n')

surveys = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\StackOverflowDeveloperSurvey2018.csv", low_memory=False, usecols=['HoursOutside']).squeeze().dropna()
print(surveys.value_counts(), '\n')

surveysTime = surveys.str.lower()
print(surveysTime.head(), '\n')

surveysTime = surveys.apply(lambda x: x.upper())
print(surveysTime.head())


def ChangeDescription(string):
    if string == 'LESS THAN 30 MINUTES':
        return 'LESS THAN HALF HOUR'
    else:
        return string


print(ChangeDescription('LESS THAN 30 MINUTES'))
print(ChangeDescription('1 HOUR'))
print(surveys.apply(ChangeDescription))