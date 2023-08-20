import pandas as pd

professions = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Prestige.csv")

professionsOriginal = professions.copy()
print(professionsOriginal.head(), '\n')

professions.rename(columns={'income' : 'incomeDollarsPerYear'}, inplace=True)
print(professions.head(), '\n')

columnsName = {
    'women':'womenPercent',
    'prestige':'prestigeIndicator'
}
professions.rename(columns=columnsName, inplace=True)
print(professions.head(), '\n')

indexName = {
    'accountants': 'bookkeepers',
    'general.managers':'managers'
}

professions.rename(index=indexName, inplace=True)
print(professions.head(), '\n')
print(professionsOriginal.head(), '\n')
