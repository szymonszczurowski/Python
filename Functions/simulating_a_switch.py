# function (argumnet){
#     switch(argument) {
#     case 0:
#         return 'lundi';
#     case 1:
#         return 'mardi';
#     case 2:
#         return 'mercedi';
#     case 3:
#         return 'jeudi';
#     case 4:
#         return 'lundi';
#     case 5:
#         return 'mardi';
#     case 6:
#         return 'mercedi';
#     default:
#         return 'error!';
#
#     };
# };

# W PYTHON NIE MA SWITCH ALE MOŻNA ZASYMULOWAC TO NP. TAK

def WeekDayInFrench(dayNumber):

    #dictionary
    names = {
        0: 'lundi',
        1: 'mardi',
        2: 'mercredi',
        3: 'jeudi',
        4: 'vendredi',
        5: 'samedi',
        6: 'dimanche'
    }
    return names.get(dayNumber, "Error")

print(WeekDayInFrench(4))
print(WeekDayInFrench(6))


