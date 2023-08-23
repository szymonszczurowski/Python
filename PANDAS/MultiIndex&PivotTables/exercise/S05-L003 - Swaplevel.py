import numpy as np
import pandas as pd

fuel = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\fuel.csv",
                   usecols=['Year','Make','Model','Range (FT1)','City Range (FT1)'],
                   index_col=['Year','Make','Model', ]).sort_index()
print(fuel.head())

fuel = fuel.swaplevel(0,1).sort_index()
print(fuel.head())
print(fuel.loc[('Alfa Romeo',1984,'Spider Veloce 2000')])

fuel = fuel.swaplevel(1,2).sort_index()
print(fuel.head())
print(fuel.loc[('Alfa Romeo','Spider Veloce 2000',1984)])
