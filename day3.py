1.Check if a Number is Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

2.Reverse a String
text = input("Enter a string: ")
reversed_text = text[::-1]
print(f"The reversed string is: {reversed_text}")

3.  Find the GCD of Two Numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
while b:
    a, b = b, a % b
print(f"The GCD is: {a}")

4.Count Words in a String
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print(f"The sentence has {word_count} words.")

5.Check if a Number is Armstrong
num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]
if sum(d**len(digits) for d in digits) == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

6. Find the Sum of an Arithmetic Progression
a = int(input("Enter the first term: "))
d = int(input("Enter the common difference: "))
n = int(input("Enter the number of terms: "))
sum_ap = n * (2 * a + (n - 1) * d) // 2
print(f"The sum of the AP is: {sum_ap}")

7. Sort a List of Numbers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_numbers = sorted(numbers)
print(f"The sorted list is: {sorted_numbers}")

8.Find the Sum of Elements in a List
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
total_sum = sum(numbers)
print(f"The sum of the elements is: {total_sum}")

9.Generate a Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

10. Check if Two Strings are Anagrams
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
