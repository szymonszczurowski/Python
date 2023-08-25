import pandas as pd
from pandas import DataFrame

products = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\WA_Sales_Products_2012-14.csv")
print(products.head(), '\n')

groups = products.groupby(by = 'Retailer country')

for country in groups:
    print(country[0])

country_names = []
for country in groups:
    country_names.append(country[0])

for country in groups:
    print(country[1].head())

print('\n################################\n')


#kraj i ilośc wierszy które posiada
for country in groups:
    print(country[0], len(country[1]))

print('\n\n')

#Python pozwala na różne sposoby np. tak:
for country, country_data in groups:
    print(country, len(country_data))


print('\n################################\n')

#Różnica pomiędzy tranzakcją najwyższa i najniższa
for country, country_data in groups:
    print(country,
          country_data['Revenue'].max() - country_data['Revenue'].min())

print('\n############## INNY SPOSÓB ##################\n')
def MaxAndMinDifference(value, column):
    result = value[column].max() - value[column].min()
    return result

for country, country_data in groups:
    print(country, MaxAndMinDifference(country_data, 'Revenue'))

print('\n################################\n')

#NAZWA KRAJU, MAXYMALNA TRANZYACKJA I KOKRETNA TRAZAKCJA(POZYCJA)
for country, country_data in groups:
    print(country,
          country_data['Revenue'].max(),
          country_data['Revenue'].idxmax())

print('\n################################\n')

#NAZWA KRAJU, MAXYMALNA TRANZYACKJA I KOKRETNA TRAZAKCJA(POZYCJA), NAZWA TRANZAKCJI
for country, country_data in groups:
    print(country,
          country_data['Revenue'].max(),
          country_data['Revenue'].idxmax(),
          country_data.loc[country_data['Revenue'].idxmax()])


print('\n################################\n')
#NAZWA KRAJU, MAXYMALNA TRANZYACKJA I KOKRETNA TRAZAKCJA(POZYCJA), NAZWA TRANZAKCJI

the_biggest = pd.DataFrame()
for country, country_data in groups:
    the_biggest =  pd.concat([the_biggest, country_data.loc[country_data['Revenue'].idxmax()]])

print(the_biggest.head())

print('\n################################\n')

#Proszty sposób z uzyciem nlargest
print(products.nlargest(1, 'Revenue'))

the_biggest = pd.DataFrame()
for country, country_data in groups:
    the_biggest =  pd.concat([the_biggest, country_data.nlargest(1, 'Revenue')])

print(the_biggest.head())