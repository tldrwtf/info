# Python Basics - Complete Reference Guide

This guide provides a comprehensive overview of fundamental Python concepts, from basic syntax and data types to control flow, functions, and commonly used built-in functions. It serves as a foundational resource for beginners and a quick reference for experienced developers.

## Quick Reference Card

| Operation       | Syntax                       | Example                            |
| :-------------- | :--------------------------- | :--------------------------------- |
| Variable        | `name = value`               | `age = 25`                         |
| String format   | `f"text {var}"`              | `f"Hello {name}"`                  |
| If statement    | `if condition:`              | `if age >= 18:`                    |
| For loop        | `for item in iterable:`      | `for i in range(5):`               |
| While loop      | `while condition:`           | `while count < 10:`                |
| Function        | `def name(params):`          | `def greet(name):`                 |
| Return          | `return value`               | `return result`                    |
| Input           | `input(prompt)`              | `name = input("Name: ")`           |
| Print           | `print(value)`               | `print("Hello")`                   |
| Comment         | `# comment`                  | `# This is a comment`              |
| List            | `[item1, item2]`             | `nums = [1, 2, 3]`                 |
| Dictionary      | `{key: value}`               | `user = {"name": "Alice"}`         |

---

## 1. Variables & Data Types

Variables are used to store data values. Python is dynamically typed, meaning you don't declare the type of a variable.

### Basic Data Types

```python
# Integer (whole numbers)
age = 25
num_students = 15

# Float (decimal numbers)
price = 19.99
pi = 3.14159

# String (text)
name = "Alice"
message = 'Hello World'
greeting = "Hi"
student_name = "Charlie"

# Boolean (True or False)
is_active = True
is_complete = False

# None (represents absence of a value)
result = None
```

### Input and Output

```python
# Input from user (always returns a string)
user_name = input("What's your name? ")
user_age = int(input("How old are you? ")) # Convert to integer

print(f"Hello, {user_name}! You are {user_age} years old.")

# Output using print()
print("Hello, World!")
print("Name:", name, "Age:", age)
print(f"My name is {name}")

# Print with custom separator and end
print("apple", "banana", "cherry", sep=", ") # Output: apple, banana, cherry
print("Loading", end="...")                  # Output: Loading... (without newline)
```

### Type Checking & Conversion

```python
# Check type
type(age)           # <class 'int'>
type(price)         # <class 'float'>
type(name)          # <class 'str'>

# Type conversion (Casting)
int("42")           # 42
float("3.14")       # 3.14
str(100)            # "100"
bool(1)             # True (any non-zero number is True)
bool(0)             # False
bool("hello")       # True (any non-empty string is True)
bool("")            # False
```

### String Operations

Strings are sequences of characters. They are immutable.

```python
# Concatenation (joining strings)
full_name = "John" + " " + "Doe" # "John Doe"

# String formatting (f-strings are preferred in modern Python)
first = "Alice"
last = "Smith"
f"My name is {first} {last}"                 # f-strings (Python 3.6+)
"My name is {} {}".format(first, last)       # .format() method
"My name is %s %s" % (first, last)           # Old style (%)

# Common string methods
text = "  Hello World!  "
print(text.lower())        # "  hello world!  "
print(text.upper())        # "  HELLO WORLD!  "
print(text.strip())        # "Hello World!" (removes leading/trailing whitespace)
print(text.replace("World", "Python")) # "  Hello Python!  "
print(text.split())        # ["Hello", "World!"] (splits by whitespace into a list)
print("Python".count('p')) # 1 (case-sensitive)
print("Python".startswith('P')) # True
print("Python".endswith('n'))   # True

# String testing methods
"hello".isalpha()    # True
"123".isdigit()      # True
"HelloWorld".isalnum() # True
" ".isspace()        # True
"Hello World".istitle() # True
```

---

## 2. Control Flow

Control flow statements determine the order in which the program's code is executed.

### If, Elif, Else Statements

Used to execute different blocks of code based on conditions.

```python
age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

score = 75
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
print(f"Your grade is: {grade}")
```

### Comparison Operators

Used to compare two values; they always return a boolean (`True` or `False`).

| Operator | Description                  | Example      | Result  |
| :------- | :--------------------------- | :----------- | :------ |
| `==`     | Equal to                     | `5 == 5`     | `True`  |
| `!=`     | Not equal to                 | `5 != 10`    | `True`  |
| `>`      | Greater than                 | `10 > 5`     | `True`  |
| `<`      | Less than                    | `5 < 10`     | `True`  |
| `>=`     | Greater than or equal to     | `10 >= 10`   | `True`  |
| `<=`     | Less than or equal to        | `5 <= 10`    | `True`  |

### Logical Operators

Combine conditional statements.

| Operator | Description                                     | Example                      | Result  |
| :------- | :---------------------------------------------- | :--------------------------- | :------ |
| `and`    | Returns `True` if both statements are `True`.   | `(5 > 3) and (10 < 20)`      | `True`  |
| `or`     | Returns `True` if at least one statement is `True`. | `(5 > 10) or (10 < 20)`      | `True`  |
| `not`    | Reverses the result, returns `False` if the result is `True`. | `not(5 > 3)`                 | `False` |

```python
is_admin = True
is_editor = False

if is_admin and is_editor:
    print("User has admin and editor privileges.")
elif is_admin or is_editor:
    print("User has either admin or editor privileges.")
if not is_admin:
    print("User is not an administrator.")
```

### Ternary Operator (Conditional Expression)

A compact way to write `if-else` statements.

```python
# Syntax: value_if_true if condition else value_if_false
age = 15
status = "Adult" if age >= 18 else "Minor"
print(status) # Output: Minor

num = 4
result = "Even" if num % 2 == 0 else "Odd"
print(result) # Output: Even
```

---

## 3. Loops

Loops are used to execute a block of code repeatedly.

### For Loops

Used for iterating over a sequence (list, tuple, dictionary, set, or string) or other iterable objects.

```python
# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop through a string
for char in "Python":
    print(char)

# Loop through a range of numbers
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5 (start, stop_exclusive)
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (start, stop_exclusive, step)
    print(i)

# Loop with index using enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Loop through dictionary (default iterates keys)
person = {"name": "Alice", "age": 30}
for key in person:
    print(key) # name, age

for value in person.values():
    print(value) # Alice, 30

for key, value in person.items():
    print(f"{key}: {value}") # name: Alice, age: 30
```

### While Loops

Executes a block of code as long as a condition is true.

```python
count = 0
while count < 3:
    print(count)
    count += 1 # Important to update the condition to avoid infinite loop
# Output: 0, 1, 2

# Example: Password input until correct
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")
```

### Loop Control Statements

*   **`break`**: Terminates the loop entirely.

    ```python
    for i in range(10):
        if i == 5:
            break # Loop stops when i is 5
        print(i)  # Output: 0, 1, 2, 3, 4
    ```

*   **`continue`**: Skips the rest of the current iteration and moves to the next.

    ```python
    for i in range(5):
        if i == 2:
            continue # Skip printing when i is 2
        print(i)  # Output: 0, 1, 3, 4
    ```

*   **`else` with loops**: The `else` block executes if the loop completes normally (without a `break`).

    ```python
    for i in range(3):
        print(i)
    else:
        print("Loop completed normally.")

    # With break:
    for i in range(3):
        if i == 1:
            break
        print(i)
    else:
        print("Loop completed normally.") # This will NOT execute
    ```

---

## 4. Functions

Functions are blocks of reusable code designed to perform a specific task.

### Basic Function Definition

```python
# Simple function without parameters or return value
def say_hello():
    print("Hello!")

say_hello()  # Call the function

# Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)  # result will be 8
print(result)

# Function that returns multiple values (as a tuple)
def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(f"X: {x}, Y: {y}") # Output: X: 10, Y: 20
```

### Parameters & Arguments

```python
# Default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()           # Output: Hello, Guest!
greet("Bob")      # Output: Hello, Bob!

# Keyword arguments
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=25, name="Charlie") # Order doesn't matter with keyword args

# Arbitrary Arguments (*args)
# Allows a function to accept a variable number of non-keyword arguments.
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))        # Output: 6
print(sum_all(10, 20, 30, 40)) # Output: 100

# Arbitrary Keyword Arguments (**kwargs)
# Allows a function to accept a variable number of keyword arguments (as a dictionary).
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="David", age=35, city="London")
# Output:
# name: David
# age: 35
# city: London
```

### Function Scope

Variables are only accessible within the region they are created.

```python
# Global variable
global_message = "I am a global message."

def my_function():
    # Local variable
    local_message = "I am a local message."
    print(global_message) # Can access global_message

my_function()
# print(local_message) # Error: local_message is not defined outside my_function

# Using 'global' keyword to modify a global variable
counter = 0

def increment_counter():
    global counter # Declare intent to modify the global 'counter'
    counter += 1

increment_counter()
print(counter) # Output: 1
```

### Docstrings

Docstrings are string literals that occur as the first statement in a module, function, class, or method definition. They are used to document code.

```python
def calculate_area(length, width):
    """
    Calculates the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

print(calculate_area.__doc__) # Access docstring
```

---

## 5. Built-in Functions

Python comes with a rich set of built-in functions that are always available.

### Common Built-ins

```python
# len(): Returns the length (number of items) of an object.
print(len([1, 2, 3]))         # Output: 3
print(len("Hello"))           # Output: 5

# min(), max(): Returns the smallest/largest item in an iterable.
print(min(1, 5, 3))           # Output: 1
print(max([1, 5, 3]))         # Output: 5

# sum(): Sums the items of an iterable.
print(sum([1, 2, 3, 4, 5]))   # Output: 15

# sorted(): Returns a new sorted list from the items in an iterable.
numbers = [3, 1, 4, 1, 5]
print(sorted(numbers))          # Output: [1, 1, 3, 4, 5]
print(sorted(numbers, reverse=True)) # Output: [5, 4, 3, 1, 1]

# reversed(): Returns a reverse iterator.
print(list(reversed([1, 2, 3]))) # Output: [3, 2, 1]

# round(): Rounds a number to a given precision.
print(round(3.14159, 2))      # Output: 3.14

# abs(): Returns the absolute value of a number.
print(abs(-5))                # Output: 5

# all(): Returns True if all elements of an iterable are true (or if the iterable is empty).
print(all([True, True, True]))   # Output: True
print(all([True, False, True]))  # Output: False

# any(): Returns True if any element of an iterable is true.
print(any([False, False, True]))  # Output: True
print(any([False, False, False])) # Output: False

# zip(): Makes an iterator that aggregates elements from each of the iterables.
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
print(list(zip(names, ages))) # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# enumerate(): Adds a counter to an iterable and returns it as an enumerate object.
for index, value in enumerate(['a', 'b', 'c']):
    print(f"{index}: {value}")
# Output:
# 0: a
# 1: b
# 2: c
```

---

## 6. Error Handling (Try-Except)

Use `try-except` blocks to gracefully handle runtime errors and prevent your program from crashing.

```python
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Division successful.") # Executes if no exception occurred
finally:
    print("Program execution attempted.") # Always executes
```

---

## Best Practices

### Naming Conventions (PEP 8)

*   **Variables and functions:** `snake_case` (e.g., `user_name`, `calculate_total`).
*   **Constants:** `UPPER_CASE` (e.g., `MAX_SIZE`, `API_KEY`).
*   **Classes:** `PascalCase` (covered in the OOP cheat sheet).

### Code Style (Readability)

*   Use meaningful variable and function names.
*   Keep functions focused on a single task (Single Responsibility Principle).
*   Add comments for complex logic (but prefer self-documenting code).

---

## See Also

-   **[Data Structures Cheat Sheet](../cheatsheets/Data_Structures_Cheat_Sheet.md)** - Core data structures like lists, dictionaries, sets, and tuples.
-   **[Functional Programming Cheat Sheet](../cheatsheets/Functional_Programming_Cheat_Sheet.md)** - Concepts like map, filter, and lambda functions.
-   **[OOP Cheat Sheet](../cheatsheets/OOP_Cheat_Sheet.md)** - Object-Oriented Programming principles.
-   **[Regex Cheat Sheet](../cheatsheets/Regex_Cheat_Sheet.md)** - Regular Expressions for pattern matching.
-   **[Big O Notation Cheat Sheet](../cheatsheets/Big_O_Notation_Cheat_Sheet.md)** - Understanding algorithm efficiency.
-   **[Error Handling Cheat Sheet](../cheatsheets/Error_Handling_Cheat_Sheet.md)** - Detailed guide on exception handling.