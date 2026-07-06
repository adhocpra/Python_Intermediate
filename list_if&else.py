#ternary: A if condition else B

# List comprehension with if/else (ternary) — every input keeps a spot in the output,
# just transformed differently depending on the condition.
# Pattern: [expr_if_true if condition else expr_if_false for item in iterable]
# (different from plain "if" filtering, which drops items instead of transforming them)

# 1. label each number as "even" or "odd"
numbers = [1, 2, 3, 4, 5, 6]
check_odd_even=["even" if num%2==0  else "odd"  for num in numbers] 
print(check_odd_even)

# 2. label each number as "positive", "negative", or "zero" (chained ternary)
nums = [-3, 0, 5, -8, 2, 0]
check= ["positive" if n>0 else "negative" if n<0 else "zero" for n in nums] 
print(check)

# 3. replace each vowel-starting word with "VOWEL", else keep the word unchanged
words = ["apple", "banana", "orange", "kiwi", "egg"]
vowel=["VOWEL" if w.startswith(("a","e","i","o", "u")) else w for w in words]
print(vowel)

# 4. mark pass/fail for each score (pass if >= 50)
scores = [45, 60, 78, 30, 90, 50]
test= ["pass" if s>=50 else "fail" for s in scores] 
print(test)

# 5. square even numbers, cube odd numbers
nums2 = [1, 2, 3, 4, 5, 6]
no=[n*n if n%2==0 else n**3  for n in nums2]
print(no)

# 6. replace negative numbers with 0, keep positive numbers as-is (clipping)
values = [-5, 3, -2, 8, -1, 0]
v= [w if w>0 else 0 for w in values]
print(v)
# 7. uppercase names longer than 4 letters, lowercase the rest
names = ["Al", "Alexander", "Bob", "Christina", "Sam"]
u= [w.upper() if len(w)>4 else w.lower() for w in names]
print(u)

# 8. label temperature as "hot" (>30), "cold" (<10), or "mild" otherwise
temps = [5, 32, 20, 8, 35, 15]
te= ["hot" if t>30 else "cold" if t<10 else "mild" for t in temps]
print(te)

# 9. convert each number to "FizzBuzz" (div by 15), "Fizz" (div by 3), "Buzz" (div by 5), or itself
nums3 = list(range(1, 16))
A= ["fizzBuzz" if num%15==0 else "fizz" if num%3==0 else "buzz" if num%5==0 else num for num in nums3]
print(A)
# 10. add "$" prefix to prices above 100, "¢" prefix to prices 100 or below
prices = [50, 150, 99, 200, 100]
pr=[f"${p}" if p>100 else f"c{p}" for p in prices]
print(pr)

# 11. mark each word as "short", "medium", or "long" based on length (<=3, <=6, else long)
words2 = ["hi", "hello", "extraordinary", "sun", "beautiful"]
w2=["short" if len(w)<=3 else "medium" if len(w)<=6 else "long" for w in words2]
print(w2)

# 12. replace None values with 0, keep other numbers as-is
data = [5, None, 8, None, 3, 12]
dt= [0 if d is None else d for d in data]
print(dt)

# 13. tag each year as "leap" or "common" (leap if divisible by 4)
years = [2000, 2001, 2004, 2023, 2024]
yr= ["leap" if y%4==0 else "common" for y in years]
print(yr)

# 14. convert grades (numbers) into letter grades: A (>=90), B (>=80), C (>=70), else F
grades = [95, 82, 74, 60, 88]
gd= ["A" if g>=90 else "B" if g>=80 else "C" if g>=70 else "Fail" for g in grades]
print(gd)

# 15. for each string, return its length if it's alphabetic, else return -1
tokens = ["hello", "123abc", "world", "42", "python"]
tk= [len(t) if t.isalpha() else -1 for t in tokens]
print(tk)