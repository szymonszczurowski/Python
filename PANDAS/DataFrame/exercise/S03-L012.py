import pandas as pd
import numpy as np

fuel = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\fuel.csv", low_memory=False,
                   usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'])

listOfCars = ['Renault', 'Toyota', 'Ford']

isInList = fuel['Make'].isin([listOfCars])

print(isInList.head())
print(fuel[isInList].head())

