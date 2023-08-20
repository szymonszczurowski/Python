import pandas as pd
import random as rd

aircraftsDict = {
    'PYT001':'Airbus 320',
    'PYT002':'Boeing 737',
    'PYT003':'Airbus 321'
}

aircrafts = pd.Series(aircraftsDict)
print(aircrafts.head())

flightsList = []

for i in range(100):
    flightsList.append(rd.choice(aircrafts.index))

print(flightsList[:5])

flights = pd.Series(flightsList)
flights.head()
flights_aircrafts = flights.map(aircrafts)

print(flights_aircrafts)