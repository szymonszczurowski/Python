import pandas as pd
import numpy as np

incidents = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Canadian Railway Crossing Incidents.csv")
incidents.set_index(['Region', 'EventType'], inplace=True)
incidents.sort_index(inplace=True)
print(incidents.head(10), '\n')

#SPOSÓB 1 WYSZUKIWANIA
print(incidents.loc[('Alberta', 'Accidents')], '\n') #Szukanie w peirwszym kluczy Alberata i drugim kluczu Accidents
print(incidents.loc[('Alberta')], '\n')
print(incidents.loc['Alberta'], '\n')

print(incidents.head(10), '\n')
#SPOSÓB 2 WYSZUKIWANIA
print(incidents.iloc[2], '\n')

#SPOSÓB 3/4 WYSZUKIWANIA
print(incidents.loc[('Alberta', 'Accidents')].loc['Public passive'], '\n')
print(incidents.loc[('Alberta', 'Accidents'), 'Public passive'], '\n')

print(incidents.head(), '\n')
