def PrintAnimal(animal):
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


PrintAnimal('BEAR')

from datetime import date


def DaysToEndOfYear(year,month,day):

    day = date(year, month, day)
    lastDay = date(day.year, 12, 31)
    delta = lastDay - day
    print('New Years Eve is still to come:', delta.days, 'days')

    return


DaysToEndOfYear(2023, 7, 11)
DaysToEndOfYear(2021, 12, 21)
DaysToEndOfYear(year=2022, month=12, day=22)
DaysToEndOfYear(day=23, month=12, year=2023)

