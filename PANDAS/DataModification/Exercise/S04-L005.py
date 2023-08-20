import pandas as pd

fortune = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\Fortune_500_2017.csv",
                      usecols=['Rank', 'Title', 'Industry', 'Hqlocation', 'Sector'])
print(fortune.head(), '\n')

fortune["Sector"] = fortune["Sector"].str.upper()
print(fortune.head(), '\n')

print(fortune[fortune['Industry'].str.lower().str.contains('comp')], '\n')

fortune[['City','State']] = fortune["Hqlocation"].str.split(",",expand=True)
fortune.head()
def BuildShortcut(row):
    industry = row["Industry"]
    result = ''
    for i in industry.split(' '):
        result += i[0]
    return result

print(BuildShortcut({'Industry':'Factory Under Newspaper'}))

fortune['IndustryShort'] = fortune.apply(BuildShortcut,axis=1)
print(fortune.head())