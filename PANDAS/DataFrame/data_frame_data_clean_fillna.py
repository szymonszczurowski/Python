import numpy as np
import pandas as pd

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv")

frame.loc[1, 'TotalFat'] = np.NaN
frame.loc[1, 'Saturated Fat'] = np.NaN
frame.loc[2, 'Saturated Fat'] = np.NaN
frame.loc[3, 'Category'] = np.NaN

print(frame.head())

print('\n================================\n')

# value - pozwala na wstawianie wartości w miejsca gdzie nie ma wartości (NaN)
print(frame.fillna(value=0).head())

print('\n================================\n')

#WYKORZYSTANIA SŁOWNIKA DO PRZYPISANA RÓŻNYCH WARTOŚCI DO RÓŻNYCH KOLUMN
replaceDefinitionTable = {'Category': 'UNKNOW',
                          'TotalFat': 0,
                          'SaturatedFat': 0}

print(frame.fillna(value=replaceDefinitionTable).head())

print('\n================================\n')

#Dla konkrentej kolumny
frame['Category'].fillna(value='UNKNOW', inplace=True)
print(frame.head())
frame['TotalFat'].fillna(value=0, inplace=True)
frame['Saturated Fat'].fillna(value=0, inplace=True)

print('\n================================\n')

#Zastąpienie brakujących dnaych średnią z kolumny
frame.loc[1, 'TotalFat'] = np.NaN
frame.loc[1, 'Saturated Fat'] = np.NaN
frame.loc[2, 'Saturated Fat'] = np.NaN
frame.loc[3, 'Category'] = np.NaN

avgTotalFat = frame['TotalFat'].mean()
print(avgTotalFat)
frame['TotalFat'].fillna(avgTotalFat, inplace=True)
print(frame.head())

print('\n================================\n')

# Method udostępnia różne metody, ffill - forward fill, bfill - backward fill
frame['Saturated Fat'].fillna(method='ffill', inplace=True) #Zasątpienie wartośći pierwszą poprzednią poprawną wartością
print(frame)