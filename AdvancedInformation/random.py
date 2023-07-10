import random

print("One random number:", random.randint(1,100))  #licza całkowita od 1 do 100 w pełnym zakresie

print('Chossing random number from $ range', random.choice(range(1,100)))  #losowanie elmentu z zakresu, Może być np. jakaś lista i wybiera jedną dostępną wartość

#którsza wersja powyższego

print('Chossing random number from $ range', random.randrange(1,100))  #losowanie elmentu z zakresu, Może być np. jakaś lista i wybiera jedną dostępną wartość

list = ["John", "Emma", "William", "Olivia", "James", "Ava", "Michael", "Sophia", "Robert", "Isabella"]

random.shuffle(list) #wymieszanie listy

print('recordet, list:', list)

print('Just a random float', random.random()) #randomowa liczba float z zakresu od 0 do 1