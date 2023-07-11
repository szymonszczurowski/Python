import datetime
#DATETIME = datetime.datetime
print('min, max', datetime.MINYEAR, datetime.MAXYEAR)
print('\n')

#TIMEDELTA - OBLICZANIE RÓZNICY CZASU
#obliczanie różnica czasu
# dl = datetime.timedelta(days=1, hours=1, minutes=30)
d1 = datetime.timedelta(days=1, hours=2, minutes=-30)
print(d1)
d2 = datetime.timedelta(days=-1, hours=-2, minutes=-3) #JEDN DZIEN WCZESNIEJ, 2 GODZINY WCZESNIEJ, 3 MINUTY WCZESNIEJ
print(d2)
print('timedelta suma', d1+d2)

print('\n')

#DATE - liczy tylko dni, bez godzin, minut, sek
import datetime

today = datetime.date.today()
daysToPay = datetime.timedelta(days=7)
print('today:', today)
print('Bills should be paid within:', daysToPay.days, "days")
print("The bill should be padid till", today + daysToPay)

print('\n')

endOfTheWorld = datetime.date.max #Ostania dostępna data
print('The final end of the world will happen (by python):', endOfTheWorld)
print(endOfTheWorld.weekday()) #dzień tygodnia

print('\n')

bornDate = datetime.date(2000, 8, 15)
today = datetime.date.today()

print(today - bornDate)

print('\n')
#################################
#DATETIME - POLACZENIE DNI I CZASU

import datetime
# from datetime import datetime

#zwraca date i godzinę - czas loklany
print('now()\t', datetime.datetime.now()) #datetime.datetime.now : moduł.nazwatypy :: MOŻNA SKRÓCIĆ W TAKI SPOSÓB from datetime import datetime
#zwraca date i godzinę - czas loklany
print('today()\t', datetime.datetime.today())
print('utcnow()\t', datetime.datetime.utcnow()) #uniwersalny czas
print('weekday()\t', datetime.datetime.today().weekday()) #zwracanie numery dnia tygodnia np. 0 - pon, 1 -wtorek
print('\n')


print('%a', datetime.datetime.now().strftime('%a')) #konwersja liczby tyg na stringa czyli np. 0 - Mon (skrótem)
print('%A', datetime.datetime.now().strftime('%A')) #konwersja liczby tyg na stringa czyli np. 0 - Monday
print('%w', datetime.datetime.now().strftime('%w')) #Dzień tygodnia ale liczone juz normalnie. Czyli niedziela to dzień 0

print('%a %A $W', datetime.datetime.now().strftime('%a %A $W'))

print('%Y-%m-%d_%H_%M_%S_%f', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')) #f - milisekundy

