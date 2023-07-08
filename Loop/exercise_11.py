data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for upData in data:
    print(upData.upper())

print('################################')


for splitData in data:
    elements = splitData.split(':')
    print(elements[0].upper(), elements[1])


print('################################')


for splitData in data:
    elements = splitData.split(':')

    if elements[0] == 'Error':
        print(elements[0].upper())
    else:
        print(elements[0])