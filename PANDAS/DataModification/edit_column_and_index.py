import pandas as pd

frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mammals.csv")

print(frame.head(), '\n')
print(frame.columns, '\n')

################################################################

#ZMIANA NAZWY KOLUMNY #1 przy użyciu listy
frame.columns = ['name', 'bodyKg', 'brainKg']
print(frame.head(), '\n')

# professions.rename(columns={'income' : 'incomeDollarsPerYear'}, inplace=True)

#ZMIANA NAZWY KOLUMNY #1 przy użyciu listy słownika. Można modyfikować np. 1 nazwe kolumny w listach trzeba wszystko nazwać
newColumnNames = {
    'bodyKg': 'body_kg',
    'brainKg': 'brain_kg'
}
frame.rename(columns=newColumnNames, inplace=True)
print(frame.head(), '\n')

################################################################


frame = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mammals.csv", index_col='name')

#ZMIANA WARTOŚĆ INDEXU #1
frame.rename(index = {'Cow': 'Land cow'}, inplace=True)
print(frame.head(), '\n')

################################################################

frameCopy = frame.copy()
frameCopy.loc['Arctic fox', 'body'] = 5 #ZMIANA WARTOŚCI W KOLUMNY body DLA Wiersza o wartości indexu ArcitcFox
print(frameCopy.head(), '\n')
