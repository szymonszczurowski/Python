age = 29
isDrunk = False
isRestictedArea = True

if age < 18:
    print('Tou are too young to buy alcohol')
elif isDrunk:
    print('Are yu drunk? We cannot sell you alcohol')
elif isRestictedArea:
    print('Restricted are. Alcohol is forbidden')
else:
    print('Ok, you can buy alcohol')