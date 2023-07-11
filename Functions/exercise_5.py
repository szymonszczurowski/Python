def PrintAnimal(animal=''):
    animal = animal.lower()
    print(animal)
    if animal == 'cat':
        txt = r'''
             |\---/|
             | o_o |
              \_^_/'''
        print(txt)
    elif animal == 'bear':
        txt = r'''
                 /  \.-"""-./  \
                 \    -   -    /
                  |   o   o   |
                  \  .-'"'-.  /
                   '-\__Y__/-'
                      `---`'''
        print(txt)
    elif animal == 'bat':
        txt = r'''
                    /\                 /\
                   / \'._   (\_/)   _.'/ \
                  /_.''._'--('.')--'_.''._\
                  | \_ / `;=/ " \=;` \ _/ |
                   \/ `\__|`\___/`|__/`  \/
                           \(/|\)/       '''
        print(txt)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
        return False

    return True




PrintAnimal('BEAR')
PrintAnimal()
print(PrintAnimal())



############################
print('\n')



from datetime import date


def DaysToEndOfYear(year=date.today().year,
                    month=date.today().month,
                    day=date.today().day):

    day = date(year, month, day)
    lastDay = date(day.year, 12, 31)
    delta = lastDay - day
    return delta.days


print('New Years Eve is still to come:', DaysToEndOfYear())
print('New Years Eve is still to come:', DaysToEndOfYear(day=23, month=12, year=2023))
print('New Years Eve is still to come:', DaysToEndOfYear(year=2022, month=12, day=22))
print('New Years Eve is still to come:', DaysToEndOfYear(2021, 12, 21))
