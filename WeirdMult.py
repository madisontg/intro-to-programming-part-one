# Madison Thorburn-Gundlach
# Due September 15, 2015
# Find the product via weird stupid Russian Peasant / Ancient Egyptian Method

# Input: ask the user for two integers to multiply (a and b).  Also establish “product” as 0.
integer_one = int(input("Gimme a number\n"))
integer_two = int(input("Gimme another\n"))
product = 0

# while loop
while integer_two != 0:
    integer_one *= 2

    if integer_two % 2 == 0:
        integer_two /= 2
    else:
        product += integer_one
        integer_two -= 1

# return
print("The product of those two numbers is", product)
