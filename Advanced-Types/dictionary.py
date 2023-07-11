#DICTIONARY - SLOWNIK
CountryLeaders = {'PL': 'Duda', 'US': 'BIDEN'}

print('Dictionary:', CountryLeaders)
print('Wartosc bedaca pod kluczem US', CountryLeaders['US'])

CountryLeaders['DE'] = 'Schulz'  # dodawnaie nowego klucza i wartości
print('Slownik po dodaniu klucza i wartosci', CountryLeaders)

print('Zwrocenie wszystkich kluczy:', CountryLeaders.keys())  # zwracanie kluczy

print('Zwrocenie wszystkich wartosci:', CountryLeaders.values())  # zwracanie wartości

print('Zwrocenie wszystkich kolekcji:', CountryLeaders.items())  # zwracaja kolekcji elementów

print('Zdjęcie elementu ze slownika', CountryLeaders.popitem())  # przechodiz po słowniku i kasuje wyświetlony element

print('Zwrocenie wartosci z pod klucza:', CountryLeaders.setdefault('FR', 'Macron'))  #Zwrocenie wartosci z pod danego klucza, w razie braku elementu zwrocenie wartosci domyślnej
# i dodanie jej do slownika

print(CountryLeaders.get('UA'))  # Sprawdzamy co jest pod danym kluczem i jeśli nic nie ma to zwraca none, ale nic nie jest dodawane

NewLeaders = {'UA': "Zelenski", 'DE': '???'}
print('dictionary newLeaders:', NewLeaders)
CountryLeaders.update(NewLeaders)  # Aktualizacja danych pod danym kluczem lub dodanie elementu jeśli nie ma danego klucza
print('dictionary countryLeaders po aktualiacji slownika ze slonika newLeaders :', CountryLeaders)
