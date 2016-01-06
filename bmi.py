# Madison Thorburn-Gundlach
# Due Semptember 8, 2015

# Calculate a person's BMI; print out where that BMI fits in the CDC
# standard weight status categories listed on pg 144

# input
weight_metric = float(input("What is your weight in kilograms?\n"))
height_metric = float(input("What is your height in meters?\n"))

# calculate BMI
bmi_float = weight_metric / height_metric **2

# return statement
print("Your BMI is ", bmi_float,".", sep = "", end = " ")
if bmi_float < 18.5:
    print("According to the CDC, you are underweight.")
if 18.5 <= bmi_float <= 24.9:
    print("According to the CDC, you are normal.")
if 25.0 <= bmi_float <= 29.9:
    print("According to the CDC, you are overweight.")
if 30.0 <= bmi_float:
    print("According to the CDC, you are obese.")
