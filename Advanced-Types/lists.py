countries = ['FR', 'US', 'DE', 'NE', 'PL']

print(countries.__len__())
print(countries[4])

countries[2] = 'IL'

print(countries)

countries.append('KC') #dodawnie elmentu na koniec listy
print(countries)
countries.insert(2, 'ES') #dodawnie elemntu na konkretnej pozycji
print(countries)
countries.remove("IL") #kasowanie elementu
print(countries)
countries.sort() #sortowanie
print(countries)
countries.reverse() #odwrócenie listy
print(countries)

print(countries.pop(2)) # Zwraca wartość ze wskazanej pozycji i ją skasuje
print(countries)

print(countries.index('PL')) #sprawdzenie pozycji elementu

print(countries.count('FR')) #sprawdzenie ile razy występuje dany element

newList = ['FI', 'SE']

countries.extend(newList) #łączenie list
print(countries)


countriesCopy = countries #przypisanie listy do innej zmiennej, ale mają to samo miejsce w pamięci

print(countries)
print(countriesCopy)

countriesCopy.clear()

print(countries)
print(countriesCopy)

countries = ['FR', 'US', 'DE', 'NE', 'PL']

countriesCopy = countries.copy() #Kopiowanie i tworzenie nowej listy, czyli nowe miejsce w pamieci

print(countries)
print(countriesCopy)

countriesCopy.clear()

print(countries)
print(countriesCopy)
