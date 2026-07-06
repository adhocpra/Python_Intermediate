#ways to change list to dict

#if tuple
pairs= [("a",1), ("b",2), ("c",3)]
d= dict(pairs)
print(d)

#if list by dict comprehension
#{key exp:value exp for item in iterable if condition}
words= ["apple", "banana", "cherry"]
new_dict= {w: len(w) for w in words}
print(new_dict)

nums= [1,2,3,4,5,6]
result= {num: num*num for num in nums if num%2==0 }
print(result)
nums= [1,2,3,4,5,6]
result= {num: num*num for num in nums if num%2==0 }
print(result)

# --- dict comprehension practice (no zip / enumerate yet) ---

# 1. build a dict from a list of tuples, but only keep pairs where the value is positive
pairs2 = [("a", 5), ("b", -2), ("c", 8), ("d", -1)]
nw= {k:v for k,v in pairs2 if v>0}
print(nw)
# 2. invert an existing dict (swap keys and values)
grades = {"Ram": "A", "Sita": "B", "Mike": "A"}
ng= { val:key for key,val in grades.items()}
print(ng)

capitol ={"India" : "Delhi", "Nepal" : "ktm", "china" : "beijing"}
nc= {val:key for key,val in capitol.items()}
print(nc)
# 3. build a dict mapping each name to True/False for whether its length is > 4
names = ["Al", "Alexander", "Bob", "Christina"]
nn= {name: len(name)>4 for name in names}
print(nn)

# 4. build a dict from a list of dicts, keyed by "name", valued by "age"
people = [{"name": "Ram", "age": 25}, {"name": "Sita", "age": 20}, {"name": "Mike", "age": 30}]
np = {d["name"] : d["age"] for d in people}
print(np)
# 5. build a dict mapping each word to its uppercase version, only for words longer than 3 letters
words2 = ["hi", "sun", "kiwi", "banana", "ox"]
wd= {w: w.upper() for w in words2 if len(w)>3}
print(wd)

# 6. build a dict mapping each number to "even"/"odd"
nums3 = [1, 2, 3, 4, 5]
nd= {n: "Even" if n%2==0 else "Odd" for n in nums3}
print(nd)

# 7. build a dict mapping each word to its first letter
words3 = ["apple", "banana", "cherry"]
p= {w:w[0] for w in words3}
print(p)

# 8. build a dict from a list of numbers, mapping each number to whether it's prime
nums4 = [2, 3, 4, 5, 6, 7, 8, 9, 10]


# 9. build a dict from a list of tuples (name, score), keeping only scores >= 60
results = [("Ram", 90), ("Sita", 55), ("Mike", 85), ("Priya", 40)]
rd= {key:value for key,value in results if value>=60}
print(rd)

# 10. build a dict from a list of tuples (product, price), doubling every price
stock = [("shoes", 120), ("bag", 45), ("watch", 200)]
dt = {key :value*2 for key,value in stock}
#dt= {key:value for key,value in stock if value==2*value} #incorrect
print(dt)

# 11. build a dict from a list of tuples, but swap each pair (value becomes key)
codes = [("NP", "Nepal"), ("US", "USA"), ("JP", "Japan")]
cd= {val:key for key,val in codes}
print(cd)
# 12. build a dict from a list of tuples (word, count), keeping only words that appear more than once
tally = [("cat", 1), ("dog", 3), ("bird", 1), ("fish", 5)]
result= {word: count for word, count in tally if count>1}
print(result)

# 13. build a dict from a list of strings, mapping each string to its reversed version
words4 = ["abc", "hello", "python"]
w4= { w: w[::-1] for w in words4}
print(w4)

# 14. build a dict from a list of tuples (student, [scores]), mapping student to their average score
records = [("Ram", [80, 90, 70]), ("Sita", [60, 75, 65]), ("Mike", [95, 85, 100])]
rd= {name:sum(scores)/len(scores) for name, scores in records}
print(rd)

# 15. build a dict from a list of numbers, mapping each number to a list containing its square and cube
nums5 = [1, 2, 3, 4]
nu= {num:(num*num, num*num*num) for num in nums5}
print(nu)

# --- dict-to-dict comprehension problems ---

# 16. build a dict from an existing dict, doubling every value
scores = {"Ram": 10, "Sita": 20, "Mike": 30}
sc= { key:value *2 for key, value in scores.items()}
print(sc)
# 17. build a dict from an existing dict, keeping only items where the value is >= 20
scores2 = {"Ram": 10, "Sita": 20, "Mike": 30, "Priya": 5}
#s2= {key:value >=20 for key,value in scores2.items()} for True and False
s2= {key:value for key,value in scores2.items() if value>=20}
print(s2)

# 18. build a dict from an existing dict, uppercasing every key
inventory = {"tv": 5, "laptop": 2, "phone": 4}
inv= {key.upper():value for key,value in inventory.items()}
print(inv)


# 19. build a dict from an existing dict, converting every value to a string prefixed with "$"
prices = {"shoes": 120, "bag": 45, "watch": 200}
pc= {key: f"$ {str(value)}" for key,value in prices.items()}
print(pc)

# 20. build a dict from an existing dict, keeping only keys that are longer than 3 letters
data = {"a": 1, "bb": 2, "ccc": 3, "dddd": 4, "eeeee": 5}
da= {key:value for key,value in data.items() if len(key)>3}
print(da)

# 21. build a dict from an existing dict, replacing each value with "pass"/"fail" based on score >= 50
scores3 = {"Ram": 90, "Sita": 40, "Mike": 65, "Priya": 30}
s3= {key:"Pass"if value >=50 else "Fail" for key,value in scores3.items()}
print(s3)

# 22. build a dict from an existing dict, mapping each key to the length of its value (value is a string)
capitals = {"Nepal": "Kathmandu", "USA": "DC", "Japan": "Tokyo"}
cp= {key:len(val) for key, val in capitals.items()}
print(cp)

# 23. build a dict from an existing dict, keeping only entries where key and value are different types of "long"
#     (key length > 3 AND value > 10)
mixed = {"a": 20, "bb": 5, "ccc": 15, "dddd": 8}


# 24. merge two dicts into one using a single dict comprehension (values from dict2 win on conflicts)
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}

# 25. build a dict from an existing dict, rounding every float value to 1 decimal place
temps = {"Mon": 23.456, "Tue": 19.234, "Wed": 25.789}
