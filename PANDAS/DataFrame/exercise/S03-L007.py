import pandas as pd
import numpy as np

fuel = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\fuel.csv", low_memory=False,
                   index_col='Vehicle ID',
                   usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'])

fuel.loc[27681, 'Combined MPG (FT1)'] = np.NaN

print(fuel.head())
print(fuel.sort_values(by=['Make', 'Model']).head())
print(fuel.sort_values(by=['Make', 'Model'], ascending=[False, False]).head())
print(fuel.sort_values(by=['Make', 'Combined MPG (FT1)'], ascending=[True, False]).head())
print(fuel.sort_values(by='Combined MPG (FT1)',na_position='first').head())
fuel.sort_values(by='Combined MPG (FT1)',na_position='first',inplace=True)
print(fuel.sort_index())