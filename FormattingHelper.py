# Madison Thorburn-Gundlach
# Due October 1, 2015
# Take input s, d, f, or q (only); ask respectively for string, integer, or float;
# format string as right-aligned minimum-width 10, integer as center-aligned minimum-width 4, or float left-aligned minimum-width 6 with exactly 2 decimal places

# input prompt
user_input = input("Gimme a letter: s, d, f, or q.\n")
user_input = user_input.lower()

# while loop for bad input
while user_input not in "sdfq":
    user_input = ("Perhpas you misread.  Your options are s, d, f, or q.  Try again.\n")
    user_input = user_input.lower()

# runs actual program part
else:
    while user_input not in "q":
        if user_input == "s":
            user_input_secondary = input("Gimme a string.\n")
            to_return = "{:>10s}".format(user_input_secondary)
            print(to_return)
            user_input = input("Gimme a letter: s, d, f, or q.\n")
        elif user_input == "d":
            user_input_secondary = int(input("Gimme an integer.\n"))
            to_return = "{:^4d}".format(user_input_secondary)
            print(to_return)
            user_input = input("Gimme a letter: s, d, f, or q.\n")
        elif user_input == "f":
            user_input_secondary = float(input("Gimme a float.\n"))
            to_return = "{:<6.2f}".format(user_input_secondary)
            print(to_return)
            user_input = input("Gimme a letter: s, d, f, or q.\n")
    else:
        pass
                
