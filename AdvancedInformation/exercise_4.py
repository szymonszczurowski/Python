import random

randomNum = []
i = 1
while i <= 10:
    randomNum.append(random.randint(1, 100))
    i+=1


print(randomNum)


#######################

number1 = random.randint(1,100)
counter = 1
number2 = 0

while number1 != number2:
    number2 = random.randint(1,100)
    print(counter, 'num2:', number2, 'num1:', number1)
    counter+=1
else:
    print('counter:', counter-1)

######################
print('###############################')

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)
groupName = 0

i=0
while i <= len(countries):
    if i % 4 == 0:
        groupName+=1
        print('----Grupa X----')

    print(countries[i])
    i+=1
else:
    'hej'