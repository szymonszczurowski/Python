hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
hitsTitles.insert(2, 'HOTEL CALIFORNIA')
hitsTitles.insert(0, 'THE SOUND OF SILENCE')
print(hitsTitles.index('HOTEL CALIFORNIA'))
hitsTitles.remove('HOTEL CALIFORNIA')
hitsTitles[1] = 'ENJOY THE SILENCE'
print(hitsTitles)

hitsToRead = hitsTitles.copy()
hitsToRead.reverse()
print(hitsToRead)
hitsToRead.sort()
print(hitsToRead)
print(hitsToRead.pop(0))
print(hitsToRead.pop(0))

additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
hitsToRead.extend(additionalSongs)
print(hitsToRead)

print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))

hitsToRead.clear()
print(hitsToRead)

'''
#1

hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN',

              'RIDERS ON THE STORM','WISH YOU WERE HERE']

print(hitsTitles)

#2

hitsTitles.append('CHILD IN TIME')

hitsTitles.append('AGAIN')

print(hitsTitles)

#3

hitsTitles.insert(2,"HOTEL CALIFORNIA")

print(hitsTitles)

#4

hitsTitles.insert(0,'THE SOUND OF SILENCE')

print(hitsTitles)

#5

print(hitsTitles.index('HOTEL CALIFORNIA'))

#6

hitsTitles.remove("HOTEL CALIFORNIA")

print(hitsTitles)

#7

hitsTitles[0]='ENJOY THE SILENCE'

print(hitsTitles)

#8

hitsToRead = hitsTitles.copy()

print(hitsToRead)

#9

hitsToRead.reverse()

print(hitsToRead)

#10

hitsToRead.sort()

print(hitsToRead)

#11

print(hitsToRead.pop(0))

print(hitsToRead.pop(0))

print(hitsToRead)

#12

additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']

print(additionalSongs)

#13

hitsToRead.extend(additionalSongs)

print(hitsToRead)

#14

print(hitsToRead.count('WISH YOU WERE HERE'))

print(hitsToRead.count('RIDERS ON THE STORM'))

#15

hitsToRead.clear()

print(hitsToRead)
'''