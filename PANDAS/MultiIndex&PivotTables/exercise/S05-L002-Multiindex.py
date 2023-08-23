import pandas as pd
import random as rd
import numpy as np

air = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Air_Traffic_Passenger_Statistics.csv", index_col=["Operating Airline","Activity Period","Activity Type Code"]).sort_index()
print(air.head(10))


print(air.loc['Air France', 200507, 'Enplaned'])

print("\n================================\n")

print(air.loc['Air France', 200507])

print("\n================================\n")

print(air.loc['Air France'].head())

print("\n================================\n")

print(air['Passenger Count'].loc['Air France', 200507, 'Enplaned'])
print(air['Passenger Count'].loc['Air France', 200507, 'Deplaned'])

print("\n================================\n")

print(air.iloc[20-1:25])
print(air.iloc[20:25,8])