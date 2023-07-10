import math


print(math.pi)
print(math.floor(math.pi))

#wyżej podajemy ścieżke
#inny sposób (nie trzeba odowływać się do za każdym razem do modułu) - czyli umieaszczany je jakby w folderze głownym
print('###########################')

from math import *

print(pi)
print(floor(pi))

#Jednak nazwy mogą być identyczne w różnych modułach, więc lepiej za kazdym razem odowływać się do moduły (1 przykład)

from math import floor
floor(pi)
