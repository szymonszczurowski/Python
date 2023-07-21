import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math


obj = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Name']).squeeze()


print(obj.head(), '\n')
print(obj.sort_values().head(), '\n') #posortowanie
print(obj.sort_values(ascending=False).head(), '\n') #posortowanie malejąco

#Sortowanie po wartościach
obj_copy = obj.copy()
obj_copy.sort_values(inplace=True) #inplace, czyli np. sortowanie odbywa się wewnętrznie
print(obj_copy.head(), '\n')

#Sortowaniie po indexach
print(obj.sort_index().head(), '\n')
pok = obj.sort_index(ascending=False)
print(pok.head(), '\n')