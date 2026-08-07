fruits= ["apple" , "banana", "cherry", "dragonfruit"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# --- enumerate() practice ---

# 1. build a list of "index: name" strings
names = ["Ram", "Sita", "Mike"]

for index,name in enumerate(names):
    print(index,name)

# 2. build a dict mapping each word to its position (index) in the list
#{key_exp:value_exp for item in iter}
words = ["cat", "dog", "bird"]
result ={ index: word for index, word in enumerate(words)}
print(result)
# 3. start counting from 1 instead of 0 (enumerate takes a start argument)
tasks = ["wake up", "brush teeth", "eat breakfast"]
for index, task in enumerate(tasks,1):
    print(index, task)

# 4. print only items at even indexes, using enumerate() with a condition
letters = ["a", "b", "c", "d", "e", "f"]
let= [letter for index, letter in enumerate(letters) if index%2==0 ]
print(let)
# 5. build a list of tuples (index, value) but only for values greater than 10
nums = [5, 15, 3, 22, 8, 30]
result= [(index,num)for index, num in enumerate(nums) if num>10]
print(result)

# 6. replace every 3rd item (index divisible by 3) in a list with "X"
items = [10, 20, 30, 40, 50, 60, 70]
result= ["X" if index %3==0 else item for index, item in enumerate(items)]
print(result)

# 7. find the index of the first word longer than 5 letters
#words2 = ["hi", "sun", "python", "ox", "banana"]


# 8. build a dict mapping index -> value, but only for odd indexes
values = ["a", "b", "c", "d", "e", "f"]
result= {index:value for index,value in enumerate(values) if index%2 !=0}
print(result)
# 9. use enumerate() inside a nested loop to print (row_index, col_index, value) for a matrix
matrix = [[1, 2], [3, 4], [5, 6]]

# 10. number each line of a multi-line string starting from 1 (split into lines first)
text = "first line\nsecond line\nthird line"