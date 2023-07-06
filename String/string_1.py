atext='This is a text.'
print(atext.endswith('ext'))
print(atext.endswith('ext'))
print(atext.islower())
print(atext.upper())
print(atext.upper().isupper())
print(atext.find('is'))
print(atext.find('is', 3))
print(atext.replace('a', '4'))
print(atext.replace('a', '4').replace('i', '1').replace('e', '3'))
print(atext.split())

somethingLikeNumber = '1000'

print(somethingLikeNumber.isdigit()) #sprawdzenie czy napis wygląda jak liczba
print(somethingLikeNumber.isdecimal()) #napis jak liczba z przecinkiem
print(somethingLikeNumber.isalpha()) #występowanie samych liter
print(somethingLikeNumber.isalnum()) #występowanie samych liter i cyfr
