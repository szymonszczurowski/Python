musclePain = False
fever = True
weakness = True

if musclePain and fever and weakness:
    print('suspicion of influenza')
else:
    print('The flu is unlikely')

############################

if musclePain and fever and weakness:
    print('suspicion of influenza')
elif weakness and not (fever or  musclePain):
    print('Just take a rest!')
else:
    print('you may be cold')

############################

isMan = True

if (musclePain and fever and weakness) or ((musclePain or fever or weakness) and isMan):
    print('suspicion of influenza')
elif weakness and not fever and not musclePain:
    print('Just take a rest!')
else:
    print('you may be cold')

############################

isCheckCompleted = False

print('CHECK IS COMPLETED' if isCheckCompleted else 'CHECK IS NOT COMPLETED')