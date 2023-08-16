import pandas as pd

frame = pd.read_csv('C:\\Users\\szczu\\Desktop\\data\\course-files\\PublicTransitExpenses.csv', usecols=['Agency', 'Reporter Type', 'Total Operating Expenses'])
print(frame.head(), '\n')

#Sprawadza czy występuje przekazany ciąg
print(frame[frame['Agency'].str.contains('washington')], '\n')

frame['Agency'] = frame['Agency'].str.lower()
print(frame[frame['Agency'].str.contains('washington')], '\n')

print('########################################################################')

frame = pd.read_csv('C:\\Users\\szczu\\Desktop\\data\\course-files\\PublicTransitExpenses.csv', usecols=['Agency', 'Reporter Type', 'Total Operating Expenses'])
print(frame[frame['Agency'].str.lower().str.contains('washington')], '\n')


print('########################################################################')

frame = pd.read_csv('C:\\Users\\szczu\\Desktop\\data\\course-files\\PublicTransitExpenses.csv', usecols=['Agency', 'Reporter Type', 'Total Operating Expenses'])

endsWithFerries = frame['Agency'].str.lower().str.strip().str.endswith('ferries')
print(frame[endsWithFerries], '\n')

print('########################################################################')

frame.set_index('Agency', inplace=True)
frame.index = frame.index.str.strip().str.upper()
print(frame.head(), '\n')

print('########################################################################')

print(frame['Reporter Type'].value_counts().head(), '\n')
print(frame['Reporter Type'].str.split(' ').head(), '\n') #Podzielenie Reporter Type na liaste ze względu na spacje
print(frame['Reporter Type'].str.split(' ').str[0].head(), '\n')
print(frame['Reporter Type'].str.split(' ', expand=True).head(), '\n') #zwrócenie odzielnnych kolumn

print('########################################################################')

frame[['ReporterType1', 'ReporterType2']] = frame['Reporter Type'].str.split(' ', expand=True)
print(frame.head(), '\n')

print('########################################################################')

frame['Agency2'] = frame.index
print(frame.head(), '\n')
# n = 10 maksymalnie podział 10 razy np. jak jest więcej niż jedna spacja
print(frame['Agency2'].str.split(' ', expand=True, n=10).head(10), '\n')

print('########################################################################')

def getCommnet(row):
    reportType = row['Reporter Type']
    cost = float(row['Total Operating Expenses'].replace('$', ''))

    if(cost > 200000):
        comment = 'CLASS A'
    else:
        comment = 'CLASS B'
    return (reportType+'/'+comment)

print( frame.apply(getCommnet, axis=1), '\n' )

print(frame.head(), '\n')