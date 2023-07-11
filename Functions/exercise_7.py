import exercise_7_geom

# def GiveGeomSeqElement(a1=1,factor=2,index=64): #pierwszy element ciągu, współczynnik ciąg geometrycznego, który element ciągu
#     #funkcja służąca do obliczeń na ciągach geometrycznych #an =a1*r^(n-1)
#     value = a1*pow(factor,index-1)
#     return value

print(exercise_7_geom.GiveGeomSeqElement())

print('\n')

a1 = 3
factor = 2
maxindex = 10
for i in range(1, maxindex + 1):
    print('i:', i, exercise_7_geom.GiveGeomSeqElement(a1, factor, i))

print('\n')


# def GiveFactorForGeomSeq(term, nextterm):
#     #funkcja GiveFactorForGeomSeq, która wyznaczy wartość współczynnika gdy znane są 2 kolejne wyrazy ciągu
#     return nextterm/term

print(exercise_7_geom.GiveFactorForGeomSeq(12,24))

print('\n')

# def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):
#     #returns sum of n first elements of geometrical sequence with first term a1 and factor
#     sumN = a1*(1-pow(factor,n))/(1-factor)
#     sumN2 = a1 * (1- factor**n)/(1-factor)
#     print(sumN2)
#     return sumN


print(exercise_7_geom.GiveSumOfNElementsGeomSeq())