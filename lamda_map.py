# map() + lambda practice

# 1. square every number in the list
nums = [1, 2, 3, 4, 5]
result= list(map(lambda x: x*x,nums))
print(result)

# 2. double every number in the list
nums2 = [10, 20, 30]
result1= list(map(lambda x: x*2,nums2))
print(result1)

# 3. uppercase every name in the list
names = ["ram", "sita", "mike"]
result2= list(map(lambda name: name.upper(),names))
print(result2)

# 4. get the length of every word in the list
words = ["banana", "apple", "kiwi", "cherry"]
result3= list(map(lambda w: len(w),words))
print(result3)

# 5. convert every price (int) into a formatted string like "$120"
prices = [120, 45, 200, 30]
result4= list(map(lambda p:f"${p}",prices))
print(result4)
# 6. add corresponding elements of two lists together (map with two iterables)
a = [1, 2, 3]
b = [10, 20, 30]
result5= list(map(lambda a,b: a+b,a,b))
print(result5)

# 7. extract just the values from a dict using map on .items()
scores = {"Ram": 90, "Sita": 75, "Mike": 85}
result6= list(map(lambda item: item[1], scores.items()))
print(result6)

# 7a. double every value in a dict using map on .values()
scores2 = {"Ram": 90, "Sita": 75, "Mike": 85}
result2= list(map(lambda s: 2*s,scores2.values() ))
print(result2)

# 7b. uppercase every key in a dict using map on .keys()
scores3 = {"ram": 90, "sita": 75, "mike": 85}
result3= list(map(lambda s3:s3.upper(), scores3.keys()))
print(result3)

# 7c. map over .items() and just print each (key, value) pair unchanged (no formatting yet)
scores4 = {"Ram": 90, "Sita": 75, "Mike": 85}
result4= list(map(lambda s4: s4, scores4.items()))
print(result4)


# 7c-i. map over .items() with a single param lambda, index into the pair to get just the key
scores4b = {"Ram": 90, "Sita": 75, "Mike": 85}


# 7c-ii. map over .items() with a single param lambda, index into the pair to get just the value
scores4c = {"Ram": 90, "Sita": 75, "Mike": 85}


# 7c-iii. map over .items() with a single param lambda, combine item[0] and item[1] into "key-value"
scores4d = {"Ram": 90, "Sita": 75, "Mike": 85}


# 7d. use itertools.starmap instead of map — it unpacks each tuple into separate lambda params
# so you can write lambda key, value: ... directly (no indexing needed)
# return just the key doubled in length, e.g. "RamRam"
from itertools import starmap
scores5 = {"Ram": 90, "Sita": 75, "Mike": 85}


# 8. build "key: value" strings from a dict using map on .items()
prices_dict = {"shoes": 120, "bag": 45, "watch": 200}

#filter with lambda

numbers= [1,2,3,4,5]

result= list(filter(lambda x:x%2==0, numbers))
print(result)

# 2. keep only words longer than 4 letters
words = ["cat", "elephant", "dog", "giraffe", "ox"]
result= list(filter(lambda w:len(w)>4, words))
print(result)

# 3. keep only negative numbers
nums = [-5, 3, -1, 8, -9, 2]
result= list(filter(lambda num: num<0, nums))
print(result)

# 4. filter a dict: keep only students who passed (score >= 60)
# hint: filter over scores.items(), lambda takes the (key, value) pair like exercise 7c did
scores = {"Ram": 90, "Sita": 55, "Mike": 85, "Priya": 40}
result= list(filter(lambda s:s[1]>60, scores.items()))
print(result)

# 5. filter a dict: keep only keys where the key name has more than 3 letters
inventory = {"tv": 5, "laptop": 2, "ox": 9, "phone": 4}
result= list(filter(lambda i:len(i[0])>3,inventory.items()))
print(result)

# --- keys() / values() / items() drills ---
# for each one, decide which of .keys(), .values(), .items() you actually need

# d1. uppercase every key
d1 = {"ram": 1, "sita": 2, "mike": 3}
result= list(map(lambda d:d.upper(),d1.keys()))
print(result)

# d2. square every value
d2 = {"a": 2, "b": 3, "c": 4}
result= list(map(lambda d:d*d, d2.values()))
print(result)

# d3. keep only pairs where the value is odd
d3 = {"a": 1, "b": 2, "c": 3, "d": 4}
result= list(filter(lambda d: d[1]%2 !=0, d3.items()))
print(result)
# d4. keep only keys that contain the letter "a"
d4 = {"ram": 1, "sita": 2, "bob": 3, "priya": 4}
result= list(filter(lambda d: "a" in d, d4.keys()))
print(result)

result2= list(filter(lambda d: "a" in d[0], d4.items()))
print(result2)
# d5. keep only values greater than 50
d5 = {"a": 30, "b": 70, "c": 90, "d": 20}
result= list(filter(lambda d: d>50, d5.values()))
print(result)

# d6. build a list of "key=value" strings
d6 = {"x": 1, "y": 2, "z": 3}
result= list(map(lambda d:f"{d[0]}={d[1]}", d6.items() ))
print(result)


# d7. sort the keys alphabetically, descending
d7 = {"banana": 1, "apple": 2, "cherry": 3}
new= sorted(d7,key=lambda d:d, reverse=True )
print(new)
# d8. sort the values, ascending
d8 = {"a": 30, "b": 10, "c": 20}
new= sorted(d8.values())
print(new)

# d9. sort by value and return a list of (key, value) tuples
d9 = {"Ram": 90, "Sita": 75, "Mike": 85}
new= sorted(d9.items(), key=lambda d:d[1])
print(new)

# d10. get the length of every key
d10 = {"tv": 1, "laptop": 2, "phone": 3}
new= list(map(lambda d: len(d), d10.keys()))
print(new)
# d11. convert every value to a string
d11 = {"a": 1, "b": 2, "c": 3}
new=list(map(lambda d: str(d), d11.values()))
print(new)

# d12. keep only pairs where the key's length equals the value
d12 = {"a": 1, "bb": 2, "ccc": 5, "dddd": 4}
new= list(filter(lambda k:len(k[0])==k[1], d12.items()))
print(new)

# d13. double every value, then filter to keep only the ones still under 100
d13 = {"a": 40, "b": 60, "c": 10, "d": 55}
new= list(filter(lambda k:2*k<100, d13.values()))
print(new)
new = list(filter(lambda v: v < 100, map(lambda v: v*2, d13.values())))
print(new)

# d14. find the single key with the shortest name (use min with key=lambda on .keys())
d14 = {"television": 1, "tv": 2, "phone": 3}

# d15. sort keys by how many vowels are in them
d15 = {"sky": 1, "apple": 2, "eel": 3, "gym": 4}