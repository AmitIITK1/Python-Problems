# 1. Find the Second Largest Number in a List
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_numbers = list(set(numbers))
unique_numbers.sort()
if len(unique_numbers) > 1:
    print(f"The second largest number is: {unique_numbers[-2]}")
else:
    print("Not enough unique numbers to find the second largest.")

# 2. Check if a String Contains Only Digits
text = input("Enter a string: ")
if text.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")

# 3. Find the Factorial of a Number Recursively
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
num = int(input("Enter a number: "))
print(f"The factorial of {num} is: {factorial(num)}")

# 4. Check if a Number is Prime
num = int(input("Enter a number: "))
if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# 5. Merge Two Dictionaries
dict1 = eval(input("Enter the first dictionary: "))
dict2 = eval(input("Enter the second dictionary: "))
merged_dict = {**dict1, **dict2}
print(f"The merged dictionary is: {merged_dict}")

# 6. Generate Pascal's Triangle
rows = int(input("Enter the number of rows: "))
triangle = [[1] * (i + 1) for i in range(rows)]
for i in range(2, rows):
    for j in range(1, i):
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
for row in triangle:
    print(" ".join(map(str, row)))

# 7. Find the Intersection of Two Lists
list1 = list(map(int, input("Enter the first list separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list separated by spaces: ").split()))
intersection = list(set(list1) & set(list2))
print(f"The intersection is: {intersection}")

# 8. Find the Missing Number in a Sequence
sequence = list(map(int, input("Enter the sequence separated by spaces: ").split()))
n = len(sequence) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(sequence)
print(f"The missing number is: {expected_sum - actual_sum}")

# 9. Convert Decimal to Binary, Octal, and Hexadecimal
num = int(input("Enter a decimal number: "))
print(f"Binary: {bin(num)[2:]}, Octal: {oct(num)[2:]}, Hexadecimal: {hex(num)[2:]}")

# 10. Rotate a List by n Positions
lst = list(map(int, input("Enter the list separated by spaces: ").split()))
n = int(input("Enter the number of positions to rotate: "))
n %= len(lst)
rotated = lst[-n:] + lst[:-n]
print(f"The rotated list is: {rotated}")
```
