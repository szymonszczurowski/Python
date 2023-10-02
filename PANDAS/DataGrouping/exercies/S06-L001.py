from datetime import datetime
import pandas as pd
from datetime import timedelta
import time


df = pd.read_csv('C:\\Users\\szczu\\Desktop\\data\\course-files\\marathon_results_2016.csv', index_col='Bib',
usecols=['Bib','40K','Half','Pace','Age','M/F','Country',
 'State','City'])
df = df[(df['40K'] != '-') & (df['Half'] != '-')]
df['40K'] = df['40K'].apply(pd.to_timedelta)
df['Half'] = df['Half'].apply(pd.to_timedelta)
df['TotalSeconds'] = df['40K'].apply(lambda x: timedelta.total_seconds(x))
df['HalfSeconds'] = df['Half'].apply(lambda x: timedelta.total_seconds(x))

print(df.head())
print('\n################################\n')

print(df.describe())
print('\n################################\n')

print(df.info())
print('\n################################\n')

print(df.value_counts())
print('\n################################\n')

print(df.nunique())
print('\n################################\n')

cites = df['City'].unique()
print(cites)