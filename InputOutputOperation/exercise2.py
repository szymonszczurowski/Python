import os
import time

print(os.getcwd())

dir = input('directory:')

if not os.path.isdir(dir):
    print('Is not a directory')
    exit()
else:
    file = input('file:')
    path = os.path.join(dir, file)

    if not os.path.exists(path):
        print('File %s does not exist!')
        exit()

    else:
        print('displaying properties of file %s' % path)


lastModified = time.localtime(os.path.getmtime(path))
print('Last modification:', lastModified)
print('File size is:, ', os.path.getsize(path))
print('Currnet directory as is:', os.getcwd())
print('Relative path to the file is', os.path.relpath(path))
