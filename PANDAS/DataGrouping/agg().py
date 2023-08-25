import pandas as pd

products = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\WA_Sales_Products_2012-14.csv")
print(products.head(), '\n')

#Wyliczenie w standardowy sposób
groups = products.groupby(by = ['Retailer country', 'Year'])
print(groups['Revenue'].sum().head(), '\n')
print(groups['Quantity'].sum().head(), '\n')
print(groups['Gross margin'].sum().head(), '\n')

print('\n################################\n')

print(groups.Revenue.sum().head(), '\n')
print(groups.Quantity.sum().head(), '\n')
# print(groups['Gross margin'].sum().head() '\n') #Nazwa zawiera spacja, wiec nie można uzyskać atrubutu

#Wyliczenie z użyciem agg

# nazwa kolumny, nazwa funckji za pomocą słownika
print(groups.agg({"Revenue" : 'sum'}).head())
print(groups.agg({"Gross margin" : 'sum'}).head())

print('\n################################\n')

#można przekazywać wiele kolumn i funkcji
myAgg = ['sum', 'min', 'max', 'mean']
print(groups.agg({
    "Revenue" :  ['sum', 'min', 'max'],
    'Quantity': myAgg,
    "Gross margin": 'mean'
}).head())


