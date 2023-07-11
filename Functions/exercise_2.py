from datetime import date


def Sylwester():
    todayDay = date.today()
    lastDay = date(todayDay.year, 12, 31)
    delta = lastDay - todayDay
    print('New Years Eve is still to come:', delta.days, 'days')

    return


Sylwester()
