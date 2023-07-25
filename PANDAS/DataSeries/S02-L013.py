import pandas as pd

countries = pd.read_csv('C:\\Users\\szczu\\Desktop\\data\\course-files\\countries.csv', usecols=['Symbol', 'Name'], index_col='Symbol').squeeze()
print(countries.head(20))
print(countries['FR'])
print(countries.loc['FR'])
print(countries[13])
print(countries.iloc[13])

nordic = ['FI','SE','NO']

print(countries[nordic])
print(countries.loc[nordic]
)