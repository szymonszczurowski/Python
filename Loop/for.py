persons = ["John", "Emma", "William", "Olivia", "James", "Ava", "Michael", "Sophia", "Robert", "Isabella"]

domain = 'mycompany.pl'

for per in persons:
    email = per + '@' + domain
    print('Email for', per, 'is', email)
else:
    print('-- end of the list --')