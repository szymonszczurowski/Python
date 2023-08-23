import pandas as pd

products = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\WA_Sales_Products_2012-14.csv")
print(products.head(), '\n')

print(products.info())
print(products.describe())
print(products['Retailer country'].value_counts())
print(products['Retailer country'].nunique())

#Wykonanie grupowania ręcznie
countries = products['Retailer country'].unique()
print(countries)
myOwnGroups = {}
for country in countries:
    myOwnSubDataFrame = products.where(products['Retailer country'] == country).dropna()
    myOwnGroups[country] = myOwnSubDataFrame

print(myOwnGroups)
print('\n', myOwnGroups['Belgium'].head())
print(myOwnGroups['Mexico'].describe())