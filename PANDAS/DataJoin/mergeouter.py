import pandas as pd

products = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\products.csv", usecols=['ProductID', 'ProductName'])
print(products.head(), '\n')

orderedProducts = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\order-details_del.csv", usecols=['OrderID', 'ProductID', 'UnitPrice', 'Quantity'])
print(orderedProducts.head(), '\n')

#Pokazanie wszystkich prduktów, których nie udało się sprzedać

merged = products.merge(right=orderedProducts, on='ProductID', how='outer', indicator=True)
print(merged.head(), '\n')
print(merged['_merge'].value_counts())

filter = merged['_merge'] == 'left_only'
print(merged[filter]) #Lista produktów, których nie ma w zamówieniach, które nigdy się nie sprzedały

