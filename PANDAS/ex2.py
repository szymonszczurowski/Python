import pandas as pd
import random as rd
import numpy as np

fb = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mrbean_facebook_statuses_with_nulls.csv")
print(fb.head())

print(fb.info(memory_usage='deep'))

fb = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\mrbean_facebook_statuses_with_nulls.csv", usecols=[ "status_message", "status_type", "link_name",
"num_reactions", "num_shares", "num_likes"])

print(fb.info(memory_usage='deep'))
print(len(fb))
print(fb["status_type"].value_counts())

fb['status_type'] = fb["status_type"].astype('category')

print(fb.info(memory_usage='deep'))
