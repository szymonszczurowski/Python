import pandas as pd

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv")
series = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv", usecols=['Item', 'Calories'], index_col='Item').squeeze()

print(frame.head())
print(series.head())

print('////////////////////////////////')

#Ilośc elementów
print(series.count(), '\n================================')
print(frame.count(), '\n') #Urcuhamia się dla każdej kolumny niezależenie. Określa ilosć znanych elementów czyli nie Nan

#Ilość elementów zawsze
print(len(series), '\n================================')
print(len(frame), '\n')

#Typ
print(series.dtypes, '\n================================')
print(frame.dtypes, '\n') #Dla każdej odzielnie

# print(series.dtypes.value_counts())
print(frame.dtypes.value_counts(), '\n') # wyświetla ilość wystepownia typów

#Określenie wymiarowości wiersze/kolomny. Kształ danych
print(series.shape, '\n================================')
print(frame.shape, '\n')

#Informacje na temat indexu i kolumny
print(series.axes, '\n================================')
print(frame.axes, '\n') #lista opisującą index i liste opisującą kolumny

print(series.index, '\n================================')
print(frame.index, '\n')

# print(series.columns, '\n================================')
print(frame.columns, '\n') #Opis nazw kolumn

#Zwrócenie wartości
print(series.values, '\n================================')
print(frame.values, '\n') #w postaci list

#Info o indexie, typy kloumn, podstawowe info. Sporo w jednym miejscu
print(series.info(), '\n================================')
print(frame.info(), '\n')

#Ile razy w okreśłonej kolumnie wysępują okreśłone wartości
print(series.value_counts(), '\n================================')
# print(frame.value_count(), '\n') #Dla całości nie możan wywołąć
print(frame['Category'].value_counts(), '\n')

# wylosowanie kilku różnych wartości
print(series.sample(), '\n================================')
print(frame.sample(), '\n')
print(frame.sample(n=4), '\n')
print(frame.sample(n=3, axis='columns').head(), '\n')
print(frame.sample(frac=0.02).head(), '\n') #Wskazaie procentowo ile ma wyświetlić