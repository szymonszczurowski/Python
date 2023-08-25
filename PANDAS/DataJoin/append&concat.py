import pandas as pd

suppliers = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\suppliers.csv", usecols=['SupplierID', 'CompanyName', 'Country'])
print(suppliers.head(), '\n')

customers = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\northwind-mongo-master\\customers.csv", usecols=['CustomerID', 'CompanyName', 'Country'])
print(customers.head(), '\n')

print(len(suppliers))
print(len(customers))

#append zostanie usunięte
print(suppliers.append(customers))
df_appended = suppliers.append(customers)
print(len(df_appended))
print(df_appended.head(40))

suppliers2= suppliers.copy()
customers2 = customers.copy()

suppliers2.rename({'SupplierID': 'CustomerID'}, axis=1, inplace=True)
print(suppliers2.head())

print(suppliers2.append(customers2))
df_appended2 = suppliers2.append(customers2)
print(len(df_appended2))
print(df_appended2.head(40))

#AKTUALNE
df_concatenated = pd.concat(objs=[suppliers, customers])
print(len(df_concatenated))
print(df_concatenated.head(40))

####
df_concatenated = pd.concat(objs=[suppliers, customers], ignore_index=True)
print(len(df_concatenated))
print(df_concatenated.head(40))

####
df_concatenated = pd.concat(objs=[suppliers2, customers], ignore_index=True )
print(len(df_concatenated))
print(df_concatenated.head(40))