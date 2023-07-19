print('=========== Część kolejna ===========')

import os


filepath = input("Podaj nazwę pliku: ")
while not os.path.isfile(filepath):
    print('Plik nie istnieje, proszę podać ponownie ścieżkę: ')
    filepath = input("Proszę o wprowadzenie ścieżki: ")

webaddresses = []

with open(filepath, "r") as file:
    for line in file:
        line = line.replace('\n', '')
        webaddresses.append(line)
foxxpl085

path = os.getcwd()

file = open(os.path.join(path, 'webs_pl.txt'), 'a')
file2 = open(os.path.join(path, 'webs_other.txt'), 'a')
for addresses in webaddresses:
    if addresses.endswith('.pl'):
        print('Adres', addresses, 'jest adresem z Polski')
        file.write(addresses + '\n')
    else:
        print('Adres', addresses, ' nie jest adresem z Polski')
        file2.write(addresses + '\n')

file.close()
file2.close()