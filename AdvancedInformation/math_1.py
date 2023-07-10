f_smaller = 3.141592653358973
f_bigger = 3.87756392764

print(f_smaller, f_bigger)
print('\n')

##############################

print('Rzutowanie na typ int (część dziesiętna jest wycinana', 'smaller:', int(f_smaller), 'bigger:', int(f_bigger))

print('\n')

##############################

print('Wartość bezwzględna', 'smaller:', abs(f_smaller), 'bigger(jako ujemna):', abs(-f_bigger))

print('\n')

##############################

print('Zaokrąglanie jak w matematyce, jako drugi parametr ilość liczb po przecinku. 0.5 >+ w górę, < 0.5 w dół ', 'smaller:',
      round(f_smaller, 2), 'bigger:', round(f_bigger, 2), 'bigger:', round(f_bigger, 3))

print('\n')


##############################

print('Wartość min i max', 'min:', min(f_smaller,f_bigger), 'max:', max(f_bigger, f_smaller))

print('\n')

##############################

list = [1,2,3,4,5,4,4,5,4]

#Nie ma zaimplementowanej funckji trzeba policzyć samemu (W modułach do importu sa)
print('Wyliczenie średniej z listy', sum(list) / len(list))

print('\n')


##############################

#typ float nie jest ptezycyzjny np. 2.675 == 2.67499999
print((round(2.675, 2)))