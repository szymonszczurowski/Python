import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math


# W kolejnej lekcji pojawia się opcja queeze. W nowszej wersji PANDAS należy używać metody squeeze():
# Nowa składnia to
# pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Speed']).squeeze()

obj = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv")
# usecols - Wskazuje kolumne która ma być przeczytana,
# .squeeze - ściśnij, jeśli dane będa miałe 1 kolumne to zwróci obiekt serii
obj2 = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Name']).squeeze()

print(type(obj))
print(type(obj2))

speed = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Speed']).squeeze()

# #Wczytanie ze schowka
# dataFromClipboard = pd.read_clipboard(sep=',')
# oneSeries = dataFromClipboard['Name']
# print(type(oneSeries))

print(speed.head()) # 5 pierwszych rekordów
print(speed.tail()) # 5 ostatnich rekordów

obj3 = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Name']).squeeze().head(3)
print(obj3.size)