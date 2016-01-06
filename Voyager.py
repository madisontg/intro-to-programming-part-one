# Madison Thorburn-Gundlach
# Due September 3, 2015
# Calculate the distance of Voyager from the sun x-input days from 9/29/09

# input
days = input("How many days has it been since September 25, 2009?\n(It may be a decimal value.)    ")

# convert from str to float
days = float(days)

# variable assignment
miles_given = 16637000000
velocity_per_day = 38241 * 24
distance = days * velocity_per_day + miles_given

# print/return value
print("Voyager 1 is approximately\n", distance, "miles away.")
