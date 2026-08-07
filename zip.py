#zip() pairs up corresponding elements from multiple iterables at once, so you can loop over them together instead of indexing manually.

names= ["R", "L" "S", "K"]
ages= [25,6,8,9,10]
result= list(zip(names, ages))
print(result)

for pair in zip(names,ages):
    print(pair[0],pair[1])
    

names= ["Radio", "Mobile", "wallet", "mug"]
prices= [20,39,67,90,8]

for item in zip(names,prices):
    print(item)
for name,price in zip(names,prices):
    print(f"{name.upper():{price*100}}")
# Because each result from zip() represents a fixed-size grouping — exactly one element from each input iterable, at a given position — and that's exactly what a tuple is designed for: an immutable, fixed-length collection of items that belong together but don't need to change.

# A few reasons tuple specifically, not list:

# Fixed size by nature — zip(names, ages) always produces 2-item groupings (or however many iterables you pass); it's never meant to grow/shrink, so an immutable structure fits the intent.
# Lightweight — tuples are cheaper to create than lists in Python, and zip() is often used for large data, so this matters for performance.
# Unpacking works the same either way — for name, age in zip(...) would work whether it yielded tuples or lists; tuple is just the more "correct" semantic choice for "these values are grouped, not a mutable sequence."
# If you ever want lists instead, you convert explicitly: [list(pair) for pair in zip(names, ages)] — but the default is tuple because that's the more accurate representation of "paired data."

# --- zip() practice ---

# 1. build a dict from two parallel lists: keys and values
keys = ["a", "b", "c"]
values = [1, 2, 3]
result=(list(zip(keys,values)))
print(result)
nw= dict(result)
print(nw)
# 2. add corresponding numbers from two lists together
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result= [a+b for a,b in zip (list1,list2)]
print(result)

# 3. combine names and scores into a list of "name: score" strings
students = ["Ram", "Sita", "Mike"]
scores = [90, 75, 85]

result= [f"{name} :{score}" for name,score in zip(students,scores)]
print(result)

# 4. zip three lists together at once (name, subject, grade)
names2 = ["Ram", "Sita"]
subjects = ["Math", "Science"]
grades = ["A", "B"]
result=list(zip(names2,subjects,grades))
print(result)

# 5. unzip a list of pairs back into two separate lists (hint: zip(*pairs))
pairs = [("a", 1), ("b", 2), ("c", 3)]

# 6. check if two lists are equal by comparing elements pairwise with zip()
a = [1, 2, 3]
b = [1, 2, 3]

# 7. build a dict mapping product name to price, filtering to keep only prices over 50
products = ["shoes", "bag", "watch", "belt"]
prices = [120, 45, 200, 30]

# 8. use zip() with range() to pair each item in a list with its 1-based position
fruits = ["apple", "banana", "cherry"]

# 9. multiply corresponding elements from two lists (element-wise product)
vec1 = [1, 2, 3]
vec2 = [4, 5, 6]

# 10. given two lists of unequal length, zip them and note that the result stops at the shorter one
short = ["x", "y"]
long_list = [1, 2, 3, 4, 5]