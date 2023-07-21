import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

pok = pd.read_csv("C:\\Users\\szczu\\Desktop\\data\\course-files\\pokemon.csv", usecols=['Name']).squeeze()

print(pok[73], '\n')
print(pok[[64, 73]], '\n') #jeżeli kilka wartości po indkesie to trzeba podać listę w liście
print(pok[2:7], '\n') #od 2 do 7 - 1
print(pok[795:], '\n') #od 795 do końca
print(pok[:4], '\n') #od początku do 4 - 1
print(pok[-2:], '\n') #szukanie od końca