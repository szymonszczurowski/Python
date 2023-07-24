import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

team = pd.Series(data=[5, 3, 2, 4, 3, 4, 4, 5], index=['Andy', 'Bob', 'John', 'Dirk', 'Francis', 'Ivan', 'Henry', 'Henry'])
print(team)
notes = pd.Series(data=['C', 'B', 'A', 'A+', 'A++'], index=[1, 2, 3, 4, 5])
print(notes)

#Map przypisało wartości z notes na podstawie indexu notes i wartości team. I zamiast liczb mamy litery
teamNotes = team.map(notes)
print(teamNotes)

#Można też przekazać słownik, a nie tylko serie
notesDic = {1: 'A', 2: 'A+', 3: 'A++', 4: 'B', 5: 'C'}
print(notesDic)
teamNotes = team.map(notesDic)
print(teamNotes)