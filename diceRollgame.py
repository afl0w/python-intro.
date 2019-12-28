import random 

def Rolldice(rolls):
    for i in range(0,rolls):
        number = random.randint(1,6)
        print(number)
    Menu()

def Menu():
    print('1. Roll a Dice')
    print('2. Roll both Dice')
    print('------------------------')
    print('3. Exit Program')
    print()
    Menu_choice = int(input('Enter Here: '))

    if (Menu_choice == 1):
        Rolldice(1)
    if (Menu_choice == 2):
        rolls = int(input('How many rolls?'))
        Rolldice(rolls)
    if (Menu_choice == 3):

        exit()



Menu()






