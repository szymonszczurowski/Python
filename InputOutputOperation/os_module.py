import os
import time

print('Currnet directory as is:', os.getcwd())





currentDir = os.getcwd()
filename = 'result.txt'
fullpath = os.path.join(currentDir, filename) #os.path.join łączenie ścieżki (bierzacy kataolg, nazwa pliku
print('\nThe constructed file path is:', fullpath)

print('Relative path to the file is', os.path.relpath(fullpath))

#Wzglęgdne - położenie pliku względem bieżącego katalogu (nazwa dysku, katalog itp)
relativePath = 'output.txt'
print('\nThe constructed file path is:', os.path.abspath(relativePath)) # sam skleja ścieżka z bierzącym katalogiem

filepath = r'c:\temp\results.txt'
print('\nThe file name path is:', os.path.basename(filepath)) #nazwa pliku
print('\nThe directory part is:', os.path.dirname(filepath)) #sciezka dostepu do katalogi w ktorym jest plik

print('\nIs file existing? ', os.path.exists(filepath)) #sprawdzenie czy istnieje


print('\n-------------------------------------------')

filepath = os.getcwd()
if os.path.exists(filepath):
    print('\nLast modify date is:', os.path.getmtime(filepath)) # data modyfikacji getMtime, utworzenia getCtime, ostatniego dostepu getAtime
    print('Last modify date is:', time.localtime(os.path.getmtime(filepath))) #konwersja na czytelniejszy sposób

    print('\nFile size is:, ', os.path.getsize(filepath)) #rozmiar pliku

    print('\nIs it a file? ', os.path.isfile(filepath)) #czy sciezka to plik?
    print('Is it a dir? ', os.path.isdir(filepath)) #czy sciezka to katalog?

    print('\nPath split:', os.path.split(filepath)) #rozbicie na nazwe i sciezke i podzial na liste
    print('Only file name part:', os.path.split(filepath)[1]) #pobranie nazwy pliku

    print('\nPath split into drive:', os.path.splitdrive(filepath)) #oderwanie nazwy dysku i sciezka dostepu do pliku
    print('Only drive:', os.path.splitdrive(filepath)[0]) #pobranie tylko nazwy dysku
