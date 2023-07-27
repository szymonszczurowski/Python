import numpy as np
import pandas as pd

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv")
frame.loc[1, 'Calories'] = np.NAN
frame.loc[2, 'Calories'] = np.NAN

print(frame.dropna().head())  # usunęło rekordy z NAN

print('\n==============how==================\n')

print(frame.dropna(how='all'))
# how='all - usunie, jeśli wszystko zawiera nan

# how='any' - oznacza to, ze jeśli w rekodzie chociąz jest jeden nan ma usunąć cały rekord

print('\n===============subset=================\n')

frame.loc[2, 'TotalFat'] = np.NAN

# subset określa, to które kolumny mają zostać sprawdzone
print(frame.dropna(subset=['TotalFat'], how='any'))

print('\n===============axis=================\n')

#axis określa czy analuzujemy wiersz wiersz czy kolumne 0-wiersz, 1-kolumna, można też słownie
print(frame.dropna(axis='rows'))

print('\n===============axis=================\n')

print(frame.dropna(axis='columns')) #usunęło kolumny

print('\n===============inplace=================\n')

#inplace modyfikuje obiket wewnątrz obiektu zamiast robienia kopii
frame.dropna(inplace=True)
print(frame)