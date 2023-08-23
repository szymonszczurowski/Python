import pandas as pd

fuel = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\fuel.csv",
                   usecols=['Year','Make','Model','Range (FT1)','City Range (FT1)'],
                   index_col=['Year','Make','Model', ]).sort_index()

print(fuel.head())

print(fuel.loc[1984])

print("\n================================\n")

print(fuel.loc[(1984,'Alfa Romeo')])

print("\n================================\n")

print(fuel.loc[(1984,'Alfa Romeo','Spider Veloce 2000')])

print("\n================================\n")

print(fuel.loc[(1984,'Alfa Romeo','Spider Veloce 2000'), 'Range (FT1)' ])


fuel = fuel.transpose()
print(fuel.head())

print("\n================================\n")


print(fuel.loc[('Range (FT1)')], 1984)
print(fuel.loc['Range (FT1)',(1984,'Alfa Romeo')])
print(fuel.loc['Range (FT1)',(1984,'Alfa Romeo','Spider Veloce 2000')])
