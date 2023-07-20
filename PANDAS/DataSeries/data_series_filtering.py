import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

# FILTROWANIE

numbers = [1, 2, 3, 12, 13, 14, 15, 16, 17, 18, 19, 20, 4, 3]
numbersSeries = pd.Series(numbers)
print(numbersSeries, '\n')

# TRUE/FALSE wartość większa od 10
print(numbersSeries > 10, '\n')

# Zwróci wartości większe od 10, ale mniejsze będa miały Nan
numbershigher10 = numbersSeries.where(numbersSeries > 10)
print(numbershigher10, '\n')

# Zwróci wartości większe od 10, ale mniejsze będa miały -1
numbershigher10 = numbersSeries.where(numbersSeries > 10, other=-1)
print(numbershigher10, '\n')

# Zwróci wartości większe od 10 i tylko te
numbershigher10 = numbersSeries.where(numbersSeries > 10).dropna()
print(numbershigher10, '\n')

# Zwróci wartości większe od 10 i zmodyfikuje orginalne obiket a nie zwróci kopie, ale jest Nan
numbersSeries.where(numbersSeries > 10, inplace=True)
print(numbersSeries, '\n')

# Usninięcie Nan wewnątrz obiektu
numbersSeries.dropna(inplace=True)
print(numbersSeries, '\n')

numbers = [1, 2, 3, 12, 13, 14, 15, 16, 17, 18, 19, 20, 4, 3]
numbersSeries = pd.Series(numbers)

# Nie można łączyć, bo oobiekt zmienia sie wewnątrznie i niczego nie zwraca
# numbersSeries.where(numbersSeries > 10, inplace=True).dropna(inplace=True)
# print(numbersSeries, '\n')

# FILTORWANIE PO INDEkSIE
numbers = [1, 2, 3, 12, 13, 14, 15, 16, 17, 18, 19, 20, 4, 3]
numbersSeries = pd.Series(numbers)
print(numbersSeries.filter(items=[0, 2, 4]))
