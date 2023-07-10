import time

# sprawdzenie wersji pythona
import sys

print(time.time()) #data w sekundach
print(time.localtime(time.time())) #data reprentowania w tuple
print(time.asctime((time.localtime(time.time())))) #data w czytelnej formie
# zamiast
# print(time.clock(), time.localtime(time.clock()))
# korzystaj z funkcji time.perf.counter():
print(time.perf_counter(), time.localtime(time.perf_counter()))

import calendar

print(calendar.month(2017,9,w=5,l=2)) #rok, miesiąć , na dzień 5 znkaów, odstpęy 2 znaki
print(calendar.month(2017,9))
print(calendar.weekday(2017, 9, 29))

calendar.setfirstweekday(6) #ustawienie pierwzego dnia tyg jako niedziela
print(calendar.month(2017,9))
print(calendar.weekday(2017, 9, 29))

print(calendar.isleap(2020)) #rok jest przestępny czy nie ?

print(calendar.leapdays(2000, 2017)) #ile było dni przestępnych w tych latach, bez roku 2017


print(calendar.calendar(2023))


####################


import time

print(time.time())
print(time.localtime(time.time()))

import calendar

print(calendar.month(2000, 8))
calendar.setfirstweekday(6)
print(calendar.month(2000, 8))

print('2000 is leap: ', calendar.isleap(2000))

print(calendar.calendar(2019))