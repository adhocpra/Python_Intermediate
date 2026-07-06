add= lambda a,b:a+b
print (add(3,5))

square= lambda x:x**2
print(square(4))

greet= lambda name: "Hello "  + name
print(greet("ram"))

is_even= lambda x: x%2==0
print(is_even(4))

##result= Aa if condition else B (this is ternary)
age=20
result= "adult" if age>=18 else "minor"
print(result)
even_odd= lambda x:"even" if x %2==0 else "odd"
print(even_odd(25))

sign= lambda x: "positive" if x>0 else "negative" if x<0 else "zero"
print(sign(-3))

maximum= lambda a,b: a if a>b else b
print(maximum(18,5))

# --- max() / min() with key=lambda ---

# 1. find the longest word in the list
words = ["cat", "elephant", "dog", "giraffe"]
result= max(words, key=lambda w:len(w))
print(result)
# 2. find the shortest name in the list
names = ["Alexander", "Bo", "Christina", "Sam"]

# 3. find the number with the largest absolute value
nums = [-10, 3, -8, 5, 2]
result= max(nums, key=lambda n: abs(n))
print(result)
# 4. find the tuple with the highest second element
scores = [("Ram", 90), ("Sita", 75), ("Mike", 85)]
result=max(scores, key=lambda s: s[1])
print(result)
# 5. find the dict (in a list of dicts) with the youngest age
people = [{"name": "Ram", "age": 25}, {"name": "Sita", "age": 20}, {"name": "Mike", "age": 30}]
result= min(people,key=lambda p:p["age"])
print(result)
# 6. find the key in a dict with the smallest value
prices = {"shoes": 120, "bag": 45, "watch": 200}
result=min(prices, key=lambda p:p[0])
print(result)

# 7. find the longest key in a dict (not the value — the key string itself)
inventory = {"tv": 5, "laptop": 2, "ox": 9, "phone": 4}
result= max(inventory, key=lambda i:len(i))
print(result)

# 8. find the word closest to 10 characters long (smallest absolute difference)
titles = ["The Matrix", "Up", "Interstellar", "It"]




#Lambda with custom function:
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    

students=[
    Student("Ram",25),
    Student("Shyam",10),
    Student("hari",14)
]
students.sort(key=lambda student:student.age)

for student in students:
    print(student.name,student.age)