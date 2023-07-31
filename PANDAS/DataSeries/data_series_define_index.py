import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

pokemon = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Attack']).squeeze()
print(pokemon)

#Zmiana kolumny indexu, index_col
pokemon = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Attack', '#'], index_col='#').squeeze()
print(pokemon)
print(pokemon[5])
print(pokemon[1:6])
print(pokemon[[11, 111]])


#Zmiana kolumny indexu, index_col
pokemon = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Name', 'Attack'], index_col='Name').squeeze()
print(pokemon)
print(pokemon['Diancie'])
print(pokemon['Diancie':'Volcanion'])
print(pokemon[['Diancie', 'Volcanion']])
