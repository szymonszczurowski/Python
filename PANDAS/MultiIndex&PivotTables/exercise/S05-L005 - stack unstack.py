import numpy as np
import pandas as pd

fuel = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\fuel.csv",
                   usecols=['Year','Make','Model','Range (FT1)','City Range (FT1)'])
print(fuel.head())

fuel.drop_duplicates(subset=['Year','Make','Model'],inplace=True)
fuel.dropna(how='any',inplace=True)
fuel.set_index(['Year','Make','Model'], inplace=True)
print(fuel.head(), '\n\n\n')


print(fuel.stack(), '\n\n\n')
print(fuel.stack().to_frame(), '\n\n\n')
print(fuel.unstack(level='Model').head(), '\n\n\n')
print(fuel.unstack(level='Year').head(), '\n\n\n')
print(fuel.stack().unstack(level='Year').head(), '\n\n\n')
print(fuel.stack().unstack(level='Make').head(), '\n\n\n')
print(fuel.stack().unstack(level=['Year','Make']).head(), '\n\n\n')
print(fuel.stack().unstack(level=['Make','Year']).sort_index(axis=1).head(), '\n\n\n')

