# Python Cheat Sheet Study Guide - UPDATED 10/17/2025

## Basics

### Variables \& Data Types

```python
# Variable assignment
name = "Allan"
age = 28
price = 3.14
is_active = True

# Type checking
type(variable)  # Returns the type
isinstance(value, int)  # Check if value is int
isinstance(value, (int, float))  # Check multiple types
```


### Input \& Output

```python
# Getting user input
username = input("Enter your name: ")
age = int(input("Enter age: "))  # Convert to integer

# Printing
print("Hello")
print(f"Hello, {name}!")  # f-string formatting
print(f"Average: {total/count:.2f}")  # 2 decimal places
```


## Control Flow

### Conditional Statements

```python
# Basic if-elif-else
if condition:
    # code
elif another_condition:
    # code
else:
    # code

# Comparison operators: ==, !=, <, >, <=, >=
if x % 2 == 1:
    print("odd")
else:
    print("even")

# Logical operators: and, or, not
if age >= 18 and has_license:
    print("Can drive")
```


### Truthy \& Falsy Values

```python
# Falsy: 0, "", [], {}, (), None, False
grocery_list = []
if grocery_list:
    print("Time to shop")
else:
    print("Nothing to buy")
```


## Loops

### While Loops

```python
# Basic while loop
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

# Infinite loop with break
while True:
    answer = input("Type 'exit' to stop: ")
    if answer == "exit":
        break

# Continue - skip iteration
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
```


### For Loops

```python
# Loop through range
for i in range(5):  # 0 to 4
    print(i)

# Loop through list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Loop through string
for letter in "ABC":
    print(letter)

# Enumerate - get index and value
for index, fruit in enumerate(fruits):
    print(f"At index {index}: {fruit}")
```


## Lists

### List Basics

```python
# Creating lists
movies = ["Inception", "The Matrix", "Interstellar"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Alice", 25, True, 3.14]
empty = []

# Accessing elements
movies[^0]        # First element
movies[-1]       # Last element
movies[1:3]      # Slicing [start:stop]
movies[:2]       # First 2 elements
movies[2:]       # From index 2 to end
movies[::-1]     # Reverse list
```


### List Methods - Time Complexity

```python
# Adding elements
mylist.append(item)        # O(1) - add to end
mylist.insert(2, item)     # O(n) - insert at position
mylist.extend([1, 2, 3])   # O(k) - add multiple items

# Removing elements
mylist.pop()               # O(1) - remove last
mylist.pop(1)              # O(n) - remove by index
mylist.remove(item)        # O(n) - remove by value
del mylist[^3]              # O(n) - delete by index
mylist.clear()             # O(1) - empty list

# Other operations
len(mylist)                # O(1) - length
mylist.count(item)         # O(n) - count occurrences
mylist.index(item)         # O(n) - find index
mylist.reverse()           # O(n) - reverse in-place
mylist.sort()              # O(n log n) - sort in-place
sorted(mylist)             # O(n log n) - return sorted copy

# Membership check
if item in mylist:         # O(n) - linear search
    print("Found")
```


## Dictionaries

### Dictionary Basics

```python
# Creating dictionaries
student = {"name": "Maya", "age": 22, "major": "CS"}
empty_dict = {}

# Accessing values
student["name"]                    # Direct access - O(1)
student.get("age")                 # Safe access - O(1)
student.get("grade", "N/A")        # With default value

# Adding/Modifying
student["age"] = 28                # O(1)
student["gpa"] = 3.8              # O(1)

# Removing
del student["major"]               # O(1)
removed = student.pop("age")       # O(1)

# Membership check
if "name" in student:              # O(1) - constant time
    print(f"Name: {student['name']}")
```


### Looping Through Dictionaries

```python
menu = {"burger": 14.50, "salad": 27.0, "fries": 2.50}

# Loop keys (default)
for item in menu:
    print(item)

# Loop values
for price in menu.values():
    print(price)

# Loop key-value pairs
for food, price in menu.items():
    print(f"{food}: ${price}")

# Get all keys/values
keys = list(menu.keys())
values = list(menu.values())
```


### Nested Dictionaries

```python
contact = {
    "Billy": {
        "phone": "12345678",
        "email": "billy@billy.com",
        "address": {"street": "1123 fun street", "city": "Python City"}
    }
}

# Accessing nested data
contact["Billy"]["phone"]
contact["Billy"]["address"]["city"]
```


## Functions

### Function Basics

```python
# Basic function
def greet(name):
    print(f"Hello, {name}!")

# Function with return
def add(num1, num2):
    return num1 + num2

# Multiple return values
def divide_with_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# Using returned values
result = add(5, 8)
q, r = divide_with_remainder(10, 3)
```


### Parameters \& Arguments

```python
# Default parameters
def introduce(name, title="Mr./Mrs"):
    print(f"Hello, {title} {name}!")

introduce("Bob")              # Uses default
introduce("Sally", "Mrs.")    # Override default

# Multiple default parameters
def calculate_interest(principal, rate=0.05, years=1):
    return principal * (1 + rate) ** years

# Positional vs keyword arguments
introduce("John", "Mr.")           # Positional
introduce(name="John", title="Mr.") # Keyword
```


## String Methods

### Common String Operations

```python
text = "  HeLlo WOrLd!  "

# Case conversion (out-of-place - returns new string)
text.lower()      # "  hello world!  "
text.upper()      # "  HELLO WORLD!  "
text.title()      # "  Hello World!  "

# Whitespace
text.strip()      # "HeLlo WOrLd!" - remove leading/trailing
text.strip("!")   # Remove specific characters

# Testing
"12345".isdigit()          # True - all digits
"AllanAhmed".isalpha()     # True - all letters
"allan123".isalnum()       # True - letters/numbers

# Searching
sentence = "Python-is-fun-and-Python-is-powerful"
sentence.count("Python")   # 2 - count occurrences
sentence.find("power")     # 26 - starting index (-1 if not found)

# Splitting and joining
words = sentence.split("-")         # Split into list
joined = " ".join(words)            # Join list with space

# Membership
if "-" in sentence:
    print("Has hyphens")
```


## Sets \& Tuples

### Sets (Unique, Unordered)

```python
# Creating sets
unique_numbers = {1, 2, 3, 4, 5}
empty_set = set()  # {} creates empty dict

# Remove duplicates
alist = [1, 1, 2, 2, 3, 3]
unique = set(alist)  # {1, 2, 3}
back_to_list = list(unique)

# Adding/Removing
fruits = {"apple", "orange"}
fruits.add("banana")
fruits.update(["grapes", "pears"])
fruits.discard("apple")  # No error if not found
fruits.remove("orange")  # Raises error if not found

# Set operations
set1 = {1, 2, 3, 4}
set2 = {2, 4, 6, 8}
set1.union(set2)          # {1, 2, 3, 4, 6, 8}
set1.intersection(set2)   # {2, 4}
set1.difference(set2)     # {1, 3}
set1 - set2               # Same as difference
```


### Tuples (Immutable)

```python
# Creating tuples
coordinates = (3, 4)
singleton = (1,)  # Comma required for single item
empty_tuple = ()

# Accessing (like lists)
first, second = coordinates  # Unpacking

# Immutable - cannot modify
# coordinates[^0] = 5  # TypeError

# Zip - combine lists
foods = ["Pizza", "steak", "nachos"]
prices = [20, 63.5, 12]
zipped = list(zip(foods, prices))
# [("Pizza", 20), ("steak", 63.5), ("nachos", 12)]

for food, price in zip(foods, prices):
    print(f"{food}: ${price}")
```


## Functional Programming

### Lambda Functions

```python
# Basic lambda syntax
# lambda parameters: expression

# Regular function
def calculate_tax(price):
    return price * 0.07

# Lambda equivalent
calculate_tax = lambda price: price * 0.07
print(calculate_tax(15))  # 1.05

# Lambda for sorting
products = [
    {'name': 'laptop', 'price': 999.99},
    {'name': 'mouse', 'price': 64.99},
    {'name': 'keyboard', 'price': 129.99}
]

# Sort by price (descending)
sorted_products = sorted(products, key=lambda p: p["price"], reverse=True)

# Sort by multiple criteria
by_category_name = sorted(products, key=lambda p: (p['category'], p['name']))
```


### Map Function

```python
# Map applies a function to each item in a list
numbers = [1, 2, 3, 4, 5]

# Traditional approach
def double_nums(alist):
    output = []
    for num in alist:
        output.append(num * 2)
    return output

# Using map with lambda
doubled = list(map(lambda num: num * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Map with complex data
users = [
    {'name': 'PETER COTTONTAIL', 'email': 'PCOTTON@EMAIL.COM'},
    {'name': 'TONY STARK', 'email': 'TONYS@EMAIL.COM'}
]

# Normalize data
def normalize_user(user):
    return {
        'name': user['name'].title(),
        'email': user['email'].lower(),
        'username': user['name'].split()[^0].lower()
    }

normalized_users = list(map(normalize_user, users))
```


### Filter Function

```python
# Filter creates a new list based on a condition
numbers = [1, 2, 3, 4, 5]

# Traditional approach
def only_evens(nums):
    output = []
    for num in nums:
        if num % 2 == 0:
            output.append(num)
    return output

# Using filter with lambda
evens = list(filter(lambda num: num % 2 == 0, numbers))
print(evens)  # [2, 4]

# Filter with user-defined function
def is_even(num):
    return num % 2 == 0

evens = list(filter(is_even, numbers))

# Real-world example
books = [
    {'title': 'Python Programming', 'rating': 4.5, 'available': True},
    {'title': 'Web Development', 'rating': 3.8, 'available': False},
    {'title': 'Data Science', 'rating': 4.9, 'available': True}
]

# Find available books with rating >= 4.0
quality_books = list(filter(lambda book: book['available'] and book['rating'] >= 4.0, books))
```


### List Comprehensions

```python
# Syntax: [expression for item in list if condition]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Double all numbers
doubled = [num * 2 for num in numbers]

# Get only evens
evens = [num for num in numbers if num % 2 == 0]

# Double only evens (combining map + filter)
doubled_evens = [num * 2 for num in numbers if num % 2 == 0]

# Combining with functions
def double_only_evens(nums):
    return [num * 2 for num in nums if num % 2 == 0]

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```


## Object-Oriented Programming

### Class Basics

```python
class Student:
    # Constructor
    def __init__(self, name, age, grades):
        self.name = name      # Instance attribute
        self.age = age
        self.grades = grades
    
    # Instance method
    def info(self):
        print(f"My name is {self.name} and I am {self.age}")
    
    def grade_avg(self):
        return sum(self.grades) / len(self.grades)
    
    def add_grade(self, grade):
        self.grades.append(grade)

# Creating objects
allan = Student("Allan", 99, [45, 90])
allan.info()
print(allan.grade_avg())
```


### Four Pillars of OOP

```python
# 1. ENCAPSULATION - Bundling data and methods
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email      # Protected (convention)
        self._password = password
    
    # Getter
    def get_email(self):
        return self._email
    
    # Setter with validation
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            return "Invalid email"

# 2. INHERITANCE - Child inherits from parent
class Character:
    def __init__(self, name, health, attack_power=10):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self, opponent):
        opponent.health -= self.attack_power

class Warrior(Character):  # Inherits from Character
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)
    
    # 3. POLYMORPHISM - Override parent method
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} slashes with sword!")
    
    def special_attack(self, opponent):
        opponent.health -= self.attack_power * 2

# 4. ABSTRACTION - Hide complexity
warrior = Warrior("Conan")  # Simple interface
warrior.attack(enemy)       # Complex implementation hidden
```


## Advanced Data Structures

### Stacks (LIFO - Last In, First Out)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None  # Top of stack
        self.tail = None  # Bottom of stack
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    def push(self, item):
        """Add item to top of stack - O(1)"""
        new_node = Node(item)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.size += 1
    
    def pop(self):
        """Remove and return top item - O(1)"""
        if self.is_empty():
            return None
        
        item = self.head.data
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
        
        self.size -= 1
        return item
    
    def peek(self):
        """View top item without removing - O(1)"""
        if self.is_empty():
            return None
        return self.head.data

# Using Python list as stack (simpler)
stack = []
stack.append(1)    # Push - O(1)
stack.append(2)
stack.append(3)
top = stack.pop()  # Pop - O(1)
peek = stack[-1]   # Peek - O(1)
```


### Queues (FIFO - First In, First Out)

```python
from collections import deque

# Using deque for efficient queue operations
queue = deque()

# Enqueue (add to end) - O(1)
queue.append("first")
queue.append("second")
queue.append("third")

print(f"Queue: {queue}")

# Dequeue (remove from front) - O(1)
front_item = queue.popleft()  # IMPORTANT: O(1) time
print(f"Dequeued: {front_item}")
print(f"Queue after: {queue}")

# Peek front
if queue:
    front = queue[^0]  # O(1)

# Note: Regular list pop(0) is O(n) - DON'T USE for queues
```


## Linked Lists

### Node \& LinkedList Implementation

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        """Add node to end - O(1) with tail"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node
    
    def traverse(self):
        """Visit all nodes - O(n)"""
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def insert_at_position(self, position, data):
        """Insert at specific position - O(n)"""
        new_node = Node(data)
        current = self.head
        counter = 1
        while counter < position:
            current = current.next
            counter += 1
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_position(self, position):
        """Delete at specific position - O(n)"""
        current = self.head
        counter = 1
        while counter < position:
            current = current.next
            counter += 1
        node_to_delete = current.next
        current.next = node_to_delete.next
    
    def get_at_position(self, position):
        """Get node at position - O(n)"""
        current = self.head
        counter = 1
        while counter < position and current:
            current = current.next
            counter += 1
        return current.data if current else None
```


### Real-World Example: Music Playlist

```python
from linked_list import Node, LinkedList

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class MusicPlaylist:
    def __init__(self, name):
        self.name = name
        self.songs = LinkedList()
        self.current_position = -1
    
    def add_song(self, title, artist, duration):
        song = Song(title, artist, duration)
        self.songs.append(song)
    
    def display(self):
        """Show all songs in playlist"""
        print(f"============= {self.name} =============")
        current = self.songs.head
        counter = 1
        while current:
            print(f"{counter}.) {current.data.title} - {current.data.artist}")
            current = current.next
            counter += 1
    
    def play_song_at_position(self, position):
        song = self.songs.get_at_position(position)
        self.current_position = position
        if song:
            print(f"Now playing: {song.title} by {song.artist}")
        else:
            print("Song not found")

# Usage
playlist = MusicPlaylist("My Favorites")
playlist.add_song("Bohemian Rhapsody", "Queen", "5:55")
playlist.add_song("Stairway to Heaven", "Led Zeppelin", "8:02")
playlist.display()
playlist.play_song_at_position(1)
```


## Time Complexity (Big O)

### Common Time Complexities

```python
# O(1) - Constant
x = 10
y = x + 1
dict_value = my_dict["key"]

# O(log n) - Logarithmic
# Binary search

# O(n) - Linear
for item in alist:
    print(item)

# O(n log n) - Linear Logarithmic
sorted_list = sorted(mylist)
mylist.sort()

# O(n²) - Quadratic (nested loops)
for num1 in nums:
    for num2 in nums:
        if num1 + num2 == target:
            return (num1, num2)
```


### Data Structure Operations

```python
# Lists
mylist[i]           # O(1) - access by index
mylist.append(x)    # O(1) - add to end
mylist.insert(i, x) # O(n) - insert at position
mylist.pop()        # O(1) - remove last
mylist.pop(i)       # O(n) - remove by index
x in mylist         # O(n) - membership check

# Dictionaries
mydict[key]         # O(1) - access
mydict[key] = val   # O(1) - add/modify
del mydict[key]     # O(1) - remove
key in mydict       # O(1) - membership check

# Sets
myset.add(x)        # O(1) - add element
x in myset          # O(1) - membership check
myset.remove(x)     # O(1) - remove element
```


## Error Handling

### Try-Except Blocks

```python
# Basic try-except
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Try-except-else
try:
    age = int(input("Age: "))
except ValueError:
    return None
else:
    return f"User age: {age}"

# Exception with variable
try:
    print(mylist[^6])
except IndexError as e:
    print(f"Error: {e}")
```


## Built-in Functions

### Commonly Used

```python
# Numeric
sum(numbers)           # Sum of list
max(numbers)           # Maximum value
min(numbers)           # Minimum value
abs(-5)                # Absolute value
round(56.789, 2)       # Round to 2 decimals

# Length
len(mylist)            # Length of list/string/dict

# Range
range(5)               # 0, 1, 2, 3, 4
range(1, 6)            # 1, 2, 3, 4, 5
range(0, 10, 2)        # 0, 2, 4, 6, 8

# Type conversion
int("42")              # String to int
float("3.14")          # String to float
str(123)               # Number to string
list(range(5))         # Range to list

# Sorting
sorted(mylist)         # Return sorted copy (out-of-place)
mylist.sort()          # Sort in-place
```


***

## PRACTICE CHALLENGES (UPDATED)

Test your understanding with these progressively challenging exercises:

### Challenge 1: Product Inventory Manager (Functional Programming)

**Difficulty: Beginner-Intermediate**

```python
"""
You have a product inventory as a list of dictionaries:
products = [
    {'name': 'Wireless Headphones', 'price': 89.99, 'category': 'Electronics', 'stock': 45},
    {'name': 'Coffee Maker', 'price': 129.99, 'category': 'Appliances', 'stock': 12},
    {'name': 'Running Shoes', 'price': 79.99, 'category': 'Sports', 'stock': 23},
    {'name': 'Bluetooth Speaker', 'price': 59.99, 'category': 'Electronics', 'stock': 67}
]

Tasks:
1. Use sorted() with lambda to sort by price (highest first)
2. Use sorted() with lambda to sort by category, then name alphabetically
3. Use map() with lambda to apply 7% tax to all prices
4. Use filter() with lambda to find products with stock < 20
5. Use list comprehension to create list of product names in Electronics category
6. Chain map and filter to get prices of Electronics items, then apply 10% discount

Bonus: Combine all into a pipeline that:
- Filters low-stock items
- Applies discount
- Sorts by discounted price
- Returns just names and final prices
"""
```

**Concepts tested:** Lambda functions, map, filter, sorted, list comprehensions, functional chaining

### Challenge 2: Employee Salary Processor

**Difficulty: Intermediate**

```python
"""
Given employee data:
employees = [
    {'name': 'Alice Johnson', 'job': 'Developer', 'salary': 75000},
    {'name': 'Bob Smith', 'job': 'Designer', 'salary': 65000},
    {'name': 'Carol Davis', 'job': 'Manager', 'salary': 85000}
]

Use ONLY functional programming (map/filter/lambda/comprehensions):
1. Apply 7% raise to all employees
2. Filter employees earning > $70,000
3. Create new dicts with 'annual_bonus' = salary * 0.15
4. Generate formatted strings: "Name (Job): $Salary"
5. Find average salary using sum() and len()
6. Group employees by job title using dictionary comprehension

Constraint: NO traditional for loops allowed!
"""
```

**Concepts tested:** Functional programming paradigm, data transformation, lambda expressions

### Challenge 3: Music Playlist with Linked List

**Difficulty: Advanced**

```python
"""
Implement a MusicPlaylist class using LinkedList that supports:

1. add_song(title, artist, duration) - adds to end
2. insert_song(position, title, artist, duration) - insert at position
3. remove_song(title) - removes by title
4. play_next() - moves to next song in playlist
5. play_previous() - moves to previous song
6. shuffle() - randomizes order (challenging with linked list!)
7. repeat_mode(mode) - supports "off", "one", "all"
8. current_song() - returns currently playing song
9. total_duration() - sums all song durations (format: MM:SS)
10. find_by_artist(artist) - returns all songs by artist

Additional requirements:
- Track current position in playlist
- Support removing current song (auto-advance to next)
- Handle edge cases (empty playlist, invalid position)
- Implement __str__() for pretty printing

Time complexity goals:
- add_song: O(1)
- play_next/previous: O(1)
- remove_song: O(n)
- shuffle: O(n)
"""
```

**Concepts tested:** Linked lists, OOP, doubly linked lists (bonus), state management, edge cases

### Challenge 4: Stack-Based Expression Evaluator

**Difficulty: Advanced**

```python
"""
Create an expression evaluator using a Stack data structure:

Implement:
1. evaluate(expression) - evaluates postfix notation (RPN)
   Example: "5 3 + 2 *" = 16
   
2. infix_to_postfix(expression) - converts standard to RPN
   Example: "5 + 3 * 2" = "5 3 2 * +"
   
3. check_balanced_parentheses(expression) - validates brackets
   Example: "((5 + 3) * 2)" = True
   Example: "((5 + 3)" = False
   
4. undo_redo_calculator() - calculator with undo/redo using two stacks
   Commands: ADD, SUB, MULT, DIV, UNDO, REDO

Requirements:
- Implement your own Stack class (no list built-ins for stack operations)
- Handle operator precedence for infix_to_postfix
- Support (), [], {} for balanced check
- Calculator must maintain history

Example calculator session:
>>> calc = UndoRedoCalculator()
>>> calc.perform("ADD", 5)  # Result: 5
>>> calc.perform("MULT", 3)  # Result: 15
>>> calc.perform("SUB", 2)   # Result: 13
>>> calc.undo()              # Result: 15
>>> calc.undo()              # Result: 5
>>> calc.redo()              # Result: 15
"""
```

**Concepts tested:** Stacks, algorithm implementation, parsing, state management, LIFO operations

### Challenge 5: Task Queue Management System

**Difficulty: Advanced**

```python
"""
Build a task management system using Queue (deque) and Priority concepts:

Implement TaskManager class:
1. add_task(name, priority, deadline) - adds task to appropriate queue
2. complete_next_task() - processes highest priority task first
3. view_upcoming(n) - shows next n tasks without removing
4. reschedule_task(name, new_deadline) - updates task deadline
5. cancel_task(name) - removes task from queues
6. tasks_by_priority(priority) - filters and returns tasks
7. overdue_tasks() - returns tasks past deadline
8. task_report() - generates formatted summary

Architecture:
- Use 3 separate queues: high_priority, medium_priority, low_priority
- Always process high before medium, medium before low
- Track completed tasks with timestamps
- Implement deadline parsing (string format: "YYYY-MM-DD")

Additional features:
- Auto-escalate priority if deadline approaching (< 2 days)
- Track average completion time per priority level
- Prevent duplicate task names
- Implement task dependencies (task B requires task A completed first)

Time complexity requirements:
- add_task: O(1)
- complete_next_task: O(1)
- find/cancel_task: O(n) acceptable
"""
```

**Concepts tested:** Queues, deque operations, priority management, real-world system design, FIFO

### Challenge 6: Text Analysis Engine (Functional + OOP)

**Difficulty: Advanced**

```python
"""
Create a TextAnalyzer class combining functional programming and OOP:

Implement using METHOD CHAINING:
analyzer = TextAnalyzer(text)
    .remove_stopwords()
    .lowercase()
    .get_word_frequency()
    .filter_by_min_count(3)
    .sort_by_frequency()
    .get_results()

Methods:
1. remove_stopwords() - removes common words (the, a, is, etc.)
2. lowercase() - converts all text to lowercase
3. get_word_frequency() - counts word occurrences
4. filter_by_min_count(n) - keeps words appearing >= n times
5. sort_by_frequency(descending=True) - sorts results
6. most_common_pairs() - finds frequent two-word combinations
7. reading_level() - calculates Flesch reading score
8. sentiment_score() - basic positive/negative word counting
9. export_to_dict() - returns data as dictionary
10. visualize_top(n) - creates ASCII bar chart of top n words

Requirements:
- Use map/filter/comprehensions where possible
- Support method chaining (return self)
- Implement __repr__() for object inspection
- Cache expensive operations
- Handle punctuation and special characters

Bonus challenge:
- Compare two texts and find common vocabulary
- Generate word cloud data structure (word + size)
- Identify sentences containing specific patterns using regex
"""
```

**Concepts tested:** OOP, functional programming, method chaining, data analysis, string manipulation

### Challenge 7: Custom Iterator with Generator Functions

**Difficulty: Expert**

```python
"""
Implement custom iterators and generators:

1. fibonacci_generator(n) - yields first n Fibonacci numbers
   Usage: for num in fibonacci_generator(10): print(num)

2. LinkedListIterator - make LinkedList iterable
   Usage: for item in my_linked_list: print(item)

3. chunk_iterator(data, size) - yields chunks of specified size
   Example: list(chunk_iterator([1,2,3,4,5], 2)) = [[1,2], [3,4], [^5]]

4. infinite_sequence(start, step) - infinite generator with takewhile
   Usage: from itertools import takewhile
          nums = takewhile(lambda x: x < 100, infinite_sequence(0, 5))

5. nested_dict_walker(d) - recursively walks nested dictionaries
   Yields (key_path, value) tuples
   Example: {'a': {'b': 1, 'c': 2}} yields ('a.b', 1), ('a.c', 2)

6. Custom range with float support: frange(start, stop, step=0.1)

Requirements:
- Use yield keyword (no manual iterator protocol)
- Support both for-loop and next() usage
- Handle StopIteration properly
- Implement __iter__() and __next__() for LinkedList

Advanced challenge:
- Create bidirectional iterator (forward and backward)
- Implement iterator with peek() method (look ahead without consuming)
- Create iterator pipeline: filter -> map -> take(n)
"""
```

**Concepts tested:** Generators, iterators, yield, lazy evaluation, advanced Python patterns

***

## Quick Reference Tips

**DRY Principle:** Don't Repeat Yourself - use functions and loops

**Naming Conventions:**

- Variables/functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`

**Common Patterns:**

```python
# Swap variables
a, b = b, a

# Multiple assignment
x = y = z = 0

# Conditional expression
result = "even" if x % 2 == 0 else "odd"

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in numbers if x % 2 == 0]

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}

# Combining map + filter (functional approach)
result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))

# Equivalent list comprehension (more Pythonic)
result = [x * 2 for x in numbers if x % 2 == 0]
```

