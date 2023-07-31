import numpy as np
import pandas as pd

color = ['green', 'green', 'blue', 'blue', 'red', 'red', 'white']
size = ['S', 'S', 'S', 'M', 'M', 'M', 'L']
gender = ['M', 'W', 'M', 'W', 'M', 'W', 'U']
clothes = pd.DataFrame({'color': color, 'size': size, 'gender': gender})
print(clothes)

print('\n=======================Filtorwanie Sposób 1=========================\n')
isColorBlue = clothes['color'] == 'blue'
isColorGreen = clothes['color'] == 'green'
isColorRed = clothes['color'] == 'red'
print(clothes[isColorBlue | isColorGreen | isColorRed])

print('\n=======================Filtorwanie Sposób 2=========================\n')
myColors = clothes['color'].isin(['blue', 'green', 'red'])
print(clothes[myColors])

clothes.loc[6, 'size'] = np.NAN
print('\n=======================Filtorwanie Sposób 3 - zwrórci tylko produkty bez NaN=========================\n')
hasSize = clothes['size'].notnull()
print(clothes[hasSize])

print('\n=======================Filtorwanie Sposób 4 - zwrórci tylko produkty z NaN=========================\n')
sizeUnknown = clothes['size'].isnull()
print(clothes[sizeUnknown])

print('\n=======================Filtorwanie Sposób 5 - Zwrca wartośći pomiędzy=========================\n')
frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mcdonalds.csv",
                    usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat'])
caloriesBetween = frame['Calories'].between(300, 400)
print(frame[caloriesBetween])
