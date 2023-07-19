import os
try:
    print(os.getcwd())
    line = input('Enter the value: ')
    path = input('Enter the path: ')

    file = open(path, 'w+')
    file.write(line + ' - ' + path)
    file.close()

    value = int(line)
    print('The value saved in file is:', value)
except FileNotFoundError as e:
    print('Error opening file', e)
except ValueError as e:
    print('The value entered cannot be converted to a number', e)
except:
    print('SORRY - WE HAVE AN ERROR')
else:
    print('Actions completed successfully')
finally:
    print('**** THE END ****')