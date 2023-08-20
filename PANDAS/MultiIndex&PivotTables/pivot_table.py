import pandas as pd

sales = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\WA_Sales_Products_2012-14.csv")
print(sales.head(), '\n')

#TABELE PRZESTAWNE

print(sales.pivot_table(index='Retailer country', columns=['Year', 'Quarter'], values='Revenue').head(), '\n')

print(sales.pivot_table(index='Retailer country', columns=['Year', 'Quarter'], values='Revenue', aggfunc='sum').head(), '\n')

print(sales.pivot_table(index='Retailer country', columns='Year', values='Revenue').head(), '\n')

print(sales.pivot_table(index='Retailer country', columns='Year', values='Gross margin', aggfunc='min').head(), '\n')

print(sales.pivot_table(index='Retailer country', columns='Year', values='Gross margin', aggfunc=['min', 'max']).head(), '\n')

pivTab = sales.pivot_table(index='Retailer country', columns='Year', values='Gross margin', aggfunc=['min', 'max']).head()
print(pivTab.columns, '\n')

print(pivTab.swaplevel(axis='columns'), '\n')
print(pivTab.swaplevel(axis='columns').sort_index(axis='columns').head(), '\n')

pivTab = pivTab.swaplevel(axis='columns').sort_index(axis='columns')
print(pivTab.head())


