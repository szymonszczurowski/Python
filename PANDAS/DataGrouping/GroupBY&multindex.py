import pandas as pd

products = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\WA_Sales_Products_2012-14.csv")
print(products.head(), '\n')

groups = products.groupby(by = ['Retailer country', 'Year']) #Stworzy się multiindex
print(groups.size().head(), '\n')

print(groups.sum(numeric_only=True).head(10), '\n')
print(groups.mean(numeric_only=True).head(10), '\n')
print(groups.get_group(("Australia", 2012)).head())