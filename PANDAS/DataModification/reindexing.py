import numpy as np
import pandas as pd

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mammals.csv")
print(frame.head(), '\n')

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mammals.csv", index_col='name')
print(frame.head(), '\n')

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mammals.csv")
print(frame.head(), '\n')

#Ustawienie indexu
frame.set_index('name', inplace=True)
print(frame.head(), '\n')

#Wrócenie do indexu automatycznego
frame.reset_index(inplace=True)
print(frame.head(), '\n')

################################################################

frame.set_index('brain', inplace=True)
print(frame.head(), '\n')

#Ustawienei kolejnego indexu powoduje skasowanie obecnego indexu
frame.set_index('name', inplace=True)
print(frame.head(), '\n')

frame.reset_index(inplace=True)
print(frame.head(), '\n')