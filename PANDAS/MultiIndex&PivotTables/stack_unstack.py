import pandas as pd

incidents = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Canadian Railway Crossing Incidents.csv")
incidents.set_index(['Region', 'EventType'], inplace=True)
incidents.sort_index(inplace=True)
print(incidents.head(10), '\n')

#Zamienianie kolejnosci kolumn

#stack() - najbardziej wenwtrzny poziom kolumn przepisuje do wierszy
print(incidents.stack(), '\n') #Obiekt serii
print(incidents.stack().to_frame(), '\n') #Obiekt data frame


stackedIncidents = incidents.stack().to_frame()
print(stackedIncidents.unstack().head(), '\n')
print(stackedIncidents.unstack().unstack().head(), '\n') #Umltindex już nim nie jest
print(stackedIncidents.unstack(0).head(), '\n') #za pomocą level można okreśłić, który poziom ma być użyty
print(stackedIncidents.unstack(level = 'Region').head(), '\n') #można użyć nazwy

print(stackedIncidents.head())
print(stackedIncidents.unstack(level=['Region', 'EventType']))

print(stackedIncidents.loc[('Alberta', 'Accidents', 'Private'), 0])

