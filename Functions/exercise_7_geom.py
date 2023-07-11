def GiveGeomSeqElement(a1=2,factor=2,index=2):
    #zwraca n-ty wyraz ciągu geometrycznego zaczynającego się od elementu a1 i mającego
    value = a1*pow(factor,index-1)
    return value
print('element 64 =',GiveGeomSeqElement(1,2,64))

print('------------------------------------------------')

def GiveFactorForGeomSeq(term, nextterm):
    #zwraca współczynnik dla ciągu geometrycznego mającego dwa kolejne wyrazy ciągu
    return nextterm/term
print('Factor is', GiveFactorForGeomSeq(12,24))

print('------------------------------------------------')

def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):
    #zwraca sumę n pierwszych elementów ciągu geometrycznego z pierwszym członem a1 i współczynnikiem
    sumN = a1*(1-pow(factor,n))/(1-factor)
    return sumN
print('Sum of n elements is', GiveSumOfNElementsGeomSeq(2,3,4))