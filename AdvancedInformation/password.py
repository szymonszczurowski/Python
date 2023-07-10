# for i in range(32, 127):
#     print(i, chr(i))
import random

ints = range(33, 127)
print(ints)
password = ''

for i in range(16):
    password += chr(random.choice(ints))

print('Password is', password)

#################

passList = []
passLeng = 16
i = 0
while i <= passLeng:
    passList.append(chr(random.randint(33, 64))) #cyfry
    i+=1
    if i == passLeng:
        break
    passList.append(chr(random.randint(33, 64, ))) #znaki specjalne
    i+=1
    if i == passLeng:
        break
    passList.append(chr(random.randint(65, 90))) #duże litery
    i+=1
    if i == passLeng:
        break
    passList.append(chr(random.randint(91, 96))) #znaki specjalne
    i+=1
    if i == passLeng:
        break
    passList.append(chr(random.randint(97, 122))) #małe litery
    i+=1
    if i == passLeng:
        break


random.shuffle(passList)
print(''.join(passList))