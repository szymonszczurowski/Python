import numpy as np
import pandas as pd

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv", usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat'])
print(frame.head())
print(frame.dtypes)
print(frame.info(memory_usage='deep')) #paramtetr zwraca dokładną pamięć

frame.loc[1, 'Category'] = np.NAN
print(frame.head())
frame.loc[1, 'Calories'] = np.NAN
print(frame.head())

print(frame.info(memory_usage='deep'))

# frame['Calories'].astype('int') #Bład (nie można konwertować NaN na int)+
frame['Calories'].fillna(value=0, inplace=True)
print(frame.head())
frame['Calories'] = frame['Calories'].astype('int') #Konwersja typu na int

print(frame.info(memory_usage='deep'))

print('\n================================================================\n')

print(frame['Category'].value_counts()) #Zliczanie poszczegółnych kategorii

#stype('category') - wskazuje, że w tej kolumnie powtarzają się pola tekstowe i zastępuje je kolumną category co zmniejsza zużycie pamięci
frame['Category'] = frame['Category'].astype('category') #parametre catagory nie ma związku z nazwą Category z przykładu data frame
print(frame.head())
print(frame.info(memory_usage='deep')) #Zuzycie pamięci się zmniejszyło

print('\n================================================================\n')

frame['Serving Size'] = frame['Serving Size'].astype('category')
print(frame.head())
print(frame.info(memory_usage='deep'))