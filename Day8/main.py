# Welcome to day 8!
# Today our project is about making a Caesar Cipher.

import art
import funcs

welcome_logo = art.logo

print(art.logo)
print("Welcome to our encoding machine!")

should_continue = True
while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    funcs.caesar(in_direction=direction, in_text=text, in_shift=shift)

    restart = input("Type 'yes' if you want to go again. Otherwise 'no'. \n")
    if restart == "no":
        should_countinue = False
        print("Goodbye")
    elif restart == "yes":
        should_continue = True
