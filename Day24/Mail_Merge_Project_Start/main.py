#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os.path
save_path = 'Output/ReadyToSend/'

with open("Input/Names/invited_names.txt", mode="r") as names:
    names_list = names.read().splitlines()

print(names_list) # Just a quick check


for index in range(0, len(names_list)):
    with open("Input/Letters/starting_letter.txt") as template:
        name_of_file = f"to_{names_list[index]}"
        completeName = os.path.join(save_path, name_of_file + ".txt")
        template = template.read()
        template = template.replace("[name]", names_list[index])
        with open(completeName, mode="w+") as new_letter:
            new_letter.write(template)


