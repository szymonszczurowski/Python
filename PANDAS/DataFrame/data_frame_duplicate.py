import numpy as np
import pandas as pd

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv", usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat'])

color = ['green', 'green', 'blue', 'blue', 'red', 'red', 'white']
size = ['S', 'S', 'S', 'M', 'M', 'M', 'L']
gender = ['M', 'W', 'M', 'W', 'M', 'W', 'U']
clothes = pd.DataFrame({'color': color, 'size': size, 'gender': gender})
print(clothes, '\n')

print(clothes['color'].is_unique) #TRUE/FALSE UNIKLANE
print(clothes['color'].unique()) #ZWRACANIE listy wartości w sposób uniklany
print(clothes['color'].nunique()) #Ilość uniklanych wartośći
print(len(clothes['color'].unique())) #Ilość uniklanych wartośći


clothes.loc[6, 'color'] = np.NaN
print(clothes)
print(clothes['color'].is_unique)
print(clothes['color'].unique())
print(clothes['color'].nunique()) #Nie liczy wartośći null
print(len(clothes['color'].unique())) #Liczy wartośći null

print('\n=======================keep= "first" =========================\n')

# WARTOŚCI POWTARZAJĄCYCH SIĘ
uniqueValues = clothes['color'].duplicated(keep='first') #Pierwszą napotkaną powtarzającą wartość oznacza jako False
print(clothes[~ uniqueValues], '\n')

print('\n=======================keep= "last" =========================\n')

#Ostatnią napotkaną wartość oznacza jako False
uniqueValues = clothes['color'].duplicated(keep='last')
print(clothes[uniqueValues], '\n')

print('\n=======================keep= False =========================\n')

print(clothes['color'].duplicated(keep=False)) #Pozostawia wartości powtarzająće się
uniqueValues = clothes['color'].duplicated(keep=False)
print(clothes[uniqueValues])

print('\n=======================REMOVE=========================\n')

#USUNIĘCIE WARTOŚCI POWTARZAJĄCYCH SIĘ
print(clothes.drop_duplicates(subset=['color'], keep='first'), '\n')

print(clothes.drop_duplicates(['color', 'size']))

print('\n================================================\n')
#wyciąga wszystko co jest zdublowane
uniqueValue = clothes.duplicated(subset=['color'], keep=False)
print(uniqueValue)

print('\n================================================\n')
#pokazuje same unikaty bez dubli
print(clothes.drop_duplicates(subset=['color'], keep=False))
