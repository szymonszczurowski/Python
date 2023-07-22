import pandas as pd
import numpy as np
import math as math
import matplotlib.pyplot as plt

index = ['a', 'b', 'c', 'd', 'e', 'e']
values = ['Austria', 'Belgium', 'Canada', 'Denmark', 'England', 'Estonia']

s = pd.Series(data = values, index = index)


print(s)
# WSKAZANIE POZYCJI
print(s[1])
# WSKAZANIE WARTOŚCI INDEXU
print(s['b'])
print(s['e']) #Zwróci serię
# print(s['f']) #błąd

print('\n================================================================\n')

#GET
# WSKAZANIE POZYCJI
print(s.get(1))
# WSKAZANIE WARTOŚCI INDEXU
print(s.get('b'))
print(s.get('e')) #Zwróci serię
# print(s.get('f')) #błąd

print('\n================================================================\n')

#AT
# print(s.at[1]) #błąd
print(s.at['b'])
print(s.at['e']) #Zwróci serię
# print(s.at['f']) #błąd

print('\n================================================================\n')

#IAT - wyszukiwane po pozycji
# WSKAZANIE POZYCJI
print(s.iat[1])
# WSKAZANIE WARTOŚCI INDEXU
# print(s.iat['b']) #błąd
print(s[[0, 1]]) #Zwróci serię

print('\n================================================================\n')

#NAJELPSZE:::::::: chyba

#LOC - wyszukiwane po wartości indexu
# print(s.loc[1]) #błąd
print(s.loc['b'])
print(s.loc['e'])

print('\n================================================================\n')

#ILOC - wyszukiwane po pozcji indexu

print(s.iloc[1])
# print(s.iloc['b']) #błąd
print(s.iloc[[0, 1]])

