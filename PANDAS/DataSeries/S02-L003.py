import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math
import datetime as datetime


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdaysSeries = pd.Series(weekdays)
print(weekdaysSeries)

freeDays = [False, False, False, False, False, True, True]
freeDaysSeries = pd.Series(freeDays)
print(freeDaysSeries)

holidays = {
    'New Year': datetime.date(2023, 1, 1),
    'Epiphany': datetime.date(2023, 1, 6),
    'Easter': datetime.date(2023, 4, 1)
}
holidaysSeries = pd.Series(holidays)
print(holidaysSeries)