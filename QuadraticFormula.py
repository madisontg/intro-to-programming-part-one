# Madison Thorburn-Gundlach
# Due September 22, 2015
# Solve the quadratic formula; return correct number of correct roots.

import math

# collect input
a = float(input("What is 'a'?\n"))
b = float(input("What is 'b'?\n"))
c = float(input("What is 'c'?\n"))
discriminant =  b**2 - 4 * a * c

# mathsssssss
if discriminant < 0:
    print("There are no real roots.")
    print("Imaginary roots are:")
    root_imaginary_one = (-1 * b + math.sqrt(-1 * discriminant)) / 2 * a
    print(root_imaginary_one, "j", sep = "")
    root_imaginary_two = (-1 * b - math.sqrt(-1 * discriminant)) / 2 * a
    print(root_imaginary_one, "j", sep = "")
elif discriminant == 0:
    print("There is one root:")
    root = (-1 * b + math.sqrt(discriminant)) / 2 * a
    if root % 1 == 0:
        root = int(root)
    print(root)
else:
    print("There are two roots:")
    root_one = (-1 * b + math.sqrt(discriminant)) / 2 * a
    if root_one % 1 == 0:
        root_one = int(root_one)
    root_two = (-1 * b + math.sqrt(discriminant)) / 2 * a
    if root_two % 1 == 0:
        root_two = int(root_two)
    print(root_one, "and", root_two)
