import numpy as np
import pandas as pd

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\sleep_time.csv")
print(frame.head(), '\n')

#USUWANIE KOLUMN
del frame['bodywt']
frame.drop(axis=1, columns=['awake', 'brainwt'], inplace=True)
# frame.drop(axis='column', columns=['awake', 'brainwt'], inplace=True)
frame.drop(columns=['order'], inplace=True)
print(frame.head(), '\n')

#USUWANIE WIERSZY // Domyślne axis = 0

frame.drop(axis=0, labels=[1, 2], inplace=True)
frame.drop(axis='rows', labels=3, inplace=True)
frame.drop(labels=4, inplace=True)
frame.drop(5, inplace=True)
print(frame.head(), '\n')

# DODOWANIE WIERSZY
new_row_dict = {
    'ID': 3,
    'name': 'Panda3',
    'genus': np.NaN,
    'vore': np.NaN,
    'conservation': np.NaN,
    'sleep_total': 10,
    'sleep_rem': 11,
    'sleep_cycle': 12
}

new_row_df = pd.DataFrame([new_row_dict])
print(new_row_df)

professions = pd.concat([frame, new_row_df], ignore_index=True)
print(professions.tail())

subset = frame[0:5]
frame = pd.concat([frame, subset], ignore_index=True)
print(frame.tail())
