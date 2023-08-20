import pandas as pd

fb = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mrbean_facebook_statuses_with_nulls.csv")
print(fb.head())

print(fb.info())

fb = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mrbean_facebook_statuses_with_nulls.csv", usecols=["status_message", "status_type", "link_name",
"num_reactions", "num_shares", "num_likes"])

print(fb.info())
print(len(fb))
print(fb['status_type'].nunique())
print(fb["status_type"].value_counts())
fb["status_type"] = fb["status_type"].astype('category')
print(fb["link_name"].nunique())
print(fb["link_name"].value_counts().head())
fb["link_name"] = fb["link_name"].astype('category')
print(fb.info(memory_usage='deep'))

fb["num_reactions"].fillna(0,inplace = True)
fb["num_shares"].fillna(0,inplace = True)

fb["num_reactions"] = fb["num_reactions"].astype('int')
fb["num_shares"] = fb["num_shares"].astype('int')
fb["num_likes"] = fb["num_likes"].astype('int')

print(fb.info(memory_usage='deep'))