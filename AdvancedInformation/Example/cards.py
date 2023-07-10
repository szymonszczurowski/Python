colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
allCards = []

for color in colors:
    for figure in figures:
        allCards.append("%s - %s" % (color, figure))

print(allCards)

print('\n')
print('#####################')
print('\n')


import random

random.shuffle(allCards)
print(allCards)

# Sposob 1

player1 = []
player2 = []

max = len(allCards)

i = 0
while i <= max-1:
    if(i % 2 == 0):
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
    i+=1

print('Player 1:', player1, '\nPlayer 2:', player2)


# Sposob 2
print('\n')

player1 = allCards[:12]
player2 = allCards[12:]

print('Player 1:', player1, '\nPlayer 2:', player2)
