import numpy as np
import pandas as pd

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv", usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat'])
print(frame.head())

print('\n================================\n')

has400CalOrMore = frame['Calories'] >= 400
print(has400CalOrMore[:5])

print('\n==============WHERE==================\n')

print(frame.where(has400CalOrMore).head()) #Zwróci dane w orginalnym ksztacłcie, wszystkie rekordy, ale tam gdzei warunek jest niespołniony zwróci NaN
print(frame.where(has400CalOrMore).dropna(how='all').head()) #Można skorzystać dropna

print('\n===============FILTROWANIE, przekazanie obiektu serii================\n')
print(frame[has400CalOrMore].head()) #Zwróci rekordy spełniające warunki

print('\n==============QUERY==================\n')
print(frame.query(expr='Category == "Desserts"'), '\n')
print(frame.query(expr='Category in ["Desserts", "Beverages"]'), '\n')
print(frame.query(expr='Category == "Desserts" and Calories < 200'), '\n')