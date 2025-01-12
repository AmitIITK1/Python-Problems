# 1. Factorial of a Number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}.")

# 2. Prime Numbers Between 1 and 100
for num in range(2, 101):
    if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
        print(num, end=" ")

# 3. Check Palindrome String
string = input("Enter a string: ")
print(f"'{string}' is a palindrome." if string == string[::-1] else f"'{string}' is not a palindrome.")

# 4. Count Vowels in a String
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
print(f"The number of vowels in '{string}' is {sum(1 for char in string if char in vowels)}.")

# 5. Fibonacci Sequence
n = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
  
# 6. Sum of Digits in a Number
number = input("Enter a number: ")
print(f"The sum of digits in {number} is {sum(int(digit) for digit in number)}.")

# 7. Number Guessing Game
import random
target = random.randint(1, 100)
while True:
    guess = int(input("Guess a number: "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("You guessed it!")
        break

# 8. Largest and Smallest in a List
numbers = list(map(int, input("Enter numbers: ").split()))
print(f"Largest: {max(numbers)}, Smallest: {min(numbers)}")

# 9. Reverse String Without Slicing
string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print(f"Reversed: {reversed_string}")

#10. Check Armstrong Number
number = int(input("Enter a number: "))
num_digits = len(str(number))
armstrong_sum = sum(int(digit) ** num_digits for digit in str(number))
print(f"{number} is an Armstrong number." if number == armstrong_sum else f"{number} is not an Armstrong number.")
