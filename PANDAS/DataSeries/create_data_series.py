import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

cities = ['London', 'Berlin', 'Warsaw', 'Paris']
print(cities)

# TWORZENIE OBIKETU SERIES
citiesSeries = pd.Series(cities)
print(citiesSeries)

primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19]
primeSeries = pd.Series(primeNumbers)
print(primeSeries)

logicalValues = [True, False, False, True, False, False]
logicalSeries = pd.Series(logicalValues)
print(logicalSeries)

SpielbergFilmography = {
    'Jaws': 1975,
    '1941': 1979,
    'Indiana Jones and The Raiders of the Lost Ark': 1981,
    'E.T. the Extra-Terrestrial': 1982
}

SpielbergFilmographySeries = pd.Series(SpielbergFilmography)
print(SpielbergFilmographySeries)
