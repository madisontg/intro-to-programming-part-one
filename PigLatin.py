# Madison Thorburn-Gundlach
# Due September 29, 2015
# Pig Latin Generator

# prompt for user input
user_input = input("Gimme a word. Please.\nAlso you can enter '.' to exit.\n")

# while loop to continue until "."
while user_input != ".":
    user_input.lower()
    # slice to see if word begins with vowel
    vowel_start = user_input[0] in "aeiou"
    
    # if True add "yay"
    if vowel_start == True:
        print(user_input+"yay")

    # else new string, add to until equals vowel, add new string plus "ay" to end of word
    else:
        to_append = user_input[0]
        index = 1
        if user_input[index] in "aeiou":
            print(user_input[index:]+to_append+"ay")
        else:
            to_append = to_append+user_input[index]
            index += 1
            
    user_input = input("Gimme another one, or enter '.' to quit.\n")
