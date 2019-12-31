import random 
#Numbers on dice start from 0 - 6 
#Action to perform random number from 0 -6 
def Rolldice(rolls):
    for i in range(0,rolls):
        number = random.randint(i,6)
        print(number)
    Menu()
#Dice game Main Menu for user
def Menu():
    print('1. Roll a Dice')
    print('2. Roll both Dice')
    print('------------------------')
    print('3. Exit Program')
    print()
    Menu_choice = int(input('Enter Here: '))
#Calculation/action based on the number inputed by user
    if (Menu_choice == 1):
        Rolldice(1)
    if (Menu_choice == 2):
        rolls = int(input('How many rolls?'))
        Rolldice(rolls)
    if (Menu_choice == 3):

        exit()



Menu()






