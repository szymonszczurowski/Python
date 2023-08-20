import pandas as pd

pt = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\WA_Sales_Products_2012-14.csv")
print(pt.head(), '\n')

#Zakłdamy, ze dane wczytane mają postać tabeli przestawnej i chcemy zrobić z niego data frame

pt = pt.pivot_table(index='Retailer country', columns='Year', values='Revenue', aggfunc='sum')
print(pt.head(), '\n')

pt.reset_index(inplace=True)
print(pt.head(), '\n')

#Brak zapisu w jakimś miejscu, więc zamieniamy wartosc na 0 zamiastg NaN
pt.fillna(0, inplace=True)

df = pt.melt(id_vars='Retailer country', var_name='YearOfTransaction', value_name='RevenueSum')
print(df.head(), '\n')

df = pt.melt(id_vars='Retailer country',value_vars=[2012, 2013], var_name='YearOfTransaction', value_name='RevenueSum')
print(df.head(), '\n')

upvt = pt.unstack().to_frame().swaplevel()
upvt.columns=['RevenueSum']
print(upvt.head())


#Unstack - lepiej jak coś ulepszamy/poprawiamy na bieżąco, melt - lepiej jak wczytuje coś w postaci tabeli przestawnej