import pandas as pd

incidents = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Canadian Railway Crossing Incidents.csv")
print(incidents.head(), '\n')

incidents.set_index('Region', inplace=True)
print(incidents.head(), '\n')
print(incidents.index, '\n')

incidents.reset_index(inplace=True)

incidents.set_index(['Region', 'EventType'], inplace=True)
print(incidents.head(), '\n')
print(incidents.index, '\n') #levels  - elemnety innej listy, labels - pozycje wartości w levels

print(incidents.index.get_level_values(0))
print(incidents.index.get_level_values(1))

incidents.index.set_names(['Area', 'Event'], inplace=True)
print(incidents.head(), '\n')
