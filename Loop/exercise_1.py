firstRow = 1
lastRow = 31
currentRow = firstRow

while currentRow <= lastRow:
    print('Row number:', currentRow)
    currentRow+=1
else:
    print('end')

print('####################################')

number = 1
while number <= 13:
    print("square number:", number, " = ", number*number)
    print("cube number:", number, " = ", number*number*number)
    number+=1
else:
    print('end')

print('####################################')

start = 0
end = 16
while end >= start:
    print(start, 2**start)
    start+=1

print('####################################')

startStar = 0
endStar = 10

while startStar <= endStar:
    print(startStar*'*')
    startStar+=1