import pandas as pd
import numpy as np

animals = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\sleep_time.csv", index_col='ID').dropna()


herbi = animals.where( animals['vore'] == 'herbi')
print(len(herbi))
herbi = animals.where( animals['vore'] == 'herbi').dropna()
print(len(herbi))

carni = animals.where( animals['vore'] == 'carni')
print(len(carni))
carni = animals.where( animals['vore'] == 'carni').dropna()
print(len(carni))

omni = animals.where( animals['vore'] == 'omni')
print(len(carni))
omni = animals.where( animals['vore'] == 'omni').dropna()
print(len(carni))

print('carni mean sleep time:', carni['sleep_total'].mean())
print('herbi mean sleep time:', herbi['sleep_total'].mean())
print('omni mean sleep time:', omni['sleep_total'].mean())

print(animals.query("sleep_total > 14"))
print(animals.query("sleep_total > 14 and vore == 'herbi'"))
print(animals.query("sleep_total > 14 and vore == 'herbi' and bodywt > 1"))