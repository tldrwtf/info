## Python Basics

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
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def insert_at_position(self, position, data):
        new_node = Node(data)
        current = self.head
        counter = 1
        while counter < position:
            current = current.next
            counter += 1
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_position(self, position):
        current = self.head
        counter = 1
        while counter < position:
            current = current.next
            counter += 1
        node_to_delete = current.next
        current.next = node_to_delete.next
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
## Practice Challenges

### Challenge 1: Smart Shopping List Manager

**Difficulty: Beginner**

```python
"""
Create a shopping list manager that:
1. Allows adding items with quantities and prices
2. Prevents duplicate items (update quantity instead)
3. Shows total cost of all items
4. Finds the most expensive item
5. Removes items by name
6. Shows items sorted by price (high to low)

Example Usage:
add_item("apple", quantity=5, price=1.50)
add_item("banana", quantity=3, price=0.75)
total_cost()  # Returns 9.75
most_expensive()  # Returns ("apple", 7.50)
"""
```

**Concepts tested:** Dictionaries, functions, loops, sorting, max/min operations

### Challenge 2: Grade Book Analyzer

**Difficulty: Intermediate**

```python
"""
Build a gradebook system with a Student class that:
1. Stores student name and list of assignments (dict with assignment: score)
2. Calculates weighted average (tests=50%, homework=30%, projects=20%)
3. Determines letter grade (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60)
4. Tracks grade trends (improving/declining based on last 3 assignments)
5. Compares two students and returns who has better average
6. Implements __str__ method for pretty printing

Create a GradeBook class that:
1. Manages multiple students (dict with name: Student object)
2. Finds top N students
3. Calculates class average
4. Shows students below class average
5. Exports report to formatted string
"""
```

**Concepts tested:** OOP, encapsulation, dictionaries, list comprehension, statistical analysis

### Challenge 3: Task Priority Queue

**Difficulty: Intermediate-Advanced**

```python
"""
Implement a TaskQueue class using a LinkedList that:
1. Each task has: name, priority (1-5), deadline (string), status
2. insert_task() - adds task in priority order (5 = highest)
3. complete_task() - marks first incomplete task as done
4. show_pending() - displays only incomplete tasks
5. overdue_tasks() - returns tasks past deadline (you choose date format)
6. delete_task(name) - removes specific task
7. reorder_priorities() - auto-adjust priorities based on deadline proximity

Time complexity requirement: 
- Insert: O(n) acceptable
- Complete: O(1)
- Show pending: O(n)
"""
```

**Concepts tested:** Linked lists, OOP, custom sorting, time complexity awareness

### Challenge 4: Text Analysis Engine

**Difficulty: Advanced**

```python
"""
Create a TextAnalyzer class that processes text files and provides:

1. word_frequency() - returns dict of word: count (case-insensitive)
2. most_common_words(n) - returns top n words (exclude common words: the, a, an, is, etc.)
3. sentence_count() - counts sentences (. ! ?)
4. average_word_length() - calculates average length
5. find_longest_words(n) - returns n longest unique words
6. reading_time() - estimates time (avg 200 words/minute)
7. lexical_diversity() - unique words / total words ratio
8. word_pairs() - finds most common two-word combinations

Optimization requirement:
- Use sets for unique word tracking
- Use dictionaries for O(1) lookups
- Implement caching for expensive operations
"""
```

**Concepts tested:** String manipulation, sets, dictionaries, algorithm optimization, data analysis

### Challenge 5: Music Playlist Manager (Advanced OOP)

**Difficulty: Advanced**

```python
"""
Build a music streaming system with inheritance and polymorphism:

Base class: MediaItem (attributes: title, artist, duration)
Child classes: Song, Podcast, Audiobook

Playlist class that:
1. Supports different media types
2. Shuffle() - randomize order
3. sort_by(criteria) - sort by title, artist, or duration
4. total_duration() - sum of all items (handle different time formats)
5. create_subset(duration_limit) - generate playlist under time limit
6. remove_duplicates() - keep only unique items
7. merge(other_playlist) - combine two playlists intelligently

User class that:
1. Has multiple playlists
2. favorite_artists() - returns top 3 most frequent artists
3. listening_history - tracks plays with timestamps
4. recommend() - suggests songs based on history (simple algorithm)

Requirements:
- Implement __eq__ for comparing media items
- Use polymorphism for different play() behaviors
- Handle edge cases (empty playlists, invalid durations)
"""
```

**Concepts tested:** Advanced OOP (inheritance, polymorphism, special methods), data structures, algorithm design, real-world system modeling

### Challenge 6: Cache System with Time Complexity

**Difficulty: Expert**

```python
"""
Implement an LRU (Least Recently Used) Cache:

Requirements:
1. Fixed capacity (set at initialization)
2. get(key) - retrieve value, mark as recently used - O(1)
3. put(key, value) - add/update, evict LRU if full - O(1)
4. delete(key) - remove specific item - O(1)
5. clear() - empty cache - O(1)
6. most_used() - return key with highest access count
7. cache_hit_rate() - percentage of successful gets

Implementation constraints:
- Use dictionary + doubly linked list for O(1) operations
- Track access frequency for each item
- Implement custom Node class for doubly linked list
- Thread-safety not required but consider the design

Test your implementation:
- Verify all operations are O(1)
- Test eviction policy works correctly
- Handle edge cases (capacity=1, duplicate puts, etc.)
"""
```

**Concepts tested:** Advanced data structures, time complexity analysis, doubly linked lists, hash tables, system design

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
```
