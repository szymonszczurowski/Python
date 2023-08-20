import pandas as pd
import numpy as np

professions = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Prestige.csv")
print(professions.head())

dict = {
    'name': 'data scientist',
    'education' : np.NaN,
    'income' : np.NaN,
    'women' : np.NaN,
    'prestige' : np.NaN,
    'census' : np.NaN,
    'type' : np.NaN
}

dict = pd.DataFrame([dict])
frame = pd.concat([professions, dict], ignore_index=True)
print(frame.tail())

taxi = professions[professions["name"]=='taxi.drivers']
print(taxi.head())

professions.drop(98, inplace=True)
print(professions.tail())

del professions ["census"]
print(professions.tail())

professions.drop(columns='type', inplace=True)
print(professions.tail())