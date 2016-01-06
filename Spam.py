# Madison Thorburn-Gundlach
# September 28 LAB
# Order from a menu in the Monty Python Spam sketch using random

import random

spam_before = random.randint(0,3)
spam_after = random.randint(0,3)
print("baked ham")
print("broiled ham")
print("smoked ham")
print("grilled ham")
user_order = input("Whaddaya want?\n")

print("SPAM "*spam_before, user_order, "SPAM "*spam_after)
