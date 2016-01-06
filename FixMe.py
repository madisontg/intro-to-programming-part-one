# Madison Thorburn-Gundlach
# September 14, 2015 Lab

#####################################################################################################################################

#The following comments explain what the code that follows *should* do.
#Fix the code so that it works that way, retaining as much of the original
#code as possible and answer the questions as required.
#1. The following code should find the average of 4 values (simple mean)

##hw1 = 90
##hw2 = 80
##hw3 = 70
##hw4 = 79
##hw_average = (hw1+hw2+hw3+hw4) / 4;
##print("The average of hw assignments 1-4 (with grade values ",hw1,", ", hw2,", ", hw3, ", and ", hw4, ")\nis ",hw_average, sep = "")

#(a) What is the average according to the original program run? (before you make any changes)
# 259.75

#(b) Add parentheses to change hw1+hw2+hw3+hw4 / 4 to: (hw1+hw2+hw3+hw4)/4. What
# is the value of average now?  Is this correct now?
# 79.75.  Yes, this is the correct answer.  Before the parenthases there was an issue with order of operations.

#(c) Finally, correct these lines fully to allow correct calculation of the average using good
# style and variable names.

######################################################################################################################################

#2. Uncomment this code and comment out the code from question 1.
# The following code should read in a value and output the appropriate month name.

##months_since_December = int(input("NASA released an update last December.  How many months has it been since then? "))
##if 1 <= months_since_December <= 12:
##    if months_since_December == 1:
##        print("This month is January")
##    elif months_since_December == 2:
##        print("This month is February")
##    elif months_since_December == 3:
##        print("This month is March")
##    elif months_since_December == 4:
##        print("This month is April")
##    elif months_since_December == 5:
##        print("This month is May")
##    elif months_since_December == 6:
##        print("This month is June")
##    elif months_since_December == 7:
##        print("This month is July")
##    elif months_since_December == 8:
##        print("This month is August")
##    elif months_since_December == 9:
##        print("This month is September")
##    elif months_since_December == 10:
##        print("This month is October")
##    elif months_since_December == 11:
##        print("This month is November")
##    elif months_since_December == 12:
##        print("This month is December")
##else:
##    print("Invalid month")

#(a) This program is better structured as a elif than as an else-if.  Write as a comment below this
# why this is the case and then change the above to use elif instead of else-if
# These statements are all dependent upon what the "value" input contains.

# Else-if is better suited to nested statements with if statements that are dependent upon a previously stated if statement
# instead of all if/elif/else being dependent on the same one thing.

#(b) What is the output with input 7?
# "Some month I don't care about"

#(c) Type in 19 as the month.  What is the output with this input?
# "Some month I don't care about"

#(d) I would like this program to have all the months and, when given a month that is 
# larger than 12 or less than 1, it should simply say, "Invalid month".  While you are at it,
# fix the variable name and prompt to make more sense.

###########################################################################################################################

#3. Comment out the code from Question 2 and uncomment the following code.
# The following code does ... something, not really sure what.  We'll figure it out.

##number1 = -1
##done = True
##decimal = 2.9+0.1+0.1+0.1+.1+0.1+.05
##print(decimal)
##if number1 < 0 and done:
##    if decimal == 3.35:
##        print("We're done here")
##    elif number1 == -1:
##        print("Still got more work")
##else:
##    if (done or decimal == 2):
##        number1 = 1 
##    else:
##        (1-number1)
##    if not done:
##            print("Interesting 2")
##    else:
##        print(number1)
            
#(a) Comment out the code for Questions 1 and 2 and uncomment this code. Rename n and d
# to number1 and decimal.

#(b) Run this code.  What is it's output?
# "3.45  Still got more work"

#(c) What is the "if" condition that the "else" on the line prior to number1 = (done....)
# corresponds to?  Hint: Indentation should help here.
# "if number1 < 0 and done:"

#(d) In the else portion of the first if, neither Interesting nor Interesting 2 
# will be an output.  Explain why, no matter what I set number1, decimal, and 
# done to earlier, neither will be output.
# Number1 must be negative OR done must be false in order to print Interesting or Interesting 2.
# Number1 is set to 1 because done == True is True.
# done is True.

#(e) Carefully remove the redundant cases (if-statement that produces Interesting
# with the accompanying code) so that the program still works like it did before removing it (regardless
# of what number1, done, and decimal are set to in the first 3 lines). "Unpack" the single-line
# conditional setting number1 below the else: statement and otherwise reformat the above code to
# follow class style standards.

##########################################################################################################

#4. The following code is supposed to calculate the average of any number of values.
# Instead it runs forever.  Answer the following questions to fix it.

##value = int(input("Please enter values (type -1 to stop): "))
##total = 0
##count = 0
##done = False;
##while done == False:
##    value = int(input("Please enter values (type -1 to stop): "))
##    if value == -1:
##        done = True
##    else:
##        total += value
##        count += 1
##print("The average is",total / count)

#(a) Uncomment these lines of code and make sure Questions 1-3 are commented out now.
# Run the program.  Why does the program not even start?
# Invalid syntax.  The code tries to set done equal to false in the parameters of the while loop.

#(b) Fix this part of the program to run.  Specifically,
# so that it keeps accepting numbers from the console until the user types -1.

#(c) Does this program now calculate the average of the input values?  Why not?
# No.  It will always say that the average is -1 since value is set to whatever the user last entered,
# and the user will always enter -1 last to break the loop as instructed.

#(d) Fix this program to keep a running total and also a count of the number
# of numbers entered.  After the loop finishes, have it print out the actual
# average of the numbers entered.







