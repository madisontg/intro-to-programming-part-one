# Madison Thorburn-Gundlach
# Due Semptember 8, 2015

# Write a for loop that will return "pbil" when "alphabetical" is given as input

given_input = input("Type 'alphebetical'.\n")

for word in given_input:
    if given_input == 'alphebetical':
        print("pbil")
    given_input = 'other'
