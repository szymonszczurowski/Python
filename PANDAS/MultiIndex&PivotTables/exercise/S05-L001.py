import pandas as pd
import random as rd
import numpy as np

air = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Air_Traffic_Passenger_Statistics.csv")
print(air.head())

air.set_index([ "Operating Airline","Activity Period"], inplace=True)
print(air.head(10))

air.reset_index(inplace=True)
air.set_index(["Activity Period", "Operating Airline"], inplace=True)
print(air.head(10))

air.sort_index(ascending=[False, True], inplace=True)
print(air.head(10))

air.reset_index(inplace=True)
print(air.head(10))

air.set_index(["Activity Period", "Operating Airline","Activity Type Code"], inplace=True)
print(air.head(10))
