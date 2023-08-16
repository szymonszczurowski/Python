import pandas as pd

incidents = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Canadian Railway Crossing Incidents.csv")
incidents.set_index(['Region', 'EventType'], inplace=True)
incidents.sort_index(inplace=True)
print(incidents.head(10), '\n')

#Zmiana kolejności indexu, lub zmiana indexu SPOSÓB 1
#Żeby ustawić inny index, trzeba zresetować
incidents.reset_index(inplace=True)
incidents.set_index(['EventType', 'Region'], inplace=True)
incidents.sort_index(inplace=True)

print(incidents.head(10), '\n')

#SPOSÓB 2
#Zmiana kolejności indexu
print(incidents.swaplevel().sort_index().head(), '\n') #i, j = poziomy zamiany multindexu