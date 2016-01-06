# Madison Thorburn-Gundlach
# Due September 29, 2015
# "Guess which word" using lists

import random
# five word options
species_list = ["human", "vulcan", "romulan", "klingon", "organian"]
sentinel = "quit"

# randomly generate which species is the correct answer
correct_species = species_list[random.randint(0,4)]

# user prompt
print('Five options: "human", "vulcan", "romulan", "klingon", "organian".')
print("Yes, everything is supposed to be lowercase--it's case-sensitive.")
user_guess = input("Take a guess.\nType 'quit' to quit early.\n")
user_guess.lower()

# compare user prompt to correct answer; react
while user_guess != sentinel:
    if user_guess == correct_species:
        print("Correct!")
        user_guess = "quit"
    else:
        user_guess = input("Nope! Guess again!.\nType 'quit' to quit early.\n")
    

