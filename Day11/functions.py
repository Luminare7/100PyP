# File for all used functions

import random
from deck import cards_dict


def draw_add(whose_hand, whose_points):
    picked_key = random.choice(list(cards_dict))  # Questo mi da un solo key a caso
    if picked_key == "ace":
        if whose_points <= 10:
            whose_hand.append({picked_key: cards_dict["ace"][1]})
            whose_points += cards_dict["ace"][1]
        else:
            whose_hand.append({picked_key: cards_dict["ace"][0]})
            whose_points += cards_dict["ace"][0]
    else:
        whose_hand.append({picked_key: cards_dict[picked_key]})
        whose_points += cards_dict[picked_key]
    return whose_points
