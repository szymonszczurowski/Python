import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

monotionicList = (1, 2, 4, 67, 99)
monotionicListSeries = pd.Series(monotionicList)
print(monotionicListSeries)

print(monotionicListSeries.sum())
print(monotionicListSeries.min())
print(monotionicListSeries.max())
print(monotionicListSeries.mean())  # średnia
print(monotionicListSeries.count())  # ilość elementów za pomocą atrubuty to .size
print(monotionicListSeries.product())  # Wymnożenie wszystkich liczb przez siebie
print(monotionicListSeries.keys())  # jak zbudowany jest index, za pomocą atrubuty to .index
print(monotionicListSeries.tolist())  # konwersja na list. Jest dużo metod konwersji

print(monotionicListSeries.add(10))  # dodanie do każdego elmentu danej wartosci, ale nie na stałe, nie zmodyfikowane
# Robią się kopie, wiec najlepiej przypsac ją do zmiennej
newSeries = monotionicListSeries.add(10)
print(newSeries)

print('\n================================\n')

currencies = ['USD', 'EUR', 'PLN', 'EUR', 'EUR']
countries = ['USA', 'Spain', 'Poland', 'Portugal', 'Italy']

#Jako indexy waluta, wartości to państwa
curSeries = pd.Series(countries, currencies)
print(curSeries)

#Tak czytelniej
curSeries = pd.Series(index=currencies, data=countries, )
print(curSeries)


#W data series indexy nie musza być unikalne, w słownikach już tak