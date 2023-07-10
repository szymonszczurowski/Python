line = 'this IS a Very STRANGE text'

print(line.capitalize()) #konwersja tekstu na zdania rozpoczynającego się dużą literą, a reszta małą

print(line.title()) #konwersja tekstu na każde słowo rozpoczynającego się dużą literą, a reszta małą

print(line.upper())
print(line.lower())

print(line.swapcase()) #duze na małe, małe na duże

line = 'der Fluß'
print(line.casefold()) # rozpoznaja inne znaki i zapisuje je w innje formie, Ż an z nie zamieni, Ó na o nie zamieni i tak dalej, więc z Polskim tak średnio

line = 'der ŻÓŁĆ'
print(line.casefold())


#########################################

line = 'this IS a Very STRANGE text'


print(line.count('e'))
print(line.find('e'))
print(line.rfind('e'))
print(line.find('p'))
print(line.rfind('p')) #zwróci -1 jak nie ma zanku
# print(line.index('p'))
# print(line.rindex('p')) #index zwróci błąd

print('e' in line)


#########################################

line = 'this IS a Very STRANGE text'

print(line.startswith('this'))
print(line.endswith("THIS"))

line = """sdfffffffffff
asgearfgweragwergerwg
ergergererg
"""

print(line)
print(line.count('\n'))

#########################################

import string

print(string.ascii_letters)
print(string.digits)

#########################################

line = 'this IS a Very STRANGE text'

list = line.split(' ') #rozbijanie tekstu
print(list)

print(' '.join((list))
)
