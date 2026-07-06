# List comprehension practice problems
#The most classic method
nums =[1,2,3,4,5]
squares= []
for num in nums:
    squares.append(num*num)
print(squares)

# 1. Create a list of squares for the numbers in `numbers`.
numbers = [1, 2, 3, 4, 5]
squares= [num*num for num in numbers]
print(squares)

# 2. Create a list of uppercase strings from `names`.
names = ["alice", "bob", "charlie", "diana"]
upper= [name.upper() for name in names]
print(upper)

# 3. Create a list of only odd numbers from `numbers`.
numbers = [10, 15, 20, 25, 30, 35]
result= [num for num in numbers if num % 2 !=0]
print(result)


# 4. Create a list of lengths for each word in `words`.
words = ["apple", "banana", "kiwi", "avocado"]
a= [len(word) for word in words]
print(a)

# 5. Create a list of names that start with the letter "a" or "A".
names = ["Alice", "bob", "Anil", "alex", "arthur"]
b= [n for n in names if n.lower().startswith("a")]
print(b)

# 6. Create a list of booleans showing whether each number is positive.
numbers = [-5, 0, 3, -1, 10]
c=[n for n in numbers if n>0] #filters positivr
print(c)

c= [n>0 for n in numbers]
print(c)

# 7. From `items`, create a list that contains only alphabetic strings.
items = ["hello", "123", "python", "42", "world"]
d= [i for i in items if str.isalpha(i)]
print(d)

# 8. Create a list of paired tuples using values from two lists.
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
pt= [(l,s) for l,s in zip(list1,list2)]
print(pt)
# 9. Create a list of strings that have a length greater than 4.
words = ["hi", "hello", "world", "pie", "python"]
e=[w for w in words if len(w)>4]
print(e)

# 10. Given `text_numbers`, create a list of integers.
text_numbers = ["5", "10", "15", "20"]
f= [int(t) for t in text_numbers]
print(f)

# 11. Create a list of numbers from 1 to 20 using range().
ls1= [num for num in range(1,21)]
print(ls1)
# 12. Create a list of even numbers from 1 to 30 using range() with a step.
ls2= [num for num in range (1,30) if num %2 ==0]
print(ls2)
# 13. Create a list of squares for every number from 1 to 10 using range().
# ls3=[num for num in numbers if math.sqr(num) in range (1,10)]
# ptint(ls3)
ls3= [num*num for num in range(1,11)]
print(ls3)
# 14. Create a list of multiples of 3 between 1 and 50 using range().
ls4=[num for num in range (1,51) if num %3==0]
print(ls4)
ls4= [num for num in range (3,51,3)]
# 15. Create a list of numbers from 10 down to 1 using range() with a negative step.
ls5=[num for num in range(10,0,-1)]
print(ls5)
# 16. Create a list of tuples (n, n*n) for n from 1 to 5 using range().
ls6= [(n,n*n) for n in range(1,6)]
print(ls6)
# 17. Create a list marking each number 1-15 as "fizz" if divisible by 3, "buzz" if divisible by 5, else the number itself.
# 18. Create a list of the first 10 powers of 2 (2**0, 2**1, ... 2**9) using range().
# 19. Given a list of numbers, create a list of only the prime numbers.
#     numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# 20. Create a flattened list from a list of lists.
#     matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
