import numpy as np
import pandas as pd

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv", usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat'])
print(frame.head())

#RANKING KALORYCZNOŚCI DAN (Nadanie numerów ze względu na cos)

print(frame['Calories'].rank().head())

print('\n================================\n')

#Jeśłi kilka wartości jest takch samych to wyliczania jest to poprzez (1 miejsce  + ostatnie miejsce / 2))
frame['CaloriesRank'] = frame['Calories'].rank() #Dodanie kolumny raking do danych
print(frame.head())

print('\n================================\n')

print(frame.sort_values(by = 'Calories').head(30))

print('\n===============Ranking jest teraz malejący=================\n')

#Ranking jest teraz malejący
frame['CaloriesRank'] = frame['Calories'].rank(ascending=False)
print(frame.sort_values(by = 'Calories', ascending=False).head(30)) #Teraz ranking jest jak ranking

print('\n================================\n')

#Wyciągnięcie 3 najbardziej kalorycznych dań
print(frame.sort_values(by = 'Calories', ascending=False, inplace=True))
print(frame.head(3), '\n')

#Można użyc detykowanej funckji
print(frame.nlargest(n=3, columns='Calories')) #ilość, kolumna

print('\n================================\n')

#Wyciągnięcie 3 najmniej kalorycznych dań

print(frame.tail(3), '\n')
print(frame.nsmallest(n=3, columns='Calories'))