import pandas as pd
import numpy as np

animals = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\sleep_time.csv", index_col='ID').dropna()


print(animals.where(animals['vore'] == 'herbi').dropna())
