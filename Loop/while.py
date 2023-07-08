i=1
imax=10

while i <= imax:
    print(i, 'I like Python')
    i+=1

print('#####################################')

i=1
while i <= imax:
    print(i, 'I like Python')
    i+=2
else:
    print('Now i=', i)

print('#####################################')


i=10
imin=0

while i >= imin:
    print(i, 'I like Python')
    i-=2
else:
    print('Now i=', i)