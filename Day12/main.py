# Welcome to day 12!
import random
import guess_funcs

print("Welcome to the Number Guessing Game!\n"
      "I'm Thinking of a number between 1 and 100")

print(f"You have {guess_funcs.available_attempts} lives!")
print(f"The number to guess is: {guess_funcs.number_to_guess}")  # Debug line

game_should_continue = True
while guess_funcs.available_attempts > 0 and game_should_continue:
    game_progress = guess_funcs.guess_checker(guess_funcs.available_attempts)
    game_should_continue = game_progress[0]
    guess_funcs.available_attempts = game_progress[1]
    # print(f"the game progress is: {game_progress}, the guessed number is {guessed_number}") #debug line

if guess_funcs.available_attempts < 1 and game_should_continue:
    print(f"YOU LOST!\nThe number to guess was {guess_funcs.number_to_guess}")
elif not game_should_continue:
    print("VICTORY!")
