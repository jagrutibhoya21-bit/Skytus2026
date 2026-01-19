#  1 Function to check if a number is prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter number: "))
print("Prime Number" if is_prime(num) else "Not Prime")


#  2   Function to reverse a string
def reverse_string(s):
    return s[::-1]

text = input("Enter string: ")
print("Reversed:", reverse_string(text))

# 3   Function to find factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

num = int(input("Enter number: "))
print("Factorial:", factorial(num))


#  4  Function to calculate simple interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

print("Simple Interest:", simple_interest(p, r, t))


# 5 Function to check palindrome word
def is_palindrome(word):
    return word == word[::-1]

word = input("Enter word: ")
print("Palindrome" if is_palindrome(word) else "Not Palindrome")



#  6   Function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

text = input("Enter string: ")
print("Vowel count:", count_vowels(text))


# 7   Function to merge two lists
def merge_lists(list1, list2):
    return list1 + list2

l1 = [1, 2, 3]
l2 = [4, 5, 6]

print("Merged List:", merge_lists(l1, l2))


# 8  Function to find GCD of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD:", gcd(x, y))

#  9  Function to find area of rectangle
def area_rectangle(length, width):
    return length * width

l = float(input("Enter length: "))
w = float(input("Enter width: "))

print("Area of Rectangle:", area_rectangle(l, w))

#  10 Function to check Armstrong number

def is_armstrong(n):
    temp = n
    sum = 0
    digits = len(str(n))

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    return sum == n

num = int(input("Enter number: "))
print("Armstrong Number" if is_armstrong(num) else "Not Armstrong")


