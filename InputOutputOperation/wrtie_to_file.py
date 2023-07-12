import os

filename = os.path.join(os.getcwd(), 'output.csv')

line = 'Europe'

cities = ['London', 'Berlin', 'Paris', 'Warsaw', 'Madrid', 'Rome']

file = open(filename, 'w') #w - wrtie zapi, a (append)- dopisane
file.write(line)
file.write('\n') #Zapis danych do pliku
#file.writelines(cities) #Dopisanie listy wartości do pliku
for city in cities:
    file.write(city+'\n')

file.close()

################################################################

file = open(filename, 'a') #w - wrtie zapi, a (append)- dopisane
file.write(line)
file.write('\n') #Zapis danych do pliku
#file.writelines(cities) #Dopisanie listy wartości do pliku
for city in cities:
    file.write(city+'\n')

file.close()

################################################################


file = open(filename, 'w+') #w - wrtie zapi, a (append)- dopisane, w+ - plik otwarty do odczytu i zapisu, można mieszać czytanie i zapis
file.write(line)
file.write('\n') #Zapis danych do pliku
#file.writelines(cities) #Dopisanie listy wartości do pliku
for city in cities:
    file.write(city+'\n')

file.close()

################################################################

file = open(filename, 'a+') #w - wrtie zapi, a (append)- dopisane, w+ - plik otwarty do odczytu i zapisu, można mieszać czytanie i zapis i dodajemy rzeczy bez kasowania zawartości
file.write(line)
file.write('\n') #Zapis danych do pliku
#file.writelines(cities) #Dopisanie listy wartości do pliku
for city in cities:
    file.write(city+'\n')

file.close()
