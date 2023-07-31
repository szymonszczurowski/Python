import pandas as pd

fuel = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\fuel.csv", low_memory=False,
                   index_col='Vehicle ID',
                   usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'])

print(fuel['Make'].head(), '\n')
print(fuel['Make'].value_counts().head(), '\n')

print(fuel.iloc[1874].info(), '\n')
print(fuel['Combined MPG (FT1)'].iloc[1873], '\n')
print(fuel.loc[1873, 'Combined MPG (FT1)'], '\n')
print(fuel['Combined MPG (FT1)'].max(), '\n')
print(fuel["Combined MPG (FT1)"].idxmax(), '\n')
print(fuel.loc[fuel["Combined MPG (FT1)"].idxmax()])

shortFuel = fuel[['Make', 'Model']]
print(shortFuel.head(), '\n')