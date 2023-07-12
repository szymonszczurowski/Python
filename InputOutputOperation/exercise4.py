import os
file_path = os.path.join(os.getcwd(), 'orders.csv')

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip() #usuniecie białych znaków z końca i początku łańcucha
        # line = line.replace('\n', '')
        order = line.split(',')
        if len(order) == 3:
            print('Order from drugstore {}, item {}, amount {}'.format(order[0], order[1], order[2]))
        else:
            print('\nLine {} malformed!!!\n'.format(line))
    else:
        print("Processing finished")