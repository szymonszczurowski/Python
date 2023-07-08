string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for i in range(10):
    print(string_A)

print('#######################################')

for i in range(5):
    print(string_B)
    print(string_A)

print('#######################################')


for i in range(10):
    print('*' * i)

print('#######################################')

for i in range(1,10):
    if i % 2 == 0:
        print("x"*i)
    else:
        print("o"*i)
