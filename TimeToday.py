# Madison Thorburn-Gundlach
# Due September 1, 2015

# Given seconds, output current time

# Variables
user_input = input("Give me a number between 1 and 86,400.")
seconds_input = int(user_input)
seconds_remaining = seconds_input % 60
minutes_total = seconds_input // 60
minutes = minutes_total % 60
hours = minutes_total // 60

# Print
print("The time is", hours, ":", minutes, ":", seconds_remaining)

