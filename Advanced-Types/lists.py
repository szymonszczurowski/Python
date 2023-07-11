 # The code snippet demonstrates various operations on a list called "countries". It shows how to access elements, change values, add and remove elements, sort and reverse the list, find the index and count of elements, extend the list with another list, create
countries = ['FR', 'US', 'DE', 'NE', 'PL']

print("długość listy:", countries.__len__())
print("długość listy:", len(countries))
print("elment o indeksie:", countries[4])

# Zmiana wartości elemntu na pozycji 2
print('Lista przez zmianą elemntu:', countries)
countries[2] = 'IL'
print('Lista po zmianie elemntu:', countries)

countries.append('KC')  # dodawnie elmentu na koniec listy
print('Lista po dodaniu elemntu:', countries)

countries.insert(2, 'ES')  # dodawnie elemntu na konkretnej pozycji
print('Lista po dodaniu elemntu na pozycji 2 (ES):', countries)

countries.remove("IL")  # kasowanie elements
print('Lista po skasowaniu elemntu (IL):', countries)

countries.sort()  # sortowanie
print('Lista po sortowaniu:', countries)

countries.reverse()  # odwrócenie listy
print('Lista po odwróceniu: ', countries)

print(countries.pop())  # Zwraca wartość z ostaniej pozyacji i kasuje z listy
print('Lista po zdjęciu elementu z ostaniej pozycji za pomocą pop()', countries)

print(countries.pop(2))  # Zwraca wartość ze wskazanej pozycji i ją skasuje
print('Lista po zdjęciu elementu z 2 pozycji za pomocą pop()', countries)

print('Zwrócenie indexu elemntu PL z listy:', countries.index('PL'))  # sprawdzenie pozycji elementu

print('Ilość wystąpień elemntu FR w liśćie:', countries.count('FR'))  # sprawdzenie ile razy występuje dany element

newList = ['FI', 'SE']

print('Nowa lista:', newList)
countries.extend(newList)  # przyłączenie nowej listy do countries
print('Lista  counties po połączeniu z newList:', countries)

countriesCopy = countries  # przypisanie listy do innej zmiennej, ale mają to samo miejsce w pamięci

print(countries)
print(countriesCopy)

countriesCopy.clear()  # Wyczysczenie listy

print(countries)
print(countriesCopy)

countries = ['FR', 'US', 'DE', 'NE', 'PL']

countriesCopy = countries.copy()  # Kopiowanie i tworzenie nowej listy, czyli nowe miejsce w pamieci

print(countries)
print(countriesCopy)

countriesCopy.clear()

print(countries)
print(countriesCopy)
