values = [10, 43, 12, 48, 12, 11, 18, 98, 57, 28, 19, 27, 49, 19, 74]

i = 0
# max = len(values)
amount = 0
while i <= values.__len__()-3:
    if values[i] < values[i + 1] < values[i + 2]:
        print(i, ':', values[i], values[i+1], values[i+2])
        amount+=1
    else:
        print(i, ':', 'this iteration lacks 3 ascending numbers:(')
    i+=1
else:
    print('The board had', amount, 'solutions')


numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

