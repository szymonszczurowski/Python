import pandas as pd

fuel = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\fuel.csv", low_memory=False,
                   usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'
                            ])
print(fuel.head(), '\n')

print(fuel.info(), '\n')
print(fuel.dtypes, '\n')
print(fuel.dtypes.value_counts(), '\n')
print(fuel['Make'].value_counts().head(10), '\n')
print(fuel.index, '\n')
print(fuel.axes, '\n')
print(fuel.values)
print(fuel.columns, '\n')
print(fuel.shape, '\n')

print(fuel.count())
print(len(fuel))