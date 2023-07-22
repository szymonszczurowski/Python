import pandas as pd
import numpy as np
import math as math
import matplotlib.pyplot as plt

index = ['a', 'b', 'c', 'd', 'e1', 'e2']
index2 = ['a', 'b', 'c', 'd', 'e', 'e']
values = ['Austria', 'Belgium', 'Canada', 'Denmark', 'England', 'Estonia']
values2 = ['Austria', 'Belgium', 'Canada', 'Denmark', 'England', 'Estonia']
s = pd.Series(data = values, index = index)
s2 = pd.Series(data = values, index = index)


searchList = ['a', 'b']
print(s.loc[searchList], '\n')

searchListNonFound = ['a', 'b', 'f']
# print(s.loc[searchListNonFound])

# reindex - zwrócenie nowej serii, brane są pod uwage wszystkie elemnty, którę znajdują się na liście argumentu (nie może być duplikatów)
print(s.reindex(searchList), '\n')
# print(s2.index.intersection(searchList), '\n')

# intersection - zwrócenie listy elementów występującej w jednej i w drugiej liście, czyli wartość wspólną
print(s.index.intersection(searchList), '\n')
print(s.index.intersection(searchListNonFound), '\n')
print(s2.index.intersection(searchList), '\n')