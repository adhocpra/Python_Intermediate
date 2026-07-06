#sorted(iterable, key=lambda x: ..., reverse=False)


students = [
    ("Ram",25),
    ("Bi",23),
    ("Mike",34)
]
#this is regular
students.sort()
print(students)

students.sort(key= lambda student :student[1])
print(students)

students.sort(key= lambda student:student[1], reverse=True)
print(students)


products = [
    ("shoes", 120),
    ("bag",45),
    ("watch",200),
    ("belt",30)
]
products.sort(key=lambda product:product[1])
print(products)

products.sort(key=lambda product:product[1], reverse=True)
print(products)

names= ["Alexander", "Bob", "Christina", "Al", "Sam"]
names.sort(key=lambda name:len(name))
print(names)

names.sort(key=lambda name:len(name), reverse=True)
print(names)

words= ["banana", "apple", "cherry", "kiwi"]
words.sort(key=lambda word:word[-1])
print(words)

nums= [-10,3,-1,8,-5,2]
nums.sort(key=lambda num:abs(num))
print(nums)

#sorted
nums = [5,2,8,1,9]
print(sorted(nums))
print(sorted(nums, reverse=True))

word= "python"
print(sorted(word))
#sorted(iterable, key=lambda x: x[index], reverse=True/False)

coords= [(1,5),(3,2),(2,8),(4,1)]
new=sorted(coords, key=lambda coord:coord[1])
print(new)


students= [("Alexander", 90), ("Bo",85),("Christiana",78)]
new=sorted(students, key= lambda student:len(student[0]))
print(new)

data= [[1, 2, 3], [4, 5, 1], [7, 8, 2]]
new= sorted(data, key= lambda data:data[-1])
print(new)

employees=(("Ram",25),("Sita",20),("Mike",30),("Priya",20))
new_age= sorted(employees, key=lambda employee:employee[1])
print(new_age)
new_name=sorted(new_age,key=lambda nn:nn[0])
print(new_name)

# 1. sort people by age
people = [{"name": "Ram", "age": 25}, {"name": "Sita", "age": 20}, {"name": "Mike", "age": 30}]
new=sorted(people, key=lambda p:p["age"])
print(new)

# 2. sort emails by domain
emails = ["ram@gmail.com", "sita@yahoo.com", "mike@gmail.com", "priya@hotmail.com"]
# email= "ram@gmail.com"
# parts= email.split("@")
# print(parts)
# print(parts[0])
# print(parts[1])
new=sorted(emails,key=lambda e:e.split("@")[1])
print(new)

# 3. sort words by last letter
words = ["banana", "apple", "cherry", "kiwi"]


# 4. sort products by price descending
products = [("shoes", 120), ("bag", 45), ("watch", 200), ("belt", 30)]


# 5. sort names ignoring case
names = ["ram", "Alice", "bob", "Zara", "mike"]

new=sorted(names, key=lambda n: n.lower())
print(new)

# sort by value
scores = {"Ram": 90, "Sita": 75, "Mike": 85, "Priya": 60}
new= sorted(scores, key= lambda s:scores[s],reverse=True)
print(new)

# 2. sort by key alphabetically
inventory = {"banana": 5, "apple": 12, "cherry": 3, "mango": 8}
new=sorted(inventory, key=lambda k:k)
print(new)
#new=sorted(inventory)

# 3. sort by value descending (highest first)
votes = {"Alice": 120, "Bob": 95, "Charlie": 150, "Diana": 80}
new= sorted(votes, key= lambda v:votes[v],reverse =True)
print(new)
# 4. sort and return as list of tuples
students = {"Ram": 90, "Sita": 75, "Mike": 85}
new= sorted(students.items(), key= lambda s:s[1])
print(new)

#dict review
person = {"name": "Sita", "age": 22, "city": "Kathmandu"}
print(person["city"])
print(person["age"])

car= {"brand": "Toyota", "model": "Corolla", "year": 2020}
for key in car.keys():
    print(key)
for key in car:
    print(key)

for value in car.values():
    print(value)

for c in car:
    print(c, car[c])

 #. loop and print key: value
student = {"name": "Ram", "grade": "A", "marks": 95}
for s in student:
    print(s + ":",student[s])

for key in student.keys():
    print(key)

#or value in student.values():
    print(value)

population = {"Nepal": 30, "India": 1400, "USA": 330, "China": 1400}
new= sorted(population,key= lambda p:population[p])
print(new)

fruits = {"mango": 5, "apple": 12, "banana": 3, "cherry": 8}
new=sorted(fruits, key=lambda f:fruits[f])
print(new)

prices = {"shoes": 120, "bag": 45, "watch": 200, "belt": 30}
new= dict(sorted(prices.items(), key=lambda p:p[1],reverse=True))
print(new)

capitals = {"Nepal": "Kathmandu", "USA": "Washington", "Japan": "Tokyo", "France": "Paris"}
new=sorted(capitals, key=lambda c:len(capitals[c]))
print(new)

# 1. sort by age
people = {"Ram": 25, "Sita": 20, "Mike": 30, "Priya": 22}
new= sorted(people, key=lambda p:people[p])
print(new)
# 2. sort cities by name length
cities = {"KTM": "Kathmandu", "NYC": "New York", "TKY": "Tokyo", "LON": "London"}
new= sorted(cities, key=lambda c:len(cities[c]))
print(new)
# 3. sort by number of characters in key
products = {"television": 500, "tv": 200, "phone": 300, "laptop": 800}
new=sorted(products, key= lambda p:len(p))
print(new)
# 4. sort by remainder when divided by 3
nums = {"a": 10, "b": 7, "c": 9, "d": 5}
new= sorted(nums, key= lambda n:nums[n] % 3)
print(new)

# 5. sort by last letter of key
words = {"banana": 1, "apple": 2, "cherry": 3, "kiwi": 4}
new= sorted(words, key= lambda word:word[-1])
print(new)

# --- more dict problems (lambda only) ---

# 6. use max() with key=lambda to find the key with the highest value
population = {"Nepal": 30, "India": 1400, "USA": 330, "China": 1400}

# 7. use min() with key=lambda to find the key with the shortest value (string)
capitals = {"Nepal": "Kathmandu", "USA": "DC", "Japan": "Tokyo", "France": "Paris"}

# 8. use filter() with a lambda to keep only dict items where the value is above a threshold
scores = {"Ram": 90, "Sita": 55, "Mike": 85, "Priya": 40}
threshold = 60

# 9. use filter() with a lambda to keep only keys that start with a vowel
grades = {"Ram": "A", "Sita": "B", "Ishwor": "A", "Priya": "C", "Anish": "B"}

# 10. use map() with a lambda to build a list of "key: value" strings from dict.items()
prices = {"shoes": 120, "bag": 45, "watch": 200}

# 11. sort dict items by value descending, breaking ties by key ascending (lambda returning a tuple)
votes = {"Alice": 120, "Bob": 95, "Charlie": 120, "Diana": 80}

# 12. sort a dict of lists by the length of each list value
teams = {"A": [1, 2, 3], "B": [4, 5], "C": [6, 7, 8, 9]}

# 13. sort dict keys by the sum of ASCII values of each key (use sum + ord inside the lambda)
words = {"cab": 1, "ab": 2, "dad": 3}

# 14. sort a dict of tuples by the second element of the tuple value
matches = {"team1": ("won", 3), "team2": ("lost", 0), "team3": ("won", 5)}

# 15. sort dict keys using a lambda that looks up rank in a separate priority dict
priority = {"low": 3, "medium": 2, "high": 1}
tasks = {"clean": "low", "deploy": "high", "review": "medium"}

