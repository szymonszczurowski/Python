import pandas as pd

products = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\products.csv", usecols=['ProductID', 'ProductName', 'CategoryID', 'UnitPrice'])
print(products.head(2), '\n')

categories = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\categories1.csv", usecols=['CategoryID', 'CategoryName', 'Description'])
print(categories.head(2), '\n')

orders = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\order-details.csv")
print(orders.head(2), '\n')

merged = products.merge(categories, on='CategoryID')
print(merged.head(2), '\n')
merged = merged.merge(orders, on='ProductID', suffixes=['_prod', '_order'])
print(merged.head(2), '\n')