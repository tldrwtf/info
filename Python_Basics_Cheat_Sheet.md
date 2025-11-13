# Python Basics - Complete Reference Guide

## Quick Reference Card

| Operation | Syntax | Example |
|-----------|--------|---------|
| Variable | `name = value` | `age = 25` |
| String format | `f"text {var}"` | `f"Hello {name}"` |
| If statement | `if condition:` | `if age >= 18:` |
| For loop | `for item in iterable:` | `for i in range(5):` |
| While loop | `while condition:` | `while count < 10:` |
| Function | `def name(params):` | `def greet(name):` |
| Return | `return value` | `return result` |
| Input | `input(prompt)` | `name = input("Name: ")` |
| Print | `print(value)` | `print("Hello")` |
| List | `[item1, item2]` | `nums = [1, 2, 3]` |
| Dictionary | `{key: value}` | `user = {"name": "Alice"}` |
| Comment | `# comment` | `# This is a comment` |

## Table of Contents

- [Variables & Data Types](#variables--data-types)
- [Control Flow](#control-flow)
- [Loops](#loops)
- [Functions](#functions)
- [Built-in Functions](#built-in-functions)

---

## Variables & Data Types

### Basic Data Types

```python
# Integer
age = 25

# Float
price = 19.99

# String
name = "Wilson"
message = 'Hello World'

# Boolean
is_active = True
is_complete = False

# None (null value)
result = None
```

### Type Checking & Conversion

```python
# Check type
type(42)           # <class 'int'>
type(3.14)         # <class 'float'>
type("hello")      # <class 'str'>

# Type conversion
int("42")          # 42
float("3.14")      # 3.14
str(100)           # "100"
bool(1)            # True
bool(0)            # False
```

### String Operations

```python
# Concatenation
full_name = "John" + " " + "Doe"

# String formatting
name = "Wilson"
age = 30
f"My name is {name} and I'm {age}"           # f-strings (Python 3.6+)
"My name is {} and I'm {}".format(name, age) # .format()

# Common methods
text = "  Hello World  "
text.lower()        # "  hello world  "
text.upper()        # "  HELLO WORLD  "
text.strip()        # "Hello World"
text.replace("World", "Python")  # "  Hello Python  "
text.split()        # ["Hello", "World"]
```

---

## Control Flow

### If Statements

```python
# Basic if
if condition:
    # code block
    pass

# If-else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# If-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### Comparison Operators

```python
==    # Equal to
!=    # Not equal to
>     # Greater than
<     # Less than
>=    # Greater than or equal to
<=    # Less than or equal to
```

### Logical Operators

```python
# and - Both conditions must be True
if age >= 18 and has_license:
    print("Can drive")

# or - At least one condition must be True
if is_weekend or is_holiday:
    print("Day off")

# not - Negates the condition
if not is_raining:
    print("Go outside")
```

### Ternary Operator

```python
# Syntax: value_if_true if condition else value_if_false
status = "Adult" if age >= 18 else "Minor"

result = "Even" if num % 2 == 0 else "Odd"
```

---

## Loops

### For Loops

```python
# Loop through range
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (step of 2)
    print(i)

# Loop through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Loop through string
for char in "Python":
    print(char)
```

### While Loops

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# While with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")

# While with continue
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
```

### Loop Control

```python
# break - Exit the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4

# continue - Skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # Prints 0, 1, 3, 4

# else with loops (executes if loop completes without break)
for i in range(5):
    print(i)
else:
    print("Loop completed")
```

---

## Functions

### Basic Function Definition

```python
# Simple function
def greet():
    print("Hello!")

greet()  # Call the function

# Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Wilson")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)  # result = 8
```

### Parameters & Arguments

```python
# Default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()           # "Hello, Guest!"
greet("Wilson")    # "Hello, Wilson!"

# Multiple parameters
def calculate_total(price, tax_rate=0.07):
    tax = price * tax_rate
    return price + tax

total = calculate_total(100)        # Uses default tax_rate
total = calculate_total(100, 0.10)  # Override tax_rate

# *args - Variable number of arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

sum_all(1, 2, 3)        # 6
sum_all(1, 2, 3, 4, 5)  # 15

# **kwargs - Variable keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Wilson", age=30, city="NYC")
```

### Return Values

```python
# Single return
def square(n):
    return n * n

# Multiple returns
def get_user_info():
    return "Wilson", 30, "NYC"

name, age, city = get_user_info()

# Return dictionary
def create_user(name, age):
    return {
        "name": name,
        "age": age,
        "active": True
    }
```

### Function Scope

```python
# Global variable
global_var = "I'm global"

def my_function():
    # Local variable
    local_var = "I'm local"
    print(global_var)  # Can access global

# print(local_var)  # Error! Can't access local outside function

# Modifying global variable
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1
```

### Docstrings

```python
def calculate_tax(price, tax_rate):
    """
    Calculate tax and return total price.

    Args:
        price (float): The original price
        tax_rate (float): Tax rate as decimal (e.g., 0.07 for 7%)

    Returns:
        float: Total price including tax
    """
    return price * (1 + tax_rate)
```

---

## Built-in Functions

### Common Built-ins

```python
# Length
len([1, 2, 3])         # 3
len("Hello")           # 5

# Min/Max
min(1, 5, 3)           # 1
max([1, 5, 3])         # 5

# Sum
sum([1, 2, 3, 4, 5])   # 15

# Sorted (returns new list)
sorted([3, 1, 4, 1, 5])         # [1, 1, 3, 4, 5]
sorted([3, 1, 4], reverse=True)  # [4, 3, 1]

# Reversed
list(reversed([1, 2, 3]))  # [3, 2, 1]

# Round
round(3.14159, 2)      # 3.14

# Abs (absolute value)
abs(-5)                # 5

# All (returns True if all elements are True)
all([True, True, True])   # True
all([True, False, True])  # False

# Any (returns True if any element is True)
any([False, False, True])  # True
any([False, False, False]) # False

# Zip (combine iterables)
names = ["Wilson", "Bob", "Charlie"]
ages = [25, 30, 35]
list(zip(names, ages))  # [('Wilson', 25), ('Bob', 30), ('Charlie', 35)]

# Enumerate (add counter to iterable)
for index, value in enumerate(['a', 'b', 'c']):
    print(f"{index}: {value}")
```

### Input/Output

```python
# Input (always returns string)
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert to int

# Output
print("Hello, World!")
print("Name:", name, "Age:", age)
print(f"My name is {name}")

# Print with separator
print("apple", "banana", "cherry", sep=", ")  # apple, banana, cherry

# Print without newline
print("Loading", end="...")
```

### Type Checking

```python
isinstance(42, int)           # True
isinstance("hello", str)      # True
isinstance([1, 2], list)      # True
isinstance({}, dict)          # True
```

---

## Best Practices

### Naming Conventions

```python
# Variables and functions: snake_case
user_name = "Wilson"
def calculate_total():
    pass

# Constants: UPPER_CASE
MAX_SIZE = 100
API_KEY = "abc123"

# Classes: PascalCase (covered in OOP cheat sheet)
class UserProfile:
    pass
```

### Code Style

```python
# Use meaningful variable names
# Bad
x = 42
# Good
user_age = 42

# Keep functions focused on one task
# Bad
def do_everything():
    # 100 lines of code
    pass

# Good
def validate_email(email):
    # specific task
    pass

def send_email(to, subject, body):
    # specific task
    pass
```

### Error Handling Preview

```python
# Try-except for error handling
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This always executes")
```

---

## Quick Reference Card

| Concept       | Syntax                  | Example                  |
| ------------- | ----------------------- | ------------------------ |
| Variable      | `name = value`          | `age = 25`               |
| If statement  | `if condition:`         | `if age >= 18:`          |
| For loop      | `for item in iterable:` | `for i in range(5):`     |
| While loop    | `while condition:`      | `while count < 10:`      |
| Function      | `def name(params):`     | `def greet(name):`       |
| Return        | `return value`          | `return result`          |
| Input         | `input(prompt)`         | `name = input("Name: ")` |
| Print         | `print(value)`          | `print("Hello")`         |
| Comment       | `# comment`             | `# This is a comment`    |
| String format | `f"text {var}"`         | `f"Hello {name}"`        |

---

## See Also

- **[Data Structures Cheat Sheet](./Data_Structures_Cheat_Sheet.md)** - Core data structures in Python
- **[Error Handling Cheat Sheet](./Error_Handling_Cheat_Sheet.md)** - Exception handling and debugging
- **[File Operations Cheat Sheet](./File_Operations_Cheat_Sheet.md)** - Working with files and directories
- **[Functional Programming Cheat Sheet](./Functional_Programming_Cheat_Sheet.md)** - Functional programming concepts
- **[Decorators Cheat Sheet](./Decorators_Cheat_Sheet.md)** - Function and class decorators

---
