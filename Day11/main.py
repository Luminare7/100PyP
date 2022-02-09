# CAPSTONE PROJECT AT DAY11
from art import logo
import functions

hand_dealer = []
hand_player = []
cash_player = 1000
print(logo)
print("Welcome to the blackjack terminal!")


def begin_play(cash_player):
    bid = int(input("Choose your bid! $"))

    if bid > cash_player:
        print("You can't bid more money than you own!")
        begin_play()
    else:
        points_dealer = 0
        points_player = 0
        # Here I draw two cards for each and calculate the points
        player_first = functions.draw_add(hand_player, points_player)
        player_second = functions.draw_add(hand_player, player_first)
        dealer_first = functions.draw_add(hand_dealer, points_dealer)
        dealer_second = functions.draw_add(hand_dealer, dealer_first)
        points_player += player_second
        points_dealer += dealer_second

        print(f"[{hand_dealer[0]}, ?]\nPoints: {dealer_first}")
        print(f"{hand_player}\nPoints: {points_player}")

        if points_player == 21:
            cash_player += bid
            print(f"Jackpot! Your new balance is: {cash_player}")
            redo = input("'Y' to play again, 'N' to cash out.")
            if redo == "Y":
                begin_play()
            else:
                print("Goodbye")
                return cash_player
        else:
            hit_stand = "H"
            while points_player < 22 and hit_stand != "S":
                if bid*2 <= cash_player:
                    ask_double_bid = input("Do you want to to double your bid? Type 'yes' or 'no': ")
                    if ask_double_bid == "yes":
                        bid += bid
                    else:
                        bid += 0
                hit_stand = input("Type 'H' to HIT, type 'S' to STAND: ")
                if hit_stand == "H":
                    player_new = functions.draw_add(hand_player, points_player)
                    points_player += player_new
                    print(f"[{hand_dealer[0]}, ?]\nPoints: {dealer_first}")
                    print(f"{hand_player}\nPoints: {points_player}")
                else:
                    print(f"[{hand_dealer}\nPoints: {points_dealer}")
                    print(f"{hand_player}\nPoints: {points_player}\n Available Cash: {cash_player}")
            if points_player > 21:
                cash_player -= bid
                print("BUSTED! You have more than 21 points")
                redo = input("'Y' to play again, 'N' to cash out: ")
                if redo == "Y":
                    begin_play()
                else:
                    print("Goodbye")
                    return cash_player
            while points_dealer < 17:
                dealer_new = functions.draw_add(hand_dealer, points_dealer)
                points_dealer += dealer_new
                print(f"[{hand_dealer}\nPoints: {points_dealer}")
                print(f"{hand_player}\nPoints: {points_player}\n Available Cash: {cash_player}")
            if points_dealer >= 22:
                cash_player += bid
                print(f"You Won! Your new balance is: {cash_player}")
                redo = input("'Y' to play again, 'N' to cash out: ")
                if redo == "Y":
                    begin_play()
                else:
                    print("Goodbye")
                    return cash_player
            else:
                if points_dealer > points_player:
                    cash_player -= bid
                    print(f"You Lost! Your new balance is: {cash_player}")
                    redo = input("'Y' to play again, 'N' to cash out: ")
                    if redo == "Y":
                        begin_play()
                    else:
                        print("Goodbye")
                        return cash_player
                elif points_player == points_dealer:
                    cash_player += 0
                    print(f"It's a draw! Your new balance is: {cash_player}")
                    redo = input("'Y' to play again, 'N' to cash out: ")
                    if redo == "Y":
                        begin_play()
                    else:
                        print("Goodbye")
                        return cash_player
                else:
                    print(f"You Won! Your new balance is: {cash_player}")
                    redo = input("'Y' to play again, 'N' to cash out: ")
                    if redo == "Y":
                        begin_play()
                    else:
                        print("Goodbye")
                        return cash_player
    return cash_player


cash_player = begin_play(cash_player)
print(cash_player)