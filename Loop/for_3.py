for x in range(1, 6):
    for y in range(1, 6):
        print(x, '*', y, ' = ', x * y)

print('#############################')

for x in range(1, 6):
    line = str(x)
    for y in range(1, 6):
        line += ('\t%3d' % (x * y))
    print(line)
