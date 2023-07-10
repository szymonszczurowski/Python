import random

myNumbers = []

while len(myNumbers) < 7:
    newNumber = random.randint(1,49)

    if newNumber in myNumbers:
        print('Eliminated:', newNumber)
        continue #przskoczenie do nowego losowania i pominiecie dodania elementu

    myNumbers.append(newNumber)

print("Those nmbers will win:", myNumbers)