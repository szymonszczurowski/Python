# filename = input('Enter fileName: ') #Wszystko co wczytuje to zawsze string
#
# print("The file name is: {}".format(filename))
# print(filename)


while True:
    fileSizeStr = input('Enter the max file size: ')

    if fileSizeStr.isdecimal():
        fileSizeInt = int(fileSizeStr)
        break


print('The max size is {}'.format(fileSizeInt))
print('Size in KB is {}'.format(fileSizeInt * 1024))
