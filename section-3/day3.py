####################################### BMI 2.0 #######################################

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#
# It should tell them the interpretation of their BMI based on the BMI value.
#
#     Under 18.5 they are underweight
#     Over 18.5 but below 25 they have a normal weight
#     Over 25 but below 30 they are slightly overweight
#     Over 30 but below 35 they are obese
#     Above 35 they are clinically obese.


# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(weight/ height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif 18.5 < bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif 25 < bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight")
elif 30 < bmi < 35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")


####################################### Leap Year #######################################

# Write a program that works out whether if a given year is a leap year.


# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# A leap year must be:

# Evenly divisible by 4
# NOT evenly divisible by 100
# Evenly divisible by 400

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("Leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")


####################################### Pizza Ordering Practice  #######################################

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

total = 0

if size == "S":
    if add_pepperoni == "Y":
        total = 18
    else:
        total = 15
elif size == "M":
    if add_pepperoni == "Y":
        total = 23
    else:
        total = 20
elif size == "L":
    if add_pepperoni == "Y":
        total = 28
    else:
        total = 25

if extra_cheese == "Y":
    total += 1

print(
    f"Your final bill is: ${total}."
)


####################################### Love Calculator #######################################

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

names = name1 + name2

true_count = 0
love_count = 0

for letter in names:
    for inner_letter in "TRUE":
        if letter.upper() == inner_letter.upper():
            true_count += 1
    for inner_letter in "LOVE":
        if letter.upper() == inner_letter.upper():
            love_count += 1

true_count *= 10
total_count = true_count + love_count

if total_count < 10 or total_count > 90:
    print(f"Your score is {total_count}, you go together like coke and mentos.")
elif 40 < total_count < 50:
    print(f"Your score is {total_count}, you are alright together.")
else:
    print(f"Your score is {total_count}.")




