import pandas as pd

products = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\WA_Sales_Products_2012-14.csv")
print(products.head(), '\n')

data = products.groupby(by='Retailer country')
print(data.mean(numeric_only=True).head())
print(data.sum().head())
print(data.count().head())
print(data.min().head())
print(data.max().head())

print('\n################################\n')

print(data['Revenue'].sum().head())
print(data[['Revenue', 'Quantity']].sum().head())
