# Welcome to day4!

import random

choice = int(input("What do you chose?\nType 0 for Rock, 1 for Paper, 2 for Scissors."))

if(choice >= 3 or choice < 0):
    print("Invalid choice, you lost! :(")
else:

    choices = ["Rock", "Paper", "Scissors"]
    player_choice = choices[choice]
    computer_number_choice = random.randint(0, len(choices)-1)
    computer_choice = choices[computer_number_choice]

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    ascii_list = [rock, paper, scissors]

    def narration():
        print("Player Choice is: " + player_choice)
        print(ascii_list[choice])
        print("Computer Choice is: " + computer_choice)
        print(ascii_list[computer_number_choice])
    def draw():
        print("Then we have a draw!")
    def pwin():
        print("The Player Won!")
    def cwin():
        print("The Computer Won!")


    narration()
    if(choice == computer_number_choice):
        draw()
    elif(choice == 0):
        if(computer_number_choice == 1):
            pwin()
        else:
            cwin()
    elif(choice == 1):
        if(computer_number_choice == 0):
            pwin()
        else:
            cwin()
    else:
        if(computer_number_choice == 0):
            cwin()
        else:
            pwin()



