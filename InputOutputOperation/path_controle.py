import os

print(os.getcwd())

fileIsOk = False

while not fileIsOk:
    filename = input('Enter path to results file: ')
    if os.path.isfile(filename):
        fileIsOk = True
    else:
        print('File name is not correct, try again')

print('This results file is {}'.format(filename))


print('\n================================\n')

import os
print(os.getcwd())

while True:
    filename = input('Enter path to results file: ')
    if os.path.isfile(filename):
        break
    else:
        print('File name is not correct, try again')

print('This results file is {}'.format(filename))