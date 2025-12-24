# Python Functional Programming - Complete Reference Guide

## Quick Reference Card

| Operation | Syntax | Example |
|-----------|--------|---------|
| Lambda | `lambda x: x**2` | `square = lambda x: x**2` |
| Map | `map(func, iterable)` | `map(lambda x: x*2, [1,2,3])` |
| Filter | `filter(func, iterable)` | `filter(lambda x: x%2==0, [1,2,3,4])` |
| Reduce | `reduce(func, iterable)` | `reduce(lambda x,y: x+y, [1,2,3,4])` |
| List comp | `[x for x in iterable]` | `[x*2 for x in [1,2,3]]` |
| List filter | `[x for x in iterable if cond]` | `[x for x in [1,2,3,4] if x%2==0]` |
| Dict comp | `{k: v for k, v in items}` | `{x: x**2 for x in range(3)}` |
| Set comp | `{x for x in iterable}` | `{x**2 for x in [1,2,2,3]}` |
| Generator | `(x for x in iterable)` | `(x**2 for x in range(1000000))` |
| All/Any | `all(iterable)`, `any(iterable)` | `all(x > 0 for x in nums)` |

## Table of Contents
- [Lambda Functions](#lambda-functions)
- [Map](#map)
- [Filter](#filter)
- [Reduce](#reduce)
- [List Comprehensions](#list-comprehensions)
- [Dictionary Comprehensions](#dictionary-comprehensions)
- [Set Comprehensions](#set-comprehensions)
- [Generator Expressions](#generator-expressions)
- [Advanced Functional Concepts](#advanced-functional-concepts)

---

## Lambda Functions

### What is a Lambda?
```python
# Anonymous function - function without a name
# Syntax: lambda parameters: expression

# Regular function
def add(x, y):
    return x + y

# Lambda equivalent
lambda x, y: x + y

# Assign to variable
add = lambda x, y: x + y
result = add(3, 5)  # 8
```

### Lambda Examples
```python
# Single parameter
square = lambda x: x ** 2
square(5)  # 25

# Multiple parameters
multiply = lambda x, y: x * y
multiply(4, 3)  # 12

# No parameters
get_pi = lambda: 3.14159
get_pi()  # 3.14159

# With conditional
max_val = lambda a, b: a if a > b else b
max_val(10, 5)  # 10
```

### Lambda with Built-in Functions
```python
# Sorting with key
students = ["Wilson", "bob", "Charlie", "david"]
sorted(students, key=lambda name: name.lower())
# ['Wilson', 'bob', 'Charlie', 'david']

# Complex sorting
products = [
    {'name': 'laptop', 'price': 999.99},
    {'name': 'mouse', 'price': 29.99},
    {'name': 'keyboard', 'price': 129.99}
]

# Sort by price (highest first)
sorted(products, key=lambda p: p['price'], reverse=True)

# Sort by name length
sorted(products, key=lambda p: len(p['name']))

# Multiple sort criteria
sorted(products, key=lambda p: (p['price'], p['name']))
```

### When to Use Lambdas
```python
# Good - Simple, one-time use
squares = map(lambda x: x**2, [1, 2, 3, 4])

# Bad - Complex logic (use regular function instead)
# complex_lambda = lambda x: x**2 if x > 0 else -x**2 if x < 0 else 0

# Better - Regular function for complex logic
def complex_operation(x):
    if x > 0:
        return x ** 2
    elif x < 0:
        return -x ** 2
    else:
        return 0
```

---

## Map

### Basic Map Usage
```python
# map() applies a function to every item in an iterable
# Syntax: map(function, iterable)

numbers = [1, 2, 3, 4, 5]

# Double each number
doubled = map(lambda x: x * 2, numbers)
list(doubled)  # [2, 4, 6, 8, 10]

# Note: map returns an iterator, convert to list to see results
```

### Map with Lambda
```python
numbers = [1, 2, 3, 4, 5]

# Square numbers
squares = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# Convert to strings
strings = list(map(lambda x: str(x), numbers))
# ['1', '2', '3', '4', '5']

# Apply calculation
prices = [10, 20, 30]
with_tax = list(map(lambda p: p * 1.07, prices))
# [10.7, 21.4, 32.1]
```

### Map with Regular Functions
```python
def calculate_tax(price):
    return price * 1.07

prices = [100, 200, 300]
prices_with_tax = list(map(calculate_tax, prices))
# [107.0, 214.0, 321.0]

# Built-in functions work too
numbers = ['1', '2', '3']
integers = list(map(int, numbers))  # [1, 2, 3]
```

### Map with Multiple Iterables
```python
# Map with two lists
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]

sums = list(map(lambda x, y: x + y, numbers1, numbers2))
# [11, 22, 33]

# Combine first and last names
first_names = ["John", "Jane", "Bob"]
last_names = ["Doe", "Smith", "Johnson"]

full_names = list(map(lambda f, l: f + " " + l, first_names, last_names))
# ['John Doe', 'Jane Smith', 'Bob Johnson']
```

### Practical Map Examples
```python
# Normalize user data
users = [
    {'name': 'Wilson JOHNSON', 'email': 'Wilson@EMAIL.COM'},
    {'name': 'BOB SMITH', 'email': 'BOB@EMAIL.COM'}
]

def normalize_user(user):
    return {
        'name': user['name'].title(),
        'email': user['email'].lower(),
        'username': user['email'].split('@')[0].lower()
    }

normalized = list(map(normalize_user, users))
# [{'name': 'Wilson Johnson', 'email': 'Wilson@email.com', 'username': 'Wilson'}, ...]

# Extract specific fields
products = [
    {'id': 1, 'name': 'Laptop', 'price': 999},
    {'id': 2, 'name': 'Mouse', 'price': 29}
]

names = list(map(lambda p: p['name'], products))
# ['Laptop', 'Mouse']
```

---

## Filter

### Basic Filter Usage
```python
# filter() returns items where function returns True
# Syntax: filter(function, iterable)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers
evens = filter(lambda x: x % 2 == 0, numbers)
list(evens)  # [2, 4, 6, 8, 10]

# Get odd numbers
odds = list(filter(lambda x: x % 2 != 0, numbers))
# [1, 3, 5, 7, 9]

# Numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
# [6, 7, 8, 9, 10]
```

### Filter with Lambda
```python
# Filter strings by length
words = ["hi", "hello", "hey", "goodbye", "yes"]
long_words = list(filter(lambda w: len(w) > 3, words))
# ['hello', 'goodbye']

# Filter by first letter
a_words = list(filter(lambda w: w.startswith('h'), words))
# ['hi', 'hello', 'hey']

# Remove empty strings
strings = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda s: s != "", strings))
# ['hello', 'world', 'python']

# Simpler - filter(None, ...) removes falsy values
non_empty = list(filter(None, strings))
```

### Filter with Regular Functions
```python
def is_positive(n):
    return n > 0

numbers = [-2, -1, 0, 1, 2, 3]
positives = list(filter(is_positive, numbers))
# [1, 2, 3]

def is_adult(age):
    return age >= 18

ages = [15, 18, 21, 16, 25, 17]
adults = list(filter(is_adult, ages))
# [18, 21, 25]
```

### Practical Filter Examples
```python
# Filter users by condition
users = [
    {'name': 'Wilson', 'age': 30, 'active': True},
    {'name': 'Bob', 'age': 25, 'active': False},
    {'name': 'Charlie', 'age': 35, 'active': True}
]

# Active users only
active_users = list(filter(lambda u: u['active'], users))

# Users over 30
over_30 = list(filter(lambda u: u['age'] > 30, users))

# Filter products by price range
products = [
    {'name': 'Laptop', 'price': 999},
    {'name': 'Mouse', 'price': 29},
    {'name': 'Keyboard', 'price': 79}
]

affordable = list(filter(lambda p: p['price'] < 100, products))
# [{'name': 'Mouse', 'price': 29}, {'name': 'Keyboard', 'price': 79}]

# Filter transactions
transactions = [
    {'type': 'deposit', 'amount': 100},
    {'type': 'withdrawal', 'amount': 50},
    {'type': 'deposit', 'amount': 200}
]

deposits = list(filter(lambda t: t['type'] == 'deposit', transactions))
# [{'type': 'deposit', 'amount': 100}, {'type': 'deposit', 'amount': 200}]
```

---

## Reduce

### Basic Reduce Usage
```python
from functools import reduce

# reduce() applies function cumulatively to items
# Syntax: reduce(function, iterable, initial_value)

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
# 15 (1+2=3, 3+3=6, 6+4=10, 10+5=15)

# Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
# 120 (1*2=2, 2*3=6, 6*4=24, 24*5=120)

# Maximum value
max_val = reduce(lambda x, y: x if x > y else y, numbers)
# 5
```

### Reduce with Initial Value
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum with initial value
total = reduce(lambda x, y: x + y, numbers, 10)
# 25 (10+1=11, 11+2=13, 13+3=16, 16+4=20, 20+5=25)

# Build string
words = ['Hello', 'World', 'Python']
sentence = reduce(lambda x, y: x + ' ' + y, words, '')
# ' Hello World Python'
```

### Practical Reduce Examples
```python
from functools import reduce

# Sum of prices
products = [
    {'name': 'Laptop', 'price': 999},
    {'name': 'Mouse', 'price': 29},
    {'name': 'Keyboard', 'price': 79}
]

total_price = reduce(lambda acc, p: acc + p['price'], products, 0)
# 1107

# Flatten nested lists
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda acc, lst: acc + lst, nested, [])
# [1, 2, 3, 4, 5, 6]

# Count occurrences
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
count = reduce(
    lambda acc, word: {**acc, word: acc.get(word, 0) + 1},
    words,
    {}
)
# {'apple': 3, 'banana': 2, 'cherry': 1}
```

---

## List Comprehensions

### Basic Syntax
```python
# [expression for item in iterable]

# Traditional way
squares = []
for x in range(5):
    squares.append(x ** 2)
# [0, 1, 4, 9, 16]

# List comprehension
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]
```

### With Conditions
```python
# [expression for item in iterable if condition]

# Even numbers only
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Squares of odd numbers
odd_squares = [x**2 for x in range(10) if x % 2 != 0]
# [1, 9, 25, 49, 81]

# Filter and transform
words = ["hello", "hi", "hey", "goodbye"]
long_words_upper = [w.upper() for w in words if len(w) > 3]
# ['HELLO', 'GOODBYE']
```

### With If-Else
```python
# [expression_if_true if condition else expression_if_false for item in iterable]

# Label numbers as even or odd
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']

# Categorize scores
scores = [95, 75, 85, 60, 90]
grades = ["Pass" if s >= 70 else "Fail" for s in scores]
# ['Pass', 'Pass', 'Pass', 'Fail', 'Pass']
```

### Nested List Comprehensions
```python
# Create 2D matrix
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Flatten 2D list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
# [1, 2, 3, 4, 5, 6]

# Cartesian product
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
combinations = [(c, s) for c in colors for s in sizes]
# [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]
```

### Practical Examples
```python
# Extract field from dictionaries
users = [
    {'name': 'Wilson', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

names = [u['name'] for u in users]
# ['Wilson', 'Bob', 'Charlie']

# Filter and extract
adults = [u['name'] for u in users if u['age'] >= 30]
# ['Wilson', 'Charlie']

# String processing
text = "Hello World"
vowels = [c for c in text if c.lower() in 'aeiou']
# ['e', 'o', 'o']

# Parse CSV-like data
data = "1,2,3\n4,5,6\n7,8,9"
rows = [[int(x) for x in row.split(',')] for row in data.split('\n')]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

---

## Dictionary Comprehensions

### Basic Syntax
```python
# {key_expression: value_expression for item in iterable}

# Create dictionary from range
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
# {'a': 1, 'b': 2, 'c': 3}
```

### With Conditions
```python
# {key: value for item in iterable if condition}

# Only even numbers
evens = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Filter dictionary
prices = {'apple': 0.50, 'banana': 0.30, 'cherry': 2.00}
expensive = {k: v for k, v in prices.items() if v > 0.40}
# {'apple': 0.50, 'cherry': 2.00}
```

### Transform Dictionaries
```python
# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# Update values
prices = {'apple': 1.00, 'banana': 0.50}
with_tax = {k: v * 1.07 for k, v in prices.items()}
# {'apple': 1.07, 'banana': 0.535}

# Transform keys
scores = {'Wilson': 85, 'bob': 92, 'charlie': 78}
uppercase_keys = {k.upper(): v for k, v in scores.items()}
# {'Wilson': 85, 'BOB': 92, 'CHARLIE': 78}
```

### Practical Examples
```python
# Count characters
text = "hello"
char_count = {char: text.count(char) for char in text}
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Create lookup table
users = [
    {'id': 1, 'name': 'Wilson'},
    {'id': 2, 'name': 'Bob'}
]
user_lookup = {u['id']: u['name'] for u in users}
# {1: 'Wilson', 2: 'Bob'}

# Grade students
scores = {'Wilson': 92, 'Bob': 85, 'Charlie': 78}
grades = {
    name: 'A' if score >= 90 else 'B' if score >= 80 else 'C'
    for name, score in scores.items()
}
# {'Wilson': 'A', 'Bob': 'B', 'Charlie': 'C'}
```

---

## Set Comprehensions

### Basic Syntax
```python
# {expression for item in iterable}

# Squares
squares = {x**2 for x in range(5)}
# {0, 1, 4, 9, 16}

# Unique lengths
words = ["hello", "hi", "hey", "hello", "goodbye"]
lengths = {len(w) for w in words}
# {2, 3, 5, 7}
```

### With Conditions
```python
# {expression for item in iterable if condition}

# Even squares
even_squares = {x**2 for x in range(10) if x % 2 == 0}
# {0, 4, 16, 36, 64}

# Unique vowels
text = "Hello World"
vowels = {c.lower() for c in text if c.lower() in 'aeiou'}
# {'e', 'o'}
```

### Practical Examples
```python
# Remove duplicates while transforming
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {x**2 for x in numbers}
# {1, 4, 9, 16}

# Extract unique domains
emails = ['Wilson@gmail.com', 'bob@yahoo.com', 'charlie@gmail.com']
domains = {email.split('@')[1] for email in emails}
# {'gmail.com', 'yahoo.com'}

# Unique first letters
names = ['Wilson', 'Bob', 'Charlie', 'Anna']
initials = {name[0].upper() for name in names}
# {'A', 'B', 'C'}
```

---

## Generator Expressions

### Basic Syntax
```python
# (expression for item in iterable)
# Like list comprehension but with () instead of []

# Generator (lazy evaluation)
gen = (x**2 for x in range(5))
# <generator object>

# Convert to list to see values
list(gen)  # [0, 1, 4, 9, 16]

# Memory efficient for large datasets
# List - creates entire list in memory
squares_list = [x**2 for x in range(1000000)]  # Uses lots of memory

# Generator - creates values on-demand
squares_gen = (x**2 for x in range(1000000))   # Minimal memory
```

### Using Generators
```python
# Iterate once
gen = (x**2 for x in range(5))
for square in gen:
    print(square)  # 0, 1, 4, 9, 16

# Generator is exhausted after iteration
list(gen)  # []

# With sum(), max(), etc.
gen = (x**2 for x in range(5))
total = sum(gen)  # 30

# next() to get values one at a time
gen = (x**2 for x in range(5))
next(gen)  # 0
next(gen)  # 1
next(gen)  # 4
```

---

## Advanced Functional Concepts

### Combining Map, Filter, Reduce
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get sum of squares of even numbers
result = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)),
    0
)
# 220 (4 + 16 + 36 + 64 + 100)

# Same with comprehension (more readable)
result = sum(x**2 for x in numbers if x % 2 == 0)
# 220
```

### Function Composition
```python
# Compose functions
def compose(f, g):
    return lambda x: f(g(x))

add_five = lambda x: x + 5
multiply_two = lambda x: x * 2

# Multiply then add
composed = compose(add_five, multiply_two)
composed(3)  # 11 (3 * 2 = 6, 6 + 5 = 11)
```

### Partial Functions
```python
from functools import partial

# Create specialized functions from general ones
def power(base, exponent):
    return base ** exponent

# Create square and cube functions
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

square(5)  # 25
cube(3)    # 27
```

### All and Any
```python
# all() - True if all elements are True
all([True, True, True])     # True
all([True, False, True])    # False

# any() - True if any element is True
any([False, False, True])   # True
any([False, False, False])  # False

# Check if all numbers are positive
numbers = [1, 2, 3, 4, 5]
all(x > 0 for x in numbers)  # True

# Check if any number is even
any(x % 2 == 0 for x in numbers)  # True
```

---

## Comparison: Functional vs Traditional

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Task: Get sum of squares of even numbers

# Traditional approach
total = 0
for num in numbers:
    if num % 2 == 0:
        square = num ** 2
        total += square
# total = 220

# Functional with map/filter/reduce
from functools import reduce
total = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)),
    0
)
# total = 220

# List comprehension (best balance)
total = sum(x**2 for x in numbers if x % 2 == 0)
# total = 220
```

---

## Practical Data Processing

Functional programming is extremely powerful for "cleaning" and analyzing real-world datasets.

### 1. Data Normalization (Map)
Standardizing inconsistent user input.

```python
users = [
    {'name': 'alice smith', 'email': 'ALICE@Email.com'},
    {'name': 'BOB jones', 'email': 'bob@REDO.org'}
]

def clean_user(user):
    return {
        'name': user['name'].title(),
        'email': user['email'].lower(),
        'username': user['name'].lower().replace(" ", "_")
    }

cleaned = list(map(clean_user, users))
# Result: [{'name': 'Alice Smith', 'email': 'alice@email.com', 'username': 'alice_smith'}, ...]
```

### 2. Transaction Analysis (Filter)
Finding specific patterns in financial data.

```python
transactions = [
    {'id': 1, 'amount': 150.0, 'type': 'credit', 'status': 'valid'},
    {'id': 2, 'amount': -50.0, 'type': 'debit', 'status': 'invalid'},
    {'id': 3, 'amount': 500.0, 'type': 'credit', 'status': 'valid'}
]

# Find valid credits over 100
high_value = list(filter(
    lambda t: t['type'] == 'credit' and t['amount'] > 100 and t['status'] == 'valid', 
    transactions
))
```

### 3. Multi-level Sorting (Lambda)
Sorting by multiple fields (e.g., Category first, then Price).

```python
products = [
    {'name': 'Laptop', 'price': 999, 'cat': 'Electronics'},
    {'name': 'Mouse', 'price': 25, 'cat': 'Electronics'},
    {'name': 'Shoes', 'price': 80, 'cat': 'Apparel'}
]

# Sort by Category (asc), then Price (desc)
# Note: Use negative price for descending numerical sort within lambda
sorted_products = sorted(products, key=lambda p: (p['cat'], -p['price']))
```

---

## See Also

- **[Python Basics Cheat Sheet](Python_Basics_Cheat_Sheet.md)** - Functions and basic concepts
- **[Decorators Cheat Sheet](Decorators_Cheat_Sheet.md)** - functools decorators and advanced functions
- **[Iterators and Generators Cheat Sheet](Iterators_and_Generators_Cheat_Sheet.md)** - Generator expressions and lazy evaluation
- **[Standard Library Essentials Cheat Sheet](Standard_Library_Essentials_Cheat_Sheet.md)** - functools, itertools modules

---