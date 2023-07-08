age = 27

if age >= 18:
    print('You are adult and you can buy alcohol')
else:
    print("Tou are too young to buy alcohol")

isDrunk = False

if age >= 18 and not isDrunk:
    print('You are adult and you can buy alcohol')
else:
    print("Sorry, we cannot sell you alcohol")

isRestictedArea = True

if age >= 18 and not isDrunk and not isRestictedArea:
    print('You are adult and you can buy alcohol')
else:
    print("Sorry, we cannot sell you alcohol")