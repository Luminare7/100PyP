# Functions for the game!
import random


def set_difficulty():
    diff = input("Choose a Difficulty!\n"
                 "Type 'easy' or 'hard': ")
    if diff == "easy":
        lives = 10
        return lives
    else:
        lives = 5
        return lives


def set_number_to_guess():
    guessable = random.randint(1, 101)
    return guessable


available_attempts = set_difficulty()
number_to_guess = set_number_to_guess()


def guess_checker(attempts):
    guessed_number = int(input("Make a guess: "))
    if guessed_number == number_to_guess:
        should_continue = False
        return [should_continue, attempts]
    else:
        attempts -= 1
        should_continue = True
        print(f"Guess again!\nYou have {available_attempts - 1} available attempts left")
        if guessed_number < number_to_guess:
            print("The number you guessed was too low!")
        elif guessed_number > number_to_guess:
            print("The number you guessed was too high!")
        return [should_continue, attempts]
