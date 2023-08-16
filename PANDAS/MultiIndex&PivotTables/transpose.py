import pandas as pd

incidents = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Canadian Railway Crossing Incidents.csv")
incidents.set_index(['Region', 'EventType'], inplace=True)
incidents.sort_index(inplace=True)
print(incidents.head(10), '\n')

print(incidents.count(), '\n')
print(len(incidents), '\n')

#TO co w kolumnach jest teraz w wierszach to co w wierszach jest w kolumnach
print(incidents.transpose())

events = incidents.transpose()
print(events.head(), '\n')
print(events.loc['Private'], '\n')

print(events.loc['Public passive', ('Manitoba', 'Accidents')], '\n')
print(events.iloc[0, 5], '\n')

#W DRUGĄ STRONE

print(events.transpose())
