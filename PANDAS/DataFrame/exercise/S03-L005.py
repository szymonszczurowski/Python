import pandas as pd
import numpy as np

fuel = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\fuel.csv", low_memory=False,
                   index_col='Vehicle ID',
                   usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'])

fuel.loc[27705, 'Class'] = np.NaN
fuel.loc[26561, 'Class'] = np.NaN
fuel.loc[27550, 'Fuel Type'] = np.NaN

print(fuel.head())
print(fuel.dropna().head())
print(fuel.dropna(axis='columns', how='any').head())
print(fuel.dropna(subset=['Class'], how='any').head())
fuel.dropna(subset=['Class'], how='any', inplace=True)
fuel.dropna(subset=['Fuel Type'], how='any', inplace=True)
print(fuel.head())