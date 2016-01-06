# Madison Thorburn-Gundlach
# September 28 LAB
# Exercise 10 on pg 220

S = "I had a cat named amanda when I was little."
index = 0
count = 0

while index < 43:
    if S[index] == "a":
        count += 1
    index += 1
print(count)
