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
    Dice_choice = int(input('Enter Here: '))

    if Dice_choice == '1'




