# Madison Thorburn-Gundlach
# Due September 15, 2015
# Loop weird Russian/Egyptian multiplication method thing

#establish sentinel value
run = True

# while loop to run "infinitely"
while run == True:
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
    run_input = int(input("Wanna go again? 1 for yes, 0 for no.\n"))
    if run_input == 0:
        run = False
