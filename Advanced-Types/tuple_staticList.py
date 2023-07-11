#tuple - krotka - statyczna lista

tax = (3,5,8,8,23)
print('tuple:', tax)
print('element na indeksie 2 tuple:', tax[2])
print('ostatni element:', tax[-1])
print('zwracanie indeksu elementu:', tax.index(5))
print('zwracanie ilosci wystapien:', tax.count(8))
print('maksymalna wartosc:', max(tax)) #maksymalna występująca wartość

#Tuple nie można modyfikować
#W razie modyfikacji trzeba konwertowac na listę
taxList = list(tax) #konwersja tuple na liste
print(taxList)

taxList.append(30)
newTax = tuple(taxList) #konwersja listy na tuple
print(newTax)

tax = (3,5,8,8,23)
(tax1, tax2, tax3, tax4, tax5) = tax #przypisywnaie elementów w tuple do zmiennych
print(tax1, tax2, tax3, tax4, tax5)

a=1
b=10
print(a,b)

(a,b)=(b,a)
print(a,b)