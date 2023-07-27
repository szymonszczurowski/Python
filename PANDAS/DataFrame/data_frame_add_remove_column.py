import pandas as pd


frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv", usecols=['Item','Category', 'Calories', 'TotalFat', 'Sugars', 'Protein', 'Cholesterol'])
print(frame.head())
print(frame.TotalFat.head())

#Dodawanie kolumn na końcu
frame['TotalFat0'] = 0
print(frame.head())

SugarAndFat = frame.Sugars + frame.TotalFat
frame['SugarAndFat'] = SugarAndFat
print(frame.head())

frame['SugarAndProtein'] = frame.Sugars + frame.Protein

#Dodawnie kolumn na pozycje
frame.insert(loc=2, column='SPF', value=frame.Sugars + frame.Protein + frame.TotalFat) #pozyjca, nazwa, wartości

#USUWANIE
del frame['SugarAndProtein'] #1

frame = frame.drop(columns=['SugarAndFat']) #2

#axis=0 - wiersz, axis=1 - kolumna
frame.drop(labels='TotalFat0', axis=1, inplace=True) #3

frame.drop(columns=['SPF'],  inplace=True) #4

