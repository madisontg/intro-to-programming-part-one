# Madison Thorburn-Gundlach
# Due Semptember 8, 2015

##my_var = 4 # execute assignment 1
##my_var = 3 # execute assignment 2
##my_var = 2 # execute assignment 3
##my_var = 12 # executes assignment 4

my_var = 1
while my_var <= 15:
    print(my_var, end = ":")
    if my_var % 2:
        if my_var **3 != 27:
            my_var_two = my_var + 4
            print("Assignment 1")
        else:
            my_var_two = my_var / 1.5
            print("Assignment 2")
    else:
         if my_var <= 10:
              my_var_two = my_var * 2
              print("Assignment 3")
         else:
              my_var_two = my_var - 2
              print("Assignment 4")
    my_var += 1
