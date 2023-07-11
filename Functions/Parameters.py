from datetime import date
from datetime import timedelta


def GiveWorkingDay(year, month, day):
    #prints the nearst working day date
    # day = date.today()
    day = date(year, month, day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day


    print('working day for', day, 'is', workingday)

    return


GiveWorkingDay(2013, 7, 11)
GiveWorkingDay(2023, 7, 15)
GiveWorkingDay(year=2023, month=7, day=15)
GiveWorkingDay(day=6, month=12, year=2016)

