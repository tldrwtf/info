# Python Programming Quick Reference
For a comprehensive breakdown of the below topics, [view the comprehensive study guide](https://github.n3u.dev/README2)

## SYNTAX REFERENCE

### Python Basics

```python
# Variables & Types
name = "Allan"
age = 28
price = 3.14
is_active = True

# Type checking & conversion
type(variable)
isinstance(value, int)
str(123)  # Convert to string
int("42")  # Convert to int

# Input/Output
username = input("Enter name: ")
print(f"Hello, {name}!")  # f-string
```


### Control Flow

```python
# If-elif-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Comparison: ==, !=, <, >, <=, >=
# Logical: and, or, not
if age >= 18 and has_license:
    print("Can drive")

# Truthy/Falsy: 0, "", [], {}, (), None, False are falsy
```

### Loops

```python
# While loop
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

# For loop with range
for i in range(5):  # 0-4
    print(i)

# For loop with list
for fruit in fruits:
    print(fruit)

# Enumerate (index + value)
for index, item in enumerate(mylist):
    print(f"{index}: {item}")

# Break & Continue
for num in range(10):
    if num == 3:
        continue  # Skip 3
    if num == 7:
        break  # Exit loop
    print(num)
```

### Lists

```python
# Creation & Access
movies = ["Inception", "Matrix"]
first = movies[^0]
last = movies[-1]
slice_result = movies[1:3]

# Methods - Time Complexity
mylist.append(item)        # O(1)
mylist.insert(2, item)     # O(n)
mylist.pop()               # O(1)
mylist.pop(0)              # O(n)
mylist.remove(value)       # O(n)
mylist.index(value)        # O(n)
item in mylist             # O(n)
```

### Dictionaries

```python
# Creation & Access
student = {"name": "Maya", "age": 22}
name = student["name"]           # O(1)
age = student.get("age", 0)      # O(1) safe

# Modification
student["gpa"] = 3.8             # O(1)
del student["age"]               # O(1)
removed = student.pop("major")   # O(1)

# Iteration
for key in student:
    print(key)
for value in student.values():
    print(value)
for key, value in student.items():
    print(f"{key}: {value}")

# Membership - O(1) constant!
if "name" in student:
    print("Found")
```

### Functions

```python
# Basic function
def greet(name):
    print(f"Hello, {name}!")

# With return
def add(a, b):
    return a + b

# Default parameters
def introduce(name, title="Mr./Mrs"):
    print(f"{title} {name}")

# Multiple returns
def stats(numbers):
    return sum(numbers), max(numbers), min(numbers)

total, maximum, minimum = stats([1, 2, 3])
```

### String Methods

```python
text = "  Hello World!  "

text.lower()           # "  hello world!  "
text.upper()           # "  HELLO WORLD!  "
text.strip()           # "Hello World!"
text.split()           # ["Hello", "World!"]
"-".join(["a", "b"])   # "a-b"

"123".isdigit()        # True
"abc".isalpha()        # True
text.count("o")        # 2
text.find("World")     # 8 (index)
```

### Sets \& Tuples

```python
# Sets (unique, unordered)
numbers = {1, 2, 3, 4}
numbers.add(5)                    # O(1)
5 in numbers                      # O(1)
set1.union(set2)
set1.intersection(set2)
set1.difference(set2)

# Tuples (immutable)
coords = (3, 4)
x, y = coords  # Unpacking

# Zip
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

### Built-in Functions

```python
sum(numbers)           # Sum
max(numbers)           # Maximum
min(numbers)           # Minimum
len(mylist)            # Length
abs(-5)                # Absolute value
round(3.14159, 2)      # 3.14

range(5)               # 0-4
range(1, 6)            # 1-5
range(0, 10, 2)        # 0, 2, 4, 6, 8

sorted(mylist)         # Return sorted copy
mylist.sort()          # Sort in-place
```

### Regular Expressions

```python
import re

# Basic methods
re.search(r"\d+", text)      # Find first match
re.findall(r"\d+", text)     # Find all matches
re.match(r"Hello", text)     # Check if starts with
re.sub(r"cats", "dogs", text)  # Find & replace

# Metacharacters
\d   # Digit (0-9)
\w   # Word character (letters, digits, _)
\s   # Whitespace
.    # Any character
\b   # Word boundary

# Quantifiers
+    # One or more
*    # Zero or more
?    # Zero or one
{3}  # Exactly 3
{2,4}  # Between 2 and 4

# Character sets
[aeiou]      # Any vowel
[a-z]        # Lowercase letters
[0-9]        # Digits
[A-Z0-9]     # Uppercase or digits

# Groups
match = re.search(r"(\d{3})-(\d{4})", "555-1234")
area = match.group(1)  # "555"
number = match.group(2)  # "1234"

# Compile for reuse
pattern = re.compile(r"\d{3}-\d{4}")
results = pattern.findall(text)
```

### Functional Programming

```python
# Lambda functions
calculate_tax = lambda price: price * 0.07
sorted_products = sorted(products, key=lambda p: p["price"])

# Map - apply function to all items
doubled = list(map(lambda x: x * 2, numbers))

# Filter - keep items that meet condition
evens = list(filter(lambda x: x % 2 == 0, numbers))

# List comprehensions (most Pythonic)
doubled = [x * 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
doubled_evens = [x * 2 for x in numbers if x % 2 == 0]

# Dictionary comprehension
squared = {x: x**2 for x in range(5)}
```

### Object-Oriented Programming

```python
# Basic class
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def grade_avg(self):
        return sum(self.grades) / len(self.grades)
    
    def add_grade(self, grade):
        self.grades.append(grade)

# Create object
student = Student("Allan", 20, [85, 90, 92])

# Encapsulation (getters/setters)
class User:
    def __init__(self, username, email):
        self.username = username
        self._email = email  # Protected
    
    def get_email(self):
        return self._email
    
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email

# Inheritance
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def attack(self, opponent):
        opponent.health -= 10

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150)
    
    # Polymorphism - override parent method
    def attack(self, opponent):
        opponent.health -= 20
        print(f"{self.name} slashes with sword!")
```

### Data Structures - Advanced

```python
# Stack (LIFO - Last In, First Out)
stack = []
stack.append(1)    # Push - O(1)
stack.append(2)
top = stack.pop()  # Pop - O(1)
peek = stack[-1]   # Peek - O(1)

# Queue (FIFO - First In, First Out)
from collections import deque
queue = deque()
queue.append("first")     # Enqueue - O(1)
queue.append("second")
first = queue.popleft()   # Dequeue - O(1)

# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):  # O(1) with tail
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def traverse(self):  # O(n)
        current = self.head
        while current:
            print(current.data)
            current = current.next
```

### APIs \& HTTP Requests

```python
import requests

# GET request
response = requests.get("https://api.example.com/posts")
data = response.json()
print(response.status_code)  # 200 = success

# POST request
new_post = {"title": "My Post", "body": "Content", "userId": 1}
response = requests.post(url, json=new_post)

# Query parameters
params = {"userId": 1, "limit": 10}
response = requests.get(url, params=params)

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <token>"
}
response = requests.get(url, headers=headers)

# Status Codes
# 200 OK - Success
# 201 Created - Resource created
# 400 Bad Request - Client error
# 401 Unauthorized - Missing credentials
# 404 Not Found - Resource doesn't exist
# 500 Internal Server Error - Server error
```

### API Authentication (Spotify Example)

```python
import requests
import base64
from creds import client_id, client_secret

def get_token():
    # Step 1: Create credentials string
    cred_string = f"{client_id}:{client_secret}"
    
    # Step 2: Encode to base64
    cred_bytes = cred_string.encode('utf-8')
    cred_b64 = base64.b64encode(cred_bytes).decode('utf-8')
    
    # Step 3: Create headers with encoded credentials
    headers = {
        "Authorization": f"Basic {cred_b64}"
    }
    
    # Step 4: Request body
    data = {
        "grant_type": "client_credentials"
    }
    
    # Step 5: POST request to get token
    url = "https://accounts.spotify.com/api/token"
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        token_data = response.json()
        return token_data["access_token"]

# Using the token
def search_song(title):
    token = get_token()
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    params = {
        "q": title,
        "type": "track",
        "limit": 1
    }
    
    url = "https://api.spotify.com/v1/search"
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data["tracks"]["items"][^0]
```

### Time Complexity Reference

```python
# O(1) - Constant
dict[key]
list[index]
set.add(item)

# O(log n) - Logarithmic
# Binary search

# O(n) - Linear
for item in list:
    process(item)

# O(n log n) - Linearithmic
sorted(list)
list.sort()

# O(n²) - Quadratic
for i in list1:
    for j in list2:
        compare(i, j)

# Data Structure Operations
List: append O(1), insert O(n), access O(1)
Dict: access O(1), add O(1), delete O(1)
Set: add O(1), check membership O(1)
```



# STUDY GUIDES

## 1. Python Basics \& Fundamentals

### Core Concepts

- **Variables:** Store data with descriptive names
- **Data Types:** int, float, str, bool
- **Type Conversion:** `int()`, `float()`, `str()`
- **Input/Output:** `input()` for user input, `print()` for output
- **F-strings:** Modern string formatting `f"Hello, {name}!"`


### Key Patterns

```python
# Variable assignment
x = 10
name = "Allan"

# Multiple assignment
a = b = c = 0

# Swap variables
a, b = b, a

# Type conversion with validation
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid number")
```


### Study Tips

- Always use meaningful variable names
- Use f-strings for cleaner string formatting
- Remember: variables are case-sensitive
- Practice type conversions early

***

## 2. Control Flow \& Logic

### Comparison Operators

- `==` Equal to
- `!=` Not equal to
- `<` Less than
- `>` Greater than
- `<=` Less than or equal
- `>=` Greater than or equal


### Logical Operators

- `and` - Both conditions must be True
- `or` - At least one condition must be True
- `not` - Inverts the boolean value


### If-Elif-Else Structure

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```


### Truthy/Falsy Values

**Falsy values:** `0`, `""`, `[]`, `{}`, `()`, `None`, `False`
**Everything else** is truthy

### Complex Conditions

```python
age = 25
is_weekend = True

# Both must be true
if age >= 18 and is_weekend:
    print("Can enter club")

# At least one must be true
if age < 13 or age > 65:
    print("Special pricing")

# Invert condition
if not is_weekend:
    print("It's a weekday")
```


***

## 3. Loops \& Iteration

### While Loops

```python
# Basic countdown
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# Infinite loop with break
while True:
    answer = input("Continue? (y/n): ")
    if answer == 'n':
        break

# Skip with continue
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
```


### For Loops

```python
# Loop with range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# Loop through list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Loop through string
for char in "Python":
    print(char)

# Enumerate for index + value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```


### Study Tips

- Use `while` when you don't know iterations in advance
- Use `for` when iterating over collections or known ranges
- `break` exits the loop completely
- `continue` skips to next iteration

***

## 4. Lists \& Functions

### List Operations

```python
# Creation
movies = ["Inception", "Matrix", "Interstellar"]
numbers = [1, 2, 3, 4, 5]
mixed = ["text", 42, True, 3.14]

# Access
first = movies[^0]
last = movies[-1]
slice_result = movies[1:3]

# Modification
movies.append("Avatar")         # Add to end
movies.insert(1, "Titanic")     # Insert at position
movies.remove("Matrix")         # Remove by value
popped = movies.pop()           # Remove last
movies[^0] = "New Movie"         # Update

# Searching
index = movies.index("Avatar")
count = numbers.count(3)
exists = "Matrix" in movies
```


### Function Patterns

```python
# Basic function
def greet(name):
    print(f"Hello, {name}!")

# With return value
def add(a, b):
    return a + b

# Default parameters
def introduce(name, title="Mr./Mrs"):
    print(f"{title} {name}")

# Multiple returns
def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

area, perimeter = calculate_rectangle(5, 3)

# Temperature conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
```


***

## 5. Dictionaries

### Dictionary Essentials

```python
# Creation
student = {
    "name": "Maya",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8
}

# Access - O(1) constant time!
name = student["name"]
age = student.get("age", 0)  # Safe with default

# Modification
student["gpa"] = 3.9        # Update
student["email"] = "maya@university.edu"  # Add
del student["major"]        # Delete
removed = student.pop("age")  # Remove and return

# Iteration
for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(f"{key}: {value}")

# Membership check - O(1)
if "name" in student:
    print("Found")
```


### Nested Dictionaries

```python
contacts = {
    "Billy": {
        "phone": "555-1234",
        "email": "billy@example.com",
        "address": {
            "street": "123 Main St",
            "city": "Python City"
        }
    }
}

# Access nested data
phone = contacts["Billy"]["phone"]
city = contacts["Billy"]["address"]["city"]
```


### Why Dictionaries are Powerful

- **O(1) access** - Lightning fast lookups by key
- **Flexible keys** - Use strings, numbers, tuples as keys
- **Organized data** - Perfect for structured information
- **Memory efficient** - Better than lists for lookups

***

## 6. Sets, Tuples \& Built-in Functions

### Sets (Unique, Unordered)

```python
# Creation
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # {} creates dict

# Remove duplicates
mylist = [1, 1, 2, 2, 3, 3]
unique = set(mylist)  # {1, 2, 3}

# Operations
numbers.add(6)              # O(1)
numbers.discard(3)          # O(1) - no error if missing
numbers.remove(4)           # O(1) - error if missing
6 in numbers                # O(1) - fast membership

# Set mathematics
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union = set1.union(set2)              # {1,2,3,4,5,6}
intersection = set1.intersection(set2)  # {3, 4}
difference = set1.difference(set2)     # {1, 2}
```


### Tuples (Immutable)

```python
# Creation
coordinates = (3, 4)
singleton = (1,)  # Comma required!

# Unpacking
x, y = coordinates

# Cannot modify
# coordinates[^0] = 5  # TypeError!

# Zip multiple lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, lives in {city}")
```


### Essential Built-in Functions

```python
# Numeric
sum([1, 2, 3, 4, 5])       # 15
max([1, 2, 3, 4, 5])       # 5
min([1, 2, 3, 4, 5])       # 1
abs(-10)                   # 10
round(3.14159, 2)          # 3.14

# Length & Range
len("Python")              # 6
len([1, 2, 3])            # 3
range(5)                  # 0-4
list(range(1, 6))         # [1, 2, 3, 4, 5]

# Type operations
type(42)                  # <class 'int'>
isinstance(42, int)       # True
int("42")                 # 42
float("3.14")             # 3.14
str(100)                  # "100"
```


***

## 7. Object-Oriented Programming Basics

### Classes \& Objects

```python
class Student:
    def __init__(self, name, age, grades):
        # Constructor - runs when object is created
        self.name = name      # Instance attribute
        self.age = age
        self.grades = grades
    
    def info(self):
        # Instance method
        print(f"Name: {self.name}, Age: {self.age}")
    
    def grade_avg(self):
        return sum(self.grades) / len(self.grades)
    
    def add_grade(self, grade):
        self.grades.append(grade)

# Creating objects (instances)
student1 = Student("Allan", 20, [85, 90, 92])
student2 = Student("Maya", 22, [95, 88, 91])

# Using methods
student1.info()
avg = student1.grade_avg()
student1.add_grade(87)
```


### Why Use Classes?

- **Organization:** Group related data and functions
- **Reusability:** Create multiple objects from one blueprint
- **Maintainability:** Change one place, affects all instances
- **Real-world modeling:** Cars, Users, Products, etc.

***

## 8. OOP Advanced - The Four Pillars

### 1. Encapsulation

Hide data and provide controlled access

```python
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email         # Protected
        self._password = password   # Protected
    
    # Getter
    def get_email(self):
        return self._email
    
    # Setter with validation
    def set_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self._email = new_email
            return "Email updated"
        return "Invalid email format"
```


### 2. Inheritance

Child classes inherit from parent

```python
# Parent class
class Character:
    def __init__(self, name, health, attack_power=10):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self, opponent):
        opponent.health -= self.attack_power
    
    def display_stats(self):
        print(f"{self.name} - HP: {self.health}")

# Child classes inherit everything from Character
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)
    
    def special_attack(self, opponent):
        opponent.health -= self.attack_power * 2

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=30)

# Usage
warrior = Warrior("Conan")
mage = Mage("Gandalf")
warrior.attack(mage)  # Inherited method
```


### 3. Polymorphism

Same method name, different behavior

```python
class Character:
    def attack(self, opponent):
        opponent.health -= 10
        print(f"{self.name} attacks!")

class Warrior(Character):
    def attack(self, opponent):
        opponent.health -= 20
        print(f"{self.name} slashes with sword!")

class Mage(Character):
    def attack(self, opponent):
        opponent.health -= 30
        print(f"{self.name} casts fireball!")

# Same method name, different results
warrior.attack(enemy)  # "Conan slashes with sword!"
mage.attack(enemy)     # "Gandalf casts fireball!"
```


### 4. Abstraction

Hide complexity, show simplicity

```python
# User only sees simple interface
car = Car("Toyota", "Camry", 2024)
car.start_engine()  # Complex internal process hidden
car.drive(50)       # Don't need to know how engine works
car.refuel()        # Simple method, complex process
```


***

## 9. Time Complexity \& Big O Notation

### Understanding Big O

Big O describes how performance scales with input size

### Common Time Complexities

```python
# O(1) - Constant (BEST)
# Same time regardless of size
x = mylist[^5]
value = mydict["key"]
myset.add(item)

# O(log n) - Logarithmic (EXCELLENT)
# Cuts problem in half each time
# Binary search

# O(n) - Linear (GOOD)
# Scales proportionally
for item in mylist:
    print(item)

# O(n log n) - Linearithmic (ACCEPTABLE)
# Efficient sorting
sorted(mylist)
mylist.sort()

# O(n²) - Quadratic (BAD)
# Nested loops - avoid when possible
for i in list1:
    for j in list2:
        compare(i, j)

# O(2ⁿ) - Exponential (TERRIBLE)
# Doubles with each addition - avoid!
```


### Data Structure Time Complexities

**Lists:**

- Access by index: O(1)
- Append to end: O(1)
- Insert at position: O(n)
- Pop from end: O(1)
- Pop from beginning: O(n)
- Search (in): O(n)

**Dictionaries:**

- Access by key: O(1) 
- Add/Update: O(1) 
- Delete: O(1) 
- Search key: O(1) 

**Sets:**

- Add: O(1) 
- Remove: O(1) 
- Membership check: O(1) 


### When to Choose What

- Need fast lookups? → **Dictionary or Set**
- Need ordered data? → **List**
- Need unique items? → **Set**
- Need key-value pairs? → **Dictionary**

***

## 10. Linked Lists

### Why Linked Lists?

- Dynamic size (grows/shrinks easily)
- Efficient insertions/deletions at beginning
- Foundation for stacks, queues, graphs


### Node Structure

```python
class Node:
    def __init__(self, data):
        self.data = data    # The actual value
        self.next = None    # Pointer to next node
```


### LinkedList Implementation

```python
class LinkedList:
    def __init__(self):
        self.head = None  # First node
        self.tail = None  # Last node
    
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        """Add to end - O(1) with tail"""
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def traverse(self):
        """Visit all nodes - O(n)"""
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def insert_at_position(self, position, data):
        """Insert at position - O(n)"""
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for _ in range(position - 2):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_position(self, position):
        """Delete at position - O(n)"""
        if position == 1:
            self.head = self.head.next
            return
        
        current = self.head
        for _ in range(position - 2):
            current = current.next
        
        current.next = current.next.next
```


### Real-World Application: Music Playlist

```python
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class MusicPlaylist:
    def __init__(self, name):
        self.name = name
        self.songs = LinkedList()
        self.current_position = 0
    
    def add_song(self, title, artist, duration):
        song = Song(title, artist, duration)
        self.songs.append(song)
    
    def next_song(self):
        self.current_position += 1
        song = self.songs.get_at_position(self.current_position)
        print(f"Now playing: {song.title}")
    
    def previous_song(self):
        if self.current_position > 1:
            self.current_position -= 1
            song = self.songs.get_at_position(self.current_position)
            print(f"Now playing: {song.title}")
```


***

## 11. Stacks \& Queues

### Stacks (LIFO - Last In, First Out)

Think: Stack of plates - take from top, add to top

```python
# Python list as stack
stack = []
stack.append(1)    # Push - O(1)
stack.append(2)
stack.append(3)
top = stack.pop()  # Pop - O(1)
peek = stack[-1]   # Peek - O(1)

# Custom Stack class
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, item):
        """Add to top - O(1)"""
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        """Remove from top - O(1)"""
        if self.head is None:
            return None
        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return item
    
    def peek(self):
        """View top without removing - O(1)"""
        return self.head.data if self.head else None
```

**Stack Use Cases:**

- Undo/Redo functionality
- Browser back button
- Function call stack
- Expression evaluation


### Queues (FIFO - First In, First Out)

Think: Line at store - first person served first

```python
from collections import deque

# Use deque for efficient queues
queue = deque()

# Enqueue (add to end) - O(1)
queue.append("first")
queue.append("second")
queue.append("third")

# Dequeue (remove from front) - O(1)
first_item = queue.popleft()

# Peek front - O(1)
if queue:
    front = queue[^0]

# DO NOT use list.pop(0) - it's O(n)!
```

**Queue Use Cases:**

- Print job queue
- Task scheduling
- Breadth-first search
- Message queues

***

## 12. Functional Programming

### Lambda Functions

Anonymous one-line functions

```python
# Regular function
def add(a, b):
    return a + b

# Lambda equivalent
add = lambda a, b: a + b

# Common use: sorting
products = [
    {"name": "laptop", "price": 999},
    {"name": "mouse", "price": 25}
]

# Sort by price descending
sorted_products = sorted(products, 
                        key=lambda p: p["price"], 
                        reverse=True)

# Conditional lambda (ternary)
is_even = lambda x: "even" if x % 2 == 0 else "odd"
```


### Map Function

Apply function to every item

```python
numbers = [1, 2, 3, 4, 5]

# Double all numbers
doubled = list(map(lambda x: x * 2, numbers))
# [2, 4, 6, 8, 10]

# Process complex data
users = [
    {"name": "JOHN DOE", "email": "JOHN@EMAIL.COM"},
    {"name": "JANE SMITH", "email": "JANE@EMAIL.COM"}
]

# Normalize names and emails
normalized = list(map(
    lambda u: {
        "name": u["name"].title(),
        "email": u["email"].lower()
    },
    users
))
```


### Filter Function

Keep items that meet condition

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get only evens
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8, 10]

# Real-world: filter products
books = [
    {"title": "Python Guide", "rating": 4.5, "available": True},
    {"title": "Web Dev", "rating": 3.8, "available": False},
    {"title": "Data Science", "rating": 4.9, "available": True}
]

# Available books with rating >= 4.0
quality_books = list(filter(
    lambda b: b["available"] and b["rating"] >= 4.0,
    books
))
```


### List Comprehensions (Most Pythonic)

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Double all
doubled = [x * 2 for x in numbers]

# Get evens only
evens = [x for x in numbers if x % 2 == 0]

# Double only evens (map + filter combined)
doubled_evens = [x * 2 for x in numbers if x % 2 == 0]

# Dictionary comprehension
squared = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Real-world example
employees = [
    {"name": "Alice", "job": "Developer", "salary": 75000},
    {"name": "Bob", "job": "Designer", "salary": 65000},
    {"name": "Charlie", "job": "Developer", "salary": 80000}
]

# High-earning developers
high_devs = [
    emp["name"] 
    for emp in employees 
    if emp["job"] == "Developer" and emp["salary"] > 70000
]
# ["Alice", "Charlie"]
```


### Performance Comparison

**List Comprehensions** → Fastest, most Pythonic

**Map/Filter** → Good for functional style

**Regular loops** → Best for complex logic

***

## 13. Regular Expressions (Regex)

### Core Methods

```python
import re

# search() - find first match, return match object
match = re.search(r"\d+", "I have 123 apples")
if match:
    print(match.group())  # "123"

# findall() - find all matches, return list
numbers = re.findall(r"\d+", "I have 5 cats and 3 dogs")
# ["5", "3"]

# match() - check if starts with pattern
result = re.match(r"Hello", "Hello world")  # Match object
result = re.match(r"Hello", "world Hello")  # None

# sub() - find and replace
text = "I love cats. Cats are great."
new_text = re.sub(r"[Cc]ats?", "dogs", text)
# "I love dogs. Dogs are great."
```


### Metacharacters

```python
\d   # Any digit (0-9)
\w   # Word character (letters, digits, _)
\s   # Whitespace (space, tab, newline)
.    # Any character except newline
\b   # Word boundary

# Examples
re.findall(r"\d", "abc123")       # ['1', '2', '3']
re.findall(r"\w+", "hello_world") # ['hello_world']
re.findall(r"\s", "hello world")  # [' ']
re.findall(r"\bcat\b", "cat cats scatter")  # ['cat']
```


### Quantifiers

```python
+    # One or more
*    # Zero or more
?    # Zero or one
{n}  # Exactly n times
{n,m}  # Between n and m times

# Examples
re.findall(r"\d+", "I have 123 apples and 45 oranges")
# ['123', '45']

re.findall(r"\d{3}", "123 45 6789")
# ['123', '678']

re.findall(r"\d{2,4}", "1 12 123 1234 12345")
# ['12', '123', '1234', '1234']

re.findall(r"colou?r", "color colour")
# ['color', 'colour']
```


### Character Sets

```python
[aeiou]     # Any vowel
[a-z]       # Lowercase letters
[A-Z]       # Uppercase letters
[0-9]       # Digits
[a-zA-Z0-9] # Alphanumeric

# Examples
re.findall(r"[aeiou]", "hello world")  # ['e', 'o', 'o']
re.findall(r"[0-5]", "0123456789")     # ['0','1','2','3','4','5']

# Email pattern
pattern = r"[a-zA-Z0-9._+-]+@[a-zA-Z_]+\.[a-z]{2,3}"
emails = re.findall(pattern, "Contact: john@test.com or sally@example.org")
```


### Groups \& Substitution

```python
# Capture groups with ()
text = "John Smith, 555-1234"
match = re.search(r"(\w+) (\w+), (\d{3}-\d{4})", text)
if match:
    first_name = match.group(1)   # "John"
    last_name = match.group(2)    # "Smith"
    phone = match.group(3)        # "555-1234"

# Named groups
pattern = r"(?P<first>\w+) (?P<last>\w+)"
match = re.search(pattern, "John Smith")
print(match.group('first'))  # "John"

# Rearrange with sub
date = "12/25/2024"
new_format = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\1-\2", date)
# "2024-12-25"

# Privacy protection
feedback = "Call me at 555-0123 for help"
clean = re.sub(r"\d{3}-\d{4}", "[PHONE REMOVED]", feedback)
```


### Compile for Efficiency

```python
# Compile pattern once, reuse many times
email_pattern = re.compile(r"[a-zA-Z0-9._+-]+@[a-zA-Z_]+\.[a-z]{2,3}")

text1 = "Email: john@test.com"
text2 = "Contact: sarah@example.org"

emails1 = email_pattern.findall(text1)
emails2 = email_pattern.findall(text2)
```


***

## 14. APIs \& HTTP Requests

### API Fundamentals

**API:** Application Programming Interface - lets programs talk to each other

**HTTP Methods (CRUD):**

- **POST** → Create data in database
- **GET** → Read/retrieve data
- **PUT** → Update existing data
- **DELETE** → Remove data


### Making Requests

```python
import requests

# GET request - retrieve data
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# Check status code
print(response.status_code)  # 200 = success

# Parse JSON to Python dict/list
data = response.json()
print(data)

# POST request - create data
new_post = {
    "title": "My Post",
    "body": "This is the content",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)

if response.status_code == 201:  # 201 = Created
    print("Post created successfully!")
    print(response.json())
```


### Query Parameters

Send data through URL

```python
# Method 1: Add to URL
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts?userId=1"
)

# Method 2: Use params dict (preferred)
params = {
    "userId": 1,
    "limit": 10
}
response = requests.get(url, params=params)
```


### Headers

Additional request information

```python
headers = {
    "Content-Type": "application/json",
    "User-Agent": "My-App/1.0",
    "Authorization": "Bearer <token>"  # For auth
}

response = requests.get(url, headers=headers)
```


### HTTP Status Codes

```python
# 2xx - Success
200  # OK - Request successful
201  # Created - Resource created successfully
204  # No Content - Success but no data returned

# 3xx - Redirection
301  # Moved Permanently

# 4xx - Client Error (Your mistake)
400  # Bad Request - Malformed/missing data
401  # Unauthorized - Missing proper credentials
404  # Not Found - Resource doesn't exist
429  # Too Many Requests - Rate limit exceeded

# 5xx - Server Error (Their problem)
500  # Internal Server Error - Something broke
503  # Service Unavailable - Temporarily down
504  # Gateway Timeout - Server too slow
```


### Virtual Environment Setup

```bash
# Create virtual environment
# Windows:
python -m venv venv

# Mac/Linux:
python3 -m venv venv

# Activate
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# Install packages
pip install requests

# Check installations
pip list
```


***

## 15. API Authentication (Advanced)

### Authentication Types

**1. API Key Authentication:**

- Simple key attached to requests
- Get key from API service (account or docs)
- Add to headers for access

**2. Token Authentication:**

- POST request with credentials
- Server validates and returns token
- Store token for future requests
- Include token in headers


### Spotify OAuth Example (Client Credentials)

```python
import requests
import base64
from creds import client_id, client_secret

def get_token():
    """Get Spotify access token using OAuth"""
    
    # Step 1: Token endpoint URL
    url = "https://accounts.spotify.com/api/token"
    
    # Step 2: Combine client ID and secret
    cred_string = f"{client_id}:{client_secret}"
    
    # Step 3: Encode to base64 (web-safe format)
    cred_bytes = cred_string.encode('utf-8')
    cred_b64 = base64.b64encode(cred_bytes).decode('utf-8')
    
    # Step 4: Create authorization header
    headers = {
        "Authorization": f"Basic {cred_b64}"
    }
    
    # Step 5: Request body
    data = {
        "grant_type": "client_credentials"
    }
    
    # Step 6: Send POST request
    response = requests.post(url, headers=headers, data=data)
    
    # Step 7: Extract access token
    if response.status_code == 200:
        token_data = response.json()
        return token_data["access_token"]
    else:
        return None

# Using the token to search songs
def search_song(title):
    """Search for a song on Spotify"""
    
    # Get authentication token
    token = get_token()
    
    # Spotify search endpoint
    url = "https://api.spotify.com/v1/search"
    
    # Query parameters
    params = {
        "q": title,       # Song title to search
        "type": "track",  # Searching for tracks
        "limit": 1        # Return 1 result
    }
    
    # Headers with Bearer token
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    # Send GET request
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        track = data["tracks"]["items"][^0]
        
        print(f"Song: {track['name']}")
        print(f"Artist: {track['artists'][^0]['name']}")
        print(f"Album: {track['album']['name']}")
        print(f"Preview: {track['preview_url']}")
        
        return track
    else:
        print(f"Error: {response.status_code}")
        return None

# Example usage
search_song("Bohemian Rhapsody")
```


### Base64 Encoding

Why: Makes credentials web-safe for transmission

```python
import base64

# Encoding
text = "username:password"
text_bytes = text.encode('utf-8')
encoded = base64.b64encode(text_bytes)
encoded_string = encoded.decode('utf-8')

# Decoding
decoded_bytes = base64.b64decode(encoded)
decoded_string = decoded_bytes.decode('utf-8')
```


### Real-World Music App (MiPod)

```python
class MiPod:
    def __init__(self, name):
        self.name = name
        self.playlist = []
    
    def get_token(self):
        """Get Spotify access token"""
        # Token logic here
        return token
    
    def search_song(self, title):
        """Search Spotify for song"""
        token = self.get_token()
        # Search logic with token
        return song_data
    
    def add_song(self, song):
        """Add song to playlist"""
        self.playlist.append(song)
        print(f"Added: {song['name']}")
    
    def view_playlist(self):
        """Display current playlist"""
        print(f"===== {self.name}'s Playlist =====")
        for i, song in enumerate(self.playlist, 1):
            print(f"{i}. {song['name']} - {song['artist']}")

# Usage
my_ipod = MiPod("Allan")
song = my_ipod.search_song("Stairway to Heaven")
my_ipod.add_song(song)
my_ipod.view_playlist()
```


***

## PRACTICE CHALLENGES (Updated)

### Challenge 1: Weather API Data Aggregator

**Difficulty:** Intermediate
**Topics:** APIs, Dictionaries, Functions, Error Handling

```python
"""
Build a weather data manager:
1. Fetch weather from OpenWeatherMap API
2. Store data in dictionary (city: data)
3. Calculate average temperature across cities
4. Find hottest/coldest city
5. Use query parameters for units (metric/imperial)
6. Handle HTTP errors (404, 401, 500)
7. Cache responses (don't refetch same city)

Bonus: 
- Retry logic for 429 (too many requests)
- Regex to validate city names
- Convert temperatures between C/F
"""
```


### Challenge 2: Student Grade Management System

**Difficulty:** Intermediate
**Topics:** OOP, Dictionaries, Functions, List Comprehensions

```python
"""
Create complete gradebook with OOP:

Student class:
- name, student_id, courses{}
- add_grade(course, score)
- calculate_gpa()
- get_transcript()

Course class:
- name, code, credits, students[]
- add_student(), drop_student()
- class_average()
- grade_distribution()

GradeBook class:
- Manage all students and courses
- top_students(n)
- honor_roll() - GPA >= 3.5
- generate_reports()

Use:
- Encapsulation for protected data
- List comprehensions for filtering
- Dictionary comprehension for distributions
- Regex to validate student IDs
"""
```


### Challenge 3: Text Analysis Engine with Regex

**Difficulty:** Advanced
**Topics:** Regex, Functional Programming, Dictionaries, OOP

```python
"""
Build comprehensive text analyzer:

Features:
1. Extract all emails, phones, URLs, dates
2. Word frequency (case-insensitive)
3. Most common word pairs (bigrams)
4. Reading time calculator (200 words/min)
5. Sentiment score (positive/negative words)
6. Remove stopwords (the, a, is, etc.)
7. Find sentences matching patterns
8. Replace patterns (e.g., censor profanity)

Requirements:
- Use re.compile() for efficiency
- Functional programming (map/filter/comprehensions)
- Method chaining support
- Cache expensive operations

Regex patterns needed:
- Email: [a-zA-Z0-9._+-]+@[a-zA-Z_]+\.[a-z]{2,3}
- Phone: \d{3}-\d{4} or \(\d{3}\) \d{3}-\d{4}
- URL: https?://[^\s]+
- Date: \d{2}/\d{2}/\d{4}
"""
```


### Challenge 4: Spotify Playlist Manager

**Difficulty:** Advanced
**Topics:** APIs, Authentication, OOP, Linked Lists, Functional Programming

```python
"""
Build complete music app with Spotify API:

MusicApp class:
- Authenticate with Spotify OAuth
- Search songs by title/artist
- Create playlists (use LinkedList)
- Add/remove songs from playlist
- Shuffle playlist
- Get song recommendations
- Play queue (use deque)

Playlist class:
- songs (LinkedList)
- shuffle() - randomize order
- sort_by("plays", "duration", "title")
- total_duration()
- filter_by_genre()

Features:
- Handle API rate limits (429)
- Cache search results
- Use map() to normalize song data
- Use filter() for genre filtering
- Regex to validate playlist names

Advanced:
- Recently played (Stack)
- Up next queue (Queue)
- Favorite artists analysis
- Export playlist to JSON
"""
```


### Challenge 5: Task Management System

**Difficulty:** Expert
**Topics:** Stacks, Queues, Linked Lists, OOP, Time Complexity

```python
"""
Build enterprise task manager:

Task class:
- name, priority (1-5), deadline, status, dependencies[]
- mark_complete(), is_overdue()

TaskManager:
- high_priority (Queue)
- medium_priority (Queue)
- low_priority (Queue)
- completed (Stack for undo)
- history (LinkedList)

Methods:
1. add_task() - adds to correct queue
2. get_next_task() - processes highest priority
3. complete_task() - move to completed stack
4. undo_complete() - pop from stack, return to queue
5. auto_escalate() - bump priority if deadline < 2 days
6. dependency_check() - verify dependencies met
7. overdue_report() - filter tasks past deadline

Requirements:
- All queue ops O(1) - use deque
- Regex for deadline parsing
- Topological sort for dependencies
- Export to JSON for persistence

Time complexity targets:
- add_task: O(1)
- get_next_task: O(1)
- search: O(n)
"""
```


***

## FINAL STUDY TIPS

### Code Every Day

- **20 minutes minimum** - consistency beats intensity
- **One concept** - master before moving on
- **Build projects** - apply multiple concepts
- **Debug actively** - read error messages carefully
- **Refactor code** - make it cleaner, more efficient

### Best Practices

```python
# Good variable names
user_age = 25  # Clear
x = 25         # Unclear

# DRY - Don't Repeat Yourself
def calculate_total(items):
    return sum(item.price for item in items)

# Comments for why, not what
# Calculate tax including regional surcharge
total = price * 1.07  # Good

# This multiplies price by 1.07
total = price * 1.07  # Bad (obvious)

# Use f-strings
name = "Allan"
print(f"Hello, {name}!")  # Modern
print("Hello, " + name + "!")  # Old style
```
