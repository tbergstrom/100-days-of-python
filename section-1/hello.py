print("1" * 50)  # 1: Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python print function.
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")


print("2" * 50)  # 2: Look at the code in the code editor on the right. There are errors in all of the lines of code. Fix the code so that it runs without errors.
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


print("3" * 50)  # 3: Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.
inputName = input("What is your name?")
print(len(inputName))


print("4" * 50)  # 4: Write a program that switches the values stored in the variables a and b.
a = input("a: ")
b = input("b: ")

temp = a
a = b
b = temp

print("a: " + a)
print("b: " + b)

