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
#Wyświetli się tylko w tedy kiedy nie dojdzie to żadnego błędu
else: # Dodanie else do try: powoduje to, że ta linijka wyświetla się jedynie jak nie ma błędy, jakby print był po prsotu na końcu to i tak by sę wyświetlał
    print('Every person should have around:', taskPerPerson)
finally: #Instrukcje w tym bloku zostąną wykonanie niezależnie czy będzie błąd czy nie
    print('Script finished with/without errors')

print("\n----------------------------------------------------------------\n")

