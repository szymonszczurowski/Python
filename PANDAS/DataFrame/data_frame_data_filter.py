import numpy as np
import pandas as pd

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv", usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat'])
print(frame.head())

print('\n================================\n')

print((frame['Calories'] >= 400).head())
print((frame['TotalFat'] <= 20).head())

print('\n================================\n')

caloriesGreaterEqual400 = frame['Calories'] >= 400

print('\n===============caloriesGreaterEqual400=================\n')
print(frame[caloriesGreaterEqual400].head()) #Wyświetlenie rekordów spełniająych ten warunek
print('\n==============totalFatLessEqual20==================\n')
print(frame[frame['Calories'] <= 20].head()) #Wyświetlenie rekordów spełniająych ten warunek

print('\n================isBreakFast, caloriesGreaterEqual400, totalFatLessEqual20================\n')

isBreakFast = frame['Category'] == 'Breakfast'

print(frame[isBreakFast & caloriesGreaterEqual400 & frame['TotalFat'] <= 20].head())

print('\n================================\n')

print(frame[~ isBreakFast].head()) #dania, które nie są śniadaniami ~ zanegowanie
