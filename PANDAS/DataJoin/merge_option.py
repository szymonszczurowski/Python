import pandas as pd

products = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\products.csv", usecols=['ProductID', 'ProductName', 'CategoryID', 'UnitPrice'])
print(products.head(), '\n')

categories = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\categories1.csv", usecols=['CategoryID', 'CategoryName', 'Description'])
print(categories.head(), '\n')

merged = products.merge(categories, on='CategoryID')
print(merged.head())

print('\n################################\n')

#INNA NAZWA KOLUMNY
categories.rename({'CategoryID': 'ID'}, axis=1, inplace=True)
print(categories.head())
# merged = products.merge(categories, on='CategoryID')
# print(merged.head())

#Jedna z metod naprawy
merged = products.merge(categories, left_on='CategoryID', right_on='ID') #Wskazanie kolumn dla lewej i prawej strony
print(merged.head())

print('\n################################\n')

#DWIE TAKIE SAME NAZWY KOLUMN
products.rename({'ProductName': 'Name'}, axis=1, inplace=True)
categories.rename({'CategoryName': 'Name'}, axis=1, inplace=True)

merged = products.merge(categories, left_on='CategoryID', right_on='ID') #Sytuacja rozwiązuje się atomatycznie i przypisuje suffix, ale można określić go samemu
print(merged.head())

merged = products.merge(categories, left_on='CategoryID', right_on='ID', suffixes=['_prod', '_category']) #Sytuacja rozwiązuje się atomatycznie i przypisuje suffix, ale można określić go samemu
print(merged.head())

print('\n################################\n')

#Wykonanie złączenia w oparciu o index, nic nie trzeba robić, bo samo się robi
categories.set_index('ID', inplace=True)

merged = products.merge(categories, left_on='CategoryID', right_on='ID', suffixes=['_prod', '_category'])
print(merged.head())

print('\n################################\n')

#SORTOWANIE, dane sortowane są według klucza złączenia
merged = products.merge(categories, left_on='CategoryID', right_on='ID', suffixes=['_prod', '_category'], sort=True)
print(merged.head())
