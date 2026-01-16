# 1. String length
s = input("Enter string: ")
print("Length:", len(s))

# 2. Convert to lowercase
print(s.lower())

# 3. Replace spaces with underscores
print(s.replace(" ", "_"))

# 4. First and last character
print("First:", s[0], "Last:", s[-1])

# 5. Reverse string
print("Reverse:", s[::-1])

# 6. Count letter frequency
ch = input("Enter character: ")
print("Count:", s.count(ch))

# 7. Check word present
word = input("Enter word: ")
print(word in s)

# 8. Name & age using f-string
name = input("Name: ")
age = int(input("Age: "))
print(f"My name is {name} and I am {age} years old")

# 9. Remove extra spaces
s2 = "   Hello Python   "
print(s2.strip())

# 10. Join words with -
words = ["Python", "is", "easy"]
print("-".join(words))