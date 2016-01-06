# Madison Thorburn-Gundlach
# Due September 29, 2015
# "Guess which word"

import random
# five word options
possible_one = "human"
possible_two = "vulcan"
possible_three = "romulan"
possible_four = "klingon"
possible_five = "organian"
sentinel = "quit"

# randomly generate which species is the correct answer
correct_number = random.randint(1,5)
if correct_number == 1:
    correct_species = possible_one
if correct_number == 2:
    correct_species = possible_two
if correct_number == 3:
    correct_species = possible_three
if correct_number == 4:
    correct_species = possible_four
if correct_number == 5:
    correct_species = possible_five
    
# user prompt
print('Five options: "human", "vulcan", "romulan", "klingon", "organian".')
print("Yes, everything is supposed to be lowercase--it's case-sensitive.")
user_guess = input("Take a guess.\nType 'quit' to quit early.\n")

# compare user prompt to correct answer; react
while user_guess != sentinel:
    if user_guess == correct_species:
        print("Correct!")
        user_guess = "quit"
    else:
        user_guess = input("Nope! Guess again!.\nType 'quit' to quit early.\n")
    
