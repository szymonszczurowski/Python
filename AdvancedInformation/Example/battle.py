import random

colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = [
    {'Figure': 'Ace', 'Power': 14},
    {'Figure': 'King', 'Power': 13},
    {'Figure': 'Queen', 'Power': 12},
    {'Figure': 'Jack', 'Power': 11},
    {'Figure': '10', 'Power': 10},
    {'Figure': '9', 'Power': 9}]

allCards = []

for color in colors:
    for figure in figures:
        aCard = figure.copy()
        aCard['Color'] = color
        allCards.append(aCard)

random.shuffle(allCards)

print(allCards)
print('\n')

player1 = []
player2 = []

#FIRST METHOD

player1 = allCards[:int(len(allCards)/2)]
player2 = allCards[int(len(allCards)/2):]

print(player1)
print(player2)

#SECOND METHOD
# print('\n')
#
# player1 = []
# player2 = []
#
# for n in range(len(allCards)):
#     if (n % 2 == 0):
#         player1.append(allCards[n])
#     else:
#         player2.append(allCards[n])
#
# print(player1)
# print(player2)


while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    stack = []

    if card1["Power"] == card2["Power"]:
        while card1["Power"] == card2["Power"]:

            print('WAR', card1['Power'], card2['Power'])
            stack.append(card1)
            stack.append(card2)

            if len(player1) < 2:
                player2.extend(stack)
                player2.extend(player1)
                player1 = []
                print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2) * '*')
                break
            elif len(player2) < 2:
                player1.extend(stack)
                player1.extend(player2)
                player2 = []
                print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
                break
            else:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                stack.append(card1)
                stack.append(card2)
                card1 = player1.pop(0)
                card2 = player2.pop(0)
        else:
            if card1["Power"] > card2["Power"]:
                stack.append(card1)
                stack.append(card2)
                player1.extend(stack)
                print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
            else:
                stack.append(card1)
                stack.append(card2)
                player2.extend(stack)
                print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2) * '*')


    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
    else:
        player2.append(card2)
        player2.append(card1)
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2) * '*')

if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')



# while len(player1) > 0 and len(player2) > 0:
#     card1 = player1.pop(0)
#     card2 = player2.pop(0)
#     stack = []
#
#
#     if card1['Power'] == card2['Power']:
#         while card1["Power"] == card2["Power"]:
#
#             print('WAR', card1['Power'], card2['Power'])
#             stack.append(card1)
#             stack.append(card2)
#
#             if len(player1) < 2:
#                 player2.extend(stack)
#                 player2.extend(player1)
#                 player1 = []
#                 print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2) * '*')
#                 break
#             elif len(player2) < 2:
#                 player1.extend(stack)
#                 player1.extend(player2)
#                 player2 = []
#                 print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
#                 break
#             else:
#                 card1 = player1.pop(0)
#                 card2 = player2.pop(0)
#                 stack.append(card1)
#                 stack.append(card2)
#                 card1 = player1.pop(0)
#                 card2 = player2.pop(0)
#         else:
#             if card1["Power"] > card2["Power"]:
#                 stack.append(card1)
#                 stack.append(card2)
#                 player1.extend(stack)
#                 print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
#     elif card1['Power'] > card2['Power']:
#         player1.append(card1)
#         player1.append(card2)
#         print('ROUND WON BY PLAYER 1', 'Player 1 have:', len(player1), 'Player 2 have:', len(player2))
#
#     else:
#         player2.append(card1)
#         player2.append(card2)
#         print('ROUND WON BY PLAYER 2', 'Player 1 have:', len(player1), 'Player 2 have:', len(player2))
#
# if len(player1) > 0:
#     print('PLAYER 1 WON!!!!')
# else:
#     print('PLAYER 2 WON!!!!')

