# Python Cheat Sheet -

Update now includes **Regular Expressions (Regex)**, **Control Flow**, and all foundational Python concepts.

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

# Multiple conditions with and/or
age = 25
is_weekend = True

if age >= 18 and is_weekend:
    print("Can enter club on weekend")
    
# NOT operator reverses truth
if not is_weekend:
    print("It's a weekday")
```


### Grade Evaluation Example

```python
score = int(input("Enter your test score: "))

if score >= 90 and score <= 100:
    print("Grade: A - Excellent!")
elif score >= 80 and score < 90:
    print("Grade: B - Good Job!")
elif score >= 70 and score < 80:
    print("Grade: C - Satisfactory")
elif score >= 60 and score < 70:
    print("Grade: D - Needs improvement")
elif score >= 1 and score < 60:
    print("Grade: F - Please see teacher")
else:
    print("Invalid score")
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
    print("Still loading...")

# Continue - skip iteration
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)  # Skips printing 3

# Countdown example
number = 10
while number >= 1:
    print(number)
    number = number - 1
print("Blast Off!")
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
    print(f"Character: {letter}")

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

# Membership check - O(1) constant time
if "name" in student:
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

# Library example
library = {
    "book1": {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    },
    "book2": {
        "title": "Brave New World",
        "author": "Aldous Huxley"
    }
}
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

# Format phone number with defaults
def format_phone_number(number, country_code="+1"):
    return f"{country_code}-{number}"
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

# Real-world example
allan_hobbies = {"coding", "gaming", "reading"}
peter_hobbies = {"gaming", "hiking", "reading"}
common_interests = allan_hobbies.intersection(peter_hobbies)
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


## Regular Expressions (Regex)

### Regex Basics

```python
import re

# re.search() - finds FIRST match, returns match object
text = "My phone is 555-1234"
match = re.search(r"\d+", text)  # Finds "555"
if match:
    print(match.group())  # Unpack with .group()

# re.findall() - finds ALL occurrences, returns list
numbers = re.findall(r"\d+", "I have 5 cats and 3 dogs")
print(numbers)  # ['5', '3']

# re.match() - checks if text STARTS with pattern
result = re.match(r"Hello", "Hello world")  # Match object
result = re.match(r"Hello", "world Hello")  # None

# re.sub() - find and replace (powerful .replace())
text = "I love cats. cats are great."
new_text = re.sub(r"cats", "dogs", text)
```


### Metacharacters

```python
import re

# \d - any digit (0-9)
re.findall(r"\d", "abc123xyz")  # ['1', '2', '3']

# \w - word character (letters, digits, underscores)
re.findall(r"\w+", "hello_world123")  # ['hello_world123']

# \s - whitespace (spaces, tabs, newlines)
re.findall(r"\s", "hello world")  # [' ']

# . - wildcard (any character except newline)
re.findall(r".", "abc")  # ['a', 'b', 'c']
```


### Quantifiers

```python
# + means "one or more"
re.findall(r"\d+", "I have 123 apples and 45 oranges")
# ['123', '45']

# * means "zero or more"
re.findall(r"\d*", "abc123")  # ['', '', '', '123', '']

# ? means "zero or one"
re.findall(r"colou?r", "color colour")  # ['color', 'colour']

# {n} means "exactly n times"
re.findall(r"\d{3}", "123 45 6789")  # ['123', '678']

# {n,m} means "between n and m times"
re.findall(r"\d{2,4}", "1 12 123 1234 12345")
# ['12', '123', '1234', '1234']

# \b - word boundary
re.findall(r"\bcat\b", "cat cats scatter")  # ['cat']
```


### Character Sets

```python
# [] allows custom character matching
re.findall(r"[aeiou]", "hello")  # ['e', 'o'] - vowels

# Ranges
re.findall(r"[a-z]+", "Hello123World")  # ['ello', 'orld']
re.findall(r"[0-9]", "abc123")  # ['1', '2', '3']
re.findall(r"[A-Z]", "Hello World")  # ['H', 'W']

# Partial ranges
re.findall(r"[0-5]", "0123456789")  # ['0', '1', '2', '3', '4', '5']

# Email pattern example
pattern = r"[a-zA-Z0-9._+-]+@[a-zA-Z_]+\.[a-z]{2,3}"
emails = re.findall(pattern, "Contact: john@email.com or sally@test.org")
```


### Groups and Substitution

```python
# Groups () - capture patterns
text = "John Smith, 555-1234"
match = re.search(r"(\w+) (\w+), (\d{3}-\d{4})", text)
if match:
    first = match.group(1)  # "John"
    last = match.group(2)   # "Smith"
    phone = match.group(3)  # "555-1234"

# Named groups
pattern = r"(?P<first>\w+) (?P<last>\w+)"
match = re.search(pattern, "John Smith")
print(match.group('first'))  # "John"

# Rearranging with sub
date = "12/25/2024"
new_format = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\1-\2", date)
print(new_format)  # "2024-12-25"

# Replace phone numbers for privacy
feedback = "Call me at 555-0123 for details"
cleaned = re.sub(r"\d{3}-\d{4}", "[PHONE REMOVED]", feedback)
```


### Compile (Store Patterns)

```python
# Compile for reuse
email_pattern = re.compile(r"[a-zA-Z0-9._+-]+@[a-zA-Z_]+\.[a-z]{2,3}")

# Use compiled pattern
text1 = "Email: john@test.com"
text2 = "Contact: sarah@company.org"

emails1 = email_pattern.findall(text1)
emails2 = email_pattern.findall(text2)
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

# Lambda with conditionals (ternary operator)
check_even = lambda x: "even" if x % 2 == 0 else "odd"
print(check_even(4))  # "even"
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

# Real-world data processing
employees = [
    {'name': 'Alice', 'job': 'Developer', 'salary': 75000},
    {'name': 'Bob', 'job': 'Designer', 'salary': 65000}
]

# High-earning developers
high_devs = [emp['name'] for emp in employees 
             if emp['job'] == 'Developer' and emp['salary'] > 70000]

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
    
    def remove_last_grade(self):
        if self.grades:
            self.grades.pop()
    
    def clear_grades(self):
        self.grades.clear()

# Creating objects
allan = Student("Allan", 99, [45, 90])
allan.info()
print(allan.grade_avg())
allan.add_grade(85)
```


### Encapsulation

```python
class User:
    def __init__(self, username, email, password):
        # Public attribute
        self.username = username
        # Protected attributes (convention with _)
        self._email = email
        self._password = password
    
    # Getter methods
    def get_email(self):
        return self._email
    
    def get_password(self):
        return self._password
    
    # Setter methods with validation
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email
            return "Email updated"
        else:
            return "Invalid email"
    
    def set_password(self, new_password):
        if len(new_password) >= 8 and "!" in new_password:
            self._password = new_password
            return "Password changed"
        else:
            return "Invalid password"

# Usage
user = User("alice", "alice@email.com", "pass!123")
print(user.get_email())
user.set_email("newemail@test.com")
```


### Inheritance \& Polymorphism

```python
# Parent Class
class Character:
    def __init__(self, name, health, attack_power=10):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name}")
    
    def display_stats(self):
        print(f"{self.name} - Health: {self.health}, Attack: {self.attack_power}")

# Child class (Inheritance)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)
    
    # Polymorphism - Override parent method
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} slashes with sword!")
    
    def special_attack(self, opponent):
        opponent.health -= self.attack_power * 2
        print(f"{self.name} uses POWER STRIKE!")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=30)
    
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} casts a spell!")

# Usage - Abstraction (simple interface, complex implementation hidden)
warrior = Warrior("Conan")
mage = Mage("Gandalf")

warrior.attack(mage)  # Different behavior for each class
warrior.special_attack(mage)
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
# Always use deque for queue operations!
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
        if self.is_empty():
            print("List is empty")
            return
        
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def insert_at_position(self, position, data):
        """Insert at specific position - O(n)"""
        new_node = Node(data)
        
        # Case 1: Insert at beginning
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return
        
        # Case 2: Insert elsewhere
        current = self.head
        counter = 1
        
        while counter < position - 1 and current:
            current = current.next
            counter += 1
        
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_position(self, position):
        """Delete at specific position - O(n)"""
        if self.is_empty():
            print("List is empty")
            return
        
        # Case 1: Delete head
        if position == 1:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        
        # Case 2: Delete elsewhere
        current = self.head
        counter = 1
        
        while counter < position - 1 and current:
            current = current.next
            counter += 1
        
        if current and current.next:
            node_to_delete = current.next
            current.next = node_to_delete.next
            
            # If deleting last node, update tail
            if current.next is None:
                self.tail = current
    
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
    
    def next_song(self):
        if self.current_position != -1:
            self.current_position += 1
            self.play_song_at_position(self.current_position)
    
    def previous_song(self):
        if self.current_position > 1:
            self.current_position -= 1
            self.play_song_at_position(self.current_position)

# Usage
playlist = MusicPlaylist("My Favorites")
playlist.add_song("Bohemian Rhapsody", "Queen", "5:55")
playlist.add_song("Stairway to Heaven", "Led Zeppelin", "8:02")
playlist.display()
playlist.play_song_at_position(1)
playlist.next_song()
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

# Dictionaries (Hash Tables)
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
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a valid number")

print("Program continues...")

# Multiple exceptions
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

# Type checking
isinstance(value, int)
type(variable)
```


***

## COMPREHENSIVE PRACTICE CHALLENGES

### Challenge 1: Data Cleaning with Regex

**Difficulty: Beginner**

```python
"""
You have messy customer feedback data. Use regex to:

feedback_list = [
    "Great service! Call me at 555-1234. Email: john@email.com",
    "Terrible    experience    with   extra   spaces!!!",
    "My order #12345 arrived on 12/25/2024. Phone: 555-9876"
]

Tasks:
1. Remove all phone numbers (format: ###-####) and replace with "[REDACTED]"
2. Clean up multiple spaces (2+) into single spaces
3. Extract all email addresses
4. Extract all dates (format: MM/DD/YYYY)
5. Extract order numbers (format: #followed by 5 digits)
6. Count exclamation marks in each feedback
7. Find feedback containing words starting with 'T' or 't'

Bonus: Create a clean_feedback() function that takes raw feedback 
and returns a sanitized dictionary with extracted data
"""
```

**Concepts tested:** Regex patterns, metacharacters, quantifiers, character sets, groups, re.sub(), re.findall()

### Challenge 2: Smart Product Inventory (Functional + OOP)

**Difficulty: Intermediate**

```python
"""
Build an inventory system combining functional programming and OOP:

Create Product class with:
- Attributes: name, category, price, stock, supplier
- Methods: restock(), sell(), apply_discount()
- Property decorators for calculated fields

Create Inventory class with:
- Uses dictionary to store products (key: product_id)
- filter_products(criteria) - uses lambda/filter
- sort_products(by="price", descending=False) - uses lambda/sorted
- low_stock_alert(threshold=10) - list comprehension
- total_value() - map + sum
- category_report() - dictionary comprehension
- bulk_discount(category, percentage) - map with conditional

Requirements:
- Use map() to apply 7% tax to all product prices
- Use filter() to find products with stock < threshold
- Use list comprehension for fast queries
- Use lambda for custom sorting (price, name, stock)
- Implement __str__ and __repr__ for Product class

Test with:
products = [
    {'id': 1, 'name': 'Laptop', 'category': 'Electronics', 'price': 999, 'stock': 5},
    {'id': 2, 'name': 'Mouse', 'category': 'Electronics', 'price': 25, 'stock': 50},
    {'id': 3, 'name': 'Desk', 'category': 'Furniture', 'price': 299, 'stock': 8}
]
"""
```

**Concepts tested:** OOP, lambda, map, filter, list comprehensions, encapsulation, property decorators

### Challenge 3: Log File Analyzer with Regex

**Difficulty: Intermediate-Advanced**

```python
"""
Parse and analyze server log files using regex:

Sample log entry:
"[2024-10-21 14:23:45] ERROR 192.168.1.100 - Failed login attempt from user: admin@company.com"
"[2024-10-21 14:25:12] INFO 10.0.0.5 - Successful request /api/users?id=12345"
"[2024-10-21 14:26:33] WARNING 172.16.0.1 - High memory usage (87%)"

Create LogAnalyzer class that:
1. parse_log_entry(line) - extract timestamp, level, IP, message using groups
2. find_all_ips() - extract unique IP addresses (use set)
3. error_count() - count ERROR entries
4. filter_by_time_range(start_hour, end_hour) - filter logs
5. find_failed_logins() - extract user emails from failed login attempts
6. extract_api_requests() - find all API endpoints called
7. suspicious_activity() - IPs with >5 failed attempts (use dictionary counter)
8. export_report() - formatted summary with statistics

Regex patterns needed:
- Timestamp: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}
- IP addresses: IPv4 pattern
- Email addresses: email pattern
- Log levels: ERROR|WARNING|INFO
- API endpoints: /api/\w+

Use re.compile() for efficiency
"""
```

**Concepts tested:** Advanced regex, groups, character sets, quantifiers, OOP, dictionaries, sets

### Challenge 4: Music Streaming Service (Advanced OOP)

**Difficulty: Advanced**

```python
"""
Build complete music streaming system using inheritance and polymorphism:

Base classes:
- MediaItem (title, artist, duration, plays_count)
- Playlist (name, items[], owner)

Child classes:
- Song (inherits MediaItem) + album, genre
- Podcast (inherits MediaItem) + episode_number, show_name
- Audiobook (inherits MediaItem) + narrator, chapter

User class:
- playlists[], listening_history[]
- create_playlist(), add_to_playlist()
- play(media_item) - increments play_count
- get_recommendations() - based on history

StreamingService class (manages everything):
- users{}, media_library{}
- add_user(), add_media()
- search(query) - searches titles, artists (regex)
- trending() - top 10 most played items
- generate_report() - statistics by category

Requirements:
- Implement __eq__ to compare media items
- Use polymorphism for different play() behaviors
- Linked list for playlist (insert, delete, traverse)
- Queue for play queue using deque
- Dictionary for O(1) user/media lookup
- Use filter() to search by genre
- Use map() to normalize all titles to title case
- Track play history with timestamps

Advanced features:
- shuffle() - randomize playlist order
- sort_playlist(by="plays", "duration", "title")
- remove_duplicates() from playlist
- merge_playlists()
- auto_playlist(genre, min_duration) - creates playlist based on criteria
"""
```

**Concepts tested:** Advanced OOP (inheritance, polymorphism, encapsulation), linked lists, queues, dictionaries, functional programming, regex

### Challenge 5: Grade Management System

**Difficulty: Intermediate**

```python
"""
Create comprehensive grade tracking system:

Student class:
- name, student_id, courses{}
- add_grade(course, score)
- calculate_gpa() - weighted by credits
- get_transcript() - formatted string
- academic_standing() - Dean's List, Probation, Good Standing

Course class:
- name, code, credits, students[]
- add_student()
- drop_student()
- class_average()
- grade_distribution() - returns {A: count, B: count, ...}
- curve_grades(adjustment) - add points to all

GradeBook class (manages all):
- students{}, courses{}
- top_students(n) - returns top n by GPA
- failing_students() - GPA < 2.0
- honor_roll() - GPA >= 3.5
- course_rankings() - sort courses by average
- generate_reports()
- export_to_dict() for saving

Validation:
- Use try-except for invalid grades
- Use regex to validate student_id format (e.g., "STU-12345")
- Use control flow for grade letter assignment

Features:
- List comprehension for filtering students
- Dictionary comprehension for grade distribution
- Lambda for custom sorting
- Encapsulation with getters/setters
"""
```

**Concepts tested:** OOP, encapsulation, dictionaries, list comprehensions, exception handling, regex validation, control flow

### Challenge 6: Task Queue System with Priority

**Difficulty: Advanced**

```python
"""
Build task management system using stacks and queues:

Task class:
- name, priority (1-5), deadline, status, dependencies[]
- mark_complete()
- is_overdue()
- can_start() - checks if dependencies complete

TaskManager class:
- high_priority = Queue (deque)
- medium_priority = Queue (deque)
- low_priority = Queue (deque)
- completed = Stack (for undo functionality)
- task_history = LinkedList (maintains order)

Methods:
1. add_task(name, priority, deadline) - adds to correct queue
2. get_next_task() - processes highest priority first
3. complete_task(task) - moves to completed stack
4. undo_complete() - pops from stack, returns to queue
5. reschedule(task, new_priority)
6. cancel_task(name)
7. view_upcoming(n) - shows next n without removing
8. overdue_report() - uses filter() with date comparison
9. dependency_check(task) - ensures dependencies met
10. auto_escalate() - bump priority if deadline < 2 days

Statistics:
- average_completion_time()
- tasks_by_category()
- productivity_score()

Requirements:
- Use deque for all queues (O(1) operations)
- Use custom Stack class (implemented with linked list)
- Use regex to parse deadline strings
- Use datetime for date comparisons
- Implement time complexity: add O(1), get_next O(1), search O(n)
- Use dictionary to track task IDs for fast lookup

Advanced:
- Topological sort for task dependencies
- Serialize to JSON for persistence
- Load from file and rebuild data structures
"""
```

**Concepts tested:** Queues (deque), stacks, linked lists, OOP, datetime, regex, dictionaries, time complexity, algorithms

### Challenge 7: Text Processing Pipeline

**Difficulty: Expert**

```python
"""
Create advanced text analysis system combining multiple concepts:

TextProcessor class:
Pipeline methods (return self for chaining):
1. load(text or filename)
2. clean() - remove special chars, normalize spaces (regex)
3. tokenize() - split into words
4. remove_stopwords(words_list) - filter out common words
5. stem_words() - basic stemming (remove -ing, -ed)
6. count_words() - frequency dictionary
7. find_patterns(regex_pattern) - custom pattern matching
8. extract_entities() - find emails, phones, URLs, dates (regex)

Analysis methods:
1. word_frequency(top_n) - returns top n words
2. reading_level() - Flesch reading score calculation
3. sentiment_score() - basic positive/negative word counting
4. most_common_pairs() - bigrams
5. find_sentences() - split on sentence boundaries (regex)
6. sentence_complexity() - avg words per sentence
7. lexical_diversity() - unique/total ratio
8. keyword_extraction(n) - TF-IDF basic implementation

Comparison features:
9. compare_texts(text1, text2) - similarity score
10. common_vocabulary(text1, text2) - intersection
11. unique_to_each(text1, text2) - difference

Requirements:
- Use regex extensively for parsing
- Use dictionaries for O(1) word lookups
- Use sets for unique word operations
- Use list comprehensions for transformations
- Implement method chaining (return self)
- Cache expensive operations (use @property)
- Handle file I/O with exception handling
- Use functional programming where appropriate

Advanced patterns:
- Named entity recognition (basic with regex)
- Email/URL extraction with complex patterns
- Date parsing (multiple formats)
- Phone number normalization
- Hash tags and mentions extraction

Example usage:
processor = TextProcessor()
result = (processor
    .load("article.txt")
    .clean()
    .remove_stopwords(['the', 'a', 'is'])
    .count_words()
    .get_results())
"""
```

**Concepts tested:** Advanced regex, OOP, method chaining, dictionaries, sets, functional programming, file I/O, exception handling, caching, text algorithms

***

## Quick Reference Tips

**Naming Conventions:**

- Variables/functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Protected attributes: `_leading_underscore`

**Common Patterns:**

```python
# Swap variables
a, b = b, a

# Multiple assignment
x = y = z = 0

# Conditional expression (ternary)
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

**Time Complexity Quick Reference:**

- List access: O(1)
- List append: O(1)
- List insert: O(n)
- Dict access: O(1)
- Dict add/remove: O(1)
- Set membership: O(1)
- List membership: O(n)

