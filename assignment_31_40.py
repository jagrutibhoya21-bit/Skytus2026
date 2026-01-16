# 31. Student dictionary
students = {"Amit": 85, "Riya": 90}
print(students)

# 32. Add key-value
students["Neha"] = 88
print(students)

# 33. Delete key
del students["Amit"]
print(students)

# 34. Merge dictionaries
d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2)
print(d1)

# 35. Check key exists
print("Riya" in students)

# 36. Word frequency
text = "python is easy and python is powerful"
words = text.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)

# 37. Max value key
print(max(students, key=students.get))

# 38. Reverse key-value
rev = {v: k for k, v in students.items()}
print(rev)

# 39. Update value
students["Riya"] = 95
print(students)

# 40. List of tuples to dictionary
pairs = [("a", 1), ("b", 2)]
print(dict(pairs))