from datetime import timedelta

import numpy as np
import pandas as pd

df = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\marathon_results_2016.csv",
                   usecols=['Bib','40K','Half','Pace','Age','M/F','Country','State','City'], index_col='Bib')
print(df.head())

df['40K'] = df['40K'].replace('-', 0)
df['Half'] = df['Half'].replace('-', 0)

df['40K'] = df['40K'].apply(pd.to_timedelta)
df['Half'] = df['Half'].apply(pd.to_timedelta)

df['TotalSeconds'] = df['40K'].apply(lambda x: timedelta.total_seconds(x))
df['HalfSeconds'] = df['Half'].apply(lambda x: timedelta.total_seconds(x))

df['TotalSeconds'] = df['TotalSeconds'].replace(0, np.nan)
df['HalfSeconds'] = df['HalfSeconds'].replace(0, np.nan)

print(df.pivot_table(index="Age",columns="M/F",values="TotalSeconds", aggfunc='mean').head())
print(df.pivot_table(index="Age",columns="M/F",values=["HalfSeconds","TotalSeconds"] ).swaplevel(axis=1).head())