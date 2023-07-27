import numpy as np
import pandas as pd

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv", usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat'])
print(frame.head())

print('\n================================\n')

#kind = okreśłenie parametru sortownia

print(frame.sort_values(by='Calories').head())

print('\n===============SORTOWANIE WEDŁUG WARTOSCI=================\n')

print(frame.sort_values(by='Calories', ascending=False).head())

print('\n================================\n')

frame['Calories'] = frame['Calories'].astype('float') #Trzeba zrobić konwersję int na float, aby użyć NaN
frame.loc[82, 'Calories'] = np.NAN
print(frame.head())
print('\n')
print(frame.loc[82])

print('\n================================\n')

#Wartość NaN w sortowaniu traktownia jest jako wartość największa
print(frame.sort_values(by='Calories').tail())
#Można zmienić to za pomocą paraamtreu na_position
print(frame.sort_values(by='Calories', na_position='first').head())

print('\n================================\n')

#Sortowanie ze względu na nazwę i kolejno na Item
print(frame.sort_values(by=['Category', 'Item']).head(20))

#Ustawienie klejności sortowania dla każdego osobno, Jedno rosnąco, drugie malejąćo, czyli niezależnie
print(frame.sort_values(by=['Category', 'Item'], ascending=[True, False]).head(20))


print('\n===============SORTOWANIE WEDŁUG INDEX=================\n')

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv", usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat'], index_col='Item')
print(frame.head())

print('\n================================\n')

print(frame.sort_index(ascending=True).head())