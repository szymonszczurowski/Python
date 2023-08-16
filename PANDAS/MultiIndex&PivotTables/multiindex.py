import pandas as pd
import numpy as np

incidents = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Canadian Railway Crossing Incidents.csv")
print(incidents.head(10), '\n')

print(incidents.set_index('Region').head(10), '\n')
print(incidents.set_index('EventType').head(10), '\n')

print(incidents.set_index(['Region', 'EventType']).head(10), '\n') #USTAWIENIE KILKU INDEXÓW

incidents.set_index(['EventType', 'Region'], inplace=True) #USTAWIENIE KILKU INDEXÓW
print(incidents.head(), '\n')

incidents.sort_index(inplace=True) #Posortowanie, żeby index, żeby pogrupować`
print(incidents.head(), '\n')

incidents.sort_index(ascending=[True, False],inplace=True) #pierwszy klucz posortowany rosnąco, drugi malejąco
print(incidents.head(), '\n')
