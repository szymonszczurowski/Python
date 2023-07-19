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
        except ValueError as e:
            print('ERROR Line:', line, '=== It came to an error due to incorrect conversion of the data in the third field to the int type ===', e)
        except IndexError as e:
            print('ERROR Line:', line, '=== There was an error due to insufficient fields ===', e)
        except:
            print('ERROR line:', line, sys.exc_info()[0])

print("Processing finished")