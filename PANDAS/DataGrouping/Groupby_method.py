import pandas as pd

products = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\WA_Sales_Products_2012-14.csv")
print(products.head(), '\n')
#by - kolumna/lista kolumn względem, której ma być grupwanie
groups = products.groupby(by="Retailer country")
print(type(groups))
print(len(groups))
print(groups.size())

print('\n################################\n')

print(groups.first().head()) #Z każdej grupy wyciąga pierwszy wiersz
print('\n################################\n')
print(groups.last().head()) #Z każdej grupy wyciąga ostatni wiersz
print('\n################################\n')
print(groups.groups) #Atrybut jakie grupy zostały zindentyfikowane

print('\n################################\n')

print(products.loc[groups.groups['Belgium']].head())
#PROŚCIEJ
print(groups.get_group('Belgium').head())