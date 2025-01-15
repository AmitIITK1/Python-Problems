# 1. Count the Frequency of Each Character in a String
string = input("Enter a string: ")
frequency = {}
for char in string:
    frequency[char] = frequency.get(char, 0) + 1
print(f"The frequency of each character is: {frequency}")

# 2. Find All Unique Elements in a List
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_elements = [num for num in numbers if numbers.count(num) == 1]
print(f"The unique elements are: {unique_elements}")

# 3. Calculate the GCD of Two Numbers
from math import gcd
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"The GCD of {a} and {b} is: {gcd(a, b)}")

# 4. Generate a Random Password
import random
import string
length = int(input("Enter the desired password length: "))
password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
print(f"The generated password is: {password}")

# 5. Check if Two Strings are Anagrams
str1 = input("Enter the first string: ").replace(" ", "").lower()
str2 = input("Enter the second string: ").replace(" ", "").lower()
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# 6. Find the Transpose of a Matrix
rows = int(input("Enter the number of rows: "))
matrix = [list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split())) for i in range(rows)]
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("The transpose of the matrix is:")
for row in transpose:
    print(" ".join(map(str, row)))

# 7. Find the Sum of All Odd Numbers in a List
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
odd_sum = sum(num for num in numbers if num % 2 != 0)
print(f"The sum of all odd numbers is: {odd_sum}")

# 8. Convert a List of Tuples into a Dictionary
tuples = eval(input("Enter a list of tuples (key, value) format: "))
dictionary = dict(tuples)
print(f"The dictionary is: {dictionary}")

# 9. Determine if a String is a Pangram
string = input("Enter a string: ").lower()
alphabet = set("abcdefghijklmnopqrstuvwxyz")
if alphabet.issubset(set(string)):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")

# 10. Find the Longest Word in a Sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print(f"The longest word is: {longest_word}")
