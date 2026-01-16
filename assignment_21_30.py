# 21. Tuple of 5 numbers
t = (10, 20, 30, 40, 50)
print(t)

# 22. Third element
print(t[2])

# 23. Unpack tuple
a, b, c, d, e = t
print(a, b, c, d, e)

# 24. Set of fruits
fruits = {"apple", "banana", "mango", "orange", "grapes"}
print(fruits)

# 25. Add fruit
fruits.add("kiwi")
print(fruits)

# 26. Remove fruit
fruits.remove("banana")
print(fruits)

# 27. Union
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)

# 28. Intersection
print(s1 & s2)

# 29. Subset check
print({1, 2}.issubset(s1))

# 30. Remove duplicates using set
lst = [1, 2, 2, 3, 3]
print(list(set(lst)))