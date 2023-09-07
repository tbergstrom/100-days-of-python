# BMI Calculator

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = int(weight) / float(height)**2
print(bmi)
bmi_as_int = int(bmi)
print(bmi_as_int)


# Life In Weeks

# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


year_int = 365
week_int = 7

age_in_weeks = age * 52
age_in_months = age * 12
age_in_days = age * 365

ninety_in_weeks = 90 * 52
ninety_in_months = 90 * 12
ninety_in_days = 90 * 365

remaining_days = ninety_in_days - age_in_days
remaining_weeks = ninety_in_weeks - age_in_weeks
remaining_months = ninety_in_months - age_in_months

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")


# Tip Calculator

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to tip calculator")
total_bill = float(input("What was the total bill?"))
tip_input = input("What percentage tip would you like to give? 10, 12, or 15?")
tip_converted = int(1) + (int(tip_input)/100)
num_guests = int(input("How many people to split the bill?"))
print(f"Each person should pay: ${(total_bill / num_guests) * tip_converted}")
