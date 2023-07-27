import pandas as pd

mc = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv")
print(mc.head())
print(mc.tail())

mc2 = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv",
                  usecols=['Item', 'Serving Size', 'Calories', 'Calories from Fat', 'TotalFat'])
print(mc2.head())
print(mc2.tail())

mc3 = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv",
                  usecols=['Item', 'Serving Size', 'Calories', 'Calories from Fat', 'TotalFat'], index_col='Item')
print(mc3.head())
print(mc3.tail())
