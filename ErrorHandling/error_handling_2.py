import sys

taskPerPerson = 0

# W razie błędu zostanie wyświetlony błąd, możan również zaimportować sys i wyswietlić o jaki błąd chodi
try:
    tasks = 32
    personStr = input('How many person are there in the team? ')
    person = int(personStr)

    taskPerPerson = tasks / person
    #RÓŻNICOWANIE BŁĘDÓW
except ValueError as e: #Jeżeli ktoś wprowadzi wartość, której nie da się skonwertować na liczbe całkowtią
    print('Sorry - you need to enter an integer number -', e) #Można dodać zmienną, którą wyświetli dodatko inforamacje o błedzie
except ZeroDivisionError: #Jeśli użytkownik wprowadził zero
    print('Sorry - you need to enter value > 0')
except:
    print('Something went wrong...', sys.exc_info()[0]) #Najważniesze opis błędu w sys. jest na początku


print('Every person should have around:', taskPerPerson)