tax = [3,5,8,8,23]
print(tax)
print(tax[2])
print(tax[-1])
print(tax.index(5))
print(tax.count(8))
print(max(tax)) #maksymalna występująca wartość

#Tuple nie można modyfikować

taxList = list(tax)

print(taxList)


taxList.append(30)


newTax = tuple(taxList)
print(newTax)

(tax1, tax2, tax3, tax4, tax5) = tax #przypisywnaie elementów w tuple do zmiennych
print(tax1, tax2, tax3, tax4, tax5)

a=1
b=10
print(a,b)

(a,b)=(b,a)

print(a,b)