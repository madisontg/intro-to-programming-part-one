# Madison Thorburn-Gundlach
# Due September 22, 2015
# Find a two digit number AB that, when squared, a) doesn't exceed 999 and b) ends in "AB"

number = 10
squared = (number * number)

#math loops
while squared < 999:
    squared_str = str(squared)
    last_two = squared_str[-2:]
    last_two = int(last_two)
    if last_two == number:
        print(number, squared)
        squared = 1000
    else:
        number += 1
        squared = number * number
        print(number, squared)

    
