import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

surveys = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\StackOverflowDeveloperSurvey.csv", usecols=['CompanySize']).squeeze()
print(surveys.head(), '\n')
print(surveys[3], '\n')
print(surveys[1:11], '\n')
print(surveys[12345], '\n')
print(surveys[12341:12351], '\n')

surveysCopy = surveys.copy()
surveysCopy.sort_values(inplace=True)
print(surveysCopy[3], '\n')
print(surveysCopy[1:11], '\n')
print(surveysCopy[12345], '\n')
print(surveysCopy[12341:12351], '\n')
print(surveysCopy[[3, 12345]], '\n' )

surveysCopy.reset_index(drop=True, inplace=True) #Restowanie indeksu
print(surveysCopy[3], '\n')
print(surveysCopy[1:11], '\n')
print(surveysCopy[12345], '\n')
print(surveysCopy[12341:12351], '\n')

# No cóż, w tym zadaniu zobaczyć można pewien niuans. Sortowanie zmieniło kolejność
# elementów, ale nie przebudowało indeksu. Część poleceń pobiera wartości dokładnie w oparciu
# o indeks, a inne bazują poprostu na kolejności elementów. To dlatego zwracane wyniki były
# pozornie sprzeczne. Wystarczyło jednak przebudować indeks i wszystko zaczęło działać!