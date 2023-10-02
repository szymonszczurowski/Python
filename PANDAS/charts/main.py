import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bar = pd.read_csv('C:\\Users\\szczu\\Desktop\\data\\course-files\\weather_barcelona.csv', index_col='Date')
rom = pd.read_csv('C:\\Users\\szczu\\Desktop\\data\\course-files\\weather_rome.csv', index_col='Date')
ams = pd.read_csv('C:\\Users\\szczu\\Desktop\\data\\course-files\\weather_amsterdam.csv', index_col='Date')

bar.head()
bar.plot()
plt.show()

bar['TempMax'].plot() #Wyodrębnienie kolumny
plt.show()

bar.plot(y='TempMax')
plt.show()

bar[['TempMax', 'TempMin']].plot()
plt.show()

bar.plot(y=['TempMax', 'TempMin'])
plt.show()
