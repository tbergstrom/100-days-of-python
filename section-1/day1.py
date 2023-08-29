print("1" * 50)  # 1: Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python print function.
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")


print("2" * 50)  # 2: Look at the code in the code editor on the right. There are errors in all of the lines of code. Fix the code so that it runs without errors.
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


print("3" * 50)  # 3: Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.
input_name = input("What is your name?")
print(len(input_name))


print("4" * 50)  # 4: Write a program that switches the values stored in the variables a and b.
a = input("a: ")
b = input("b: ")

temp = a
a = b
b = temp

print("a: " + a)
print("b: " + b)


print("5" * 25, " Day 1 Project ", "5" * 25)
# Project :#1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in.
#
# 3. Ask the user for the name of a pet.
#
# 4. Combine the name of their city and pet and show them their band name.
#
# 5. Make sure the input cursor shows on a new line:

print("Welcome to Band Name Generator")
city_input = input("Please enter the name of your city: \n")
pet_input = input("Please enter your pet's name: \n")
band_name = city_input + " " + pet_input
print("Your band name could be " + band_name)
