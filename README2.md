# MASTER REFERENCE SHEET

## CORE PYTHON SYNTAX REFERENCE

### Variables \& Data Types - Complete Guide

```python
# ========== BASIC TYPES ==========
# Integer
age = 28
count = 0
negative = -5

# Float
price = 3.14
temperature = 98.6
scientific = 1.5e10  # Scientific notation

# String
name = "Allan"
message = 'Hello'
multiline = """This is
a multiline string"""

# Boolean
is_active = True
has_permission = False

# ========== TYPE CONVERSION (CASTING) ==========
# To integer
age_string = "28"
age_int = int(age_string)  # 28
float_to_int = int(3.14)   # 3 (truncates)

# To float
price_string = "3.14"
price_float = float(price_string)  # 3.14
int_to_float = float(5)            # 5.0

# To string
num = 42
num_string = str(num)  # "42"
formatted = f"The answer is {num}"  # f-string

# To boolean
bool(1)      # True
bool(0)      # False
bool("")     # False
bool("text") # True

# ========== TYPE CHECKING ==========
type(28)              # <class 'int'>
type(3.14)            # <class 'float'>
type("hello")         # <class 'str'>

isinstance(28, int)   # True
isinstance(28, (int, float))  # True - check multiple types

# ========== NONE TYPE ==========
result = None  # Represents absence of value
if result is None:
    print("No value assigned")

# ========== MULTIPLE ASSIGNMENT ==========
x = y = z = 0  # All equal to 0
a, b, c = 1, 2, 3  # Tuple unpacking

# ========== SWAP VARIABLES ==========
a, b = b, a  # Pythonic swap (no temp variable needed)

# ========== NAMING CONVENTIONS ==========
# Variables: snake_case
user_name = "Allan"
total_count = 100

# Constants: UPPER_SNAKE_CASE
MAX_SIZE = 1000
API_KEY = "abc123"

# Classes: PascalCase
class UserProfile:
    pass

# Functions: snake_case
def calculate_total():
    pass
```


### Input \& Output - Complete Patterns

```python
# ========== BASIC INPUT ==========
name = input("Enter your name: ")
age = input("Enter your age: ")  # Returns string

# ========== INPUT WITH CONVERSION ==========
age = int(input("Enter age: "))
price = float(input("Enter price: "))

# ========== INPUT WITH VALIDATION ==========
while True:
    try:
        age = int(input("Enter age: "))
        if 0 <= age <= 150:
            break
        print("Age must be between 0 and 150")
    except ValueError:
        print("Please enter a valid number")

# ========== BASIC OUTPUT ==========
print("Hello, World!")
print("Hello", "World")  # Space added automatically

# ========== F-STRING FORMATTING ==========
name = "Allan"
age = 28
print(f"My name is {name} and I am {age}")

# Expressions in f-strings
print(f"5 + 3 = {5 + 3}")
print(f"Uppercase: {name.upper()}")

# Number formatting
price = 19.99
print(f"Price: ${price:.2f}")  # 2 decimal places
print(f"Price: ${price:>10.2f}")  # Right-aligned, width 10

# ========== STRING CONCATENATION ==========
first = "John"
last = "Doe"
full_name = first + " " + last  # "John Doe"

# ========== MULTIPLE PRINT ARGUMENTS ==========
print("Name:", name, "Age:", age)
print("Total:", 100, sep=" | ")  # Custom separator
print("Line 1", end="")  # No newline
print(" Line 2")  # Continues on same line

# ========== FORMATTED STRING LITERALS ==========
width = 10
height = 5
print(f"Area: {width * height}")
print(f"Dimensions: {width}x{height}")

# ========== PRINT TO FILE ==========
with open("output.txt", "w") as f:
    print("Hello, File!", file=f)
```


### Control Flow - Exhaustive Examples

```python
# ========== BASIC IF-ELIF-ELSE ==========
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

# ========== COMPARISON OPERATORS ==========
x = 10
y = 20

x == y  # Equal to
x != y  # Not equal to
x < y   # Less than
x > y   # Greater than
x <= y  # Less than or equal
x >= y  # Greater than or equal

# ========== LOGICAL OPERATORS ==========
age = 25
has_license = True

# AND - both must be True
if age >= 18 and has_license:
    print("Can drive")

# OR - at least one must be True
if age < 13 or age > 65:
    print("Special pricing")

# NOT - inverts boolean
if not has_license:
    print("Cannot drive")

# ========== CHAINED COMPARISONS ==========
age = 25
if 18 <= age < 65:
    print("Working age")

score = 85
if 80 <= score <= 89:
    print("B grade")

# ========== TRUTHY/FALSY VALUES ==========
# Falsy: 0, 0.0, "", [], {}, (), None, False
# Truthy: Everything else

grocery_list = []
if grocery_list:
    print("Time to shop")
else:
    print("Nothing to buy")  # This executes

# ========== CONDITIONAL EXPRESSIONS (TERNARY) ==========
age = 20
status = "adult" if age >= 18 else "minor"

max_value = a if a > b else b  # Get larger value

# ========== MEMBERSHIP OPERATORS ==========
fruits = ["apple", "banana", "orange"]

if "apple" in fruits:
    print("We have apples")

if "grape" not in fruits:
    print("No grapes available")

# ========== IDENTITY OPERATORS ==========
x = [1, 2, 3]
y = [1, 2, 3]
z = x

x is z      # True - same object
x is y      # False - different objects
x == y      # True - same values

# ========== NESTED CONDITIONS ==========
age = 25
has_ticket = True
is_weekend = True

if age >= 18:
    if has_ticket:
        if is_weekend:
            print("Can enter club - weekend special")
        else:
            print("Can enter club")
    else:
        print("Need ticket")
else:
    print("Too young")

# Better: compound conditions
if age >= 18 and has_ticket and is_weekend:
    print("Can enter club - weekend special")
```


### Loops - Complete Patterns

```python
# ========== WHILE LOOPS ==========

# Basic while loop
count = 1
while count <= 5:
    print(count)
    count += 1

# Countdown
number = 10
while number >= 1:
    print(number)
    number -= 1
print("Blast Off!")

# While with condition check
running = True
counter = 0
while running:
    counter += 1
    if counter >= 10:
        running = False

# Infinite loop with break
while True:
    answer = input("Continue? (y/n): ")
    if answer.lower() == 'n':
        break
    print("Still processing...")

# While-else (executes if loop completes normally)
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed normally")

# ========== FOR LOOPS ==========

# Loop with range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (step of 2)
    print(i)

for i in range(10, 0, -1):  # Countdown: 10, 9, ..., 1
    print(i)

# Loop through list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Loop through string
for char in "Python":
    print(char)

# Loop through dictionary
student = {"name": "Allan", "age": 28, "major": "CS"}

# Keys only (default)
for key in student:
    print(key)

# Values only
for value in student.values():
    print(value)

# Key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

# ========== ENUMERATE ==========
# Get index and value
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Start counting from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# ========== ZIP ==========
# Iterate multiple lists together
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")

# ========== BREAK STATEMENT ==========
# Exit loop immediately
for i in range(10):
    if i == 5:
        break  # Exits loop when i is 5
    print(i)  # Prints 0, 1, 2, 3, 4

# ========== CONTINUE STATEMENT ==========
# Skip to next iteration
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Only prints odd numbers

# ========== PASS STATEMENT ==========
# Placeholder (does nothing)
for i in range(5):
    pass  # TODO: implement later

# ========== NESTED LOOPS ==========
# Multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()  # Blank line after each row

# ========== LOOP WITH ELSE ==========
# Else executes if loop completes without break
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")

# ========== LIST COMPREHENSION (INLINE FOR LOOP) ==========
# Create list in one line
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
doubled = [x * 2 for x in [1, 2, 3, 4, 5]]
```



## COMPLETE LISTS GUIDE - ALL METHODS \& PATTERNS

### List Creation \& Access

```python
# ========== CREATION METHODS ==========
# Empty list
empty = []
empty_with_constructor = list()

# List with initial values
numbers = [1, 2, 3, 4, 5]
mixed = ["text", 42, True, 3.14, None]
nested = [[1, 2], [3, 4], [5, 6]]

# List from range
nums = list(range(10))  # [0, 1, 2, ..., 9]
evens = list(range(0, 20, 2))  # [0, 2, 4, ..., 18]

# List from string
chars = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# ========== ACCESSING ELEMENTS ==========
fruits = ["apple", "banana", "orange", "grape", "mango"]

# Positive indexing (0-based)
first = fruits[0]      # "apple"
second = fruits[1]     # "banana"

# Negative indexing (from end)
last = fruits[-1]      # "mango"
second_last = fruits[-2]  # "grape"

# ========== SLICING ==========
# Syntax: list[start:stop:step]

fruits = ["apple", "banana", "orange", "grape", "mango"]

fruits[1:3]      # ["banana", "orange"] - items 1 and 2
fruits[:3]       # ["apple", "banana", "orange"] - first 3
fruits[2:]       # ["orange", "grape", "mango"] - from index 2 to end
fruits[:]        # Copy entire list
fruits[-3:]      # Last 3 elements
fruits[::2]      # Every 2nd element
fruits[::-1]     # Reverse list
fruits[1:4:2]    # ["banana", "grape"] - from 1 to 4, step 2

# ========== LENGTH ==========
len(fruits)  # 5

# ========== CHECKING EXISTENCE ==========
if "apple" in fruits:
    print("We have apples")  # O(n) time complexity

if "pear" not in fruits:
    print("No pears")
```


### List Modification Methods - Complete Reference

```python
# ========== APPEND - Add to End (O(1)) ==========
fruits = ["apple", "banana"]
fruits.append("orange")
# ["apple", "banana", "orange"]

# ========== INSERT - Add at Position (O(n)) ==========
fruits.insert(0, "grape")  # Insert at beginning
# ["grape", "apple", "banana", "orange"]

fruits.insert(2, "mango")  # Insert at index 2
# ["grape", "apple", "mango", "banana", "orange"]

# ========== EXTEND - Add Multiple Items (O(k)) ==========
fruits = ["apple", "banana"]
fruits.extend(["orange", "grape"])
# ["apple", "banana", "orange", "grape"]

# Alternative: concatenation
fruits = fruits + ["mango", "pear"]

# ========== REMOVE - Remove by Value (O(n)) ==========
fruits = ["apple", "banana", "orange", "banana"]
fruits.remove("banana")  # Removes first occurrence
# ["apple", "orange", "banana"]

# Raises ValueError if not found
try:
    fruits.remove("pear")
except ValueError:
    print("Pear not in list")

# ========== POP - Remove by Index (O(1) at end, O(n) elsewhere) ==========
fruits = ["apple", "banana", "orange"]

last = fruits.pop()  # Remove and return last item
# last = "orange"
# fruits = ["apple", "banana"]

first = fruits.pop(0)  # Remove and return first item
# first = "apple"
# fruits = ["banana"]

# ========== DEL - Delete by Index or Slice (O(n)) ==========
fruits = ["apple", "banana", "orange", "grape"]
del fruits[1]  # Delete "banana"
# ["apple", "orange", "grape"]

del fruits[1:3]  # Delete slice
# ["apple"]

# ========== CLEAR - Remove All Items (O(1)) ==========
fruits = ["apple", "banana", "orange"]
fruits.clear()
# []

# ========== SORT - In-Place Sorting (O(n log n)) ==========
numbers = [5, 2, 8, 1, 9]
numbers.sort()  # Ascending
# [1, 2, 5, 8, 9]

numbers.sort(reverse=True)  # Descending
# [9, 8, 5, 2, 1]

# Sort strings
fruits = ["banana", "apple", "orange"]
fruits.sort()  # Alphabetical
# ["apple", "banana", "orange"]

# Sort with key function
words = ["Python", "java", "C++", "javascript"]
words.sort(key=str.lower)  # Case-insensitive sort
# ["C++", "java", "javascript", "Python"]

# Sort complex objects
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
students.sort(key=lambda s: s["grade"], reverse=True)
# Sorted by grade, highest first

# ========== SORTED - Return New Sorted List (O(n log n)) ==========
numbers = [5, 2, 8, 1, 9]
sorted_nums = sorted(numbers)  # Original unchanged
# sorted_nums = [1, 2, 5, 8, 9]
# numbers still [5, 2, 8, 1, 9]

# ========== REVERSE - Reverse In-Place (O(n)) ==========
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
# [5, 4, 3, 2, 1]

# ========== REVERSED - Return Reverse Iterator ==========
numbers = [1, 2, 3, 4, 5]
reversed_nums = list(reversed(numbers))
# [5, 4, 3, 2, 1]

# ========== INDEX - Find First Occurrence (O(n)) ==========
fruits = ["apple", "banana", "orange", "banana"]
idx = fruits.index("banana")  # 1

# Raises ValueError if not found
try:
    idx = fruits.index("grape")
except ValueError:
    print("Not found")

# Search in slice
idx = fruits.index("banana", 2)  # Search from index 2

# ========== COUNT - Count Occurrences (O(n)) ==========
numbers = [1, 2, 3, 2, 4, 2, 5]
count = numbers.count(2)  # 3

fruits = ["apple", "banana", "apple"]
apple_count = fruits.count("apple")  # 2

# ========== COPY - Shallow Copy (O(n)) ==========
original = [1, 2, 3]
copy1 = original.copy()
copy2 = original[:]  # Alternative
copy3 = list(original)  # Alternative

# Deep copy for nested lists
import copy
nested = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(nested)
```


### Advanced List Patterns

```python
# ========== LIST COMPREHENSION - ADVANCED ==========

# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# With if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]

# Nested comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
# [1, 2, 3, 4, 5, 6]

# Multiple conditions
filtered = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
# [0, 10, 20, 30, ...]

# ========== UNPACKING ==========
first, second, third = [1, 2, 3]

# With * operator (rest)
first, *rest = [1, 2, 3, 4, 5]
# first = 1, rest = [2, 3, 4, 5]

*beginning, last = [1, 2, 3, 4, 5]
# beginning = [1, 2, 3, 4], last = 5

first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5

# ========== COMBINING LISTS ==========
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]

# Extend
list1.extend(list2)

# Unpacking
combined = [*list1, *list2]

# ========== FILTERING LISTS ==========
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension
evens = [x for x in numbers if x % 2 == 0]

# Filter function
evens = list(filter(lambda x: x % 2 == 0, numbers))

# ========== MAPPING LISTS ==========
numbers = [1, 2, 3, 4, 5]

# List comprehension
doubled = [x * 2 for x in numbers]

# Map function
doubled = list(map(lambda x: x * 2, numbers))

# ========== REDUCING LISTS ==========
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, numbers)  # 15

# ========== LIST AS STACK ==========
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
top = stack.pop()  # Pop - returns 3

# ========== LIST AS QUEUE (NOT RECOMMENDED) ==========
# Use collections.deque instead!
from collections import deque
queue = deque()
queue.append(1)  # Enqueue - O(1)
queue.append(2)
first = queue.popleft()  # Dequeue - O(1)

# ========== REMOVE DUPLICATES ==========
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]

# Using set (loses order)
unique = list(set(numbers))

# Preserve order
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

# Using dict (Python 3.7+)
unique = list(dict.fromkeys(numbers))

# ========== FINDING MIN/MAX ==========
numbers = [5, 2, 8, 1, 9]
minimum = min(numbers)  # 1
maximum = max(numbers)  # 9

# With key function
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92}
]
top_student = max(students, key=lambda s: s["grade"])

# ========== SUM, AVERAGE ==========
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)  # 15
average = sum(numbers) / len(numbers)  # 3.0

# ========== ALL/ANY ==========
numbers = [2, 4, 6, 8]
all_even = all(x % 2 == 0 for x in numbers)  # True

numbers = [1, 2, 3, 4]
has_even = any(x % 2 == 0 for x in numbers)  # True

# ========== ENUMERATE WITH INDEX ==========
fruits = ["apple", "banana", "orange"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# ========== ZIP MULTIPLE LISTS ==========
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")

# Create list of tuples
combined = list(zip(names, ages, cities))
# [("Alice", 25, "NYC"), ("Bob", 30, "LA"), ...]

# Unzip
names, ages, cities = zip(*combined)
```


***

## COMPLETE DICTIONARIES GUIDE - HASH TABLES MASTERY

### Dictionary Creation \& Access

```python
# ========== CREATION METHODS ==========

# Empty dictionary
empty = {}
empty_with_constructor = dict()

# Dictionary with initial values
student = {
    "name": "Allan",
    "age": 28,
    "major": "Computer Science",
    "gpa": 3.8
}

# Using dict() constructor
student = dict(name="Allan", age=28, major="CS")

# From list of tuples
pairs = [("name", "Allan"), ("age", 28)]
student = dict(pairs)

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ========== ACCESSING VALUES - O(1) ==========
student = {"name": "Allan", "age": 28}

# Direct access (raises KeyError if not found)
name = student["name"]  # "Allan"

# Safe access with get() - returns None or default
age = student.get("age")  # 28
grade = student.get("grade")  # None
grade = student.get("grade", "N/A")  # "N/A" as default

# ========== CHECKING KEYS - O(1) ==========
if "name" in student:
    print(f"Name: {student['name']}")

if "grade" not in student:
    print("Grade not recorded")

# ========== GETTING ALL KEYS/VALUES ==========
keys = student.keys()  # dict_keys(['name', 'age'])
values = student.values()  # dict_values(['Allan', 28])
items = student.items()  # dict_items([('name', 'Allan'), ('age', 28)])

# Convert to list
keys_list = list(student.keys())
values_list = list(student.values())
```


### Dictionary Modification Methods

```python
# ========== ADDING/UPDATING - O(1) ==========
student = {"name": "Allan", "age": 28}

# Add new key-value
student["major"] = "CS"
# {"name": "Allan", "age": 28, "major": "CS"}

# Update existing
student["age"] = 29
# {"name": "Allan", "age": 29, "major": "CS"}

# ========== UPDATE - Merge Dictionaries ==========
student = {"name": "Allan", "age": 28}
updates = {"age": 29, "gpa": 3.8, "major": "CS"}

student.update(updates)
# {"name": "Allan", "age": 29, "gpa": 3.8, "major": "CS"}

# ========== SETDEFAULT - Add if Not Exists ==========
student = {"name": "Allan"}

# Returns value if exists, sets and returns if not
age = student.setdefault("age", 28)
# student now has "age": 28

# If key exists, returns existing value
name = student.setdefault("name", "Bob")
# name is "Allan", not "Bob"

# ========== POP - Remove and Return Value - O(1) ==========
student = {"name": "Allan", "age": 28, "major": "CS"}

# Remove and return value
age = student.pop("age")  # Returns 28
# student = {"name": "Allan", "major": "CS"}

# With default if key doesn't exist
gpa = student.pop("gpa", 0.0)  # Returns 0.0

# ========== POPITEM - Remove Last Inserted ==========
student = {"name": "Allan", "age": 28, "major": "CS"}
item = student.popitem()  # Returns ("major", "CS")

# ========== DEL - Delete Key ==========
student = {"name": "Allan", "age": 28}
del student["age"]
# {"name": "Allan"}

# Raises KeyError if not found
try:
    del student["gpa"]
except KeyError:
    print("Key not found")

# ========== CLEAR - Remove All Items ==========
student = {"name": "Allan", "age": 28}
student.clear()
# {}

# ========== COPY - Shallow Copy ==========
original = {"name": "Allan", "age": 28}
copy1 = original.copy()
copy2 = dict(original)  # Alternative

# Deep copy for nested dicts
import copy
nested = {"person": {"name": "Allan", "age": 28}}
deep_copy = copy.deepcopy(nested)
```


### Iteration Patterns

```python
student = {
    "name": "Allan",
    "age": 28,
    "major": "CS",
    "gpa": 3.8
}

# ========== ITERATE KEYS (DEFAULT) ==========
for key in student:
    print(key)
    # name
    # age
    # major
    # gpa

# ========== ITERATE VALUES ==========
for value in student.values():
    print(value)
    # Allan
    # 28
    # CS
    # 3.8

# ========== ITERATE KEY-VALUE PAIRS ==========
for key, value in student.items():
    print(f"{key}: {value}")
    # name: Allan
    # age: 28
    # major: CS
    # gpa: 3.8

# ========== ITERATE WITH ENUMERATION ==========
for i, (key, value) in enumerate(student.items(), start=1):
    print(f"{i}. {key}: {value}")
```


### Advanced Dictionary Patterns

```python
# ========== NESTED DICTIONARIES ==========
contacts = {
    "Alice": {
        "phone": "555-1234",
        "email": "alice@email.com",
        "address": {
            "street": "123 Main St",
            "city": "Boston",
            "zip": "02101"
        }
    },
    "Bob": {
        "phone": "555-5678",
        "email": "bob@email.com"
    }
}

# Access nested values
alice_phone = contacts["Alice"]["phone"]
alice_city = contacts["Alice"]["address"]["city"]

# Safe access with get()
zip_code = contacts.get("Alice

---

# Now continue with the next topic

Perfect! Continuing with the complete guide...

***

## COMPLETE DICTIONARIES GUIDE - CONTINUED

### Advanced Dictionary Patterns (Continued)

```python
# ========== NESTED DICTIONARIES (CONTINUED) ==========
contacts = {
    "Alice": {
        "phone": "555-1234",
        "email": "alice@email.com",
        "address": {
            "street": "123 Main St",
            "city": "Boston",
            "zip": "02101"
        }
    },
    "Bob": {
        "phone": "555-5678",
        "email": "bob@email.com"
    }
}

# Safe access with get() for nested dicts
alice_zip = contacts.get("Alice", {}).get("address", {}).get("zip", "N/A")

# ========== DICTIONARY COMPREHENSION ==========
# Basic
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# From two lists
keys = ["name", "age", "city"]
values = ["Allan", 28, "Boston"]
person = {k: v for k, v in zip(keys, values)}
# {"name": "Allan", "age": 28, "city": "Boston"}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}

# From list of dicts
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92}
]
grade_lookup = {s["name"]: s["grade"] for s in students}
# {"Alice": 85, "Bob": 92}

# ========== MERGING DICTIONARIES ==========
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Method 1: update()
merged = dict1.copy()
merged.update(dict2)
# {"a": 1, "b": 2, "c": 3, "d": 4}

# Method 2: unpacking (Python 3.5+)
merged = {**dict1, **dict2}

# Method 3: union operator (Python 3.9+)
merged = dict1 | dict2

# If keys overlap, later dict wins
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}
# {"a": 1, "b": 3, "c": 4}

# ========== DEFAULTDICT - Auto-Initialize ==========
from collections import defaultdict

# Regular dict - KeyError if key doesn't exist
counts = {}
# counts["apple"] += 1  # KeyError!

# defaultdict with int (defaults to 0)
counts = defaultdict(int)
counts["apple"] += 1  # Works! Initializes to 0 first
counts["banana"] += 1
# defaultdict(<class 'int'>, {'apple': 1, 'banana': 1})

# defaultdict with list (defaults to [])
groups = defaultdict(list)
groups["fruits"].append("apple")
groups["fruits"].append("banana")
groups["vegetables"].append("carrot")
# {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']}

# ========== COUNTER - Count Occurrences ==========
from collections import Counter

# Count items in list
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = Counter(fruits)
# Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Most common
most_common = counts.most_common(2)  # Top 2
# [('apple', 3), ('banana', 2)]

# Count characters
text = "mississippi"
char_counts = Counter(text)
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Arithmetic with Counters
c1 = Counter(["a", "b", "c"])
c2 = Counter(["a", "b", "d"])
c1 + c2  # Add counts
c1 - c2  # Subtract counts
c1 & c2  # Intersection (min)
c1 | c2  # Union (max)

# ========== ORDEREDDICT - Preserve Order ==========
# Note: Regular dicts preserve order in Python 3.7+
from collections import OrderedDict

ordered = OrderedDict()
ordered["first"] = 1
ordered["second"] = 2
ordered["third"] = 3

# Move to end
ordered.move_to_end("first")  # Moves "first" to end

# Move to beginning
ordered.move_to_end("third", last=False)

# ========== FILTERING DICTIONARIES ==========
student = {"name": "Allan", "age": 28, "gpa": 3.8, "major": "CS"}

# Keep only certain keys
keys_to_keep = ["name", "age"]
filtered = {k: student[k] for k in keys_to_keep}
# {"name": "Allan", "age": 28}

# Filter by condition
high_values = {k: v for k, v in student.items() if isinstance(v, (int, float)) and v > 10}

# ========== INVERTING DICTIONARIES ==========
original = {"Alice": 85, "Bob": 92, "Charlie": 85}

# Simple inversion (loses duplicates)
inverted = {v: k for k, v in original.items()}
# {85: "Charlie", 92: "Bob"}  # Alice lost!

# Invert with multiple values
from collections import defaultdict
inverted = defaultdict(list)
for name, grade in original.items():
    inverted[grade].append(name)
# {85: ["Alice", "Charlie"], 92: ["Bob"]}

# ========== GROUPING WITH DICTIONARIES ==========
students = [
    {"name": "Alice", "grade": "A", "age": 20},
    {"name": "Bob", "grade": "B", "age": 22},
    {"name": "Charlie", "grade": "A", "age": 21},
    {"name": "David", "grade": "B", "age": 20}
]

# Group by grade
from collections import defaultdict
by_grade = defaultdict(list)
for student in students:
    by_grade[student["grade"]].append(student["name"])
# {"A": ["Alice", "Charlie"], "B": ["Bob", "David"]}

# ========== DICTIONARY OPERATIONS ==========
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 4, "d": 5}

# Keys in both
common_keys = dict1.keys() & dict2.keys()
# {"b", "c"}

# Keys in dict1 but not dict2
unique_to_dict1 = dict1.keys() - dict2.keys()
# {"a"}

# Key-value pairs in both
common_items = dict1.items() & dict2.items()
# {("b", 2)}

# ========== PRACTICAL PATTERNS ==========

# Count word frequency
text = "the quick brown fox jumps over the lazy dog"
word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1
# {"the": 2, "quick": 1, "brown": 1, ...}

# Better with Counter
from collections import Counter
word_counts = Counter(text.split())

# Build lookup table
students = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]
lookup = {s["id"]: s for s in students}
# {1: {"id": 1, "name": "Alice"}, 2: {...}}

# Cache/memoization
cache = {}
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]

# Configuration management
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "admin"
    },
    "api": {
        "timeout": 30,
        "retries": 3
    }
}

# API response parsing
response_json = {
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    }
}
users = response_json["data"]["users"]
```


***

## COMPLETE FUNCTIONS GUIDE - MASTERY LEVEL

### Function Basics - All Patterns

```python
# ========== BASIC FUNCTION DEFINITION ==========
def greet():
    """Simple function with no parameters"""
    print("Hello, World!")

greet()  # Call the function

# ========== FUNCTION WITH PARAMETERS ==========
def greet(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

greet("Allan")  # "Hello, Allan!"

# Multiple parameters
def add(a, b):
    """Function with multiple parameters"""
    return a + b

result = add(5, 3)  # 8

# ========== RETURN VALUES ==========
def square(x):
    """Function that returns a value"""
    return x ** 2

result = square(5)  # 25

# Multiple return values (returns tuple)
def divide_with_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

q, r = divide_with_remainder(10, 3)  # q=3, r=1

# Early return
def is_even(n):
    if n % 2 == 0:
        return True
    return False

# No return = returns None
def print_message(msg):
    print(msg)
    # Implicitly returns None

# ========== DEFAULT PARAMETERS ==========
def greet(name, greeting="Hello"):
    """Default parameter value"""
    print(f"{greeting}, {name}!")

greet("Allan")              # "Hello, Allan!"
greet("Allan", "Hi")        # "Hi, Allan!"
greet("Allan", greeting="Hey")  # "Hey, Allan!"

# Multiple defaults
def create_user(username, email, role="user", active=True):
    return {
        "username": username,
        "email": email,
        "role": role,
        "active": active
    }

user = create_user("allan", "allan@email.com")
admin = create_user("admin", "admin@email.com", role="admin")

# ========== KEYWORD ARGUMENTS ==========
def introduce(name, age, city):
    print(f"{name}, {age}, from {city}")

# Positional arguments
introduce("Allan", 28, "Boston")

# Keyword arguments (order doesn't matter)
introduce(age=28, city="Boston", name="Allan")

# Mix positional and keyword (positional must come first)
introduce("Allan", age=28, city="Boston")

# ========== *ARGS - Variable Positional Arguments ==========
def sum_all(*args):
    """Accept any number of arguments"""
    return sum(args)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# args is a tuple
def print_args(*args):
    print(type(args))  # <class 'tuple'>
    for arg in args:
        print(arg)

# ========== **KWARGS - Variable Keyword Arguments ==========
def print_info(**kwargs):
    """Accept any number of keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Allan", age=28, city="Boston")
# name: Allan
# age: 28
# city: Boston

# kwargs is a dictionary
def create_profile(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    return kwargs

profile = create_profile(name="Allan", age=28)

# ========== COMBINING ARGS AND KWARGS ==========
def flexible_function(required, *args, default="value", **kwargs):
    """
    required: required positional argument
    *args: additional positional arguments
    default: optional parameter with default
    **kwargs: additional keyword arguments
    """
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

flexible_function("must_have", 1, 2, 3, default="custom", key1="val1", key2="val2")

# ========== UNPACKING ARGUMENTS ==========
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # Unpacks list into arguments

def greet(name, age):
    print(f"{name} is {age}")

person = {"name": "Allan", "age": 28}
greet(**person)  # Unpacks dict into keyword arguments

# ========== LAMBDA FUNCTIONS ==========
# Simple lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple parameters
add = lambda a, b: a + b
print(add(3, 4))  # 7

# Lambda with conditional
is_even = lambda x: "even" if x % 2 == 0 else "odd"
print(is_even(4))  # "even"

# Lambda in sorting
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)

# ========== DOCSTRINGS - DOCUMENTATION ==========
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    
    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)

# ========== TYPE HINTS (Python 3.5+) ==========
def add(a: int, b: int) -> int:
    """Add two integers and return the result"""
    return a + b

def greet(name: str, age: int) -> None:
    """Greet a person (returns nothing)"""
    print(f"Hello, {name}! You are {age}")

from typing import List, Dict, Optional, Union

def process_names(names: List[str]) -> Dict[str, int]:
    """Process list of names and return length dictionary"""
    return {name: len(name) for name in names}

def find_user(user_id: int) -> Optional[Dict[str, str]]:
    """Find user by ID, returns None if not found"""
    # Implementation
    return None

# ========== NESTED FUNCTIONS ==========
def outer(x):
    """Function inside a function"""
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
result = add_5(3)  # 8

# ========== CLOSURES ==========
def make_multiplier(n):
    """Returns a function that multiplies by n"""
    def multiplier(x):
        return x * n
    return multiplier

times_3 = make_multiplier(3)
print(times_3(10))  # 30

times_5 = make_multiplier(5)
print(times_5(10))  # 50

# ========== DECORATORS - BASIC ==========
def uppercase_decorator(func):
    """Decorator that converts result to uppercase"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"hello, {name}"

print(greet("allan"))  # "HELLO, ALLAN"

# ========== RECURSION ==========
def factorial(n):
    """Calculate factorial recursively"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

def fibonacci(n):
    """Calculate Fibonacci number recursively"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# ========== PRACTICAL FUNCTION PATTERNS ==========

# Function that modifies lists
def remove_duplicates(items):
    """Remove duplicates while preserving order"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Function with validation
def create_user(username, email):
    """Create user with validation"""
    if not username or len(username) < 3:
        raise ValueError("Username must be at least 3 characters")
    if "@" not in email:
        raise ValueError("Invalid email address")
    return {"username": username, "email": email}

# Function that returns multiple types
def divide(a, b):
    """Divide two numbers, returns result or error message"""
    if b == 0:
        return None, "Cannot divide by zero"
    return a / b, None

result, error = divide(10, 2)
if error:
    print(error)
else:
    print(result)

# Generator function
def count_up_to(n):
    """Generate numbers from 1 to n"""
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)  # 1, 2, 3, 4, 5

# Function with callback
def process_items(items, callback):
    """Process each item with callback function"""
    results = []
    for item in items:
        results.append(callback(item))
    return results

numbers = [1, 2, 3, 4, 5]
doubled = process_items(numbers, lambda x: x * 2)
```


***

## COMPLETE STRING METHODS GUIDE

### String Creation \& Basic Operations

```python
# ========== STRING CREATION ==========
# Single quotes
name = 'Allan'

# Double quotes
message = "Hello, World!"

# Triple quotes (multiline)
paragraph = """This is
a multiline
string"""

# Raw strings (ignore escape characters)
path = r"C:\Users\name\folder"

# F-strings (formatted string literals)
name = "Allan"
age = 28
intro = f"My name is {name} and I am {age}"

# ========== STRING CONCATENATION ==========
first = "Hello"
last = "World"

# Using +
combined = first + " " + last  # "Hello World"

# Using join (more efficient for multiple strings)
words = ["Hello", "World", "!"]
sentence = " ".join(words)  # "Hello World !"

# ========== STRING REPETITION ==========
repeated = "Ha" * 3  # "HaHaHa"
line = "-" * 50  # 50 dashes

# ========== STRING INDEXING ==========
text = "Python"
first = text[0]    # "P"
last = text[-1]    # "n"
second = text[1]   # "y"

# ========== STRING SLICING ==========
text = "Python Programming"
text[0:6]      # "Python"
text[:6]       # "Python" (from start)
text[7:]       # "Programming" (to end)
text[::2]      # "Pto rgamn" (every 2nd char)
text[::-1]     # Reverse string
```


### String Methods - Complete Reference

```python
# ========== CASE CONVERSION ==========
text = "Hello World"

text.upper()       # "HELLO WORLD"
text.lower()       # "hello world"
text.title()       # "Hello World"
text.capitalize()  # "Hello world" (only first letter)
text.swapcase()    # "hELLO wORLD" (swap case)

# Case checking
"hello".islower()  # True
"HELLO".isupper()  # True
"Hello".istitle()  # True

# ========== WHITESPACE METHODS ==========
text = "  Hello World  "

text.strip()       # "Hello World" (both ends)
text.lstrip()      # "Hello World  " (left side)
text.rstrip()      # "  Hello World" (right side)

# Strip specific characters
"###Hello###".strip("#")  # "Hello"
"...data...".strip(".")   # "data"

# ========== SEARCHING METHODS ==========
text = "Python is awesome. Python is powerful."

# Find substring
text.find("Python")     # 0 (first occurrence)
text.find("Python", 10) # 19 (search from index 10)
text.find("Java")       # -1 (not found)

# Index (like find but raises ValueError if not found)
text.index("Python")    # 0
# text.index("Java")    # ValueError!

# Count occurrences
text.count("Python")    # 2
text.count("is")        # 2

# Check start/end
text.startswith("Python")     # True
text.endswith("powerful.")    # True
text.startswith("Java")       # False

# ========== SPLITTING & JOINING ==========
text = "apple,banana,orange"

# Split into list
fruits = text.split(",")  # ["apple", "banana", "orange"]

# Split by whitespace (default)
sentence = "Hello World Python"
words = sentence.split()  # ["Hello", "World", "Python"]

# Split with maxsplit
text = "a,b,c,d,e"
parts = text.split(",", 2)  # ["a", "b", "c,d,e"]

# Splitlines (split by newlines)
text = "Line 1\nLine 2\nLine 3"
lines = text.splitlines()  # ["Line 1", "Line 2", "Line 3"]

# Join list into string
words = ["Hello", "World"]
joined = " ".join(words)  # "Hello World"
joined = "-".join(words)  # "Hello-World"

# ========== REPLACE METHOD ==========
text = "I love cats. Cats are great."

# Replace all occurrences
new_text = text.replace("cats", "dogs")
# "I love dogs. Cats are great."

new_text = text.replace("cats", "dogs", 1)  # Replace first only
# "I love dogs. Cats are great."

# Case-sensitive
text.replace("Cats", "Dogs")  # Only replaces "Cats"

# ========== CHECKING METHODS ==========
"12345".isdigit()       # True - all digits
"abc".isalpha()         # True - all letters
"abc123".isalnum()      # True - letters or numbers
"   ".isspace()         # True - all whitespace
"Python".isidentifier() # True - valid variable name

# ========== ALIGNMENT & PADDING ==========
text = "Python"

# Center (width 20)
text.center(20)      # "       Python       "
text.center(20, "*") # "*******Python*******"

# Left align
text.ljust(20)       # "Python              "
text.ljust(20, "-")  # "Python--------------"

# Right align
text.rjust(20)       # "              Python"
text.rjust(20, "-")  # "--------------Python"

# Zero-fill (for numbers)
"42".zfill(5)        # "00042"

# ========== FORMATTING ==========
# Old-style % formatting
name = "Allan"
age = 28
text = "My name is %s and I am %d" % (name, age)

# str.format()
text = "My name is {} and I am {}".format(name, age)
text = "My name is {0} and I am {1}".format(name, age)
text = "My name is {name} and I am {age}".format(name=name, age=age)

# F-strings (modern, best)
text = f"My name is {name} and I am {age}"
text = f"5 + 3 = {5 + 3}"
text = f"Uppercase: {name.upper()}"

# Number formatting
price = 19.99
f"Price: ${price:.2f}"        # "Price: $19.99" (2 decimals)
f"Price: ${price:>10.2f}"     # Right-aligned, width 10
f"Price: ${price:0>10.2f}"    # Zero-padded

# ========== ENCODING/DECODING ==========
text = "Python"

# Encode to bytes
encoded = text.encode("utf-8")  # b'Python'
encoded = text.encode("ascii")

# Decode from bytes
decoded = encoded.decode("utf-8")  # "Python"

# ========== PARTITION & SPLIT ==========
email = "user@example.com"

# Partition (split into 3 parts)
username, at, domain = email.partition("@")
# username="user", at="@", domain="example.com"

# Reverse partition
path = "/home/user/documents/file.txt"
head, sep, tail = path.rpartition("/")
# head="/home/user/documents", sep="/", tail="file.txt"

# ========== TRANSLATE & MAKETRANS ==========
# Replace multiple characters at once
text = "hello world"
translation_table = str.maketrans("helo", "w3l0")
translated = text.translate(translation_table)
# "w3ll0 w0rld"

# Remove characters
translation_table = str.maketrans("", "", "aeiou")
no_vowels = "hello world".translate(translation_table)
# "hll wrld"

# ========== PRACTICAL STRING PATTERNS ==========

# Email validation (basic)
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[1]

# Extract file extension
filename = "document.pdf"
name, extension = filename.rsplit(".", 1)
# name="document", extension="pdf"

# Clean user input
user_input = "  HELLO WORLD  "
cleaned = user_input.strip().lower()  # "hello world"

# Create slug from title
title = "My Awesome Blog Post!"
slug = title.lower().replace(" ", "-").replace("!", "")
# "my-awesome-blog-post"

# Parse CSV line
csv_line = "John,Doe,28,Boston"
fields = csv_line.split(",")

# Format currency
amount = 1234.56
formatted = f"${amount:,.2f}"  # "$1,234.56"

# Truncate long text
def truncate(text, length=50):
    if len(text) <= length:
        return text
    return text[:length-3] + "..."

# Check palindrome
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

is_palindrome("A man a plan a canal Panama")  # True

# Count words
def word_count(text):
    return len(text.split())

# Title case with exceptions
def smart_title(text):
    exceptions = ["a", "an", "the", "and", "or", "but"]
    words = text.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or word.lower() not in exceptions:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    return " ".join(result)

smart_title("the lord of the rings")
# "The Lord of the Rings"
```



## COMPLETE SETS \& TUPLES GUIDE

### Sets - Unique, Unordered Collections

```python
# ========== SET CREATION ==========
# Using curly braces
numbers = {1, 2, 3, 4, 5}

# Using set() constructor
empty_set = set()  # Note: {} creates empty dict!
from_list = set([1, 2, 3, 2, 1])  # {1, 2, 3} - duplicates removed
from_string = set("hello")  # {'h', 'e', 'l', 'o'}

# Set with different types (must be hashable)
mixed = {1, "hello", 3.14, True}

# Cannot have mutable types
# invalid = {[1, 2], {3, 4}}  # TypeError!
# But can have tuples (immutable)
valid = {(1, 2), (3, 4)}

# ========== SET OPERATIONS - ALL O(1) ==========
fruits = {"apple", "banana", "orange"}

# Add element - O(1)
fruits.add("grape")
# {"apple", "banana", "orange", "grape"}

# Add multiple elements - O(k) where k is number of elements
fruits.update(["mango", "pear"])
# Can also use: fruits.update("strawberry")  # Adds each char!

# Remove element - O(1), raises KeyError if not found
fruits.remove("banana")
# {"apple", "orange", "grape", "mango", "pear"}

# Discard element - O(1), no error if not found
fruits.discard("watermelon")  # No error
fruits.discard("apple")  # Removes "apple"

# Pop random element - O(1)
random_fruit = fruits.pop()  # Returns and removes a random element

# Clear all elements - O(1)
fruits.clear()  # set()

# ========== MEMBERSHIP TESTING - O(1) ==========
fruits = {"apple", "banana", "orange"}

if "apple" in fruits:
    print("We have apples!")  # Very fast!

if "grape" not in fruits:
    print("No grapes")

# ========== SET LENGTH ==========
len(fruits)  # 3

# ========== SET MATHEMATICS ==========
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union - all elements from both sets
union = set1.union(set2)
# {1, 2, 3, 4, 5, 6, 7, 8}
union = set1 | set2  # Alternative syntax

# Intersection - elements in both sets
intersection = set1.intersection(set2)
# {4, 5}
intersection = set1 & set2  # Alternative syntax

# Difference - elements in set1 but not in set2
difference = set1.difference(set2)
# {1, 2, 3}
difference = set1 - set2  # Alternative syntax

# Symmetric difference - elements in either set but not both
sym_diff = set1.symmetric_difference(set2)
# {1, 2, 3, 6, 7, 8}
sym_diff = set1 ^ set2  # Alternative syntax

# ========== SET COMPARISONS ==========
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3}

# Subset - all elements of set1 are in set2
set1.issubset(set2)  # True
set1 <= set2  # Alternative syntax

# Proper subset - subset but not equal
set1 < set2  # True

# Superset - set2 contains all elements of set1
set2.issuperset(set1)  # True
set2 >= set1  # Alternative syntax

# Proper superset
set2 > set1  # True

# Disjoint - no common elements
set1.isdisjoint({7, 8, 9})  # True
set1.isdisjoint(set2)  # False (they share elements)

# Equality
set1 == set3  # True
set1 == set2  # False

# ========== IN-PLACE SET OPERATIONS ==========
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Update (union in-place)
set1.update(set2)
# set1 = {1, 2, 3, 4, 5, 6, 7, 8}

set1 = {1, 2, 3, 4, 5}
set1 |= set2  # Alternative

# Intersection update
set1 = {1, 2, 3, 4, 5}
set1.intersection_update(set2)
# set1 = {4, 5}

set1 = {1, 2, 3, 4, 5}
set1 &= set2  # Alternative

# Difference update
set1 = {1, 2, 3, 4, 5}
set1.difference_update(set2)
# set1 = {1, 2, 3}

set1 = {1, 2, 3, 4, 5}
set1 -= set2  # Alternative

# Symmetric difference update
set1 = {1, 2, 3, 4, 5}
set1.symmetric_difference_update(set2)
# set1 = {1, 2, 3, 6, 7, 8}

set1 = {1, 2, 3, 4, 5}
set1 ^= set2  # Alternative

# ========== PRACTICAL SET PATTERNS ==========

# Remove duplicates from list
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(numbers))  # [1, 2, 3, 4, 5] (order not preserved)

# Find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))  # [4, 5]

# Find unique to each list
unique_to_list1 = list(set(list1) - set(list2))  # [1, 2, 3]
unique_to_list2 = list(set(list2) - set(list1))  # [6, 7, 8]

# Find all unique elements
all_unique = list(set(list1) | set(list2))  # [1, 2, 3, 4, 5, 6, 7, 8]

# Check if lists have common elements
has_common = bool(set(list1) & set(list2))

# Real-world: Friend recommendations
alice_friends = {"Bob", "Charlie", "David"}
bob_friends = {"Alice", "Charlie", "Eve", "Frank"}

# Friends in common
mutual = alice_friends & bob_friends  # {"Charlie"}

# People Alice might know (Bob's friends she doesn't know)
suggestions = bob_friends - alice_friends - {"Bob"}  # {"Eve", "Frank"}

# Real-world: Tag system
post1_tags = {"python", "programming", "tutorial"}
post2_tags = {"python", "web", "flask"}

# Find posts with specific tag
all_posts_with_python = post1_tags & post2_tags  # {"python"}

# Unique tags across posts
all_tags = post1_tags | post2_tags

# ========== FROZENSET - IMMUTABLE SET ==========
# Can be used as dict key or in another set
immutable = frozenset([1, 2, 3])
immutable = frozenset({1, 2, 3})

# All read operations work
immutable.union({4, 5})  # Returns new frozenset
# immutable.add(4)  # AttributeError - cannot modify!

# Use as dict key
lookup = {
    frozenset([1, 2]): "pair1",
    frozenset([3, 4]): "pair2"
}

# Set of sets (must use frozenset)
set_of_sets = {
    frozenset([1, 2]),
    frozenset([3, 4])
}

# ========== SET COMPREHENSION ==========
# Basic
squares = {x**2 for x in range(10)}
# {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# With condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
# {0, 4, 16, 36, 64}

# From string (unique chars)
unique_chars = {char.lower() for char in "Hello World!"}
# {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd', '!'}

# Extract unique values from list of dicts
users = [
    {"name": "Alice", "city": "NYC"},
    {"name": "Bob", "city": "LA"},
    {"name": "Charlie", "city": "NYC"}
]
cities = {user["city"] for user in users}  # {"NYC", "LA"}

# ========== ITERATING SETS ==========
fruits = {"apple", "banana", "orange"}

# Basic iteration (order not guaranteed)
for fruit in fruits:
    print(fruit)

# With enumerate (order still not guaranteed)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Sorted iteration
for fruit in sorted(fruits):
    print(fruit)  # Alphabetical order

# ========== SET PERFORMANCE BENEFITS ==========
# Fast membership testing
# List: O(n)
big_list = list(range(1000000))
999999 in big_list  # Slow - checks each element

# Set: O(1)
big_set = set(range(1000000))
999999 in big_set  # Fast - hash lookup

# Finding duplicates efficiently
def has_duplicates(items):
    return len(items) != len(set(items))

has_duplicates([1, 2, 3, 4])  # False
has_duplicates([1, 2, 2, 3])  # True

# Count unique elements
items = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_count = len(set(items))  # 4
```


***

## TUPLES - IMMUTABLE SEQUENCES

### Tuple Basics \& Operations

```python
# ========== TUPLE CREATION ==========
# Using parentheses
coordinates = (3, 4)
rgb = (255, 128, 0)

# Tuple packing (parentheses optional)
point = 10, 20
person = "Allan", 28, "Boston"

# Single element tuple (comma required!)
singleton = (42,)  # Tuple with one element
not_tuple = (42)   # This is just an integer!

# Empty tuple
empty = ()
empty = tuple()

# Tuple from list
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # (1, 2, 3)

# Tuple from string
chars = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')

# ========== ACCESSING TUPLE ELEMENTS ==========
point = (10, 20, 30)

# Indexing
x = point[^11_0]   # 10
y = point[^11_1]   # 20
z = point[-1]  # 30 (last element)

# Slicing
numbers = (0, 1, 2, 3, 4, 5)
numbers[1:4]   # (1, 2, 3)
numbers[:3]    # (0, 1, 2)
numbers[3:]    # (3, 4, 5)
numbers[::2]   # (0, 2, 4)
numbers[::-1]  # (5, 4, 3, 2, 1, 0) - reverse

# ========== TUPLE UNPACKING ==========
# Basic unpacking
point = (10, 20)
x, y = point  # x=10, y=20

# Multiple values
person = ("Allan", 28, "Boston")
name, age, city = person

# Unpacking in function returns
def get_user():
    return "Allan", 28, "Boston"

name, age, city = get_user()

# Unpacking with * (rest operator)
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers
# first=1, rest=[2, 3, 4, 5]

*beginning, last = numbers
# beginning=[1, 2, 3, 4], last=5

first, *middle, last = numbers
# first=1, middle=[2, 3, 4], last=5

# Swap variables using tuple unpacking
a, b = 5, 10
a, b = b, a  # a=10, b=5

# ========== TUPLE IMMUTABILITY ==========
point = (10, 20)
# point[^11_0] = 15  # TypeError: tuples are immutable!

# But tuple with mutable objects can be modified
data = ([1, 2], [3, 4])
data[^11_0].append(3)  # This works!
# data = ([1, 2, 3], [3, 4])

# Cannot add or remove elements
# data.append((5, 6))  # AttributeError

# ========== TUPLE METHODS (ONLY 2!) ==========
numbers = (1, 2, 3, 2, 4, 2, 5)

# Count occurrences
count = numbers.count(2)  # 3

# Find index of first occurrence
index = numbers.index(3)  # 2

# Index with start and end
index = numbers.index(2, 2)  # Find 2 starting from index 2
# Returns 3

# ========== TUPLE OPERATIONS ==========
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = (1, 2) * 3  # (1, 2, 1, 2, 1, 2)

# Length
len(tuple1)  # 3

# Membership
2 in tuple1  # True
7 in tuple1  # False

# Min, Max, Sum (for numeric tuples)
numbers = (5, 2, 8, 1, 9)
min(numbers)  # 1
max(numbers)  # 9
sum(numbers)  # 25

# ========== ITERATING TUPLES ==========
colors = ("red", "green", "blue")

# Basic iteration
for color in colors:
    print(color)

# With enumerate
for i, color in enumerate(colors):
    print(f"{i}: {color}")

# ========== NAMED TUPLES ==========
from collections import namedtuple

# Define a named tuple type
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances
p = Point(10, 20)
person = Person("Allan", 28, "Boston")

# Access by name (more readable!)
print(p.x)        # 10
print(person.name)  # "Allan"

# Still works as regular tuple
print(p[^11_0])       # 10
x, y = p          # Unpacking works

# Immutable (like regular tuples)
# person.age = 29  # AttributeError!

# Convert to dict
person_dict = person._asdict()
# {'name': 'Allan', 'age': 28, 'city': 'Boston'}

# Replace values (returns new tuple)
older_person = person._replace(age=29)

# ========== PRACTICAL TUPLE PATTERNS ==========

# Function returning multiple values
def calculate_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

minimum, maximum, average = calculate_stats([1, 2, 3, 4, 5])

# Dictionary with tuple keys
# Useful for coordinates, pairs, etc.
grid = {
    (0, 0): "origin",
    (1, 0): "right",
    (0, 1): "up",
    (1, 1): "diagonal"
}
print(grid[(1, 1)])  # "diagonal"

# Tuple as dict key for caching
cache = {}
def expensive_operation(a, b, c):
    key = (a, b, c)  # Tuple key
    if key in cache:
        return cache[key]
    result = a + b * c  # Some expensive calculation
    cache[key] = result
    return result

# Immutable configuration
CONFIG = (
    ("HOST", "localhost"),
    ("PORT", 5432),
    ("DEBUG", True)
)

# RGB colors as tuples
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Return multiple values from database query
def get_user(user_id):
    # Simulated database result
    return (user_id, "Allan", "allan@email.com", True)

user_id, name, email, is_active = get_user(1)

# ========== ZIP - WORKING WITH MULTIPLE LISTS ==========
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

# Zip creates tuples
zipped = list(zip(names, ages, cities))
# [("Alice", 25, "NYC"), ("Bob", 30, "LA"), ("Charlie", 35, "Chicago")]

# Iterate together
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")

# Unzip (use * operator)
names, ages, cities = zip(*zipped)
# names = ("Alice", "Bob", "Charlie")
# ages = (25, 30, 35)
# cities = ("NYC", "LA", "Chicago")

# Zip with different lengths (stops at shortest)
list1 = [1, 2, 3, 4]
list2 = ['a', 'b']
list(zip(list1, list2))  # [(1, 'a'), (2, 'b')]

# Use zip_longest for all elements
from itertools import zip_longest
list(zip_longest(list1, list2, fillvalue='?'))
# [(1, 'a'), (2, 'b'), (3, '?'), (4, '?')]

# Create dictionary from two lists
keys = ["name", "age", "city"]
values = ["Allan", 28, "Boston"]
person = dict(zip(keys, values))
# {"name": "Allan", "age": 28, "city": "Boston"}

# ========== TUPLES VS LISTS - WHEN TO USE ==========

# Use TUPLES when:
# 1. Data should not change
coordinates = (10, 20)
rgb_color = (255, 128, 0)

# 2. Used as dictionary keys
locations = {
    (0, 0): "home",
    (10, 5): "work"
}

# 3. Returning multiple values from function
def get_min_max(numbers):
    return min(numbers), max(numbers)

# 4. Performance (tuples are slightly faster)
# 5. Data integrity (immutability prevents accidental changes)

# Use LISTS when:
# 1. Data needs to change
shopping_list = ["milk", "eggs"]
shopping_list.append("bread")

# 2. Need methods like append, remove, sort
numbers = [3, 1, 4, 1, 5]
numbers.sort()

# 3. Don't need to use as dict key

# ========== TUPLE PACKING & UNPACKING IN PRACTICE ==========

# Swapping values
a, b = 1, 2
a, b = b, a

# Multiple assignment
x, y, z = 1, 2, 3

# Function arguments
def process(data):
    name, age, city = data  # Unpack tuple
    print(f"{name}, {age}, {city}")

process(("Allan", 28, "Boston"))

# Enumerate returns tuples
for i, value in enumerate(['a', 'b', 'c']):
    print(f"{i}: {value}")

# Dictionary items returns tuples
person = {"name": "Allan", "age": 28}
for key, value in person.items():
    print(f"{key}: {value}")

# ========== MEMORY EFFICIENCY ==========
import sys

# Tuples use less memory than lists
tuple_data = (1, 2, 3, 4, 5)
list_data = [1, 2, 3, 4, 5]

print(sys.getsizeof(tuple_data))  # Smaller
print(sys.getsizeof(list_data))   # Larger

# ========== TUPLE COMPARISON ==========
# Compares element by element
(1, 2, 3) < (1, 2, 4)    # True
(1, 2, 3) == (1, 2, 3)   # True
('a', 'b') < ('b', 'a')  # True

# Useful for sorting
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 85)
]
students.sort()  # Sorts by name (first element)
# [('Alice', 85), ('Bob', 92), ('Charlie', 85)]

# Sort by grade (second element)
students.sort(key=lambda x: x[^11_1], reverse=True)
# [('Bob', 92), ('Alice', 85), ('Charlie', 85)]
```


## COMPLETE OBJECT-ORIENTED PROGRAMMING GUIDE


### OOP Fundamentals - Classes \& Objects

```python
# ========== BASIC CLASS DEFINITION ==========
class Student:
    """A class representing a student"""
    
    def __init__(self, name, age, grades):
        """
        Constructor - runs when object is created
        self refers to the instance being created
        """
        self.name = name      # Instance attribute
        self.age = age
        self.grades = grades
    
    def info(self):
        """Instance method - must have self as first parameter"""
        print(f"My name is {self.name} and I am {self.age}")
    
    def grade_avg(self):
        """Calculate average grade"""
        return sum(self.grades) / len(self.grades)
    
    def add_grade(self, grade):
        """Add a new grade"""
        self.grades.append(grade)
    
    def remove_last_grade(self):
        """Remove the most recent grade"""
        if self.grades:
            self.grades.pop()
    
    def clear_grades(self):
        """Remove all grades"""
        self.grades.clear()

# ========== CREATING OBJECTS (INSTANCES) ==========
# Call the class like a function
student1 = Student("Allan", 20, [85, 90, 92])
student2 = Student("Maya", 22, [95, 88, 91])

# Access attributes
print(student1.name)  # "Allan"
print(student1.age)   # 20

# Call methods
student1.info()       # "My name is Allan and I am 20"
avg = student1.grade_avg()  # 89.0

# Modify attributes
student1.age = 21
student1.add_grade(87)

# ========== CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES ==========
class Car:
    # Class attribute - shared by ALL instances
    wheels = 4
    manufacturer = "Generic Motors"
    
    def __init__(self, make, model, year, fuel=100):
        # Instance attributes - unique to each object
        self.make = make
        self.model = model
        self.year = year
        self.fuel = fuel
    
    def start_engine(self):
        print(f"{self.make} {self.model} engine started!")
    
    def drive(self, miles):
        """Drive the car, consuming fuel"""
        fuel_used = miles * 0.05
        if self.fuel >= fuel_used:
            self.fuel -= fuel_used
            print(f"Drove {miles} miles. Fuel: {self.fuel:.2f}%")
        else:
            print("Not enough fuel!")
    
    def refuel(self):
        """Fill up the tank"""
        self.fuel = 100
        print("Tank refilled!")

# Create cars
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)

# Class attribute accessed via class or instance
print(Car.wheels)    # 4
print(car1.wheels)   # 4
print(car2.wheels)   # 4

# Modifying class attribute affects all instances
Car.wheels = 6
print(car1.wheels)   # 6
print(car2.wheels)   # 6

# Instance attribute is unique
print(car1.make)     # "Toyota"
print(car2.make)     # "Honda"

# ========== SPECIAL METHODS (DUNDER METHODS) ==========
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation for users (print)"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """String representation for developers (debugging)"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Define length of object"""
        return self.pages
    
    def __eq__(self, other):
        """Define equality comparison"""
        return (self.title == other.title and 
                self.author == other.author)
    
    def __lt__(self, other):
        """Define less than comparison (for sorting)"""
        return self.pages < other.pages
    
    def __add__(self, other):
        """Define addition behavior"""
        total_pages = self.pages + other.pages
        return Book(f"{self.title} & {other.title}", 
                   f"{self.author} & {other.author}", 
                   total_pages)

# Using special methods
book1 = Book("1984", "George Orwell", 328)
book2 = Book("Animal Farm", "George Orwell", 112)

print(book1)          # Calls __str__
print(len(book1))     # Calls __len__ - 328
print(book1 == book2) # Calls __eq__ - False
print(book1 < book2)  # Calls __lt__ - False

# Sort books by pages (uses __lt__)
books = [book1, book2]
books.sort()

combined = book1 + book2  # Calls __add__

# ========== PROPERTY DECORATORS ==========
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Private attribute
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set celsius from fahrenheit"""
        self._celsius = (value - 32) * 5/9

# Use like attributes (but with validation)
temp = Temperature(25)
print(temp.celsius)      # 25
print(temp.fahrenheit)   # 77.0

temp.celsius = 30        # Uses setter
temp.fahrenheit = 100    # Sets celsius via fahrenheit
# temp.celsius = -300    # Raises ValueError!

# ========== CLASS METHODS & STATIC METHODS ==========
class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
    
    @classmethod
    def margherita(cls, size):
        """Factory method - alternate constructor"""
        return cls(size, ["mozzarella", "tomato", "basil"])
    
    @classmethod
    def pepperoni(cls, size):
        """Another factory method"""
        return cls(size, ["mozzarella", "pepperoni"])
    
    @staticmethod
    def is_valid_size(size):
        """Static method - doesn't need self or cls"""
        return size in ["small", "medium", "large"]
    
    def __str__(self):
        return f"{self.size.capitalize()} pizza with {', '.join(self.toppings)}"

# Use factory methods
pizza1 = Pizza.margherita("large")
pizza2 = Pizza.pepperoni("medium")

# Use static method
if Pizza.is_valid_size("extra-large"):
    print("Valid size")
else:
    print("Invalid size")

# ========== PRIVATE & PROTECTED MEMBERS ==========
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner           # Public
        self._balance = balance      # Protected (convention)
        self.__transactions = []     # Private (name mangling)
    
    # Public method
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__log_transaction(f"Deposit: ${amount}")
    
    # Protected method (convention - can still be accessed)
    def _validate_amount(self, amount):
        return amount > 0
    
    # Private method (name mangled to _BankAccount__log_transaction)
    def __log_transaction(self, message):
        self.__transactions.append(message)
    
    # Getter for balance
    def get_balance(self):
        return self._balance
    
    # Public method to view transactions
    def get_transaction_history(self):
        return self.__transactions.copy()

account = BankAccount("Allan", 1000)

# Public access works
account.deposit(500)
print(account.owner)  # "Allan"

# Protected access works (but shouldn't be used externally)
print(account._balance)  # 1500 (works but not recommended)

# Private access is name-mangled
# print(account.__transactions)  # AttributeError!
# But can access via mangled name (not recommended)
print(account._BankAccount__transactions)  # Works but defeats purpose

# Use proper getters instead
print(account.get_balance())  # 1500
print(account.get_transaction_history())  # ["Deposit: $500"]
```


***

## THE FOUR PILLARS OF OOP

### PILLAR 1: ENCAPSULATION - Data Hiding \& Bundling

```python
# ========== ENCAPSULATION EXAMPLE ==========
class User:
    """Encapsulation: Bundle data and methods, control access"""
    
    def __init__(self, username, email, password):
        # Public attribute
        self.username = username
        
        # Protected attributes (convention with _)
        self._email = email
        self._password = password
        self._login_attempts = 0
    
    # Getter methods
    def get_email(self):
        """Controlled access to email"""
        return self._email
    
    def get_password(self):
        """Don't actually do this! Just for demonstration"""
        return "*" * len(self._password)  # Hide actual password
    
    # Setter methods with validation
    def set_email(self, new_email):
        """Validate before updating email"""
        if "@" in new_email and "." in new_email:
            self._email = new_email
            return "Email updated successfully"
        else:
            return "Invalid email format"
    
    def set_password(self, new_password):
        """Validate password requirements"""
        if len(new_password) >= 8 and any(c.isdigit() for c in new_password):
            self._password = new_password
            return "Password updated successfully"
        else:
            return "Password must be 8+ characters with at least one digit"
    
    def login(self, password):
        """Track failed login attempts"""
        if self._login_attempts >= 3:
            return "Account locked due to too many failed attempts"
        
        if password == self._password:
            self._login_attempts = 0
            return "Login successful"
        else:
            self._login_attempts += 1
            return f"Invalid password. Attempts: {self._login_attempts}/3"
    
    def reset_login_attempts(self):
        """Admin method to reset attempts"""
        self._login_attempts = 0

# Usage demonstrates encapsulation benefits
user = User("allan", "allan@email.com", "secure123")

# Can't directly access protected attributes (by convention)
# user._password = "hacked"  # Bad practice!

# Use setter methods with validation
print(user.set_email("newemail@test.com"))  # Valid
print(user.set_email("invalid"))            # Invalid

print(user.set_password("short"))           # Invalid
print(user.set_password("newpass123"))      # Valid

# Login tracking is hidden from user
print(user.login("wrong"))       # Attempt 1
print(user.login("wrong"))       # Attempt 2
print(user.login("wrong"))       # Attempt 3
print(user.login("newpass123"))  # Locked!

# ========== REAL-WORLD ENCAPSULATION: SHOPPING CART ==========
class ShoppingCart:
    """Encapsulation: Protect cart data and apply business rules"""
    
    def __init__(self):
        self.__items = []  # Private list
        self.__discount = 0
    
    def add_item(self, name, price, quantity=1):
        """Add item with validation"""
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        
        self.__items.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
    
    def remove_item(self, name):
        """Remove item by name"""
        self.__items = [item for item in self.__items 
                       if item["name"] != name]
    
    def apply_discount(self, percentage):
        """Apply discount with validation"""
        if 0 <= percentage <= 100:
            self.__discount = percentage
        else:
            raise ValueError("Discount must be between 0 and 100")
    
    def get_subtotal(self):
        """Calculate subtotal (private calculation)"""
        return sum(item["price"] * item["quantity"] 
                  for item in self.__items)
    
    def get_total(self):
        """Calculate final total with discount"""
        subtotal = self.get_subtotal()
        discount_amount = subtotal * (self.__discount / 100)
        return subtotal - discount_amount
    
    def get_item_count(self):
        """Total number of items"""
        return sum(item["quantity"] for item in self.__items)
    
    def view_cart(self):
        """Public method to view cart contents"""
        for item in self.__items:
            print(f"{item['name']}: ${item['price']} x {item['quantity']}")
        print(f"Subtotal: ${self.get_subtotal():.2f}")
        if self.__discount > 0:
            print(f"Discount: {self.__discount}%")
        print(f"Total: ${self.get_total():.2f}")

# Usage - internal details hidden
cart = ShoppingCart()
cart.add_item("Laptop", 999.99, 1)
cart.add_item("Mouse", 29.99, 2)
cart.apply_discount(10)

# Can't directly access __items (encapsulated)
# print(cart.__items)  # AttributeError!

# Use public interface instead
cart.view_cart()
print(f"Total items: {cart.get_item_count()}")
```


***

### PILLAR 2: INHERITANCE - Code Reuse \& Hierarchy

```python
# ========== BASIC INHERITANCE ==========
# Parent class (Base class, Superclass)
class Character:
    """Base character class"""
    
    def __init__(self, name, health, attack_power=10):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.alive = True
    
    def attack(self, opponent):
        """Basic attack"""
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        self.check_alive(opponent)
    
    def take_damage(self, damage):
        """Receive damage"""
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
    
    def check_alive(self, character):
        """Check if character is still alive"""
        if character.health <= 0:
            character.alive = False
            print(f"{character.name} has been defeated!")
    
    def display_stats(self):
        """Show character stats"""
        status = "Alive" if self.alive else "Defeated"
        print(f"{self.name} - HP: {self.health}, ATK: {self.attack_power}, Status: {status}")

# ========== CHILD CLASSES (SUBCLASSES) ==========
class Warrior(Character):
    """Warrior inherits from Character"""
    
    def __init__(self, name):
        # Call parent constructor with super()
        super().__init__(name, health=150, attack_power=20)
        self.armor = 10  # New attribute specific to Warrior
    
    def special_attack(self, opponent):
        """Warrior's special ability"""
        damage = self.attack_power * 2
        opponent.take_damage(damage)
        print(f"{self.name} uses POWER STRIKE on {opponent.name}!")
        print(f"{opponent.name} takes {damage} damage!")
    
    def defend(self):
        """Reduce incoming damage"""
        print(f"{self.name} raises shield! Armor increased.")
        self.armor += 5

class Mage(Character):
    """Mage inherits from Character"""
    
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=30)
        self.mana = 100  # New attribute
    
    def cast_spell(self, opponent):
        """Mage's special ability"""
        if self.mana >= 20:
            damage = self.attack_power * 1.5
            opponent.take_damage(damage)
            self.mana -= 20
            print(f"{self.name} casts FIREBALL on {opponent.name}!")
            print(f"{opponent.name} takes {damage} damage!")
        else:
            print(f"{self.name} doesn't have enough mana!")
    
    def meditate(self):
        """Restore mana"""
        self.mana = min(100, self.mana + 30)
        print(f"{self.name} meditates. Mana: {self.mana}")

class Archer(Character):
    """Archer inherits from Character"""
    
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=25)
        self.arrows = 30
    
    def shoot_arrow(self, opponent):
        """Archer's ranged attack"""
        if self.arrows > 0:
            critical = self.attack_power * 2 if self.arrows % 5 == 0 else self.attack_power
            opponent.take_damage(critical)
            self.arrows -= 1
            
            if critical > self.attack_power:
                print(f"{self.name} lands a CRITICAL HIT on {opponent.name}!")
            else:
                print(f"{self.name} shoots {opponent.name}!")
            print(f"Arrows remaining: {self.arrows}")
        else:
            print(f"{self.name} is out of arrows!")

# ========== USING INHERITED CLASSES ==========
# Create characters
warrior = Warrior("Conan")
mage = Mage("Gandalf")
archer = Archer("Legolas")

# All have inherited methods
warrior.display_stats()  # From Character
mage.display_stats()
archer.display_stats()

# All can use basic attack (inherited)
warrior.attack(mage)

# Each has their own special abilities
warrior.special_attack(archer)
mage.cast_spell(warrior)
archer.shoot_arrow(mage)

# ========== MULTILEVEL INHERITANCE ==========
class Vehicle:
    """Base class"""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"{self.brand} {self.model} starting...")

class Car(Vehicle):
    """Inherits from Vehicle"""
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def honk(self):
        print("Beep beep!")

class ElectricCar(Car):
    """Inherits from Car (which inherits from Vehicle)"""
    def __init__(self, brand, model, doors, battery):
        super().__init__(brand, model, doors)
        self.battery = battery
    
    def charge(self):
        print(f"Charging {self.brand} {self.model}...")

# ElectricCar has methods from all levels
tesla = ElectricCar("Tesla", "Model 3", 4, "75kWh")
tesla.start()    # From Vehicle
tesla.honk()     # From Car
tesla.charge()   # From ElectricCar

# ========== MULTIPLE INHERITANCE ==========
class Flyer:
    """Mixin for flying ability"""
    def fly(self):
        print(f"{self.name} takes flight!")

class Swimmer:
    """Mixin for swimming ability"""
    def swim(self):
        print(f"{self.name} dives into water!")

class Dragon(Character, Flyer):
    """Dragon can attack and fly"""
    def __init__(self, name):
        Character.__init__(self, name, health=200, attack_power=40)
    
    def breathe_fire(self, opponent):
        damage = self.attack_power * 3
        opponent.take_damage(damage)
        print(f"{self.name} breathes fire on {opponent.name}!")

class Mermaid(Character, Swimmer):
    """Mermaid can attack and swim"""
    def __init__(self, name):
        Character.__init__(self, name, health=90, attack_power=15)

# Using multiple inheritance
dragon = Dragon("Smaug")
dragon.display_stats()  # From Character
dragon.fly()            # From Flyer
dragon.breathe_fire(warrior)

mermaid = Mermaid("Ariel")
mermaid.swim()          # From Swimmer
mermaid.attack(archer)  # From Character

# ========== CHECKING INHERITANCE ==========
# isinstance() - check if object is instance of class
print(isinstance(warrior, Warrior))   # True
print(isinstance(warrior, Character)) # True (parent)
print(isinstance(warrior, Mage))      # False

# issubclass() - check if class inherits from another
print(issubclass(Warrior, Character))  # True
print(issubclass(Warrior, Mage))       # False
print(issubclass(ElectricCar, Vehicle)) # True
```


***

### PILLAR 3: POLYMORPHISM - One Interface, Many Forms

```python
# ========== METHOD OVERRIDING ==========
class Animal:
    """Base class"""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """Generic speak method"""
        print(f"{self.name} makes a sound")
    
    def move(self):
        """Generic move method"""
        print(f"{self.name} moves")

class Dog(Animal):
    """Dog overrides speak() and move()"""
    def speak(self):
        print(f"{self.name} says Woof!")
    
    def move(self):
        print(f"{self.name} runs on four legs")

class Cat(Animal):
    """Cat overrides speak() and move()"""
    def speak(self):
        print(f"{self.name} says Meow!")
    
    def move(self):
        print(f"{self.name} prowls silently")

class Bird(Animal):
    """Bird overrides speak() and move()"""
    def speak(self):
        print(f"{self.name} says Tweet!")
    
    def move(self):
        print(f"{self.name} flies through the air")

# ========== POLYMORPHISM IN ACTION ==========
# Same method name, different behavior
animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Bird("Tweety")
]

# Polymorphic behavior - each class handles it differently
for animal in animals:
    animal.speak()  # Different output for each!
    animal.move()
    print()

# Function that works with any Animal subclass
def make_animal_speak(animal):
    """Works with any Animal or subclass"""
    animal.speak()

make_animal_speak(Dog("Rex"))
make_animal_speak(Cat("Mittens"))
make_animal_speak(Bird("Polly"))

# ========== POLYMORPHISM WITH OPERATORS ==========
class Vector:
    """2D Vector class"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Define + operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Define - operator"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Define * operator (scalar multiplication)"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Define == operator"""
        return self.x == other.x and self.y == other.y

# Polymorphic operators
v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2     # Calls __add__
v4 = v1 - v2     # Calls __sub__
v5 = v1 * 3      # Calls __mul__
print(v3)        # Calls __str__
print(v1 == v2)  # Calls __eq__

# ========== POLYMORPHISM WITH PAYMENT SYSTEM ==========
class PaymentMethod:
    """Base payment class"""
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement pay()")
    
    def get_receipt(self, amount):
        return f"Payment of ${amount:.2f} processed"

class CreditCard(PaymentMethod):
    def __init__(self, card_number, cvv):
        self.card_number = card_number[-4:]  # Last 4 digits
        self.cvv = cvv
    
    def pay(self, amount):
        print(f"Processing credit card payment...")
        print(f"Card ending in {self.card_number}")
        print(f"Amount: ${amount:.2f}")
        return True

class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email
    
    def pay(self, amount):
        print(f"Processing PayPal payment...")
        print(f"Account: {self.email}")
        print(f"Amount: ${amount:.2f}")
        return True

class Bitcoin(PaymentMethod):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    
    def pay(self, amount):
        print(f"Processing Bitcoin payment...")
        print(f"Wallet: {self.wallet_address[:10]}...")
        print(f"Amount: ${amount:.2f}")
        return True

# Checkout function works with ANY payment method!
def checkout(payment_method, amount):
    """Polymorphic function - works with any PaymentMethod"""
    if payment_method.pay(amount):
        print(payment_method.get_receipt(amount))
        print("Payment successful!\n")

# Different payment methods, same interface
credit = CreditCard("1234-5678-9012-3456", "123")
paypal = PayPal("user@email.com")
bitcoin = Bitcoin("1A2B3C4D5E6F7G8H9I")

checkout(credit, 99.99)
checkout(paypal, 149.50)
checkout(bitcoin, 299.00)
```


***

### PILLAR 4: ABSTRACTION - Hiding Complexity

```python
# ========== ABSTRACTION WITH ABC MODULE ==========
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class - cannot be instantiated"""
    
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def area(self):
        """Subclasses MUST implement this"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Subclasses MUST implement this"""
        pass
    
    def describe(self):
        """Concrete method - shared by all shapes"""
        print(f"I am a {self.color} {self.__class__.__name__}")

# Can't create Shape directly
# shape = Shape("red")  # TypeError!

class Circle(Shape):
    """Concrete implementation of Shape"""
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        """Required implementation"""
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        """Required implementation"""
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    """Another concrete implementation"""
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    """Yet another implementation"""
    def __init__(self, color, base, height, side1, side2, side3):
        super().__init__(color)
        self.base = base
        self.height = height
        self.sides = (side1, side2, side3)
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return sum(self.sides)

# All shapes share the same interface
shapes = [
    Circle("red", 5),
    Rectangle("blue", 4, 6),
    Triangle("green", 3, 4, 3, 4, 5)
]

# Abstraction - we don't care HOW area is calculated
for shape in shapes:
    shape.describe()
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
    print()

# ========== REAL-WORLD ABSTRACTION: DATABASE ==========
class Database(ABC):
    """Abstract database interface"""
    
    @abstractmethod
    def connect(self):
        """Establish connection"""
        pass
    
    @abstractmethod
    def disconnect(self):
        """Close connection"""
        pass
    
    @abstractmethod
    def query(self, sql):
        """Execute query"""
        pass
    
    @abstractmethod
    def insert(self, table, data):
        """Insert data"""
        pass

class MySQL(Database):
    """MySQL implementation"""
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.connected = False
    
    def connect(self):
        print(f"Connecting to MySQL at {self.host}...")
        self.connected = True
        print("Connected!")
    
    def disconnect(self):
        print("Disconnecting from MySQL...")
        self.connected = False
    
    def query(self, sql):
        if not self.connected:
            raise Exception("Not connected!")
        print(f"MySQL Query: {sql}")
        return []  # Simulated result
    
    def insert(self, table, data):
        if not self.connected:
            raise Exception("Not connected!")
        print(f"MySQL Insert into {table}: {data}")

class PostgreSQL(Database):
    """PostgreSQL implementation"""
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.connected = False
    
    def connect(self):
        print(f"Connecting to PostgreSQL at {self.host}...")
        self.connected = True
        print("Connected!")
    
    def disconnect(self):
        print("Disconnecting from PostgreSQL...")
        self.connected = False
    
    def query(self, sql):
        if not self.connected:
            raise Exception("Not connected!")
        print(f"PostgreSQL Query: {sql}")
        return []
    
    def insert(self, table, data):
        if not self.connected:
            raise Exception("Not connected!")
        print(f"PostgreSQL Insert into {table}: {data}")

# Application code doesn't care which database is used!
def process_data(database: Database):
    """Works with ANY database implementation"""
    database.connect()
    database.query("SELECT * FROM users")
    database.insert("users", {"name": "Allan", "age": 28})
    database.disconnect()

# Abstraction - same code works with different databases
mysql_db = MySQL("localhost", "admin", "pass123")
postgres_db = PostgreSQL("localhost", "admin", "pass123")

process_data(mysql_db)
print()
process_data(postgres_db)
```


## COMPLETE DATA STRUCTURES GUIDE


### LINKED LISTS - Complete Implementation

```python
# ========== NODE CLASS - BUILDING BLOCK ==========
class Node:
    """
    A single node in a linked list
    Contains data and a reference to the next node
    """
    def __init__(self, data):
        # Data is the value stored in the node
        self.data = data
        
        # Next is a pointer/reference to the next node
        # Initially None when node is created
        self.next = None
    
    def __repr__(self):
        """String representation for debugging"""
        return f"Node({self.data})"

# ========== LINKED LIST CLASS - COMPLETE IMPLEMENTATION ==========
class LinkedList:
    """
    Singly linked list implementation
    Each node points to the next node
    """
    
    def __init__(self):
        # Head points to the first node
        # If list is empty, head is None
        self.head = None
        
        # Tail points to the last node
        # Makes appending O(1) instead of O(n)
        self.tail = None
        
        # Track size for O(1) length lookup
        self.size = 0
    
    def is_empty(self):
        """Check if list is empty - O(1)"""
        return self.head is None
    
    def __len__(self):
        """Return size of list - O(1)"""
        return self.size
    
    # ========== APPEND - ADD TO END ==========
    def append(self, data):
        """
        Add node to end of list - O(1) with tail pointer
        
        Steps:
        1. Create new node with data
        2. If list is empty, new node becomes head and tail
        3. Otherwise, link current tail to new node and update tail
        """
        new_node = Node(data)
        
        # Case 1: Empty list
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        
        # Case 2: List has nodes
        else:
            # Link current tail to new node
            self.tail.next = new_node
            # Update tail to new node
            self.tail = new_node
        
        self.size += 1
    
    # ========== PREPEND - ADD TO BEGINNING ==========
    def prepend(self, data):
        """
        Add node to beginning of list - O(1)
        
        Steps:
        1. Create new node
        2. Point new node to current head
        3. Update head to new node
        """
        new_node = Node(data)
        
        # If list is empty, update tail too
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # New node points to current head
            new_node.next = self.head
            # Head now points to new node
            self.head = new_node
        
        self.size += 1
    
    # ========== INSERT AT POSITION ==========
    def insert_at_position(self, position, data):
        """
        Insert node at specific position - O(n)
        Position starts at 1 (not 0)
        
        Steps:
        1. If position is 1, insert at beginning
        2. Otherwise, traverse to position-1
        3. Insert new node between current and next
        """
        # Validate position
        if position < 1 or position > self.size + 1:
            raise IndexError(f"Position {position} out of range")
        
        # Case 1: Insert at beginning
        if position == 1:
            self.prepend(data)
            return
        
        # Case 2: Insert at end
        if position == self.size + 1:
            self.append(data)
            return
        
        # Case 3: Insert in middle
        new_node = Node(data)
        current = self.head
        
        # Move to node before insertion point
        for _ in range(position - 2):
            current = current.next
        
        # Insert new node
        new_node.next = current.next
        current.next = new_node
        
        self.size += 1
    
    # ========== DELETE AT POSITION ==========
    def delete_at_position(self, position):
        """
        Delete node at specific position - O(n)
        
        Steps:
        1. If deleting head, update head to next node
        2. Otherwise, traverse to position-1
        3. Skip over node to delete
        """
        # Validate position
        if self.is_empty():
            raise Exception("Cannot delete from empty list")
        if position < 1 or position > self.size:
            raise IndexError(f"Position {position} out of range")
        
        # Case 1: Delete head
        if position == 1:
            deleted_data = self.head.data
            self.head = self.head.next
            
            # If list becomes empty, update tail
            if self.head is None:
                self.tail = None
            
            self.size -= 1
            return deleted_data
        
        # Case 2: Delete from middle or end
        current = self.head
        
        # Move to node before deletion point
        for _ in range(position - 2):
            current = current.next
        
        # Get data to return
        deleted_data = current.next.data
        
        # Skip over node to delete
        current.next = current.next.next
        
        # If deleted last node, update tail
        if current.next is None:
            self.tail = current
        
        self.size -= 1
        return deleted_data
    
    # ========== DELETE BY VALUE ==========
    def delete_by_value(self, value):
        """
        Delete first node with given value - O(n)
        Returns True if deleted, False if not found
        """
        if self.is_empty():
            return False
        
        # Case 1: Value is in head
        if self.head.data == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return True
        
        # Case 2: Value is elsewhere
        current = self.head
        while current.next:
            if current.next.data == value:
                # Found it - skip over
                current.next = current.next.next
                
                # If deleted last node, update tail
                if current.next is None:
                    self.tail = current
                
                self.size -= 1
                return True
            current = current.next
        
        return False  # Not found
    
    # ========== GET AT POSITION ==========
    def get_at_position(self, position):
        """
        Get data at position - O(n)
        Position starts at 1
        """
        if position < 1 or position > self.size:
            raise IndexError(f"Position {position} out of range")
        
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        return current.data
    
    # ========== SEARCH ==========
    def search(self, value):
        """
        Find position of first occurrence of value - O(n)
        Returns position (1-indexed) or -1 if not found
        """
        current = self.head
        position = 1
        
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        
        return -1  # Not found
    
    # ========== TRAVERSE ==========
    def traverse(self):
        """
        Visit all nodes and print data - O(n)
        
        Steps:
        1. Start at head
        2. Print current node data
        3. Move to next node
        4. Repeat until next is None
        """
        if self.is_empty():
            print("List is empty")
            return
        
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    # ========== DISPLAY ==========
    def display(self):
        """Pretty print the list"""
        if self.is_empty():
            print("Empty List")
            return
        
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        
        print(" -> ".join(values))
    
    # ========== REVERSE ==========
    def reverse(self):
        """
        Reverse the linked list - O(n)
        
        Steps:
        1. Keep track of previous, current, and next
        2. For each node, reverse the pointer
        3. Update head and tail
        """
        if self.is_empty() or self.head == self.tail:
            return
        
        # Swap head and tail
        self.tail = self.head
        
        prev = None
        current = self.head
        
        while current:
            # Save next node
            next_node = current.next
            # Reverse the pointer
            current.next = prev
            # Move forward
            prev = current
            current = next_node
        
        # Update head
        self.head = prev
    
    # ========== TO LIST ==========
    def to_list(self):
        """Convert linked list to Python list - O(n)"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    # ========== FROM LIST ==========
    @classmethod
    def from_list(cls, items):
        """Create linked list from Python list - O(n)"""
        linked_list = cls()
        for item in items:
            linked_list.append(item)
        return linked_list
    
    # ========== CLEAR ==========
    def clear(self):
        """Remove all nodes - O(1)"""
        self.head = None
        self.tail = None
        self.size = 0
    
    # ========== STRING REPRESENTATION ==========
    def __repr__(self):
        """String representation for debugging"""
        return f"LinkedList({self.to_list()})"
    
    def __str__(self):
        """User-friendly string representation"""
        return " -> ".join(str(item) for item in self.to_list()) + " -> None"

# ========== USAGE EXAMPLES ==========
if __name__ == "__main__":
    # Create linked list
    ll = LinkedList()
    
    # Append elements
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print("After appending 1, 2, 3:")
    ll.display()  # 1 -> 2 -> 3
    
    # Prepend element
    ll.prepend(0)
    print("\nAfter prepending 0:")
    ll.display()  # 0 -> 1 -> 2 -> 3
    
    # Insert at position
    ll.insert_at_position(3, 1.5)
    print("\nAfter inserting 1.5 at position 3:")
    ll.display()  # 0 -> 1 -> 1.5 -> 2 -> 3
    
    # Delete at position
    deleted = ll.delete_at_position(3)
    print(f"\nDeleted {deleted} at position 3:")
    ll.display()  # 0 -> 1 -> 2 -> 3
    
    # Search
    position = ll.search(2)
    print(f"\nValue 2 found at position: {position}")
    
    # Get at position
    value = ll.get_at_position(2)
    print(f"Value at position 2: {value}")
    
    # Reverse
    ll.reverse()
    print("\nAfter reversing:")
    ll.display()  # 3 -> 2 -> 1 -> 0
    
    # Convert to list
    print(f"\nAs Python list: {ll.to_list()}")
    
    # Size
    print(f"Size: {len(ll)}")

# ========== ADVANCED LINKED LIST OPERATIONS ==========
class LinkedListAdvanced(LinkedList):
    """Extended linked list with advanced operations"""
    
    def find_middle(self):
        """
        Find middle element - O(n)
        Use slow/fast pointer technique
        """
        if self.is_empty():
            return None
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def has_cycle(self):
        """
        Detect if list has a cycle - O(n)
        Use Floyd's cycle detection
        """
        if self.is_empty():
            return False
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    
    def remove_duplicates(self):
        """
        Remove duplicate values - O(n²) or O(n) with set
        """
        if self.is_empty():
            return
        
        seen = set()
        current = self.head
        seen.add(current.data)
        
        while current.next:
            if current.next.data in seen:
                # Remove duplicate
                current.next = current.next.next
                self.size -= 1
            else:
                seen.add(current.next.data)
                current = current.next
        
        # Update tail
        self.tail = current
    
    def get_nth_from_end(self, n):
        """
        Get nth node from end - O(n)
        Use two pointer technique
        """
        if n < 1:
            raise ValueError("n must be >= 1")
        
        # Move first pointer n steps ahead
        first = self.head
        for _ in range(n):
            if first is None:
                raise IndexError(f"List has fewer than {n} elements")
            first = first.next
        
        # Move both pointers until first reaches end
        second = self.head
        while first:
            first = first.next
            second = second.next
        
        return second.data
    
    def merge_sorted(self, other):
        """
        Merge two sorted linked lists - O(n + m)
        """
        dummy = Node(0)
        current = dummy
        
        ptr1 = self.head
        ptr2 = other.head
        
        while ptr1 and ptr2:
            if ptr1.data <= ptr2.data:
                current.next = ptr1
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                ptr2 = ptr2.next
            current = current.next
        
        # Attach remaining nodes
        current.next = ptr1 if ptr1 else ptr2
        
        # Create new linked list
        merged = LinkedListAdvanced()
        merged.head = dummy.next
        
        # Find tail and calculate size
        current = merged.head
        size = 0
        while current:
            merged.tail = current
            size += 1
            current = current.next
        merged.size = size
        
        return merged
```


***

## STACKS - LIFO Data Structure

```python
# ========== STACK USING LINKED LIST ==========
class Stack:
    """
    Stack implementation using linked list
    LIFO: Last In, First Out
    All operations are O(1)
    """
    
    def __init__(self):
        # Head represents top of stack
        self.head = None
        # Track size
        self.size = 0
    
    def is_empty(self):
        """Check if stack is empty - O(1)"""
        return self.head is None
    
    def __len__(self):
        """Return size - O(1)"""
        return self.size
    
    def push(self, data):
        """
        Add element to top of stack - O(1)
        
        Steps:
        1. Create new node
        2. Point new node to current head
        3. Update head to new node
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        """
        Remove and return top element - O(1)
        Raises exception if stack is empty
        
        Steps:
        1. Check if empty
        2. Save head data
        3. Move head to next node
        4. Return saved data
        """
        if self.is_empty():
            raise Exception("Stack is empty - cannot pop")
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def peek(self):
        """
        View top element without removing - O(1)
        Raises exception if stack is empty
        """
        if self.is_empty():
            raise Exception("Stack is empty - cannot peek")
        
        return self.head.data
    
    def display(self):
        """Display stack from top to bottom"""
        if self.is_empty():
            print("Stack is empty")
            return
        
        current = self.head
        print("Top ->", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Bottom")
    
    def __repr__(self):
        """String representation"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return f"Stack([{', '.join(elements)}])"

# ========== STACK USING PYTHON LIST (SIMPLER) ==========
class SimpleStack:
    """
    Stack using Python list
    Much simpler but same concept
    """
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        """Add to end - O(1)"""
        self.items.append(item)
    
    def pop(self):
        """Remove from end - O(1)"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """View last item - O(1)"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __repr__(self):
        return f"Stack({self.items})"

# ========== STACK APPLICATIONS ==========

def is_balanced_parentheses(expression):
    """
    Check if parentheses are balanced
    Example: "((()))" -> True, "(()" -> False
    """
    stack = []
    opening = "({["
    closing = ")}]"
    pairs = {"(": ")", "{": "}", "[": "]"}
    
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            if pairs[stack[-1]] != char:
                return False
            stack.pop()
    
    return len(stack) == 0

# Test
print(is_balanced_parentheses("((()))"))      # True
print(is_balanced_parentheses("({[]})"))      # True
print(is_balanced_parentheses("((()"))        # False
print(is_balanced_parentheses("({[}])"))      # False

def reverse_string(text):
    """Reverse string using stack"""
    stack = []
    
    # Push all characters
    for char in text:
        stack.append(char)
    
    # Pop to build reversed string
    reversed_text = ""
    while stack:
        reversed_text += stack.pop()
    
    return reversed_text

print(reverse_string("Python"))  # "nohtyP"

def evaluate_postfix(expression):
    """
    Evaluate postfix expression
    Example: "5 3 + 2 *" = (5 + 3) * 2 = 16
    """
    stack = []
    operators = {"+", "-", "*", "/"}
    
    for token in expression.split():
        if token not in operators:
            # Number - push to stack
            stack.append(int(token))
        else:
            # Operator - pop two operands
            b = stack.pop()
            a = stack.pop()
            
            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = a / b
            
            stack.append(result)
    
    return stack[^13_0]

print(evaluate_postfix("5 3 + 2 *"))  # 16
print(evaluate_postfix("10 5 / 3 +")) # 5

# ========== STACK USAGE EXAMPLES ==========
if __name__ == "__main__":
    # Create stack
    stack = Stack()
    
    # Push elements
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("After pushing 1, 2, 3:")
    stack.display()  # Top -> 3 -> 2 -> 1 -> Bottom
    
    # Peek
    top = stack.peek()
    print(f"\nTop element: {top}")  # 3
    
    # Pop
    popped = stack.pop()
    print(f"\nPopped: {popped}")    # 3
    stack.display()                  # Top -> 2 -> 1 -> Bottom
    
    # Check empty
    print(f"\nIs empty: {stack.is_empty()}")  # False
    
    # Size
    print(f"Size: {len(stack)}")  # 2
```


## QUEUES - FIFO Data Structure

```python
# ========== QUEUE USING COLLECTIONS.DEQUE (RECOMMENDED) ==========
from collections import deque

class Queue:
    """
    Queue implementation using deque
    FIFO: First In, First Out
    All operations are O(1) - very efficient!
    """
    
    def __init__(self):
        self.items = deque()
    
    def is_empty(self):
        """Check if queue is empty - O(1)"""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """
        Add item to end of queue - O(1)
        Also called: push, add, insert
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Remove and return item from front - O(1)
        Also called: pop, remove, delete
        Raises exception if queue is empty
        """
        if self.is_empty():
            raise Exception("Queue is empty - cannot dequeue")
        return self.items.popleft()  # O(1) - this is why we use deque!
    
    def peek(self):
        """
        View front item without removing - O(1)
        Also called: front, first
        """
        if self.is_empty():
            raise Exception("Queue is empty - cannot peek")
        return self.items[^14_0]
    
    def size(self):
        """Return number of items - O(1)"""
        return len(self.items)
    
    def display(self):
        """Display queue from front to back"""
        if self.is_empty():
            print("Queue is empty")
            return
        
        print("Front ->", end=" ")
        for item in self.items:
            print(item, end=" -> ")
        print("Back")
    
    def __repr__(self):
        """String representation"""
        return f"Queue({list(self.items)})"
    
    def __len__(self):
        """Support len() function"""
        return len(self.items)

# ========== WHY NOT USE PYTHON LIST FOR QUEUE? ==========
"""
Python lists are NOT efficient for queues because:
- list.pop(0) is O(n) - must shift all elements
- deque.popleft() is O(1) - much faster!

DON'T DO THIS:
class BadQueue:
    def __init__(self):
        self.items = []
    
    def dequeue(self):
        return self.items.pop(0)  # O(n) - SLOW!

DO THIS INSTEAD:
Use deque (as shown above) for O(1) operations
"""

# ========== QUEUE USING LINKED LIST ==========
class QueueLinkedList:
    """
    Queue implementation using linked list
    All operations are O(1)
    """
    
    def __init__(self):
        self.front = None  # Points to first node
        self.rear = None   # Points to last node
        self.size = 0
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        """Add to rear - O(1)"""
        new_node = Node(data)
        
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
    
    def dequeue(self):
        """Remove from front - O(1)"""
        if self.is_empty():
            raise Exception("Queue is empty")
        
        data = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        self.size -= 1
        return data
    
    def peek(self):
        """View front - O(1)"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.data
    
    def __len__(self):
        return self.size

# ========== QUEUE APPLICATIONS ==========

def hot_potato_game(names, num):
    """
    Hot Potato game simulation
    Players pass a potato, every nth person is eliminated
    """
    queue = Queue()
    
    # Add all players to queue
    for name in names:
        queue.enqueue(name)
    
    # Play until one person left
    while len(queue) > 1:
        # Pass the potato num-1 times
        for _ in range(num - 1):
            queue.enqueue(queue.dequeue())
        
        # Eliminate the person holding it
        eliminated = queue.dequeue()
        print(f"{eliminated} is eliminated!")
    
    # Winner
    winner = queue.dequeue()
    print(f"\n{winner} wins!")
    return winner

# Test
players = ["Alice", "Bob", "Charlie", "David", "Eve"]
hot_potato_game(players, 3)

def printer_queue_simulation():
    """
    Simulate a printer queue
    Jobs are processed in order received
    """
    class PrintJob:
        def __init__(self, name, pages):
            self.name = name
            self.pages = pages
        
        def __repr__(self):
            return f"Job({self.name}, {self.pages} pages)"
    
    printer_queue = Queue()
    
    # Add print jobs
    printer_queue.enqueue(PrintJob("Document1.pdf", 5))
    printer_queue.enqueue(PrintJob("Photo.jpg", 1))
    printer_queue.enqueue(PrintJob("Report.docx", 20))
    
    print("Print Queue:")
    printer_queue.display()
    
    # Process jobs
    print("\nProcessing jobs:")
    while not printer_queue.is_empty():
        job = printer_queue.dequeue()
        print(f"Printing {job.name} ({job.pages} pages)...")
        print(f"Remaining jobs: {len(printer_queue)}")

printer_queue_simulation()

def breadth_first_search(graph, start):
    """
    BFS algorithm using queue
    Explores level by level
    """
    visited = set()
    queue = Queue()
    
    queue.enqueue(start)
    visited.add(start)
    
    while not queue.is_empty():
        vertex = queue.dequeue()
        print(f"Visiting: {vertex}")
        
        # Add unvisited neighbors to queue
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

# Test BFS
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print("\nBreadth-First Search from A:")
breadth_first_search(graph, 'A')

# ========== PRIORITY QUEUE ==========
import heapq

class PriorityQueue:
    """
    Priority Queue - items with higher priority are dequeued first
    Uses heap for efficient operations
    """
    
    def __init__(self):
        self.items = []
        self.counter = 0  # For stable sorting
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item, priority):
        """
        Add item with priority - O(log n)
        Lower priority number = higher priority
        """
        # Use counter to maintain insertion order for same priority
        heapq.heappush(self.items, (priority, self.counter, item))
        self.counter += 1
    
    def dequeue(self):
        """Remove highest priority item - O(log n)"""
        if self.is_empty():
            raise Exception("Priority queue is empty")
        
        priority, _, item = heapq.heappop(self.items)
        return item
    
    def peek(self):
        """View highest priority item - O(1)"""
        if self.is_empty():
            raise Exception("Priority queue is empty")
        return self.items[^14_0][^14_2]
    
    def __len__(self):
        return len(self.items)

# Test Priority Queue
pq = PriorityQueue()
pq.enqueue("Low priority task", 5)
pq.enqueue("High priority task", 1)
pq.enqueue("Medium priority task", 3)

print("\nProcessing tasks by priority:")
while not pq.is_empty():
    task = pq.dequeue()
    print(f"Processing: {task}")

# ========== CIRCULAR QUEUE ==========
class CircularQueue:
    """
    Fixed-size queue that wraps around
    Efficient memory usage
    """
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def enqueue(self, item):
        """Add item - O(1)"""
        if self.is_full():
            raise Exception("Queue is full")
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
    
    def dequeue(self):
        """Remove item - O(1)"""
        if self.is_empty():
            raise Exception("Queue is empty")
        
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        print("Queue:", end=" ")
        i = self.front
        for _ in range(self.size):
            print(self.queue[i], end=" ")
            i = (i + 1) % self.capacity
        print()

# Test Circular Queue
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.display()
cq.dequeue()
cq.dequeue()
cq.enqueue(4)
cq.enqueue(5)
cq.display()

# ========== QUEUE USAGE EXAMPLES ==========
if __name__ == "__main__":
    # Create queue
    queue = Queue()
    
    # Enqueue elements
    queue.enqueue("First")
    queue.enqueue("Second")
    queue.enqueue("Third")
    print("After enqueueing:")
    queue.display()  # Front -> First -> Second -> Third -> Back
    
    # Peek
    front = queue.peek()
    print(f"\nFront element: {front}")  # "First"
    
    # Dequeue
    removed = queue.dequeue()
    print(f"\nDequeued: {removed}")  # "First"
    queue.display()  # Front -> Second -> Third -> Back
    
    # Size
    print(f"\nSize: {len(queue)}")  # 2
    
    # Check empty
    print(f"Is empty: {queue.is_empty()}")  # False
```


***

## REAL-WORLD DATA STRUCTURE APPLICATION: MUSIC PLAYLIST

```python
# ========== COMPLETE MUSIC PLAYLIST SYSTEM ==========

class Song:
    """Represents a single song"""
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # in seconds
    
    def __repr__(self):
        mins = self.duration // 60
        secs = self.duration % 60
        return f"{self.title} - {self.artist} ({mins}:{secs:02d})"

class MusicPlaylist:
    """
    Complete music playlist using linked list
    Combines concepts from all data structures
    """
    
    def __init__(self, name):
        self.name = name
        self.songs = LinkedList()  # Main playlist
        self.current_position = 0
        self.history = Stack()     # Recently played (undo)
        self.queue = Queue()       # Up next
    
    def add_song(self, title, artist, duration):
        """Add song to end of playlist"""
        song = Song(title, artist, duration)
        self.songs.append(song)
        print(f"Added: {song}")
    
    def remove_song(self, position):
        """Remove song at position"""
        if position < 1 or position > len(self.songs):
            print("Invalid position")
            return
        
        song = self.songs.delete_at_position(position)
        print(f"Removed: {song}")
    
    def display(self):
        """Show all songs in playlist"""
        print(f"\n{'='*50}")
        print(f"{self.name.center(50)}")
        print(f"{'='*50}")
        
        if self.songs.is_empty():
            print("Playlist is empty")
            return
        
        current = self.songs.head
        position = 1
        total_duration = 0
        
        while current:
            song = current.data
            marker = "▶" if position == self.current_position else " "
            print(f"{marker} {position}. {song}")
            total_duration += song.duration
            current = current.next
            position += 1
        
        mins = total_duration // 60
        secs = total_duration % 60
        print(f"\nTotal: {len(self.songs)} songs, {mins}:{secs:02d}")
        print(f"{'='*50}\n")
    
    def play_song_at_position(self, position):
        """Play specific song"""
        if position < 1 or position > len(self.songs):
            print("Invalid position")
            return
        
        song = self.songs.get_at_position(position)
        self.current_position = position
        
        # Add to history
        self.history.push(song)
        
        print(f"\n♫ Now playing: {song}")
    
    def next_song(self):
        """Play next song"""
        # Check queue first
        if not self.queue.is_empty():
            song = self.queue.dequeue()
            print(f"\n♫ Playing from queue: {song}")
            self.history.push(song)
            return
        
        # Otherwise play next in playlist
        if self.current_position < len(self.songs):
            self.current_position += 1
            self.play_song_at_position(self.current_position)
        else:
            print("End of playlist")
    
    def previous_song(self):
        """Play previous song"""
        if self.current_position > 1:
            self.current_position -= 1
            self.play_song_at_position(self.current_position)
        else:
            print("Already at first song")
    
    def queue_next(self, title, artist, duration):
        """Add song to play queue (next up)"""
        song = Song(title, artist, duration)
        self.queue.enqueue(song)
        print(f"Queued next: {song}")
    
    def view_queue(self):
        """Show upcoming songs in queue"""
        if self.queue.is_empty():
            print("Queue is empty")
            return
        
        print("\n--- Up Next ---")
        temp = []
        i = 1
        while not self.queue.is_empty():
            song = self.queue.dequeue()
            print(f"{i}. {song}")
            temp.append(song)
            i += 1
        
        # Restore queue
        for song in temp:
            self.queue.enqueue(song)
        print()
    
    def view_history(self):
        """Show recently played songs"""
        if self.history.is_empty():
            print("No history")
            return
        
        print("\n--- Recently Played ---")
        temp = []
        i = 1
        while not self.history.is_empty():
            song = self.history.pop()
            print(f"{i}. {song}")
            temp.append(song)
            i += 1
        
        # Restore history
        for song in reversed(temp):
            self.history.push(song)
        print()
    
    def shuffle(self):
        """Shuffle playlist randomly"""
        import random
        songs_list = self.songs.to_list()
        random.shuffle(songs_list)
        
        # Rebuild linked list
        self.songs.clear()
        for song in songs_list:
            self.songs.append(song)
        
        print("Playlist shuffled!")
    
    def sort_by_title(self):
        """Sort songs by title"""
        songs_list = self.songs.to_list()
        songs_list.sort(key=lambda s: s.title)
        
        self.songs.clear()
        for song in songs_list:
            self.songs.append(song)
        
        print("Sorted by title")
    
    def sort_by_artist(self):
        """Sort songs by artist"""
        songs_list = self.songs.to_list()
        songs_list.sort(key=lambda s: s.artist)
        
        self.songs.clear()
        for song in songs_list:
            self.songs.append(song)
        
        print("Sorted by artist")
    
    def search_by_title(self, query):
        """Search for songs by title"""
        print(f"\nSearching for '{query}':")
        current = self.songs.head
        position = 1
        found = False
        
        while current:
            song = current.data
            if query.lower() in song.title.lower():
                print(f"{position}. {song}")
                found = True
            current = current.next
            position += 1
        
        if not found:
            print("No songs found")
    
    def search_by_artist(self, query):
        """Search for songs by artist"""
        print(f"\nSongs by '{query}':")
        current = self.songs.head
        position = 1
        found = False
        
        while current:
            song = current.data
            if query.lower() in song.artist.lower():
                print(f"{position}. {song}")
                found = True
            current = current.next
            position += 1
        
        if not found:
            print("No songs found")

# ========== USAGE EXAMPLE ==========
if __name__ == "__main__":
    # Create playlist
    my_playlist = MusicPlaylist("Allan's Favorites")
    
    # Add songs
    my_playlist.add_song("Bohemian Rhapsody", "Queen", 354)
    my_playlist.add_song("Stairway to Heaven", "Led Zeppelin", 482)
    my_playlist.add_song("Hotel California", "Eagles", 391)
    my_playlist.add_song("Imagine", "John Lennon", 183)
    my_playlist.add_song("Hey Jude", "The Beatles", 431)
    
    # Display playlist
    my_playlist.display()
    
    # Play songs
    my_playlist.play_song_at_position(1)
    my_playlist.next_song()
    my_playlist.next_song()
    
    # Queue a song to play next
    my_playlist.queue_next("Yesterday", "The Beatles", 126)
    my_playlist.view_queue()
    
    # Play queued song
    my_playlist.next_song()
    
    # View history
    my_playlist.view_history()
    
    # Search
    my_playlist.search_by_artist("Beatles")
    
    # Shuffle
    my_playlist.shuffle()
    my_playlist.display()
```

This expanded guide now covers:

- ✅ Variables, I/O, Data Types
- ✅ Control Flow
- ✅ Loops
- ✅ Lists (exhaustive)
- ✅ Dictionaries (exhaustive)
- ✅ Functions (exhaustive)
- ✅ Strings (exhaustive)
- ✅ Sets \& Tuples (exhaustive)
- ✅ Object-Oriented Programming (all 4 pillars)
- ✅ Linked Lists (complete implementation)
- ✅ Stacks (LIFO)
- ✅ Queues (FIFO)
- ✅ Real-world application (Music Playlist)

Shall I continue with the remaining topics:

- **Complete Regular Expressions (Regex) Guide**
- **Complete Functional Programming Guide** (Lambda, Map, Filter, Comprehensions)
- **Complete APIs \& HTTP Requests Guide**
- **API Authentication (OAuth, Spotify)**
- **Pokemon Game Deep Dive**
- **Practice Challenges (20+ exercises)**
- **Interview Preparation**


## COMPLETE REGULAR EXPRESSIONS (REGEX) GUIDE


### Regex Fundamentals - Core Methods

```python
import re

# ========== RE.SEARCH() - FIND FIRST MATCH ==========
"""
Returns a Match object if pattern is found, None otherwise
Searches anywhere in the string
"""

text = "My phone number is 555-1234 and backup is 555-5678"

# Basic search
match = re.search(r"\d+", text)
if match:
    print(match.group())  # "555" - first digits found
    print(match.start())  # 19 - starting index
    print(match.end())    # 22 - ending index
    print(match.span())   # (19, 22) - tuple of start and end

# Search returns None if not found
result = re.search(r"email", text)
if result is None:
    print("Email not found")

# ========== RE.FINDALL() - FIND ALL MATCHES ==========
"""
Returns a list of all matches
Most commonly used for extracting multiple patterns
"""

text = "I have 5 cats, 3 dogs, and 12 fish"

# Find all numbers
numbers = re.findall(r"\d+", text)
print(numbers)  # ['5', '3', '12']

# Find all words
words = re.findall(r"\w+", text)
print(words)  # ['I', 'have', '5', 'cats', '3', 'dogs', 'and', '12', 'fish']

# Find all email addresses
email_text = "Contact us at info@company.com or support@company.com"
emails = re.findall(r"\w+@\w+\.\w+", email_text)
print(emails)  # ['info@company.com', 'support@company.com']

# ========== RE.MATCH() - MATCH FROM START ==========
"""
Only matches if pattern is at the beginning of string
Returns Match object or None
"""

text1 = "Hello world"
text2 = "world Hello"

# Matches because starts with "Hello"
match1 = re.match(r"Hello", text1)
if match1:
    print("Match found!")  # This prints

# Doesn't match because doesn't start with "Hello"
match2 = re.match(r"Hello", text2)
if match2 is None:
    print("No match - pattern not at start")

# Common use: validating format
phone = "555-1234"
if re.match(r"\d{3}-\d{4}", phone):
    print("Valid phone format")

# ========== RE.SUB() - SUBSTITUTE/REPLACE ==========
"""
Replace occurrences of pattern with replacement string
Like string.replace() but with regex patterns
"""

text = "I love cats. Cats are great. CATS everywhere!"

# Basic replacement (case-sensitive)
new_text = re.sub(r"cats", "dogs", text)
print(new_text)  # "I love dogs. Cats are great. CATS everywhere!"

# Case-insensitive replacement
new_text = re.sub(r"cats", "dogs", text, flags=re.IGNORECASE)
print(new_text)  # "I love dogs. dogs are great. dogs everywhere!"

# Replace with limit
new_text = re.sub(r"cats", "dogs", text, count=1, flags=re.IGNORECASE)
print(new_text)  # "I love dogs. Cats are great. CATS everywhere!"

# Remove all digits
text = "Product123 costs $45.99"
no_digits = re.sub(r"\d", "", text)
print(no_digits)  # "Product costs $."

# Clean extra whitespace
messy = "Too    many     spaces"
clean = re.sub(r"\s+", " ", messy)
print(clean)  # "Too many spaces"

# Remove HTML tags
html = "<p>This is <b>bold</b> text</p>"
clean = re.sub(r"<[^>]+>", "", html)
print(clean)  # "This is bold text"

# ========== RE.SPLIT() - SPLIT BY PATTERN ==========
"""
Split string by occurrences of pattern
Like string.split() but with regex
"""

text = "one,two;three:four five"

# Split by comma
parts = re.split(r",", text)
print(parts)  # ['one', 'two;three:four five']

# Split by multiple delimiters
parts = re.split(r"[,;:\s]+", text)
print(parts)  # ['one', 'two', 'three', 'four', 'five']

# Split with limit
parts = re.split(r",", "a,b,c,d,e", maxsplit=2)
print(parts)  # ['a', 'b', 'c,d,e']

# ========== RE.COMPILE() - COMPILE PATTERN FOR REUSE ==========
"""
Compile pattern once, reuse many times
More efficient for repeated use
"""

# Compile email pattern
email_pattern = re.compile(r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9_]+\.[a-z]{2,3}")

text1 = "Email me at john@test.com"
text2 = "Contact sarah@company.org"

# Reuse compiled pattern
emails1 = email_pattern.findall(text1)
emails2 = email_pattern.findall(text2)
print(emails1)  # ['john@test.com']
print(emails2)  # ['sarah@company.org']

# Compile with flags
pattern = re.compile(r"hello", re.IGNORECASE)
print(pattern.search("HELLO world"))  # Match found

# ========== RE.FINDITER() - ITERATOR OF MATCH OBJECTS ==========
"""
Returns iterator of Match objects
Useful when you need match positions/details
"""

text = "The price is $19.99 and tax is $1.50"
pattern = r"\$\d+\.\d+"

for match in re.finditer(pattern, text):
    print(f"Found: {match.group()} at position {match.start()}-{match.end()}")
# Found: $19.99 at position 13-19
# Found: $1.50 at position 31-36
```


### Metacharacters - Special Characters

```python
import re

# ========== \d - DIGIT (0-9) ==========
text = "abc123xyz456"
digits = re.findall(r"\d", text)
print(digits)  # ['1', '2', '3', '4', '5', '6']

# Multiple digits
numbers = re.findall(r"\d+", text)
print(numbers)  # ['123', '456']

# Non-digit (opposite)
non_digits = re.findall(r"\D", text)
print(non_digits)  # ['a', 'b', 'c', 'x', 'y', 'z']

# ========== \w - WORD CHARACTER (letters, digits, underscore) ==========
text = "hello_world123 test-case"
words = re.findall(r"\w+", text)
print(words)  # ['hello_world123', 'test', 'case']

# Non-word character (opposite)
non_word = re.findall(r"\W+", text)
print(non_word)  # [' ', '-']

# ========== \s - WHITESPACE (space, tab, newline) ==========
text = "hello world\tpython\ncode"
spaces = re.findall(r"\s", text)
print(spaces)  # [' ', '\t', '\n']

# Non-whitespace (opposite)
non_space = re.findall(r"\S+", text)
print(non_space)  # ['hello', 'world', 'python', 'code']

# ========== . - ANY CHARACTER (except newline) ==========
text = "cat bat rat"
matches = re.findall(r".at", text)
print(matches)  # ['cat', 'bat', 'rat']

# Literal dot (escape with \)
text = "file.txt and data.csv"
files = re.findall(r"\w+\.\w+", text)
print(files)  # ['file.txt', 'data.csv']

# ========== ^ - START OF STRING ==========
text = "Hello world"
if re.match(r"^Hello", text):
    print("Starts with Hello")

text = "world Hello"
if not re.match(r"^Hello", text):
    print("Doesn't start with Hello")

# ========== $ - END OF STRING ==========
text = "Hello world"
if re.search(r"world$", text):
    print("Ends with world")

# Validate email format
email = "user@example.com"
if re.match(r"^[\w.+-]+@[\w-]+\.\w+$", email):
    print("Valid email format")

# ========== \b - WORD BOUNDARY ==========
text = "cat cats scatter"

# Find whole word "cat" only
whole_word = re.findall(r"\bcat\b", text)
print(whole_word)  # ['cat'] - doesn't match 'cats' or 'scatter'

# Without boundary
all_matches = re.findall(r"cat", text)
print(all_matches)  # ['cat', 'cat', 'cat'] - matches all

# ========== \A and \Z - ABSOLUTE START AND END ==========
# Similar to ^ and $ but stricter
text = "Hello\nWorld"
print(re.match(r"^World", text, re.MULTILINE))  # Matches
print(re.match(r"\AWorld", text))  # Doesn't match

# ========== ESCAPING SPECIAL CHARACTERS ==========
# To match literal special characters, escape with \
text = "Price is $19.99"

# Wrong - $ is special
# re.search(r"$19", text)  # Won't work

# Correct - escape the $
price = re.search(r"\$\d+\.\d+", text)
print(price.group())  # "$19.99"

# Characters that need escaping: . ^ $ * + ? { } [ ] \ | ( )
special = "Test (parentheses)"
match = re.search(r"\(parentheses\)", special)
print(match.group())  # "(parentheses)"
```


### Quantifiers - Repetition

```python
import re

# ========== + - ONE OR MORE ==========
text = "aa aaa aaaa b bb"

# One or more 'a'
matches = re.findall(r"a+", text)
print(matches)  # ['aa', 'aaa', 'aaaa']

# Find numbers (one or more digits)
text = "I have 5 apples and 123 oranges"
numbers = re.findall(r"\d+", text)
print(numbers)  # ['5', '123']

# ========== * - ZERO OR MORE ==========
text = "aa a  aaa"

# Zero or more 'a'
matches = re.findall(r"a*", text)
print(matches)  # ['aa', '', 'a', '', '', 'aaa', '']

# Practical: optional whitespace
text = "hello    world"
cleaned = re.sub(r"\s*", "", text)  # Remove all spaces
print(cleaned)  # "helloworld"

# ========== ? - ZERO OR ONE (OPTIONAL) ==========
# Makes preceding character optional

text = "color colour"
matches = re.findall(r"colou?r", text)
print(matches)  # ['color', 'colour']

# Optional 's' for plural
text = "1 cat and 3 cats"
matches = re.findall(r"cats?", text)
print(matches)  # ['cat', 'cats']

# Optional protocol in URL
urls = "http://site.com and https://site.com"
matches = re.findall(r"https?://[\w.]+", urls)
print(matches)  # ['http://site.com', 'https://site.com']

# ========== {n} - EXACTLY N TIMES ==========
text = "123 45 6789 12"

# Exactly 3 digits
three_digit = re.findall(r"\d{3}", text)
print(three_digit)  # ['123', '678']

# Phone number: exactly 3 digits, dash, exactly 4 digits
phone = "Call me at 555-1234"
number = re.search(r"\d{3}-\d{4}", phone)
print(number.group())  # "555-1234"

# ========== {n,m} - BETWEEN N AND M TIMES ==========
text = "1 12 123 1234 12345"

# 2 to 4 digits
matches = re.findall(r"\d{2,4}", text)
print(matches)  # ['12', '123', '1234', '1234'] (12345 split)

# Password: 8-16 characters
password = "mypass123"
if re.match(r"^\w{8,16}$", password):
    print("Valid password length")

# ========== {n,} - N OR MORE TIMES ==========
text = "a aa aaa aaaa aaaaa"

# 3 or more 'a's
matches = re.findall(r"a{3,}", text)
print(matches)  # ['aaa', 'aaaa', 'aaaaa']

# ========== GREEDY vs NON-GREEDY ==========
html = "<div>Content 1</div><div>Content 2</div>"

# Greedy (default) - matches as much as possible
```

greedy = re.findall(r"<div>.*</div>", html)

```
print(greedy)  # ['<div>Content 1</div><div>Content 2</div>']

# Non-greedy (add ?) - matches as little as possible
```

non_greedy = re.findall(r"<div>.*?</div>", html)

```
```

print(non_greedy)  \# ['<div>Content 1</div>', '<div>Content 2</div>']

```

# Practical example: extract text between quotes
text = 'He said "Hello" and she said "Goodbye"'
greedy = re.findall(r'".*"', text)
print(greedy)  # ['"Hello" and she said "Goodbye"']

non_greedy = re.findall(r'".*?"', text)
print(non_greedy)  # ['"Hello"', '"Goodbye"']
```


### Character Sets and Ranges

```python
import re

# ========== [...] - CHARACTER SET ==========
# Matches any ONE character in the brackets

text = "hello world"

# Any vowel
vowels = re.findall(r"[aeiou]", text)
print(vowels)  # ['e', 'o', 'o']

# Any consonant (lowercase)
consonants = re.findall(r"[bcdfghjklmnpqrstvwxyz]", text)
print(consonants)  # ['h', 'l', 'l', 'w', 'r', 'l', 'd']

# ========== [a-z] - RANGE ==========
text = "Hello123World"

# Lowercase letters
lowercase = re.findall(r"[a-z]", text)
print(lowercase)  # ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']

# Uppercase letters
uppercase = re.findall(r"[A-Z]", text)
print(uppercase)  # ['H', 'W']

# Any letter
letters = re.findall(r"[a-zA-Z]+", text)
print(letters)  # ['Hello', 'World']

# Digits (alternative to \d)
digits = re.findall(r"[0-9]+", text)
print(digits)  # ['123']

# ========== [^...] - NEGATION (NOT IN SET) ==========
# ^ inside brackets means NOT

text = "abc123xyz"

# Everything except digits
non_digits = re.findall(r"[^\d]+", text)
print(non_digits)  # ['abc', 'xyz']

# Everything except vowels
no_vowels = re.findall(r"[^aeiou]+", text)
print(no_vowels)  # ['bc', '123', 'xyz']

# ========== PARTIAL RANGES ==========
# Only specific range of numbers/letters

text = "0123456789"

# Only 0-5
low_digits = re.findall(r"[0-5]", text)
print(low_digits)  # ['0', '1', '2', '3', '4', '5']

# Letters a-f (hexadecimal)
hex_text = "a5b2f8g9"
hex_chars = re.findall(r"[a-f0-9]", hex_text)
print(hex_chars)  # ['a', '5', 'b', '2', 'f', '8', '9']

# ========== MULTIPLE CHARACTER SETS ==========
# Combine multiple conditions

text = "user123@email.com"

# Letters, digits, underscore, dot
username_chars = re.findall(r"[a-zA-Z0-9_.]+", text)
print(username_chars)  # ['user123', 'email.com']

# ========== SPECIAL CHARACTERS IN SETS ==========
# Most special characters lose special meaning inside []

text = "test.$*+?"

# Match literal special characters
special = re.findall(r"[.$*+?]+", text)
print(special)  # ['.$*+?']

# But ^ - ] \ still need escaping in sets
text = "a-b^c]d"
matches = re.findall(r"[a\-b\^c\]d]+", text)
print(matches)  # ['a-b^c]d']

# ========== PRACTICAL PATTERNS ==========

# Validate username: letters, numbers, underscore, 3-16 chars
def validate_username(username):
    return bool(re.match(r"^[a-zA-Z0-9_]{3,16}$", username))

print(validate_username("user123"))    # True
print(validate_username("ab"))         # False (too short)
print(validate_username("user@name"))  # False (invalid char)

# Extract hex color codes
html = "color: #FF5733; background: #00FF00;"
colors = re.findall(r"#[0-9A-Fa-f]{6}", html)
print(colors)  # ['#FF5733', '#00FF00']

# Find words containing specific letters
text = "apple banana cherry date"
words_with_a = re.findall(r"\b\w*a\w*\b", text)
print(words_with_a)  # ['apple', 'banana', 'date']

# Extract numbers with optional decimal
text = "Price: 19.99, Quantity: 5, Tax: 1.5"
numbers = re.findall(r"\d+\.?\d*", text)
print(numbers)  # ['19.99', '5', '1.5']
```


### Groups and Capturing

```python
import re

# ========== (...) - CAPTURING GROUPS ==========
# Parentheses capture matched text

text = "John Smith, 555-1234"

# Capture name parts and phone
pattern = r"(\w+) (\w+), (\d{3}-\d{4})"
match = re.search(pattern, text)

if match:
    first_name = match.group(1)   # "John"
    last_name = match.group(2)    # "Smith"
    phone = match.group(3)        # "555-1234"
    full_match = match.group(0)   # Entire match
    
    print(f"First: {first_name}")
    print(f"Last: {last_name}")
    print(f"Phone: {phone}")

# ========== NAMED GROUPS (?P<name>...) ==========
# Give groups meaningful names

```

pattern = r"(?P<first>\w+) (?P<last>\w+), (?P<phone>\d{3}-\d{4})"

```
match = re.search(pattern, text)

if match:
    print(match.group('first'))  # "John"
    print(match.group('last'))   # "Smith"
    print(match.group('phone'))  # "555-1234"
    
    # Or as dictionary
    print(match.groupdict())
    # {'first': 'John', 'last': 'Smith', 'phone': '555-1234'}

# ========== USING GROUPS IN FINDALL ==========
email_text = "Contact: john@test.com or support@company.org"

# Without groups - returns full matches
emails = re.findall(r"\w+@\w+\.\w+", email_text)
print(emails)  # ['john@test.com', 'support@company.org']

# With groups - returns tuples of groups
pattern = r"(\w+)@(\w+)\.(\w+)"
parts = re.findall(pattern, email_text)
print(parts)  # [('john', 'test', 'com'), ('support', 'company', 'org')]

# ========== BACKREFERENCES \1, \2, etc. ==========
# Reference captured groups within the pattern

# Find repeated words
text = "the the quick brown brown fox"
duplicates = re.findall(r"\b(\w+)\s+\1\b", text)
print(duplicates)  # ['the', 'brown']

# Find palindrome words (simplified)
text = "mom dad noon racecar"
# Match word where first half equals reversed second half
palindromes = re.findall(r"\b(\w)(\w)(\w)\3\2\1\b", text)

# ========== SUBSTITUTION WITH GROUPS ==========
# Use groups in replacement string with \1, \2 or \g<1>, \g<2>

# Swap first and last name
text = "John Smith, Jane Doe"
swapped = re.sub(r"(\w+) (\w+)", r"\2, \1", text)
print(swapped)  # "Smith, John, Doe, Jane"

# Format date from MM/DD/YYYY to YYYY-MM-DD
dates = "12/25/2024 and 06/15/2023"
formatted = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\1-\2", dates)
print(formatted)  # "2024-12-25 and 2023-06-15"

# Named groups in substitution
text = "Price: $19.99"
formatted = re.sub(
    ```
    r"\$(?P<dollars>\d+)\.(?P<cents>\d{2})",
    ```
    ```
    r"\g<dollars> dollars and \g<cents> cents",
    ```
    text
)
print(formatted)  # "Price: 19 dollars and 99 cents"

# ========== NON-CAPTURING GROUPS (?:...) ==========
# Group for precedence but don't capture

text = "http://example.com and https://test.org"

# Capturing group (default)
urls = re.findall(r"(https?)://([\w.]+)", text)
print(urls)  # [('http', 'example.com'), ('https', 'test.org')]

# Non-capturing group
urls = re.findall(r"(?:https?)://([\w.]+)", text)
print(urls)  # ['example.com', 'test.org']

# Useful for logical grouping without capture overhead
phone = "Call (555) 123-4567"
number = re.search(r"(?:\()?\d{3}(?:\))?\s?\d{3}-\d{4}", phone)
print(number.group())  # "(555) 123-4567"

# ========== LOOKAHEAD AND LOOKBEHIND ==========

# Positive lookahead (?=...)
# Match only if followed by pattern
text = "price100 cost200 value300"
# Find word only if followed by digits
words = re.findall(r"\w+(?=\d+)", text)
print(words)  # ['price', 'cost', 'value']

# Negative lookahead (?!...)
# Match only if NOT followed by pattern
text = "file.txt file.pdf document.txt"
# Find files not ending in .txt
files = re.findall(r"\w+\.(?!txt)\w+", text)
print(files)  # ['file.pdf']

# Positive lookbehind (?<=...)
# Match only if preceded by pattern
text = "price$100 cost$200 value300"
# Find numbers only if preceded by $
prices = re.findall(r"(?<=\$)\d+", text)
print(prices)  # ['100', '200']

# Negative lookbehind (?<!...)
# Match only if NOT preceded by pattern
text = "$100 price200 cost300"
# Find numbers not preceded by $
numbers = re.findall(r"(?<!\$)\d+", text)
print(numbers)  # ['00', '200', '300'] (note: includes 00 from 100)
```


### Real-World Regex Applications

```python
import re

# ========== EMAIL VALIDATION ==========
def validate_email(email):
    """Comprehensive email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(validate_email("user@example.com"))      # True
print(validate_email("invalid.email"))         # False
print(validate_email("user@domain.co.uk"))     # True

# ========== PHONE NUMBER EXTRACTION ==========
def extract_phone_numbers(text):
    """Extract various phone number formats"""
    patterns = [
        r'\d{3}-\d{3}-\d{4}',           # 555-123-4567
        r'\(\d{3}\)\s?\d{3}-\d{4}',     # (555) 123-4567
        r'\d{3}\.\d{3}\.\d{4}',         # 555.123.4567
        r'\d{10}',                      # 5551234567
    ]
    
    phones = []
    for pattern in patterns:
        phones.extend(re.findall(pattern, text))
    return phones

text = "Call me at 555-123-4567 or (555) 234-5678 or 5551112222"
print(extract_phone_numbers(text))
# ['555-123-4567', '(555) 234-5678', '5551112222']

# ========== URL EXTRACTION ==========
def extract_urls(text):
    """Extract URLs from text"""
    pattern = r'https?://(?:www\.)?[\w\-\.]+(?:\.[a-z]{2,})+(?:/[\w\-\./?%&=]*)?'
    return re.findall(pattern, text, re.IGNORECASE)

text = """
Visit https://www.example.com or http://test.org/page?id=123
"""
print(extract_urls(text))
# ['https://www.example.com', 'http://test.org/page?id=123']

# ========== PASSWORD STRENGTH CHECK ==========
def check_password_strength(password):
    """Check if password meets requirements"""
    checks = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    
    strength = sum(checks.values())
    checks['score'] = f"{strength}/5"
    return checks

print(check_password_strength("Pass123!"))
# {'length': True, 'uppercase': True, 'lowercase': True, 
#  'digit': True, 'special': True, 'score': '5/5'}

# ========== HTML TAG REMOVAL ==========
def remove_html_tags(html):
    """Remove all HTML tags from text"""
    clean = re.sub(r'<[^>]+>', '', html)
    return clean

html = "<p>This is <b>bold</b> and <i>italic</i> text</p>"
print(remove_html_tags(html))
# "This is bold and italic text"

# ========== CREDIT CARD MASKING ==========
def mask_credit_card(number):
    """Mask all but last 4 digits of credit card"""
    # Remove spaces/dashes
    clean = re.sub(r'[\s\-]', '', number)
    
    # Mask digits except last 4
    if len(clean) >= 4:
        masked = re.sub(r'\d(?=\d{4})', '*', clean)
        return masked
    return number

print(mask_credit_card("1234-5678-9012-3456"))  # "************3456"
print(mask_credit_card("1234 5678 9012 3456"))  # "************3456"

# ========== EXTRACT HASHTAGS ==========
def extract_hashtags(text):
    """Extract all hashtags from social media text"""
    return re.findall(r'#\w+', text)

tweet = "Learning #Python and #RegEx! #coding #developer"
print(extract_hashtags(tweet))
# ['#Python', '#RegEx', '#coding', '#developer']

# ========== EXTRACT @MENTIONS ==========
def extract_mentions(text):
    """Extract all @mentions"""
    return re.findall(r'@\w+', text)

tweet = "Thanks @john and @jane for the help!"
print(extract_mentions(tweet))
# ['@john', '@@jane']

# ========== DATE EXTRACTION ==========
def extract_dates(text):
    """Extract dates in various formats"""
    patterns = [
        r'\d{1,2}/\d{1,2}/\d{4}',           # MM/DD/YYYY
        r'\d{4}-\d{2}-\d{2}',               # YYYY-MM-DD
        r'\d{1,2}-\d{1,2}-\d{4}',           # MM-DD-YYYY
        r'[A-Z][a-z]{2} \d{1,2}, \d{4}',   # Jan 15, 2024
    ]
    
    dates = []
    for pattern in patterns:
        dates.extend(re.findall(pattern, text))
    return dates

text = "Meeting on 12/25/2024 or 2024-06-15. Also Jan 1, 2025"
print(extract_dates(text))
# ['12/25/2024', '2024-06-15', 'Jan 1, 2025']

# ========== FILE EXTENSION EXTRACTION ==========
def get_file_extension(filename):
    """Extract file extension"""
    match = re.search(r'\.([a-zA-Z0-9]+)$', filename)
    return match.group(1) if match else None

print(get_file_extension("document.pdf"))      # "pdf"
print(get_file_extension("photo.jpg"))         # "jpg"
print(get_file_extension("archive.tar.gz"))    # "gz"

# ========== CLEAN WHITESPACE ==========
def clean_whitespace(text):
    """Remove extra whitespace while preserving structure"""
    # Remove leading/trailing whitespace
    text = text.strip()
    # Replace multiple spaces with single space
    text = re.sub(r' +', ' ', text)
    # Replace multiple newlines with double newline
    text = re.sub(r'\n\n+', '\n\n', text)
    return text

messy = """
Hello    world!

This   has    too     many    spaces.


And    too    many    newlines.
"""
print(clean_whitespace(messy))

# ========== PARSE LOG FILES ==========
def parse_log_entry(log_line):
    """Parse Apache-style log entry"""
    pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'
    match = re.search(pattern, log_line)
    
    if match:
        return {
            'ip': match.group(1),
            'timestamp': match.group(2),
            'request': match.group(3),
            'status': int(match.group(4)),
            'size': int(match.group(5))
        }
    return None

log = '192.168.1.1 - - [24/Oct/2025:14:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234'
print(parse_log_entry(log))
# {'ip': '192.168.1.1', 'timestamp': '24/Oct/2025:14:30:45 +0000', ...}
```

## COMPLETE FUNCTIONAL PROGRAMMING GUIDE


### Lambda Functions - Anonymous Functions

```python
# ========== BASIC LAMBDA SYNTAX ==========
# lambda parameters: expression

# Regular function
def add(a, b):
    return a + b

# Lambda equivalent (anonymous function)
add_lambda = lambda a, b: a + b

print(add(5, 3))        # 8
print(add_lambda(5, 3)) # 8

# ========== SINGLE PARAMETER LAMBDA ==========
square = lambda x: x ** 2
cube = lambda x: x ** 3
double = lambda x: x * 2

print(square(5))  # 25
print(cube(3))    # 27
print(double(7))  # 14

# ========== MULTIPLE PARAMETERS ==========
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else None
power = lambda base, exp: base ** exp

print(multiply(4, 5))   # 20
print(divide(10, 2))    # 5.0
print(power(2, 8))      # 256

# ========== LAMBDA WITH CONDITIONALS (TERNARY) ==========
# Syntax: value_if_true if condition else value_if_false

is_even = lambda x: "even" if x % 2 == 0 else "odd"
max_value = lambda a, b: a if a > b else b
sign = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"

print(is_even(4))        # "even"
print(max_value(10, 5))  # 10
print(sign(-5))          # "negative"

# Grade calculator
grade = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(grade(85))  # "B"

# ========== LAMBDA IN SORTING ==========
students = [
    {"name": "Alice", "grade": 85, "age": 20},
    {"name": "Bob", "grade": 92, "age": 22},
    {"name": "Charlie", "grade": 78, "age": 21}
]

# Sort by grade (descending)
by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
print([s["name"] for s in by_grade])  # ['Bob', 'Alice', 'Charlie']

# Sort by name
by_name = sorted(students, key=lambda s: s["name"])
print([s["name"] for s in by_name])  # ['Alice', 'Bob', 'Charlie']

# Sort by multiple criteria (grade desc, then name asc)
multi_sort = sorted(students, key=lambda s: (-s["grade"], s["name"]))

# Sort strings by length
words = ["python", "is", "awesome", "programming"]
by_length = sorted(words, key=lambda w: len(w))
print(by_length)  # ['is', 'python', 'awesome', 'programming']

# Sort tuples by second element
pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_pairs = sorted(pairs, key=lambda x: x[^16_1])
print(sorted_pairs)  # [(2, 'a'), (1, 'b'), (3, 'c')]

# ========== LAMBDA WITH MIN/MAX ==========
numbers = [10, 5, 8, 15, 3]

# Find min absolute value
min_abs = min(numbers, key=lambda x: abs(x))

# Find longest string
words = ["cat", "elephant", "dog", "butterfly"]
longest = max(words, key=lambda w: len(w))
print(longest)  # "butterfly"

# Find student with highest GPA
students = [
    {"name": "Alice", "gpa": 3.8},
    {"name": "Bob", "gpa": 3.9},
    {"name": "Charlie", "gpa": 3.7}
]
top_student = max(students, key=lambda s: s["gpa"])
print(top_student["name"])  # "Bob"

# ========== LAMBDA AS FUNCTION ARGUMENT ==========
def apply_operation(x, y, operation):
    """Apply operation function to x and y"""
    return operation(x, y)

# Pass lambda as argument
result = apply_operation(10, 5, lambda a, b: a + b)
print(result)  # 15

result = apply_operation(10, 5, lambda a, b: a * b)
print(result)  # 50

# ========== LAMBDA IN FILTER (Preview) ==========
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# ========== LAMBDA LIMITATIONS ==========
# Lambda can only contain EXPRESSIONS, not STATEMENTS
# ❌ No assignments
# invalid = lambda x: y = x + 1  # SyntaxError

# ❌ No multiple lines
# invalid = lambda x:
#     result = x * 2
#     return result

# ❌ No print statements (print is a function, but not recommended)
# works_but_bad = lambda x: print(x)  # Not recommended

# ✅ Use regular functions for complex logic
def complex_calculation(x):
    if x < 0:
        result = abs(x) * 2
    else:
        result = x ** 2
    return result

# ========== WHEN TO USE LAMBDA ==========
# ✅ Good uses:
# - Short, simple operations
# - Sorting keys
# - Map/filter operations
# - One-time use functions

# ❌ Bad uses:
# - Complex logic
# - Multiple operations
# - Reused functions (use def instead)
# - When readability suffers

# Bad (hard to read)
complex_lambda = lambda x: x ** 2 if x > 0 else abs(x) * 2 if x < -10 else x

# Good (clear and readable)
def process_number(x):
    if x > 0:
        return x ** 2
    elif x < -10:
        return abs(x) * 2
    else:
        return x
```


***

### Map Function - Transform Collections

```python
# ========== MAP BASICS ==========
# map(function, iterable)
# Applies function to every element

numbers = [1, 2, 3, 4, 5]

# Traditional approach
def double_all(nums):
    result = []
    for num in nums:
        result.append(num * 2)
    return result

print(double_all(numbers))  # [2, 4, 6, 8, 10]

# Using map with lambda
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Using map with regular function
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# ========== MAP WITH MULTIPLE OPERATIONS ==========
numbers = [1, 2, 3, 4, 5]

# Square all numbers
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Convert to strings
strings = list(map(str, numbers))
print(strings)  # ['1', '2', '3', '4', '5']

# Convert to absolute values
negatives = [-1, -2, 3, -4, 5]
absolutes = list(map(abs, negatives))
print(absolutes)  # [1, 2, 3, 4, 5]

# Round to 2 decimals
prices = [19.999, 29.456, 39.123]
rounded = list(map(lambda x: round(x, 2), prices))
print(rounded)  # [20.0, 29.46, 39.12]

# ========== MAP WITH STRINGS ==========
words = ["hello", "world", "python"]

# Convert to uppercase
uppercase = list(map(str.upper, words))
print(uppercase)  # ['HELLO', 'WORLD', 'PYTHON']

# Get length of each word
lengths = list(map(len, words))
print(lengths)  # [5, 5, 6]

# Capitalize first letter
capitalized = list(map(str.capitalize, words))
print(capitalized)  # ['Hello', 'World', 'Python']

# ========== MAP WITH COMPLEX DATA ==========
users = [
    {"name": "ALICE", "age": 25, "email": "ALICE@EMAIL.COM"},
    {"name": "BOB", "age": 30, "email": "BOB@EMAIL.COM"}
]

# Normalize user data
def normalize_user(user):
    return {
        "name": user["name"].title(),
        "age": user["age"],
        "email": user["email"].lower(),
        "username": user["name"].split()[^16_0].lower()
    }

normalized = list(map(normalize_user, users))
print(normalized)
# [{'name': 'Alice', 'age': 25, 'email': 'alice@email.com', 'username': 'alice'}, ...]

# Extract specific field
names = list(map(lambda u: u["name"], users))
print(names)  # ['ALICE', 'BOB']

emails = list(map(lambda u: u["email"].lower(), users))
print(emails)  # ['alice@email.com', 'bob@email.com']

# ========== MAP WITH MULTIPLE ITERABLES ==========
# map can take multiple iterables
numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20, 30, 40]

# Add corresponding elements
sums = list(map(lambda x, y: x + y, numbers1, numbers2))
print(sums)  # [11, 22, 33, 44]

# Multiply corresponding elements
products = list(map(lambda x, y: x * y, numbers1, numbers2))
print(products)  # [10, 40, 90, 160]

# Three iterables
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
result = list(map(lambda x, y, z: x + y + z, a, b, c))
print(result)  # [12, 15, 18]

# ========== MAP WITH TYPE CONVERSION ==========
# String numbers to integers
string_nums = ["1", "2", "3", "4", "5"]
integers = list(map(int, string_nums))
print(integers)  # [1, 2, 3, 4, 5]

# Integers to floats
integers = [1, 2, 3, 4, 5]
floats = list(map(float, integers))
print(floats)  # [1.0, 2.0, 3.0, 4.0, 5.0]

# Parse price strings
price_strings = ["$19.99", "$29.50", "$39.00"]
prices = list(map(lambda p: float(p.strip("$")), price_strings))
print(prices)  # [19.99, 29.5, 39.0]

# ========== MAP RETURNS ITERATOR ==========
# map() returns an iterator, not a list
# Must convert to list to see results

numbers = [1, 2, 3]
result = map(lambda x: x * 2, numbers)
print(result)  # <map object at 0x...>
print(list(result))  # [2, 4, 6]

# Iterator is consumed after use
result = map(lambda x: x * 2, numbers)
print(list(result))  # [2, 4, 6]
print(list(result))  # [] - empty! Iterator exhausted

# ========== PRACTICAL MAP EXAMPLES ==========

# Calculate tax for all prices
prices = [10.00, 20.00, 30.00, 40.00]
with_tax = list(map(lambda p: p * 1.07, prices))
print(with_tax)  # [10.7, 21.4, 32.1, 42.8]

# Format phone numbers
numbers = ["5551234", "5555678", "5559012"]
formatted = list(map(lambda n: f"{n[:3]}-{n[3:]}", numbers))
print(formatted)  # ['555-1234', '555-5678', '555-9012']

# Parse CSV data
csv_rows = ["John,25,NYC", "Jane,30,LA", "Bob,35,Chicago"]
parsed = list(map(lambda row: row.split(","), csv_rows))
print(parsed)  # [['John', '25', 'NYC'], ['Jane', '30', 'LA'], ...]

# Calculate area of circles
radii = [1, 2, 3, 4, 5]
areas = list(map(lambda r: 3.14159 * r ** 2, radii))
print(areas)  # [3.14159, 12.56636, 28.27431, ...]

# Grade calculator
scores = [85, 92, 78, 95, 88]
grades = list(map(
    lambda s: "A" if s >= 90 else "B" if s >= 80 else "C",
    scores
))
print(grades)  # ['B', 'A', 'C', 'A', 'B']
```


***

### Filter Function - Select Elements

```python
# ========== FILTER BASICS ==========
# filter(function, iterable)
# Keeps elements where function returns True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional approach
def get_evens(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result

print(get_evens(numbers))  # [2, 4, 6, 8, 10]

# Using filter with lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Using filter with function
def is_even(x):
    return x % 2 == 0

evens = list(filter(is_even, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# ========== FILTER WITH DIFFERENT CONDITIONS ==========
numbers = list(range(1, 21))

# Get odd numbers
odds = list(filter(lambda x: x % 2 == 1, numbers))
print(odds)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Numbers greater than 10
above_10 = list(filter(lambda x: x > 10, numbers))
print(above_10)  # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Numbers divisible by 3
div_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(div_by_3)  # [3, 6, 9, 12, 15, 18]

# Numbers in range
in_range = list(filter(lambda x: 5 <= x <= 15, numbers))
print(in_range)  # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# ========== FILTER WITH STRINGS ==========
words = ["apple", "application", "banana", "app", "orange", "appreciate"]

# Words starting with 'a'
starts_with_a = list(filter(lambda w: w.startswith('a'), words))
print(starts_with_a)  # ['apple', 'application', 'app', 'appreciate']

# Words longer than 5 characters
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)  # ['application', 'banana', 'orange', 'appreciate']

# Words containing 'app'
contains_app = list(filter(lambda w: 'app' in w, words))
print(contains_app)  # ['apple', 'application', 'app', 'appreciate']

# ========== FILTER WITH COMPLEX DATA ==========
students = [
    {"name": "Alice", "grade": 85, "age": 20, "passed": True},
    {"name": "Bob", "grade": 92, "age": 22, "passed": True},
    {"name": "Charlie", "grade": 58, "age": 21, "passed": False},
    {"name": "David", "grade": 78, "age": 23, "passed": True}
]

# Students who passed
passed = list(filter(lambda s: s["passed"], students))
print([s["name"] for s in passed])  # ['Alice', 'Bob', 'David']

# Students with grade >= 80
high_achievers = list(filter(lambda s: s["grade"] >= 80, students))
print([s["name"] for s in high_achievers])  # ['Alice', 'Bob']

# Students younger than 22
young = list(filter(lambda s: s["age"] < 22, students))
print([s["name"] for s in young])  # ['Alice', 'Charlie']

# Multiple conditions (AND)
top_young = list(filter(
    lambda s: s["grade"] >= 80 and s["age"] <= 21,
    students
))
print([s["name"] for s in top_young])  # ['Alice']

# ========== FILTER WITH MULTIPLE CONDITIONS ==========
numbers = list(range(1, 101))

# Even AND divisible by 5
even_div_5 = list(filter(lambda x: x % 2 == 0 and x % 5 == 0, numbers))
print(even_div_5)  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Divisible by 3 OR 5
div_3_or_5 = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, numbers))

# NOT divisible by 2 or 3
not_div_2_or_3 = list(filter(
    lambda x: x % 2 != 0 and x % 3 != 0,
    numbers
))

# ========== FILTER NONE VALUES ==========
# filter(None, iterable) removes falsy values

mixed = [0, 1, "", "hello", None, False, True, [], [1, 2], {}, {"a": 1}]
truthy = list(filter(None, mixed))
print(truthy)  # [1, 'hello', True, [1, 2], {'a': 1}]

# Custom function to remove None
data = [1, None, 2, None, 3, 4, None, 5]
no_none = list(filter(lambda x: x is not None, data))
print(no_none)  # [1, 2, 3, 4, 5]

# ========== PRACTICAL FILTER EXAMPLES ==========

# Filter valid emails
emails = ["user@test.com", "invalid", "admin@site.org", "bad@", "@bad.com"]
valid = list(filter(lambda e: "@" in e and "." in e.split("@")[^16_1], emails))
print(valid)  # ['user@test.com', 'admin@site.org']

# Filter available products
products = [
    {"name": "Laptop", "price": 999, "in_stock": True},
    {"name": "Mouse", "price": 25, "in_stock": False},
    {"name": "Keyboard", "price": 75, "in_stock": True}
]
available = list(filter(lambda p: p["in_stock"], products))
print([p["name"] for p in available])  # ['Laptop', 'Keyboard']

# Filter by price range
affordable = list(filter(lambda p: p["price"] < 100, products))
print([p["name"] for p in affordable])  # ['Mouse', 'Keyboard']

# Filter transactions
transactions = [
    {"amount": 100, "type": "credit", "valid": True},
    {"amount": -50, "type": "debit", "valid": False},
    {"amount": 75, "type": "credit", "valid": True},
    {"amount": 200, "type": "debit", "valid": True}
]

# Valid credit transactions only
valid_credits = list(filter(
    lambda t: t["valid"] and t["type"] == "credit",
    transactions
))

# Transactions over $50
large = list(filter(lambda t: abs(t["amount"]) > 50, transactions))

# ========== FILTER VS LIST COMPREHENSION ==========
numbers = list(range(1, 21))

# Using filter
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))

# Using list comprehension (more Pythonic)
evens_comp = [x for x in numbers if x % 2 == 0]

# Both produce same result
print(evens_filter == evens_comp)  # True

# List comprehension is generally preferred in Python
# More readable and flexible
```


***

### List Comprehensions - The Pythonic Way

```python
# ========== BASIC LIST COMPREHENSION ==========
# Syntax: [expression for item in iterable]

# Traditional loop
result = []
for x in range(10):
    result.append(x ** 2)
print(result)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension
squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ========== WITH CONDITION (FILTER) ==========
# Syntax: [expression for item in iterable if condition]

numbers = list(range(1, 21))

# Only even numbers
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Only odd numbers
odds = [x for x in numbers if x % 2 == 1]

# Numbers divisible by 3
div_3 = [x for x in numbers if x % 3 == 0]
print(div_3)  # [3, 6, 9, 12, 15, 18]

# ========== TRANSFORM AND FILTER ==========
# Combine map + filter in one line

numbers = list(range(1, 11))

# Double only even numbers
doubled_evens = [x * 2 for x in numbers if x % 2 == 0]
print(doubled_evens)  # [4, 8, 12, 16, 20]

# Square only numbers > 5
squared_large = [x ** 2 for x in numbers if x > 5]
print(squared_large)  # [36, 49, 64, 81, 100]

# ========== WITH IF-ELSE (TERNARY) ==========
# Syntax: [expr_if_true if condition else expr_if_false for item in iterable]

numbers = list(range(1, 11))

# Label as even or odd
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', ...]

# Convert negative to positive, keep positive
absolutes = [x if x >= 0 else -x for x in [-1, 2, -3, 4, -5]]
print(absolutes)  # [1, 2, 3, 4, 5]

# ========== NESTED COMPREHENSIONS ==========
# Create 2D matrix
matrix = [[i + j for j in range(3)] for i in range(3)]
print(matrix)
# [[0, 1, 2],
#  [1, 2, 3],
#  [2, 3, 4]]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6]

# ========== STRING OPERATIONS ==========
words = ["hello", "world", "python", "programming"]

# Uppercase all
upper = [w.upper() for w in words]
print(upper)  # ['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']

# Get first letter
first_letters = [w[^16_0] for w in words]
print(first_letters)  # ['h', 'w', 'p', 'p']

# Filter long words
long_words = [w for w in words if len(w) > 5]
print(long_words)  # ['python', 'programming']

# Capitalize words starting with 'p'
capitalized = [w.capitalize() if w.startswith('p') else w for w in words]
print(capitalized)  # ['hello', 'world', 'Python', 'Programming']

# ========== COMPLEX DATA STRUCTURES ==========
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 95}
]

# Extract names
names = [s["name"] for s in students]
print(names)  # ['Alice', 'Bob', 'Charlie', 'David']

# Names of students with grade >= 90
high_achievers = [s["name"] for s in students if s["grade"] >= 90]
print(high_achievers)  # ['Bob', 'David']

# Add letter grade
with_letter = [
    {**s, "letter": "A" if s["grade"] >= 90 else "B" if s["grade"] >= 80 else "C"}
    for s in students
]

# ========== DICTIONARY COMPREHENSION ==========
# Syntax: {key_expr: value_expr for item in iterable}

# Square numbers
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Invert dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}

# Filter dictionary
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
high_scores = {name: score for name, score in scores.items() if score >= 90}
print(high_scores)  # {'Bob': 92, 'David': 95}

# ========== SET COMPREHENSION ==========
# Syntax: {expression for item in iterable}

# Unique squares
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x**2 for x in numbers}
print(unique_squares)  # {1, 4, 9, 16}

# Unique first letters
words = ["apple", "application", "banana", "apricot"]
first_letters = {w[^16_0] for w in words}
print(first_letters)  # {'a', 'b'}

# ========== PRACTICAL EXAMPLES ==========

# Calculate tax for prices
prices = [10, 20, 30, 40, 50]
with_tax = [p * 1.07 for p in prices]
print(with_tax)  # [10.7, 21.4, 32.1, 42.8, 53.5]

# Extract domain from emails
emails = ["user@test.com", "admin@company.org", "info@site.net"]
domains = [e.split("@")[^16_1] for e in emails]
print(domains)  # ['test.com', 'company.org', 'site.net']

# Parse CSV
csv_data = ["John,25,NYC", "Jane,30,LA", "Bob,35,Chicago"]
parsed = [row.split(",") for row in csv_data]
print(parsed)  # [['John', '25', 'NYC'], ...]

# FizzBuzz using list comprehension
fizzbuzz = [
    "FizzBuzz" if i % 15 == 0 else
    "Fizz" if i % 3 == 0 else
    "Buzz" if i % 5 == 0 else
    i
    for i in range(1, 21)
]
print(fizzbuzz)

# ========== PERFORMANCE COMPARISON ==========
import time

# Large dataset
numbers = range(1000000)

# List comprehension (fastest)
start = time.time()
result = [x * 2 for x in numbers]
comp_time = time.time() - start

# Map (fast)
start = time.time()
result = list(map(lambda x: x * 2, numbers))
map_time = time.time() - start

# Traditional loop (slowest)
start = time.time()
result = []
for x in numbers:
    result.append(x * 2)
loop_time = time.time() - start

print(f"Comprehension: {comp_time:.4f}s")
print(f"Map: {map_time:.4f}s")
print(f"Loop: {loop_time:.4f}s")

# List comprehensions are generally fastest and most Pythonic!
```


## COMPLETE APIs \& HTTP REQUESTS GUIDE

### API Fundamentals

```python
import requests

# ========== WHAT IS AN API? ==========
"""
API: Application Programming Interface
- Allows programs to communicate with each other
- HTTP methods for CRUD operations:
  - POST   → CREATE (add data to database)
  - GET    → READ (retrieve data from database)
  - PUT    → UPDATE (modify existing data)
  - DELETE → REMOVE (delete data from database)
"""

# ========== MAKING A BASIC GET REQUEST ==========
def send_request():
    """
    Basic GET request to JSONPlaceholder API
    Steps:
    1. Define URL and endpoint
    2. Make the request
    3. Check status code
    4. Parse JSON data
    """
    # Step 1: URL and endpoint
    url = "https://jsonplaceholder.typicode.com"
    endpoint = "/posts"
    
    # Step 2: Make GET request
    response = requests.get(url + endpoint)
    
    # Step 3: Check status code
    print(f"Status Code: {response.status_code}")
    # 200 = success, 404 = not found, 500 = server error
    
    # Step 4: Parse JSON to Python dict/list
    data = response.json()
    
    # Display first post
    if data:
        first_post = data[^17_0]
        print(f"\nFirst Post:")
        print(f"ID: {first_post['id']}")
        print(f"Title: {first_post['title']}")
        print(f"Body: {first_post['body']}")
    
    return data

# ========== GET REQUEST WITH SPECIFIC ID ==========
def get_post_by_id(post_id):
    """Fetch a specific post"""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        post = response.json()
        print(f"Post {post_id}:")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        return post
    else:
        print(f"Error: {response.status_code}")
        return None

# ========== POST REQUEST - CREATE DATA ==========
def create_new_post():
    """
    POST request to create new data
    Status 201 = Created successfully
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Request body - data to send
    new_post = {
        "title": "My Amazing Post",
        "body": "This is the content of my post",
        "userId": 1
    }
    
    # Send POST request with JSON data
    response = requests.post(url, json=new_post)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 201:  # 201 = Created
        print("Post created successfully!")
        created_post = response.json()
        print(f"New Post ID: {created_post['id']}")
        print(f"Title: {created_post['title']}")
        return created_post
    else:
        print("Failed to create post")
        return None

# ========== PUT REQUEST - UPDATE DATA ==========
def update_post(post_id):
    """
    PUT request to update existing data
    Replaces entire resource
    """
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    updated_data = {
        "id": post_id,
        "title": "Updated Title",
        "body": "This content has been updated",
        "userId": 1
    }
    
    response = requests.put(url, json=updated_data)
    
    if response.status_code == 200:
        print("Post updated successfully!")
        updated_post = response.json()
        print(f"Updated Title: {updated_post['title']}")
        return updated_post
    else:
        print(f"Update failed: {response.status_code}")
        return None

# ========== PATCH REQUEST - PARTIAL UPDATE ==========
def patch_post(post_id):
    """
    PATCH request - update only specific fields
    """
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    # Only update title
    partial_update = {
        "title": "Partially Updated Title"
    }
    
    response = requests.patch(url, json=partial_update)
    
    if response.status_code == 200:
        print("Post patched successfully!")
        return response.json()

# ========== DELETE REQUEST - REMOVE DATA ==========
def delete_post(post_id):
    """
    DELETE request to remove data
    Status 200 or 204 = Success
    """
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    response = requests.delete(url)
    
    if response.status_code in [200, 204]:
        print(f"Post {post_id} deleted successfully!")
        return True
    else:
        print(f"Delete failed: {response.status_code}")
        return False

# ========== QUERY PARAMETERS ==========
def query_params():
    """
    Query parameters: Send data through URL
    Format: ?key1=value1&key2=value2
    Used for filtering, sorting, pagination
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Method 1: Add to URL directly
    response = requests.get(url + "?userId=1")
    
    # Method 2: Use params dictionary (RECOMMENDED)
    params = {
        "userId": 1,
        "_limit": 5  # Limit to 5 results
    }
    response = requests.get(url, params=params)
    
    print(f"Status: {response.status_code}")
    posts = response.json()
    print(f"Received {len(posts)} posts")
    
    for post in posts:
        print(f"- {post['title']}")
    
    return posts

# ========== HEADERS ==========
def send_with_headers():
    """
    Headers: Additional information about request
    Common uses:
    - Content type
    - Authorization tokens
    - User agent
    - Custom metadata
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "MyPythonApp/1.0",
        "Accept": "application/json"
        # "Authorization": "Bearer <token>"  # For authenticated APIs
    }
    
    response = requests.get(url, headers=headers)
    
    print(f"Status: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    
    return response.json()

# ========== ERROR HANDLING ==========
def safe_api_request(url):
    """
    Proper error handling for API requests
    """
    try:
        # Make request with timeout
        response = requests.get(url, timeout=5)
        
        # Raise exception for bad status codes
        response.raise_for_status()
        
        # Try to parse JSON
        data = response.json()
        return data
        
    except requests.exceptions.Timeout:
        print("Request timed out!")
        return None
    
    except requests.exceptions.ConnectionError:
        print("Connection error - check internet!")
        return None
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return None
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    
    except ValueError:
        print("Invalid JSON response")
        return None

# ========== HTTP STATUS CODES ==========
"""
1xx - Informational
    100 Continue

2xx - Success
    200 OK - Request successful
    201 Created - Resource created successfully
    204 No Content - Success but no data to return

3xx - Redirection
    301 Moved Permanently
    302 Found (temporary redirect)

4xx - Client Error (Your mistake)
    400 Bad Request - Invalid request format/data
    401 Unauthorized - Authentication required
    403 Forbidden - Authenticated but no permission
    404 Not Found - Resource doesn't exist
    429 Too Many Requests - Rate limit exceeded

5xx - Server Error (Their problem)
    500 Internal Server Error - Something broke on server
    502 Bad Gateway - Server got invalid response
    503 Service Unavailable - Temporarily down
    504 Gateway Timeout - Server took too long
"""

def check_status_code(response):
    """Handle different status codes"""
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 201:
        print("Resource created!")
        return response.json()
    elif response.status_code == 204:
        print("Success - no content")
        return None
    elif response.status_code == 400:
        print("Bad request - check your data")
        return None
    elif response.status_code == 401:
        print("Unauthorized - need to log in")
        return None
    elif response.status_code == 404:
        print("Not found")
        return None
    elif response.status_code == 429:
        print("Too many requests - slow down!")
        return None
    elif response.status_code >= 500:
        print("Server error - try again later")
        return None
    else:
        print(f"Unexpected status: {response.status_code}")
        return None

# ========== REAL-WORLD API EXAMPLE: DOG CEO ==========
def get_random_dog():
    """
    Fetch random dog image from Dog CEO API
    Free API, no authentication required
    """
    url = "https://dog.ceo/api/breeds/image/random"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        
        if data["status"] == "success":
            image_url = data["message"]
            print(f"Random dog image: {image_url}")
            return image_url
        else:
            print("Failed to get dog image")
            return None
            
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_dog_by_breed(breed):
    """Get random image of specific breed"""
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data["message"]
    else:
        print(f"Breed '{breed}' not found")
        return None

# ========== WORKING WITH JSON ==========
def json_operations():
    """
    JSON: JavaScript Object Notation
    Python dict ↔ JSON conversion
    """
    import json
    
    # Python dict to JSON string
    data = {
        "name": "Allan",
        "age": 28,
        "skills": ["Python", "JavaScript", "APIs"]
    }
    
    json_string = json.dumps(data)
    print(f"JSON String: {json_string}")
    
    # JSON string to Python dict
    parsed = json.loads(json_string)
    print(f"Parsed: {parsed}")
    
    # Pretty print JSON
    pretty = json.dumps(data, indent=2)
    print(f"Pretty JSON:\n{pretty}")
    
    # Save to file
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)
    
    # Load from file
    with open("data.json", "r") as f:
        loaded = json.load(f)
    
    return loaded

# ========== PAGINATION ==========
def fetch_all_pages(base_url, max_pages=5):
    """
    Handle paginated API responses
    """
    all_data = []
    page = 1
    
    while page <= max_pages:
        params = {
            "_page": page,
            "_limit": 10
        }
        
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if not data:  # No more data
                break
            all_data.extend(data)
            page += 1
        else:
            print(f"Error on page {page}")
            break
    
    return all_data

# ========== RATE LIMITING ==========
def rate_limited_requests(urls, delay=1):
    """
    Add delay between requests to avoid rate limits
    """
    import time
    
    results = []
    
    for url in urls:
        response = requests.get(url)
        results.append(response.json())
        
        # Wait before next request
        time.sleep(delay)
    
    return results

# ========== ASYNC REQUESTS (ADVANCED) ==========
def concurrent_requests(urls):
    """
    Make multiple requests concurrently
    Faster than sequential requests
    """
    import concurrent.futures
    
    def fetch_url(url):
        try:
            response = requests.get(url, timeout=5)
            return response.json()
        except:
            return None
    
    # Use ThreadPoolExecutor for concurrent requests
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch_url, urls))
    
    return results
```


***

## API AUTHENTICATION - COMPLETE GUIDE


```python
import requests
import base64
from datetime import datetime, timedelta

# ========== AUTHENTICATION TYPES ==========
"""
1. API Key Authentication
   - Simple key in URL or header
   - Example: ?api_key=abc123 or Header: X-API-Key: abc123

2. Token Authentication  
   - POST credentials → receive token
   - Use token in subsequent requests
   - Token expires after time period

3. OAuth 2.0 (Spotify uses this)
   - More secure, industry standard
   - Multiple flows: client credentials, authorization code, etc.
"""

# ========== SPOTIFY API AUTHENTICATION ==========

# Store credentials (NEVER commit to GitHub!)
# Put in separate file: creds.py
"""
creds.py:
client_id = "your_client_id_here"
client_secret = "your_client_secret_here"
"""

# For this example, using placeholder
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

def get_spotify_token():
    """
    Get Spotify API access token using Client Credentials flow
    
    Steps:
    1. Create credentials string (client_id:client_secret)
    2. Encode to base64 (required by Spotify)
    3. Create authorization header
    4. POST request to token endpoint
    5. Extract and return access token
    """
    
    # Step 1: Combine client ID and secret
    cred_string = f"{client_id}:{client_secret}"
    
    # Step 2: Encode to base64
    # Convert string to bytes
    cred_bytes = cred_string.encode('utf-8')
    # Encode bytes to base64
    cred_b64_bytes = base64.b64encode(cred_bytes)
    # Convert back to string
    cred_b64 = cred_b64_bytes.decode('utf-8')
    
    # Step 3: Create authorization header
    headers = {
        "Authorization": f"Basic {cred_b64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    # Step 4: Create request body
    data = {
        "grant_type": "client_credentials"
    }
    
    # Step 5: POST request to token endpoint
    url = "https://accounts.spotify.com/api/token"
    response = requests.post(url, headers=headers, data=data)
    
    # Step 6: Extract token from response
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data["access_token"]
        expires_in = token_data["expires_in"]  # Seconds until expiration
        
        print(f"Token obtained! Expires in {expires_in} seconds")
        return access_token
    else:
        print(f"Failed to get token: {response.status_code}")
        print(response.json())
        return None

# ========== USING THE ACCESS TOKEN ==========
def search_song(title, token=None):
    """
    Search for a song on Spotify
    Requires access token
    """
    # Get token if not provided
    if token is None:
        token = get_spotify_token()
        if token is None:
            return None
    
    # Spotify search endpoint
    url = "https://api.spotify.com/v1/search"
    
    # Query parameters
    params = {
        "q": title,        # Search query
        "type": "track",   # Search for tracks
        "limit": 1         # Return 1 result
    }
    
    # Headers with Bearer token
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    # Make GET request
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract track info
        if data["tracks"]["items"]:
            track = data["tracks"]["items"][^17_0]
            
            song_info = {
                "name": track["name"],
                "artist": track["artists"][^17_0]["name"],
                "album": track["album"]["name"],
                "duration_ms": track["duration_ms"],
                "preview_url": track["preview_url"],
                "spotify_url": track["external_urls"]["spotify"]
            }
            
            print(f"\nFound: {song_info['name']} by {song_info['artist']}")
            return song_info
        else:
            print("No results found")
            return None
    else:
        print(f"Search failed: {response.status_code}")
        return None

def get_artist_info(artist_name, token=None):
    """Get information about an artist"""
    if token is None:
        token = get_spotify_token()
    
    url = "https://api.spotify.com/v1/search"
    params = {"q": artist_name, "type": "artist", "limit": 1}
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data["artists"]["items"]:
            artist = data["artists"]["items"][^17_0]
            return {
                "name": artist["name"],
                "genres": artist["genres"],
                "followers": artist["followers"]["total"],
                "popularity": artist["popularity"]
            }
    return None

# ========== TOKEN CACHING ==========
class SpotifyClient:
    """
    Reusable Spotify client with token caching
    Automatically refreshes expired tokens
    """
    
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        self.token_expires_at = None
    
    def get_token(self):
        """Get token, refresh if expired"""
        now = datetime.now()
        
        # Check if token exists and is still valid
        if self.token and self.token_expires_at and now < self.token_expires_at:
            print("Using cached token")
            return self.token
        
        # Get new token
        print("Fetching new token...")
        cred_string = f"{self.client_id}:{self.client_secret}"
        cred_b64 = base64.b64encode(cred_string.encode()).decode()
        
        headers = {"Authorization": f"Basic {cred_b64}"}
        data = {"grant_type": "client_credentials"}
        
        response = requests.post(
            "https://accounts.spotify.com/api/token",
            headers=headers,
            data=data
        )
        
        if response.status_code == 200:
            token_data = response.json()
            self.token = token_data["access_token"]
            expires_in = token_data["expires_in"]
            self.token_expires_at = now + timedelta(seconds=expires_in - 60)
            return self.token
        else:
            print(f"Token request failed: {response.status_code}")
            return None
    
    def search_track(self, query):
        """Search for track with auto-token management"""
        token = self.get_token()
        if not token:
            return None
        
        url = "https://api.spotify.com/v1/search"
        params = {"q": query, "type": "track", "limit": 5}
        headers = {"Authorization": f"Bearer {token}"}
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()["tracks"]["items"]
        return None

# Usage
client = SpotifyClient(client_id, client_secret)
tracks = client.search_track("Bohemian Rhapsody")

# ========== BASE64 ENCODING EXPLAINED ==========
def explain_base64():
    """
    Base64: Encode binary data as text
    Used to safely transmit credentials
    """
    # Original text
    text = "username:password"
    print(f"Original: {text}")
    
    # Step 1: Convert to bytes
    text_bytes = text.encode('utf-8')
    print(f"Bytes: {text_bytes}")
    
    # Step 2: Encode to base64 bytes
    encoded_bytes = base64.b64encode(text_bytes)
    print(f"Encoded bytes: {encoded_bytes}")
    
    # Step 3: Convert to string
    encoded_string = encoded_bytes.decode('utf-8')
    print(f"Base64 string: {encoded_string}")
    
    # Decode back
    decoded_bytes = base64.b64decode(encoded_bytes)
    decoded_string = decoded_bytes.decode('utf-8')
    print(f"Decoded: {decoded_string}")
    
    return encoded_string

# Note: Base64 is NOT encryption! It's encoding.
# Anyone can decode it. Always use HTTPS!
```


## POKEMON GAME - COMPLETE CAPSTONE PROJECT


This project integrates: **APIs, OOP, Data Structures, Error Handling, JSON parsing**

### Complete Pokemon Game Implementation

```python
import requests
import json
from typing import Optional, List, Dict

# ========== POKEMON CLASS (OOP) ==========
class Pokemon:
    """
    Represents a single Pokemon
    Demonstrates: OOP, Encapsulation, Methods
    """
    
    def __init__(self, name: str, pokemon_id: int, hp: int, 
                 attack: int, defense: int, sprite_url: str, 
                 types: List[str], abilities: List[str]):
        # Public attributes
        self.name = name.capitalize()
        self.id = pokemon_id
        
        # Battle stats
        self.max_hp = hp
        self.current_hp = hp
        self.attack = attack
        self.defense = defense
        
        # Visual and metadata
        self.sprite_url = sprite_url
        self.types = types
        self.abilities = abilities
        
        # Status
        self.is_fainted = False
        self.level = 5  # Starting level
        self.experience = 0
    
    def display_info(self):
        """Display detailed Pokemon information"""
        print(f"\n{'='*50}")
        print(f"{self.name.upper()} - Level {self.level}")
        print(f"{'='*50}")
        print(f"ID: #{self.id}")
        print(f"Type(s): {', '.join(self.types)}")
        print(f"HP: {self.current_hp}/{self.max_hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Abilities: {', '.join(self.abilities)}")
        print(f"Status: {'Fainted' if self.is_fainted else 'Active'}")
        print(f"Sprite: {self.sprite_url}")
        print(f"{'='*50}\n")
    
    def take_damage(self, damage: int):
        """Pokemon takes damage in battle"""
        actual_damage = max(1, damage - self.defense // 2)
        self.current_hp -= actual_damage
        
        if self.current_hp <= 0:
            self.current_hp = 0
            self.is_fainted = True
            print(f"{self.name} fainted!")
        
        return actual_damage
    
    def heal(self, amount: int = None):
        """Restore HP"""
        if amount is None:
            amount = self.max_hp
        
        self.current_hp = min(self.max_hp, self.current_hp + amount)
        self.is_fainted = False
        print(f"{self.name} restored to {self.current_hp}/{self.max_hp} HP")
    
    def gain_experience(self, exp: int):
        """Gain experience and potentially level up"""
        self.experience += exp
        exp_needed = self.level * 100
        
        if self.experience >= exp_needed:
            self.level_up()
    
    def level_up(self):
        """Level up and increase stats"""
        self.level += 1
        self.max_hp += 5
        self.current_hp = self.max_hp
        self.attack += 2
        self.defense += 2
        
        print(f"\n🎉 {self.name} leveled up to Level {self.level}!")
        print(f"Stats increased: HP +5, ATK +2, DEF +2")
    
    def __repr__(self):
        return f"Pokemon({self.name}, Level {self.level}, HP: {self.current_hp}/{self.max_hp})"
    
    def __str__(self):
        return f"{self.name} (Lv.{self.level})"


# ========== API HELPER FUNCTIONS ==========
def get_pokemon_data(identifier: str) -> Optional[Dict]:
    """
    Fetch Pokemon data from PokeAPI
    
    Args:
        identifier: Pokemon name or ID number
    
    Returns:
        Dictionary with Pokemon data or None if failed
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{identifier.lower()}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract and structure data
        pokemon_data = {
            "name": data["name"],
            "id": data["id"],
            "hp": data["stats"][^18_0]["base_stat"],
            "attack": data["stats"][^18_1]["base_stat"],
            "defense": data["stats"][^18_2]["base_stat"],
            "sprite_url": data["sprites"]["front_default"],
            "types": [t["type"]["name"] for t in data["types"]],
            "abilities": [a["ability"]["name"] for a in data["abilities"][:3]]
        }
        
        return pokemon_data
        
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"Pokemon '{identifier}' not found!")
        else:
            print(f"HTTP Error: {e}")
        return None
    
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None
    
    except (KeyError, ValueError) as e:
        print(f"Error parsing data: {e}")
        return None


def create_pokemon_from_api(identifier: str) -> Optional[Pokemon]:
    """
    Fetch data and create Pokemon object
    
    Args:
        identifier: Pokemon name or ID
    
    Returns:
        Pokemon object or None
    """
    data = get_pokemon_data(identifier)
    
    if data:
        pokemon = Pokemon(
            name=data["name"],
            pokemon_id=data["id"],
            hp=data["hp"],
            attack=data["attack"],
            defense=data["defense"],
            sprite_url=data["sprite_url"],
            types=data["types"],
            abilities=data["abilities"]
        )
        return pokemon
    
    return None


def get_random_pokemon() -> Optional[Pokemon]:
    """Get a random Pokemon (ID 1-151 for Gen 1)"""
    import random
    random_id = random.randint(1, 151)
    return create_pokemon_from_api(str(random_id))


# ========== PLAYER CLASS (OOP & DATA STRUCTURES) ==========
class Player:
    """
    Represents the player/trainer
    Demonstrates: OOP, Lists, File I/O
    """
    
    def __init__(self, name: str):
        self.name = name
        self.team: List[Pokemon] = []  # List of Pokemon
        self.max_team_size = 6
        self.pokedex: Dict[int, Pokemon] = {}  # All caught Pokemon
        self.battles_won = 0
        self.battles_lost = 0
    
    def add_pokemon(self, pokemon: Pokemon) -> bool:
        """Add Pokemon to team"""
        if len(self.team) >= self.max_team_size:
            print(f"Team is full! Maximum {self.max_team_size} Pokemon.")
            return False
        
        self.team.append(pokemon)
        self.pokedex[pokemon.id] = pokemon
        print(f"\n✅ {pokemon.name} added to your team!")
        return True
    
    def remove_pokemon(self, index: int) -> bool:
        """Remove Pokemon from team by index"""
        if 0 <= index < len(self.team):
            removed = self.team.pop(index)
            print(f"{removed.name} removed from team")
            return True
        else:
            print("Invalid Pokemon index")
            return False
    
    def display_team(self):
        """Show all Pokemon in team"""
        if not self.team:
            print("\nYour team is empty!")
            return
        
        print(f"\n{'='*60}")
        print(f"{self.name}'s Team".center(60))
        print(f"{'='*60}")
        
        for i, pokemon in enumerate(self.team, 1):
            status = "💀 Fainted" if pokemon.is_fainted else "✅ Active"
            print(f"{i}. {pokemon.name} (Lv.{pokemon.level}) - "
                  f"HP: {pokemon.current_hp}/{pokemon.max_hp} - {status}")
            print(f"   Type: {', '.join(pokemon.types)} | "
                  f"ATK: {pokemon.attack} | DEF: {pokemon.defense}")
        
        print(f"{'='*60}\n")
    
    def display_stats(self):
        """Show player statistics"""
        print(f"\n{'='*50}")
        print(f"Trainer: {self.name}")
        print(f"{'='*50}")
        print(f"Team Size: {len(self.team)}/{self.max_team_size}")
        print(f"Pokedex: {len(self.pokedex)} Pokemon caught")
        print(f"Battle Record: {self.battles_won}W - {self.battles_lost}L")
        
        if self.battles_won + self.battles_lost > 0:
            win_rate = (self.battles_won / (self.battles_won + self.battles_lost)) * 100
            print(f"Win Rate: {win_rate:.1f}%")
        print(f"{'='*50}\n")
    
    def heal_all_pokemon(self):
        """Heal all Pokemon in team"""
        for pokemon in self.team:
            pokemon.heal()
        print("All Pokemon have been healed! 💚")
    
    def get_active_pokemon(self) -> List[Pokemon]:
        """Get list of Pokemon that can battle"""
        return [p for p in self.team if not p.is_fainted]
    
    def save_team(self, filename: str = "pokemon_team.json"):
        """Save team to JSON file"""
        team_data = {
            "player_name": self.name,
            "battles_won": self.battles_won,
            "battles_lost": self.battles_lost,
            "team": [
                {
                    "name": p.name,
                    "id": p.id,
                    "level": p.level,
                    "current_hp": p.current_hp,
                    "max_hp": p.max_hp,
                    "experience": p.experience
                }
                for p in self.team
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(team_data, f, indent=2)
        
        print(f"Team saved to {filename}")


# ========== BATTLE SYSTEM ==========
class Battle:
    """
    Pokemon battle system
    Demonstrates: OOP, Game Logic, Algorithms
    """
    
    def __init__(self, player_pokemon: Pokemon, opponent_pokemon: Pokemon):
        self.player = player_pokemon
        self.opponent = opponent_pokemon
        self.turn = 1
    
    def calculate_damage(self, attacker: Pokemon, defender: Pokemon) -> int:
        """
        Calculate damage based on stats and type effectiveness
        """
        import random
        
        # Base damage
        base_damage = max(1, attacker.attack - defender.defense // 2)
        
        # Random variation (85% - 100%)
        variation = random.uniform(0.85, 1.0)
        damage = int(base_damage * variation)
        
        # Critical hit (10% chance, 1.5x damage)
        if random.random() < 0.1:
            damage = int(damage * 1.5)
            print("💥 Critical hit!")
        
        return max(1, damage)
    
    def player_turn(self) -> bool:
        """
        Player's turn
        Returns True if opponent fainted
        """
        print(f"\n--- Turn {self.turn} ---")
        print(f"Your {self.player.name} attacks!")
        
        damage = self.calculate_damage(self.player, self.opponent)
        actual_damage = self.opponent.take_damage(damage)
        
        print(f"{self.opponent.name} takes {actual_damage} damage!")
        print(f"{self.opponent.name}: {self.opponent.current_hp}/{self.opponent.max_hp} HP")
        
        return self.opponent.is_fainted
    
    def opponent_turn(self) -> bool:
        """
        Opponent's turn
        Returns True if player fainted
        """
        print(f"\nOpponent's {self.opponent.name} attacks!")
        
        damage = self.calculate_damage(self.opponent, self.player)
        actual_damage = self.player.take_damage(damage)
        
        print(f"Your {self.player.name} takes {actual_damage} damage!")
        print(f"{self.player.name}: {self.player.current_hp}/{self.player.max_hp} HP")
        
        return self.player.is_fainted
    
    def execute(self) -> bool:
        """
        Run the battle
        Returns True if player wins
        """
        print(f"\n{'='*60}")
        print(f"BATTLE START!".center(60))
        print(f"{'='*60}")
        print(f"{self.player.name} (Lv.{self.player.level}) VS {self.opponent.name} (Lv.{self.opponent.level})")
        print(f"{'='*60}\n")
        
        while True:
            # Player turn
            if self.player_turn():
                print(f"\n🎉 Victory! {self.opponent.name} fainted!")
                exp_gained = self.opponent.level * 50
                self.player.gain_experience(exp_gained)
                print(f"{self.player.name} gained {exp_gained} EXP!")
                return True
            
            # Opponent turn
            if self.opponent_turn():
                print(f"\n💀 Defeat! {self.player.name} fainted!")
                return False
            
            self.turn += 1
            input("\nPress Enter to continue...")


# ========== GAME MENU SYSTEM ==========
class PokemonGame:
    """
    Main game controller
    Demonstrates: Menu systems, User interaction, Integration
    """
    
    def __init__(self):
        self.player = None
        self.running = True
    
    def start_game(self):
        """Initialize game"""
        print("\n" + "="*60)
        print("WELCOME TO POKEMON GAME!".center(60))
        print("="*60 + "\n")
        
        name = input("Enter your trainer name: ").strip()
        if not name:
            name = "Trainer"
        
        self.player = Player(name)
        print(f"\nWelcome, {self.player.name}!")
        
        # Choose starter
        self.choose_starter()
        
        # Main game loop
        while self.running:
            self.main_menu()
    
    def choose_starter(self):
        """Let player choose starter Pokemon"""
        print("\n" + "="*60)
        print("Choose your starter Pokemon:".center(60))
        print("="*60)
        
        starters = ["bulbasaur", "charmander", "squirtle"]
        
        for i, name in enumerate(starters, 1):
            print(f"{i}. {name.capitalize()}")
        
        while True:
            try:
                choice = int(input("\nEnter choice (1-3): "))
                if 1 <= choice <= 3:
                    break
                print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a number.")
        
        starter_name = starters[choice - 1]
        print(f"\nFetching {starter_name.capitalize()}...")
        
        starter = create_pokemon_from_api(starter_name)
        if starter:
            self.player.add_pokemon(starter)
            starter.display_info()
        else:
            print("Failed to get starter. Try again.")
    
    def main_menu(self):
        """Display main game menu"""
        print("\n" + "="*60)
        print("MAIN MENU".center(60))
        print("="*60)
        print("1. View Team")
        print("2. Catch Pokemon")
        print("3. Battle Wild Pokemon")
        print("4. Heal Team")
        print("5. View Stats")
        print("6. Save Game")
        print("7. Quit")
        print("="*60)
        
        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            self.view_team()
        elif choice == "2":
            self.catch_pokemon()
        elif choice == "3":
            self.battle_wild()
        elif choice == "4":
            self.player.heal_all_pokemon()
        elif choice == "5":
            self.player.display_stats()
        elif choice == "6":
            self.player.save_team()
        elif choice == "7":
            self.quit_game()
        else:
            print("Invalid choice!")
    
    def view_team(self):
        """View player's team"""
        self.player.display_team()
        
        if self.player.team:
            print("1. View Pokemon details")
            print("2. Remove Pokemon")
            print("3. Back")
            
            choice = input("\nChoose option: ").strip()
            
            if choice == "1":
                try:
                    idx = int(input("Enter Pokemon number: ")) - 1
                    if 0 <= idx < len(self.player.team):
                        self.player.team[idx].display_info()
                except ValueError:
                    print("Invalid input")
            
            elif choice == "2":
                try:
                    idx = int(input("Enter Pokemon number to remove: ")) - 1
                    self.player.remove_pokemon(idx)
                except ValueError:
                    print("Invalid input")
    
    def catch_pokemon(self):
        """Catch a new Pokemon"""
        print("\n1. Search by name")
        print("2. Search by ID")
        print("3. Random encounter")
        
        choice = input("\nChoose option: ").strip()
        
        pokemon = None
        
        if choice == "1":
            name = input("Enter Pokemon name: ").strip()
            if name:
                print(f"Searching for {name}...")
                pokemon = create_pokemon_from_api(name)
        
        elif choice == "2":
            try:
                poke_id = int(input("Enter Pokemon ID (1-898): "))
                print(f"Searching for Pokemon #{poke_id}...")
                pokemon = create_pokemon_from_api(str(poke_id))
            except ValueError:
                print("Invalid ID")
        
        elif choice == "3":
            print("Searching for wild Pokemon...")
            pokemon = get_random_pokemon()
        
        if pokemon:
            pokemon.display_info()
            confirm = input("Add to team? (y/n): ").strip().lower()
            if confirm == 'y':
                self.player.add_pokemon(pokemon)
        else:
            print("Pokemon not found!")
    
    def battle_wild(self):
        """Battle a wild Pokemon"""
        active = self.player.get_active_pokemon()
        
        if not active:
            print("No active Pokemon! Heal your team first.")
            return
        
        print("\nChoose your Pokemon:")
        for i, p in enumerate(active, 1):
            print(f"{i}. {p}")
        
        try:
            choice = int(input("\nEnter choice: ")) - 1
            if 0 <= choice < len(active):
                player_pokemon = active[choice]
                
                print("\nSearching for wild Pokemon...")
                wild_pokemon = get_random_pokemon()
                
                if wild_pokemon:
                    battle = Battle(player_pokemon, wild_pokemon)
                    won = battle.execute()
                    
                    if won:
                        self.player.battles_won += 1
                    else:
                        self.player.battles_lost += 1
                else:
                    print("Failed to find wild Pokemon!")
        except (ValueError, IndexError):
            print("Invalid choice!")
    
    def quit_game(self):
        """Exit the game"""
        print("\nThanks for playing!")
        self.player.display_stats()
        
        save = input("Save before quitting? (y/n): ").strip().lower()
        if save == 'y':
            self.player.save_team()
        
        self.running = False


# ========== MAIN ENTRY POINT ==========
if __name__ == "__main__":
    game = PokemonGame()
    game.start_game()
```
