import math


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


factorsA = input('Please write factor a: ')
factorsB = input('Please write factor b: ')
factorsC = input('Please write factor c: ')

if check_int(factorsA) and  check_int(factorsB) and check_int(factorsC):
    a = int(factorsA)
    b = int(factorsB)
    c = int(factorsC)

    if a == 0:
        print('It is not a quadratic equation')
    else:
        delta = pow(b, 2) - 4 * a * c
        if delta < 0:
            print('no solution')
        elif delta == 0:
            x1 = (-b - math.sqrt(delta) / 2 * a)
            print("x1: ", x1)
        else:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            print('x1: ', x1, "x2: ", x2)

else:
    print('the coefficients are not integers')


print('================================\n')


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


print('This program solves equation ax^2+bx+c = 0')
print('Enter the values for a, b and c:')

a_str = input('a=')
b_str = input('b=')
c_str = input('c=')

if not (check_int(a_str) and check_int(b_str) and check_int(c_str)):
    print("a, b and c need to be int!")
else:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)

    if a == 0:
        print('a cannot be 0!')
    else:
        delta = b ** 2 - 4 * a * c

        if delta < 0:
            print("there is no solution")
        elif delta == 0:
            x1 = -b / (2 * a)
            print("there is one solution: %.2f" % (x1))
        else:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            print("there are two solutions: %.2f and %.2f" % (x1, x2))



