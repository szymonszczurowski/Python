import pandas as pd
import numpy as np

fuel = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\fuel.csv", low_memory=False,
                   usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'])

print(fuel.head())

print(fuel.info(memory_usage='deep'))
fuel['Year'] = fuel['Year'].astype('int')
print(fuel['Make'].value_counts())

fuel['Make'] = fuel['Make'].astype('category')
print(fuel.info(memory_usage='deep'))

fuel['Combined MPG (FT1)'] = fuel['Combined MPG (FT1)'].astype('float')
print(fuel.info(memory_usage='deep'))
