from datetime import date
from datetime import timedelta


def GiveWorkingDay(year=date.today().year, month=1, day=1):
    # prints the nearst working day date
    day = date(year, month, day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    return workingday


nextWorkingDay = GiveWorkingDay(2023, 7, 10)
nextWorkingDay2 = GiveWorkingDay()

print('1. Next workng day:', nextWorkingDay)
print('2. Next workng day :', nextWorkingDay2)
print('3. Next workng day :', GiveWorkingDay(2022, 5, 2))