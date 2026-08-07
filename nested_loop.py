names= ["ran", "run", "dan", "tan"]
domains= ["gmail.com", "yahoo,com", "outlook.com", "apple.com"]

emails= [ f" {name} @ {domain}" for name in names for domain in domains]
print(emails)

# --- nested loop comprehension practice ---

# 1. build all (row, col) coordinate pairs for a 3x3 grid
rows = [0, 1, 2]
cols = [0, 1, 2]
grid= [(row,col) for row in rows for col in cols]
print(grid)

# 2. flatten a list of lists into a single list using a nested loop comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat=[]

# 3. build all combinations of size and color for a product listing
sizes = ["S", "M", "L"]
colors = ["red", "blue"]

# 4. build a multiplication table as a list of "a x b = c" strings, for a and b from 1 to 3
nums_range = range(1, 4)

# 5. from a matrix, flatten it but keep only even numbers
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 6. build all unique pairs (i, j) from a list where i comes before j (no repeats, no reverse duplicates)
items = ["a", "b", "c", "d"]

# 7. build a list of every character paired with every digit 0-3
letters = ["x", "y"]
digits = range(4)

# 8. flatten a matrix and square every number in one nested comprehension
matrix3 = [[1, 2], [3, 4], [5, 6]]

# 9. build a list of (word, letter) pairs for every letter in every word
words = ["hi", "cat"]

# 10. build a list of all pairs (a, b) from two lists where a + b is even
list_a = [1, 2, 3]
list_b = [4, 5, 6]

sentences= [
    " Matter of time only",
    "DSA and leet will be easy",
    "keep grinding everyday"
]
result= [word for sentence in sentences for word in sentence.split()]
print(result)