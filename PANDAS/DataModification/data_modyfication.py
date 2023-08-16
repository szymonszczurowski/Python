import pandas as pd

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\insurance.csv")
print(frame.head(), '\n')

#1
frame.loc[2, 'Claims'] = 19
print(frame.head(), '\n')

#2
frame.loc[2, 'Claims'] = frame.loc[2, 'Claims'] + 2
print(frame.head(), '\n')

#3
frame.loc[2, 'Claims'] -= 1
print(frame.head(), '\n')

print(frame['Age'] == '<25')

isYounger25 = frame['Age'] == '<25'
print(frame.where(isYounger25).dropna().head())
print(frame[isYounger25].head())

print(frame.loc[isYounger25, 'Holders'].head()) #Warunek, Nazwa kolumny
print(frame.loc[isYounger25, 'Holders'] + 100)

#4 Zmiana danych w miejscach, które spełniają warunki
frame.loc[isYounger25, 'Holders'] = frame.loc[isYounger25, 'Holders'] + 100
print(frame.head())

#Prostszy zapis ^^^
frame.loc[isYounger25, 'Holders'] = frame['Holders'] + 100
print(frame.head())

#Prostszy zapis ^^^
frame.loc[isYounger25, 'Holders'] += 1000
print(frame.head())
