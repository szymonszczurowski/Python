for number in range(20):  #zakres od 0, 19
    print(number)

print('########################')

for number in range(1,21): #zakres od 1, 20
    print(number)

print('########################')

for number in range(1,21, 2): #zakres od 1, 20 oraz określenie o ile zwiększać number
    print(number)

print('########################')

for number in range(1,21): #zakres od 1, 20
    if number % 2 == 0:
        print('Number %2d is %s' % (number, 'even'))
    else:
        print('Number %2d is %s' % (number, 'odd'))

