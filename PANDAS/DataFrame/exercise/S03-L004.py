import pandas as pd

fuel = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\fuel.csv", low_memory=False,
                   index_col='Vehicle ID',
                   usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'])


fuel['Combined KPL'] = fuel['Combined MPG (FT1)'] * 1.609 / 3.78
print(fuel.head())

fuel.insert(loc=5, column='liters per km', value=100 / fuel['Combined KPL'])
print(fuel.head())

del fuel['Combined MPG (FT1)']
print(fuel.head())

fuel = fuel.drop(columns=['Combined KPL'])
print(fuel.head())
