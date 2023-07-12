import os
file = open(os.path.join(os.getcwd(), 'zad.txt'), "r") #r - parametr oznacza za tryb odczytu pliku (odczyt)

content = file.read() #wczytanie zawartosci pliku
print(content)
file.close() #zamkniecie pliku

################################################################
print('\n################################################################\n')

file = open(os.path.join(os.getcwd(), 'zad.txt'), "r")
for line in file:
    print(line)

file.close()

################################################################
print('\n################################################################\n')

#LEPSZY SPOSOB

#Dobre dla małdych plików, bo można wczytać całość do pamięci. Dla dużych nie wydajna
with open(os.path.join(os.getcwd(), 'zad.txt'), "r") as file:
    content = file.read()
    print(content)

################################################################
print('\n################################################################\n')

#Wczytywanie linijka po linicje, Lepsze do dużych plików.
with open(os.path.join(os.getcwd(), 'zad.txt'), "r") as file:
    for line in file:
        print(line)


################################################################
print('\n################################################################\n')


file = open(os.path.join(os.getcwd(), 'zad.txt'), "r")

# WCZYTYWANIE PO KAWAŁKU
fragment = file.read(10) # przeczytanie na raz maksymalnie 10 bajtów
while fragment: # Jak będzie pusty po przejściu to będzie FALSE
    print(file.tell(), fragment) #file.tell() - wskazuje pozycję - NIE TRZEBA UŻYWAĆ TEJ INSTRUKCJI
    fragment = file.read(10) #Wczytanie kolejnych 10 bajtów


file.close() #zamkniecie pliku


################################################################
print('\n################################################################\n')

file = open(os.path.join(os.getcwd(), 'zad.txt'), "r")

for line in file.readline(): # Wczytywanie pojedycznej lini z pliku. Nie powinno się tak robić metoda readline wczytuje cały plik na raz i dopiero później dzieli na linijki
    print(line)
file.close()
