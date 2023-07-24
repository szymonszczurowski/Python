 # The code snippet imports necessary libraries, reads a CSV file into a pandas DataFrame, and then plots various types of graphs using matplotlib.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

path = 'C:\\Users\\szczu\\PycharmProjects\\pandas\\files\\pokemon.csv'

pokemon_df = pd.read_csv(path)

#Wyrysowanie lini dla 4 wartości
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

#==============================
plt.plot([1, 2, 3, 4],[1,3,9,16], 'ro')
plt.ylabel('some numbers')
plt.show()

#==============================
# tablia,  wartośc startowa, maksymalna wartość, różnica między generowanymi liczbami
t = np.arange(0., 5., 0.2)
print(t)

#==============================
#wartość t (red kreskowane), wartośc t do 2 (blue square), watrtość t do 3 (green trójkąciki)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

#==============================
#Wykres funckji sinus
Min = 0
Max = 4 * np.pi
Step = 0.1


x = np.arange(Min, Max, Step)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('angle')
plt.ylabel('sin(angle)')
plt.show()

