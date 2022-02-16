# BAND NAME GENERATOR

# Create a greeting for your function
print("Welcome to the Band Name Generator (BANG)!")

# Ask the user for the city that they grew up in
user_city = raw_input("What city did you grow up in?\n")
#raw_input converts my input in a string

# Ask the user for the name of a pet
user_pet = raw_input("What is the name of your pet?\n")

# Combine the name of their city and pet and show them their Band Name.. lol
band_name = (user_pet + " " + user_city)
print("Your Band name could be: " + band_name)
