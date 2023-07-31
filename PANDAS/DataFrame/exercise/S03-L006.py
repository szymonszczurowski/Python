import pandas as pd
import numpy as np

fuel = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\fuel.csv", low_memory=False,
                   index_col='Vehicle ID',
                   usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'])

fuel.loc[27705, 'Class'] = np.NaN
fuel.loc[26561, 'Class'] = np.NaN
fuel.loc[27550, 'Fuel Type'] = np.NaN
fuel.loc[27705, 'Combined MPG (FT1)'] = np.NaN
fuel.loc[27681, 'Combined MPG (FT1)'] = np.NaN

print(fuel.head())
print(fuel.fillna(value=-1).head())

replaceRules = {
    'Class': '---',
    'Fuel Type': '---',
    'Combined MPG (FT1)': -1
}
print(fuel.fillna(value=replaceRules).head())

avgMPG = fuel['Combined MPG (FT1)'].mean()
print(avgMPG)

replaceRules = {
    'Class': '?',
    'Fuel Type': '?',
    'Combined MPG (FT1)': avgMPG
}

fuel.fillna(value=replaceRules, inplace=True)
print(fuel.head())

fuel.loc[27705, 'Class'] = np.NaN
fuel.loc[26561, 'Class'] = np.NaN
fuel.loc[27550, 'Fuel Type'] = np.NaN
fuel.loc[27705, 'Combined MPG (FT1)'] = np.NaN
fuel.loc[27681, 'Combined MPG (FT1)'] = np.NaN

fuel.fillna(method='ffill', inplace=True)
print(fuel.head())
