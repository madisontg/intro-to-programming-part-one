# Madison Thorburn-Gundlach
# Due Semptember 8, 2015

# Assuming a paper is 1/200 cm thick, how thick would it be if folded x times?

#  input
thickness = 1/200
folds_int = int(input("How many times do you want to fold your newspaper?\n"))

# every time you fold a paper, it doubles in thickness
for int in range(1 , folds_int):
    thickness *= 2

print("Your newspaper would be", thickness, "cm thick.")
