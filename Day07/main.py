# Day7! Let's play HANGMAN :))
import random
import hangmans
import hanglist

words = hanglist.word_list
chosen_word = random.choice(words)
chosen_word_len = len(chosen_word)

lives = 6

print(f"Psst, the solution is {chosen_word}.")  # simple debug line

# create blank spaces
display = []
for _ in range(chosen_word_len):
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter in the word! ").lower()

    # Check guessed letter
    if guess in chosen_word:
        for position in range(chosen_word_len):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = letter
    else:
        lives -= 1
        if lives <= 0:
            end_of_game = True
            print("YOU LOST!")

    if "_" not in display:
        end_of_game = True
        print("YOU WON!")

    print(f"{' '.join(display)}")
    print(hangmans.stages[lives])
