import pandas as pd

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv")
series = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv", usecols=['Item', 'Calories'], index_col='Item').squeeze()

print(type(frame))
print(type(series))

#Atrubuty to serie, więc można korzystać z metod serii
print(frame.Calories)
print(type(frame.Calories))
print(frame.Calories.mean())
print(frame.Calories.median())
print(frame.Calories.max())
print(frame.Calories.idxmax())
print(frame.Item[82])
print(frame.Item[frame.Calories.idxmax()])
#Tak samo jak wyżej
print(frame['Calories'].head())

s = frame['Item']
print(type(s))
print(s[242])
print(s.loc[242])
print(frame['Item'][242]) #Kolumna i index
print(frame.loc[242].loc['Item']) #index i kolumna

#Można  łączyć najpierw wartość indeksie, a potem informacje o kolumnie
print(frame.loc[242, 'Item'])

print(frame[['Item','Calories', 'TotalFat', 'Sugars']].head())