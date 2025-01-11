1.Helps you figure out which of the two numbers you enter is the largest.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers and display the result
if num1 > num2:
    print(f"The larger number is {num1}")
elif num1 < num2:
    print(f"The larger number is {num2}")
else:
    print("Both numbers are the same!")



2.To display all the even numbers between 1 and 50.

# Print a message before displaying the even numbers
print("Here are the even numbers between 1 and 50:")

# Loop through numbers from 1 to 50 and print only the even ones
for number in range(1, 51):
    if number % 2 == 0:
        print(number, end=" ")


3. Program checks if the number you input is positive, negative, or zero.

# Get a number from the user
number = float(input("Enter a number: "))

# Check the conditions and print the result
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


4. A fun little program that greets you by name!

# Ask the user for their name
name = input("What's your name? ")

# Greet the user
print(f"Hello, {name}! It's great to meet you.")


5. Calculates how many characters are in a string you provide.

# Take a string input from the user
user_input = input("Type something interesting: ")

# Calculate and display the length of the string
print(f"The length of what you typed is {len(user_input)} characters.")


6.Calculates the area when you provide the length and breadth.

# Get the dimensions of the rectangle
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Calculate the area
area = length * breadth

# Print the result
print(f"The area of the rectangle is {area} square units.")



7. To swap two numbers without using an extra variable.

# Input two numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Display values before swapping
print(f"Before swapping: a = {a}, b = {b}")

# Swap the numbers
a, b = b, a

# Display values after swapping
print(f"After swapping: a = {a}, b = {b}")



8. Program checks whether the given number is divisible by both 3 and 5.

# Get the number from the user
number = int(input("Enter a number: "))

# Check divisibility and print the result
if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5.")
else:
    print(f"{number} is not divisible by both 3 and 5.")


9.To check if a year is a leap year.

# Ask the user for a year
year = int(input("Enter a year: "))

# Leap year logic
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


10. Generates and displays the first 10 multiples of a number you enter.

# Get the number from the user
number = int(input("Enter a number: "))

# Print the first 10 multiples
print(f"The first 10 multiples of {number} are:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
