def DoAction(action, parameter):
    print('action:', action)
    print('parameter:', parameter)
    return

DoAction('buy', 'shoes')

# DoAction('buy', 'shoes', 'socks') #Error


print('\n')

def DoAction(action, *parameter):  # * - kolekcja elementów (tuple),
    print('action:', action)
    print('parameter:', parameter)
    for element in parameter:
        print('element is', element)
    return

DoAction('buy', 'shoes', 'socks', 't-shirt')


print('\n')

def DoAction(action, what,  **parameter):  # ** - kolekcja elementów (dictionary - słownik) klucz i wartosc,
    print('action:', action)
    print('what:', what)
    print('parameter:', parameter)
    for element in parameter:
        print('element is', parameter[element])
    return


DoAction('buy', 'shoes', size=45, color='brown', type='sport')