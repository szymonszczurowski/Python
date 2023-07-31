import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

from pandas import Series

pok = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Name', 'Attack'],
                  index_col='Name').squeeze()

#Przemnożenie przez 100
pok100 = pok * 100
print(pok100.head(), '\n')


pok2 = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Type 1', 'Name'], index_col='Name').squeeze()

#Trzeba dodać str, żeby modyfikować stringa
pokUpper = pok2.str.upper()
print(pokUpper.head(), '\n')

#Dodanie przedrotstka TYPE i uppercase
pokType = "TYPE:" + pok2.str.upper()
print(pokType.head(), '\n')

print(pok2.value_counts(), '\n')

def ReplaceType(oldType):
    if oldType == 'Grass' or oldType == "Ground":
        return 'Nature'
    else:
        return oldType

print(ReplaceType('Fire'))
print(ReplaceType('Nature'), '\n')

#Zeby skorzystać z funckji dla każdej wartości seri trzebu użyć metody apply
pokNature = pok2.apply(ReplaceType)
print(pokNature.head(), '\n')
print(pokNature.value_counts(), '\n')

#Druga metoda - lambda
pokNature = pok2.apply(lambda x: 'Nature' if x == 'Grass' or x == 'Ground' else x)
print(pokNature.head(), '\n')
print(pokNature.value_counts(), '\n')