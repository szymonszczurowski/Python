minLike = 500
minShares = 100

currentLike = 505
currentShares = 150

if minLike <= currentLike and minShares <= currentShares:
    print('10%')
else:
    print(':(')

##############################################



isPizzaOrdered = False
isBigDrinkOrdered = True
isWeekend = False

if not isWeekend and (isBigDrinkOrdered or isPizzaOrdered):
    print(':)')
else:
    print(':(')

##############################################



diskSize = 150
diskSizeUsed = 133
fileSize = 10

if fileSize < diskSize - diskSizeUsed:
    print('you can install')
else:
    print('you cannot install')