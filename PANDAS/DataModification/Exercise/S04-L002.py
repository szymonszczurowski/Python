import pandas as pd

professions = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Prestige.csv", index_col='name')
print(professions.head(), '\n')

# professions.loc['chemists', 'type'] = professions[type] = 'scientist'
# print(professions.head(), '\n')

professions.loc["chemists","type"] = 'scientist'
professions.head()

isScientist = (professions["type"] == 'scientist')
print(isScientist.head(), '\n')

professions.loc[isScientist, "income"] = professions["income"] * 1.5
print(professions.head(), '\n')

professions.loc[isScientist, "income"] *= 1.5
print(professions.head(), '\n')
