import os
import sys
file_path = os.path.join(os.getcwd(), 'orders.csv')

with open(file_path, "r") as file:
    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')

        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore {}, item {}, amount {}'.format(pharmacy_name, item, amount))
        except:
            print('ERROR line:', line, sys.exc_info()[0])

print("Processing finished")