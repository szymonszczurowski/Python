import pandas as pd

cat1 = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\categories_del_1.csv", usecols=['CategoryID', 'CategoryName'])
print(cat1.head(), '\n')

cat2 = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\categories_del_2.csv", usecols=['CategoryID', 'CategoryName'])
print(cat2.head(), '\n')

print(cat1.merge(cat2)) #Pozostaje tyko część wspólna
print(cat1.merge(cat2, on='CategoryID')) #Połączenie w oparciu na kolumny CategoryID (można również index) i tworzą się dwe kolumny x-y z pozostałych danych,
# ale dalej część wspołna
print(cat1.merge(cat2, on='CategoryID', suffixes=['_1', '_2'])) #To co wyżej, ale z określonym suffixem
print(cat1.merge(cat2, on='CategoryID', suffixes=['_1', '_2'], how='outer')) #how przyjmuje kilka opcji: inner- część współna (w tym przypadku categoryID
#left - wszystkie wiersze występujące po lewej stronie, #right - po prawej stronie, #outer - suma wierszy left i right (wiersz, którego nie ma w jedym dostaje NaN)

#W przypadku dnaych zaśmieconych np. NaN
print(cat1.merge(cat2, on='CategoryID', suffixes=['_1', '_2'], how='outer', indicator=True))
# indicator - wskazuje z kąd wziął się wiersz, #both- po lewj i po prawej stronie

cat_merged = cat1.merge(cat2, on='CategoryID', suffixes=['_1', '_2'], how='outer', indicator=True)

#Wfilrowanie danych występujących tylko po lewej
filter = cat_merged["_merge"] == "left_only"
print(filter)
print(cat_merged[filter])

#Wfilrowanie danych występujących tylko po prawej
filter = cat_merged["_merge"] == "right_only"
print(filter)
print(cat_merged[filter])

#Wfilrowanie danych występujących tylko po obydwu
filter = cat_merged["_merge"] == "both"
print(filter)
print(cat_merged[filter])

#Wszystki wartości występująće po lewej stronie
print(cat_merged = cat1.merge(cat2, on='CategoryID', suffixes=['_1', '_2'], how='left', indicator=True))
#Wszystki wartości występująće po prawej stronie
print(cat_merged = cat1.merge(cat2, on='CategoryID', suffixes=['_1', '_2'], how='right', indicator=True))