def PrintAnimal(*animals):
    txt1 = r'''
         |\---/|
         | o_o |
          \_^_/'''

    txt2 = r'''
             /  \.-"""-./  \
             \    -   -    /
              |   o   o   |
              \  .-'"'-.  /
               '-\__Y__/-'
                  `---`'''

    txt3 = r'''
                /\                 /\
               / \'._   (\_/)   _.'/ \
              /_.''._'--('.')--'_.''._\
              | \_ / `;=/ " \=;` \ _/ |
               \/ `\__|`\___/`|__/`  \/
                       \(/|\)/       '''
    for animal in animals:
        animal = animal.lower()
        if animal == 'cat':
            print(txt1)
        elif animal == 'bear':
            print(txt2)
        elif animal == 'bat':
            print(txt3)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
    return


PrintAnimal('BaT', 'Cat', 'Mora', 'bear')



############################
print('\n')



from datetime import date
from datetime import datetime

def DaysToEndOfYear(*dates):

    for d in dates:
        data = datetime.strptime(d, "%Y-%m-%d")
        day = date(data.year, data.month, data.day)
        lastDay = date(day.year, 12, 31)
        delta = lastDay - day
        print(delta)
    return


############################
print('\n')


from datetime import date


# def DaysToEndOfYear(*dates):
#     for date_today in dates:
#         date_end_year = date(date_today.year, 12, 31)
#         delta = date_end_year - date_today
#         print('Date', date_today, 'days to end of year', delta.days)
#
#
# DaysToEndOfYear(date(1999, 1, 15))
# print('----------------')
# DaysToEndOfYear(date(1999, 1, 15), date(2009, 1, 15))
# print('----------------')
# DaysToEndOfYear(date(1999, 1, 15), date(2009, 1, 15), date(2019, 1, 15))
# print('----------------')
# DaysToEndOfYear(date(1999, 1, 15), date(2009, 1, 15), date(2019, 1, 15), date.today())