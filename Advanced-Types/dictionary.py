CountryLeaders={'PL' : 'Duda', 'US': 'BIDEN'}

'''
CountryLeaders={
    'PL' : 'Duda',
    'US': 'BIDEN'
}
'''

print(CountryLeaders)
print(CountryLeaders['US'])

CountryLeaders['DE'] = 'Schulz' #dodawnaie nowego klucza i wartości
print(CountryLeaders)

print(CountryLeaders.keys()) #zwracanie kluczy
print(CountryLeaders.values()) #zwracanie wartości
print(CountryLeaders.items()) #zwracaja kolekcji elementów


print(CountryLeaders.popitem()) #przechodiz po słowniku i kasuje wyświetlony element
print(CountryLeaders.setdefault('FR', 'Macron'))  # W razie gdyby nie było określonego klucza wyświetlona zostanie wartość domyślna i zostanie an stałe dodana do listy
print(CountryLeaders.setdefault('FR', 'test'))


print(CountryLeaders.get('UA')) #Sprawdzamy co jest pod danym kluczem i jeśli nic nie ma to zwraca none, ale nic nie jest dodawane

NewLeaders = {'UA': "Zelenski", 'DE': '???'}

print(NewLeaders)
CountryLeaders.update(NewLeaders) #Aktualizacja danych pod danym kluczem lub dodanie elemtu jeśli nie ma danego klucza
print(CountryLeaders)











