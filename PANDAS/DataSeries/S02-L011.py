import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

countries = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\StackOverflowDeveloperSurvey.csv", usecols=['Country']).squeeze().dropna()
print(countries.head())
print('Poland' in countries.values)
print('Spain' in countries)
print('Spain' in countries.values)
print('Wonderland' in countries.values)
