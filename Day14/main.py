# Welcome to Day14!

import art
from game_data import data
import random

print(art.logo)


score = 0


def comparer(choice_one, choice_two):
    if choice_one['follower_count'] > choice_two['follower_count']:
        return choice_one
    else:
        return choice_two


def play_game(score):
    game_continues = True
    while game_continues:
        alt_one_index = random.randint(0, 49)
        alt_two_index = (alt_one_index + random.randint(1, 48)) % 50
        alt_one = data[alt_one_index]  # alt_one is the dictionary of data for one account on instagram
        alt_two = data[alt_two_index]  # alt_two is the other
        print(f"COMPARE A: {alt_one['name']}, a {alt_one['description']}, from {alt_one['country']}")
        print(art.vs)
        print(f"AGAINST B: {alt_two['name']}, a {alt_two['description']}, from {alt_two['country']}")
        right_alt = comparer(alt_one, alt_two)
        chosen_alt = input("Who has more followers? Type: 'A' or 'B': ")
        if chosen_alt == 'A':
            picked_account = alt_one
        else:
            picked_account = alt_two
        if picked_account == right_alt:
            score += 1
            print("Well done! On to the next")
            game_continues = True
        else:
            print("Oh no!")
            print(f"You scored {score} points!")
            game_continues = False
    again = input("Do you want to play again? Type 'yes' or 'no' ")
    if again == "yes":
        score = 0
        play_game(score)
    else:
        print("Goodbye")


play_game(score)


