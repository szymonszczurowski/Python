import pandas as pd

prod1 = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\products.csv", usecols=['ProductID', 'ProductName'], index_col='ProductID')
print(prod1.head(), '\n')

prod2 = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\products.csv", usecols=['ProductID', 'UnitPrice', 'UnitsInStock'], index_col='ProductID')
print(prod2.head(), '\n')

#JOIN DO PROSTSZYCH ŁĄCZEŃ, MERGE TO BARDZIEJ SKOMPLIKOWANYCH SYTUACJI
#JOIN POTRAFI WYSZUKIWAĆ TYLKO PO INDEXIE

#other = data do połączenia, #how - okreśła w jaki sposób łączyć (left, right), ls
print('\n################################\n')
print(prod1.join(prod2).head())


print('\n################################\n')


categories = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\categories1.csv", usecols=['CategoryID', 'CategoryName', 'Description'])
print(categories.head(), '\n')

products = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\products.csv", usecols=['ProductID', 'ProductName', 'UnitPrice', 'CategoryID'])
print(products.head(), '\n')

categories.set_index('CategoryID', inplace=True)
print(categories.head(), '\n')

print('\n################################\n')

print(products.join(categories).head()) #łączy po indeksach i w tym przpadku jest błędnie
print('\n################################\n')
print(products.join(other=categories, on="CategoryID")) #on - okrslę na którą kolumne ma patrzeć join w datyframe products
# któa z kolumn w lewym dataframe powinna być wykorzystana do wyszukiwania w prawym dataframes

