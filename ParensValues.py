# Madison Thorburn-Gundlach
# Due September 1, 2015

# Make order of operations unnecessary by making the outcomes equal anyway

# Variables
a = 11
b = 7
c = 1

# Math
test_one = a + b * c
test_two = (a + b) * c
test_three = a + (b * c)

# Is it done?
one_and_two = test_one == test_two
one_and_three = test_one == test_three

if one_and_two == True:
    if one_and_three == True:
        print("It is done.")
    else: print("Scenario three isn't the same.")
else: print("The first two don't match.")
