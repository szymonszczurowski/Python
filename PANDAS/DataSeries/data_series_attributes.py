import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

cities = ['London', 'Berlin', 'Warsaw', 'Paris']
print(cities)

citiesSeries = pd.Series(cities)
print(citiesSeries, '\n')

#ATRYBUT = wartosc którą dany obiekt posiada np. size
print(citiesSeries.size, '\n')
print(citiesSeries.nbytes, '\n') #ile bajtów zajmuje obiekt w pamięci
print(citiesSeries.is_unique, '\n') #czy wartosci są unikalne
print(citiesSeries.is_monotonic_increasing, '\n') #czy wartości są rosnące
print(citiesSeries.index, '\n') #Skąd wziął się index
print(citiesSeries.values, '\n') #wartosci
print(citiesSeries.dtype, '\n') #typ obiketu

print(citiesSeries.shape, '\n') #KSZTAŁT - Wykazuje ile elementów jest na wymiarze. tutaj 4 elementy na jednym wymairze
print(citiesSeries.axes, '\n') #zwraca współrzędne

monotonicList = [1,2,4,67,99]
monotonicListSeries = pd.Series(monotonicList)
print(monotonicListSeries, '\n')
print(monotonicListSeries.is_monotonic, '\n')
print(monotonicListSeries.is_monotonic_increasing, '\n')
print(monotonicListSeries.is_monotonic_decreasing, '\n')

stringList = ['Cola', 'Redbull', 'Sprite']
stringListSeries = pd.Series(stringList)
print(stringListSeries)
print(stringListSeries.is_monotonic, '\n')
print(stringListSeries.is_monotonic_increasing, '\n')
print(stringListSeries.is_monotonic_decreasing, '\n')

