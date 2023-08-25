import pandas as pd

categories = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\categories1.csv")
print(categories.head(), '\n')

products = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\products.csv")
print(products.head(), '\n')

suppliers = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\suppliers.csv")
print(suppliers.head(), '\n')

customers = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\customers.csv")
print(customers.head(), '\n')


