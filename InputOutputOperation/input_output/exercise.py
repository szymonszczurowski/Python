import os

webaddresses = []
line = input("Proszę o wprowadzenie adresu strony www: ")

while line != '':
    webaddresses.append(line)
    line = input("Proszę o wprowadzenie adresu strony www: ")

dirname = os.getcwd() #obecna ścieżka
filename = input("Podaj nazwę pliku: ")
filepath = os.path.join(dirname, filename)

file = open(filepath, 'w')
for address in webaddresses:
    file.write(address + '\n')
file.close()


