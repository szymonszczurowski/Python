import pandas as pd

countries = pd.read_csv('C:\\Users\\szczu\\Desktop\\data\\course-files\\countries.csv', usecols=['Symbol', 'Name'], index_col='Symbol').squeeze()
countries.dropna(inplace=True)
print(countries.head(20), '\n')

toFind = ['BB','BS']
print(countries.loc[toFind])

toFind = ['BB', 'AA', 'BS']
print(countries.index.reindex(toFind))
print(countries.index.intersection(toFind))

print(countries.loc[countries.index.intersection(toFind)])