# 1. Reverse a given string without using slicing
def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
print(reverse_string("Python"))

# 2. Find the second largest number in a list
numbers = [12, 45, 67, 89, 34, 23]
unique_numbers = list(set(numbers))
unique_numbers.sort()
print(f"Second largest number: {unique_numbers[-2]}")

# 3. Check if two strings are anagrams
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
print(is_anagram("listen", "silent"))

# 4. Calculate the sum of all even numbers in a range
start = 1
end = 50
even_sum = sum(i for i in range(start, end + 1) if i % 2 == 0)
print(f"Sum of even numbers: {even_sum}")

# 5. Generate a list of squares for numbers in a range
n = 10
squares = [i**2 for i in range(1, n+1)]
print(squares)

# 6. Find all unique elements in a list
data = [2, 3, 4, 3, 2, 5, 6, 6, 7]
unique_elements = list(set(data))
print(f"Unique elements: {unique_elements}")

# 7. Count the frequency of each character in a string
text = "hello world"
frequency = {char: text.count(char) for char in set(text)}
print(frequency)

# 8. Check if a number is a perfect square
import math
def is_perfect_square(num):
    root = math.sqrt(num)
    return root.is_integer()
print(is_perfect_square(16))

# 9. Print a pattern of stars (pyramid shape)
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# 10. Merge two dictionaries into one
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)
