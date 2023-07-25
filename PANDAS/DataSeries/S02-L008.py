import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

education = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\StackOverflowDeveloperSurvey.csv", usecols=['FormalEducation'])
print(type(education))
print(education.head(), '\n')

education = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\StackOverflowDeveloperSurvey.csv", usecols=['FormalEducation']).squeeze()
education = pd.Series(education)
print(type(education))
print(education.tail(10))

allInfo = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\StackOverflowDeveloperSurvey.csv")
country = allInfo["Country"]
print(country.head())

filterOnlyUSA = country == "United States"
print(filterOnlyUSA.head())

print(country.where(country == "United States").dropna().head(10))