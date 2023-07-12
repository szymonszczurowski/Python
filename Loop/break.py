#BREAK - PRZERWANIE PĘTLI

for candidate in range (2,31):
    isPrime = True
    for divider in range (2, candidate):
        if candidate % divider == 0:
            isPrime = False
            print( candidate, "Is not a prime number - divider is", divider)
            break #przerwanie pętli wentrznej i przejście z powrotem do pętli pierwszej
    if isPrime:
        print(candidate, 'is prime')


print('#################################')

for candidate in range (2,31):
    for divider in range (2, candidate):
        if candidate % divider == 0:
            print( candidate, "Is not a prime number - divider is", divider)
            break #przerwanie pętli wentrznej i przejście z powrotem do pętli pierwszej
    else: #nie wykona jeśli wewntrzna pętla nie zostanie złamana przez break
        print(candidate, 'is prime')



