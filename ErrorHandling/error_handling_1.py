import sys

taskPerPerson = 0

# W razie błędu zostanie wyświetlony błąd, możan również zaimportować sys i wyswietlić o jaki błąd chodi
try:
    tasks = 32
    personStr = input('How many person are there in the team? ')
    person = int(personStr)

    taskPerPerson = tasks / person
except:
    print('Something went wrong...', sys.exc_info()[0]) #Najważniesze opis błędu w sys. jest na początku


print('Every person should have around:', taskPerPerson)