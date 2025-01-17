# 1. Generate Fibonacci Sequence up to N Terms
n = int(input("Enter the number of terms: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i - 1] + fib[i - 2])
print(f"Fibonacci sequence: {fib[:n]}")

# 2. Check if a String is Palindrome (Ignoring Case and Spaces)
text = input("Enter a string: ").replace(" ", "").lower()
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# 3. Calculate the Sum of Squares of N Natural Numbers
n = int(input("Enter a number: "))
sum_of_squares = sum(i**2 for i in range(1, n + 1))
print(f"The sum of squares is: {sum_of_squares}")

# 4. Count the Number of Vowels and Consonants in a String
text = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = sum(1 for char in text if char in vowels)
consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")

# 5. Find the Largest Prime Factor of a Number
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

num = int(input("Enter a number: "))
for i in range(num, 1, -1):
    if num % i == 0 and is_prime(i):
        print(f"Largest prime factor: {i}")
        break

# 6. Transpose a Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Transpose of the matrix:")
for row in transpose:
    print(row)

# 7. Check if All Elements in a List are Unique
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
if len(numbers) == len(set(numbers)):
    print("All elements are unique.")
else:
    print("There are duplicate elements.")

# 8. Calculate the Factorial of a Number Without Recursion
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is: {factorial}")

# 9. Find the Longest Word in a Sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print(f"The longest word is: {longest_word}")

# 10. Check if a Number is a Perfect Square
import math
num = int(input("Enter a number: "))
if math.isqrt(num)**2 == num:
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
