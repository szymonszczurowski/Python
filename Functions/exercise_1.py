def PrintCat():
    # this function prints a cat ascii-art
    txt = r'''
    |\---/|
    | o_o |
     \_^_/'''
    print(txt)
    return


def PrintBear():
    # this function prints a bear ascii-art
    txt = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
    print(txt)
    return

def PrintBat():
    # this function prints a bat ascii-art
    txt = r'''
      /\                 /\
     / \'._   (\_/)   _.'/ \
    /_.''._'--('.')--'_.''._\
    | \_ / `;=/ " \=;` \ _/ |
     \/ `\__|`\___/`|__/`  \/
             \(/|\)/       '''
    print(txt)


print(r'''
    1 - Cat
    2 - Bear
    3 - Bat
''')

choose = input('Choose animal: ')
if int(choose) == 1:
    PrintCat()
elif int(choose) == 2:
    PrintBear()
elif int(choose) == 3:
    PrintBat()
else:
    print("Please choose correct option")