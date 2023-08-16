import pandas as pd

frame = pd.read_csv('C:\\Users\\szczu\\Desktop\\data\\course-files\\PublicTransitExpenses.csv', low_memory=False)
#low_memory=False - zgoda na wczytanie całego pliku do pamięci i analiza typu danych, pliku

print(frame.info(memory_usage='deep'))
#Sprawdzenie typów danych

frame = pd.read_csv('C:\\Users\\szczu\\Desktop\\data\\course-files\\PublicTransitExpenses.csv',
                    usecols=['Agency', 'Reporter Type', 'Organization Type', 'Rail (Y/N)', 'Service Costs', 'Tires and Tubes', 'Total Operating Expenses', 'Service Area Population'])
#Określenie kolumn, które potrzebujemy
print(frame.info(memory_usage='deep'))

newColumndNames = {
    'Agency' : 'Agency',
    'Reporter Type' : 'ReporterType',
    'Organization Type': 'OrganizationType',
    'Rail (Y/N)': 'IsRail',
    'Service Costs' : 'ServiceCosts',
    'Tires and Tubes' : 'TiresTubesCosts',
    'Total Operating Expenses' : 'TotalExpenses',
    'Service Area Population' : 'Population'
}

frame.rename(columns=newColumndNames, inplace=True)
#Zmiana nazw kolumn za pomocą słownika
print(frame.head())

print('\n################################\n')

print(frame['ReporterType'].nunique())
#Ilosc unikalnych wartosci

print('\n################################\n')

print(frame['ReporterType'].count())
#Zliczanie wszystkch wartosci

print('\n################################\n')

print(frame['ReporterType'].value_counts())
#Zliczenie konkretnych wartoci

print('\n################################\n')

frame['ReporterType'] = frame['ReporterType'].astype('category')
frame['OrganizationType'] = frame['OrganizationType'].astype('category')
frame['Agency'] = frame['Agency'].astype('category')
print(frame.info(memory_usage='deep'))

#Zamiana NaN na 0
frame['Population'].fillna(0, inplace=True)
#Zamiana typu float na int
frame['Population'] = frame['Population'].astype('int')

print(frame[frame['Population'] > 0].head())
print(frame.info(memory_usage='deep'))


print('\n################################\n')


frame['IsRail'].replace(('Y', 'N'), (True, False), inplace=True)
frame['IsRail'] = frame['IsRail'].astype('bool')

print(frame.head())
print(frame.info(memory_usage='deep'))

#ZamianA wartosci niezanych na False
frame['IsRail'].fillna(False, inplace=True)
frame['IsRail'] = frame['IsRail'].astype('bool')

print(frame.head())
print(frame.info(memory_usage='deep'))

print('\n################################\n')

frame['ServiceCosts'] = frame['ServiceCosts'].str.replace('$', '', regex=True)
frame['TiresTubesCosts'] = frame['TiresTubesCosts'].str.replace('$', '', regex=True)
frame['TotalExpenses'] = frame['TotalExpenses'].str.replace('$', '', regex=True)

frame['ServiceCosts'] = frame['ServiceCosts'].astype('float')
frame['TiresTubesCosts'] = frame['TiresTubesCosts'].astype('float')
frame['TotalExpenses'] = frame['TotalExpenses'].astype('float')

print(frame.head())
print(frame.info(memory_usage='deep'))

frame['Agency'] = frame['Agency'].str.title().astype('category')
frame['ReporterType'] = frame['ReporterType'].str.upper().astype('category')
frame['OrganizationType'] = frame['OrganizationType'].str.upper().astype('category')

print(frame.head())
print(frame.info(memory_usage='deep'))