import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

obj = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Name']).squeeze()

#SPRAWDZANIE CZY ELEMENT JEST W OBIEKCIE

countries = ['En', 'FR', 'PL', 'IT']
print('PL' in countries)
print('ES' in countries)

print(obj.head())
#W obiketach series in działa z indeksami
print('Venusaur' in obj) # Z wartościami nie działa
print(3 in obj) #Domyślnie jest tam obj.index
print(900 in obj)

#Żeby robić to na wartściach można użyć .values
print('Venusaur' in obj.values)
print('faf' in obj.values)