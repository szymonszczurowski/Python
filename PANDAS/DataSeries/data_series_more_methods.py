import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

pok = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Name', 'Attack'],
                  index_col='Name').squeeze()
print(pok.head(), '\n')
print(pok.count(), '\n')

pokType = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Name', 'Type 2'],
                  index_col='Type 2').squeeze()
print(pokType.head(), '\n')
print(pokType.value_counts(), '\n') # POGRPuOWANIE I ZLICZENIE i SORTUJE MALEJĄCO
print(pokType.value_counts().head(), '\n')

print(pok.min(), '\n')
print(pok.max(), '\n')
print(pok.idxmin(), '\n')  # Wskazanie indexu min wartosci
print(pok.loc[pok.idxmin()], '\n')
print(pok.idxmax(), '\n')  # Wskazanie indexu max wartosci
print(pok.loc[pok.idxmax()], '\n')

print(pok.mean(), '\n')
print(pok.sum() / pok.count())
print(pok.median(), '\n')
print(pok.std(), '\n')

print('==================================================')

listA = [1, 1, 1, 2, 3, 5, 29]
SeriaA = pd.Series(listA)
listB = [4, 4, 4, 6, 6, 8, 10]
SeriaB = pd.Series(listB)
listC = [1, 1, 1, 6, 9, 11, 13]
SeriaC = pd.Series(listC)

#Średnia
print(SeriaA.mean())
print(SeriaB.mean())
print(SeriaC.mean(), '\n' )

#Wartość środkowa
print(SeriaA.median())
print(SeriaB.median())
print(SeriaC.median(), '\n')

#Odchylenie standardowe / odrzut danych w seri
print(SeriaA.std())
print(SeriaB.std())
print(SeriaC.std(), '\n')