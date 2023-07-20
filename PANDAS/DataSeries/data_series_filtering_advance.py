import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

numbers = [1, 2, 3, 12, 13, 14, 15, 16, 17, 18, 19, 20, 4, 3]
numbersSeries = pd.Series(numbers)
print(numbersSeries, '\n')

print(numbersSeries % 2 == 1)

print(numbersSeries.where(numbersSeries % 2 == 1).dropna(), '\n')
print(numbersSeries.where(numbersSeries > 10).dropna(), '\n')

# POŁĄCZENIE WARUNKÓW SPOSÓB 1
print(numbersSeries.where((numbersSeries % 2 == 1) & (numbersSeries > 10)).dropna(), '\n')

# POŁĄCZENIE WARUNKÓW SPOSÓB 2
print(numbersSeries.where(numbersSeries % 2 == 1).where(numbersSeries > 10).dropna(), '\n')

# POŁĄCZENIE WARUNKÓW SPOSÓB 3
numbersGreater10 = numbersSeries > 10
print(numbersGreater10, '\n')
numbersOdd = numbersSeries % 2 == 1
print(numbersOdd, '\n')

print(numbersSeries.where(numbersGreater10 & numbersOdd), '\n')
print(numbersSeries.where(numbersGreater10 & numbersOdd).dropna(), '\n')


print('\n================================\n')


print(numbersSeries.between(3, 12))
print(numbersSeries.where(numbersSeries.between(3, 12)))
