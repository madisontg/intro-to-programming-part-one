# Madison Thorburn-Gundlach
# Due September 3, 2015
# Calculate the passer rating in football

# inputs
completions = input("How many completions per attempt?")
yards = input("How many yeards per attempt?")
touchdowns = input("How many touchdowns per attempt?")
interceptions = input("How many interceptions per attempt?")

# convert from str to int
completions = int(completions)
yards = int(completions)
touchdowns =  int(touchdowns)
interceptions = int(interceptions)

# calculations
C = (completions * 100 - 30) / 20
Y = (yards - 3) / 4
T = (touchdowns * 20)
I = 2.375 - (interceptions * 35)

pass_rating = ((C + Y + T + I) / 6) * 100

#print/return value
print("The pass rating is", pass_rating)
