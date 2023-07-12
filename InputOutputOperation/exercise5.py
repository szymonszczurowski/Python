import os

webaddresses = []
line = input('Enter web address like "www.python.org" or press ENTER to stop: ')
while line != '':
    webaddresses.append(line)
    line = input('Enter web address like "www.python.org" or press ENTER to stop: ')

dirname = os.getcwd()

filname = input('Write path name: ')

filepath = os.path.join(dirname, filname)

print(filepath)

file = open(filepath, 'w')
for web in webaddresses:
    file.write(web + '=' + '\n')

file.close()


print('\n================================\n')


filename =input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename =input('Enter filename to read: ')
webaddresses=[]
with open(filename,'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
for line in webaddresses:
    if line.endswith('.pl'):
        print(line,'is a polish web page')
    else:
        print(line, 'is not a polish web page')


print('\n================================\n')

import os
filename =input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename =input('Enter filename to read: ')
webaddresses=[]
with open(filename,'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
dirname = os.path.dirname(filename)
websPathPL = os.path.join(dirname,'webs_pl.txt')
websPathOther = os.path.join(dirname,'webs_other.txt')
filePL = open(websPathPL,'w')
fileOther = open(websPathOther,'w')
for line in webaddresses:
    if line.endswith('.pl'):
        filePL.write(line+"\n")
    else:
        fileOther.write(line+"\n")
filePL.close()
fileOther.close()