import pandas as pd

products = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\products.csv", usecols=['ProductID', 'ProductName'])
print(products.head(), '\n')

orderedProducts = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\order-details_del.csv", usecols=['OrderID', 'ProductID', 'UnitPrice', 'Quantity'])
print(orderedProducts.head(), '\n')

print('\n################################\n')


#Pokazanie wszystkich prduktów, których nie udało się sprzedać Z użyciem left
merged = products.merge(orderedProducts, on='ProductID', how='left', indicator=True)
print(merged, '\n')
print(merged['_merge'].value_counts())
filter = merged['_merge'] == 'left_only'
print(merged[filter])

print('\n################################\n')

#Pokazanie wszystkich prduktów, których nie udało się sprzedać Z użyciem right
merged = orderedProducts.merge(products, on='ProductID', how='right', indicator=True)
print(merged, '\n')
print(merged['_merge'].value_counts())
filter = merged['_merge'] == 'right_only'
print(merged[filter])
