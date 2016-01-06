# Madison Thorburn-Gundlach
# Due Septmeber 6, 2015
# User tries to guess a set number.
# Computer responds "too low", "too high", or "Correct"

# variable assign
correct_value = 65
guess = input("I know a number.  What do you think it is? \n")
guess = int(guess)

# check guess
while guess != correct_value:
    if guess < correct_value:
        guess = input("Too low, try again.\n")
        guess = int(guess)
    elif guess > correct_value:
        guess = input("Too high, try again.\n")
        guess = int(guess)

print("\nCorrect!")
