persons = ["John", "Emma@sales.mycompany.com", "William", "Olivia", "James", "Ava", "Michael", "Sophia@sales.mycompany.eu", "Robert", "Isabella"]

domain = '@mycompany.com'
emails = []

for word in persons:
    if '@' in word:
        newWord = word.split('@')

        newWord[0] = newWord[0] + domain
        emails.append(newWord[0])
    else:
        word = word + domain
        emails.append(word)

print(emails)


print('#######################################################')

persons = ["John", "Emma@sales.mycompany.com", "William", "Olivia", "James", "Ava", "Michael", "Sophia@sales.mycompany.eu", "Robert", "Isabella"]

domain = 'mycompany.com'
emails = []

for person in persons:
    if '@' in person:
        emails.append(person)
    else:
        email = person+'@'+domain
        emails.append(email)

for email in emails:
    print(email)



print('####################### - CONTINUE - ################################')

persons = ["John", "Emma@sales.mycompany.com", "William", "Olivia", "James", "Ava", "Michael", "Sophia@sales.mycompany.eu", "Robert", "Isabella"]

domain = 'mycompany.com'
emails = []

for person in persons:
    if '@' in person:
        emails.append(person)
        continue  #przejście do kolejnej iteracji, a jeśli warunek w if nie jest spełniony przechodzimy do kolejnych instruckji
    email = person + '@' + domain
    emails.append(email)

for email in emails:
    print(email)
