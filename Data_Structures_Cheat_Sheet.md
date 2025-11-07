# Python Data Structures - Complete Reference Guide

## Table of Contents
- [Lists](#lists)
- [Dictionaries](#dictionaries)
- [Sets](#sets)
- [Tuples](#tuples)
- [Linked Lists](#linked-lists)
- [Stacks & Queues](#stacks--queues)

---

## Lists

### Creating Lists
```python
# Empty list
my_list = []
my_list = list()

# List with values
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

# List from range
nums = list(range(5))  # [0, 1, 2, 3, 4]
```

### Accessing Elements
```python
fruits = ["apple", "banana", "cherry", "date"]

# Indexing (0-based)
fruits[0]      # "apple"
fruits[2]      # "cherry"
fruits[-1]     # "date" (last element)
fruits[-2]     # "cherry" (second to last)

# Slicing [start:end:step]
fruits[1:3]    # ["banana", "cherry"]
fruits[:2]     # ["apple", "banana"]
fruits[2:]     # ["cherry", "date"]
fruits[::2]    # ["apple", "cherry"] (every 2nd element)
fruits[::-1]   # ["date", "cherry", "banana", "apple"] (reversed)
```

### Modifying Lists
```python
# Append (add to end)
fruits.append("elderberry")  # ["apple", "banana", "cherry", "date", "elderberry"]

# Insert (add at specific index)
fruits.insert(1, "blueberry")  # ["apple", "blueberry", "banana", ...]

# Extend (add multiple items)
fruits.extend(["fig", "grape"])
fruits += ["fig", "grape"]  # Same as extend

# Remove by value
fruits.remove("banana")  # Removes first occurrence

# Remove by index
del fruits[0]          # Remove first element
item = fruits.pop()    # Remove and return last element
item = fruits.pop(1)   # Remove and return element at index 1

# Clear all elements
fruits.clear()
```

### List Methods
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Sort (modifies original list)
numbers.sort()           # [1, 1, 2, 3, 4, 5, 5, 6, 9]
numbers.sort(reverse=True)  # [9, 6, 5, 5, 4, 3, 2, 1, 1]

# Sorted (returns new sorted list)
sorted_nums = sorted(numbers)  # Original unchanged

# Reverse (modifies original)
numbers.reverse()

# Count occurrences
count = numbers.count(5)  # 2

# Find index
index = numbers.index(4)  # 2 (first occurrence)

# Copy
copy = numbers.copy()
copy = numbers[:]  # Also creates a copy
```

### List Comprehensions
```python
# Basic syntax: [expression for item in iterable]
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Transform strings
fruits = ["apple", "banana", "cherry"]
uppercase = [fruit.upper() for fruit in fruits]

# Nested list comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

### Common List Operations
```python
# Length
len([1, 2, 3])  # 3

# Concatenation
[1, 2] + [3, 4]  # [1, 2, 3, 4]

# Repetition
[1, 2] * 3  # [1, 2, 1, 2, 1, 2]

# Membership
3 in [1, 2, 3]  # True
5 not in [1, 2, 3]  # True

# Min/Max/Sum
min([3, 1, 4])  # 1
max([3, 1, 4])  # 4
sum([1, 2, 3])  # 6
```

---

## Dictionaries

### Creating Dictionaries
```python
# Empty dictionary
my_dict = {}
my_dict = dict()

# Dictionary with values
person = {
    "name": "Wilson",
    "age": 30,
    "city": "NYC"
}

# From key-value pairs
dict([("name", "Bob"), ("age", 25)])

# Using dict() constructor
user = dict(name="Charlie", age=35)
```

### Accessing Values
```python
person = {"name": "Wilson", "age": 30, "city": "NYC"}

# Direct access (raises KeyError if key doesn't exist)
name = person["name"]  # "Wilson"

# Safe access with get() (returns None if key doesn't exist)
email = person.get("email")  # None
email = person.get("email", "no-email@example.com")  # Default value

# Check if key exists
if "age" in person:
    print(person["age"])
```

### Modifying Dictionaries
```python
person = {"name": "Wilson", "age": 30}

# Add or update
person["email"] = "Wilson@email.com"  # Add new key
person["age"] = 31  # Update existing key

# Update multiple items
person.update({"city": "NYC", "phone": "555-1234"})

# Remove items
del person["city"]  # Remove specific key
email = person.pop("email")  # Remove and return value
email = person.pop("email", None)  # Safe removal with default

# Remove last inserted item (Python 3.7+)
item = person.popitem()

# Clear all items
person.clear()
```

### Dictionary Methods
```python
person = {"name": "Wilson", "age": 30, "city": "NYC"}

# Get all keys
keys = person.keys()  # dict_keys(['name', 'age', 'city'])
list(person.keys())   # ['name', 'age', 'city']

# Get all values
values = person.values()  # dict_values(['Wilson', 30, 'NYC'])

# Get all key-value pairs
items = person.items()  # dict_items([('name', 'Wilson'), ...])

# Copy
copy = person.copy()

# Get with default
age = person.setdefault("age", 0)  # Returns existing value
country = person.setdefault("country", "USA")  # Adds if missing
```

### Looping Through Dictionaries
```python
person = {"name": "Wilson", "age": 30, "city": "NYC"}

# Loop through keys
for key in person:
    print(key)

for key in person.keys():
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

### Dictionary Comprehensions
```python
# Basic syntax: {key_expr: value_expr for item in iterable}

# Create dict from list
numbers = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in numbers}  # {1: 1, 2: 4, 3: 9, ...}

# With condition
evens_squared = {x: x**2 for x in numbers if x % 2 == 0}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}  # {1: "a", 2: "b", 3: "c"}
```

### Nested Dictionaries
```python
users = {
    "user1": {"name": "Wilson", "age": 30},
    "user2": {"name": "Bob", "age": 25}
}

# Access nested values
Wilson_age = users["user1"]["age"]  # 30

# Loop through nested dict
for user_id, user_info in users.items():
    print(f"{user_id}: {user_info['name']}")
```

---

## Sets

### Creating Sets
```python
# Empty set (must use set(), {} creates empty dict)
my_set = set()

# Set with values
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}

# From list (removes duplicates)
numbers = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}
```

### Set Operations
```python
# Add element
numbers = {1, 2, 3}
numbers.add(4)  # {1, 2, 3, 4}

# Add multiple elements
numbers.update([5, 6, 7])  # {1, 2, 3, 4, 5, 6, 7}

# Remove element
numbers.remove(3)  # Raises KeyError if not found
numbers.discard(3)  # No error if not found
item = numbers.pop()  # Remove and return arbitrary element

# Clear all elements
numbers.clear()

# Membership
3 in {1, 2, 3}  # True
```

### Set Mathematics
```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union (all elements from both sets)
a | b  # {1, 2, 3, 4, 5, 6, 7, 8}
a.union(b)

# Intersection (elements in both sets)
a & b  # {4, 5}
a.intersection(b)

# Difference (in a but not in b)
a - b  # {1, 2, 3}
a.difference(b)

# Symmetric difference (in a or b, but not both)
a ^ b  # {1, 2, 3, 6, 7, 8}
a.symmetric_difference(b)

# Subset
{1, 2}.issubset({1, 2, 3})  # True

# Superset
{1, 2, 3}.issuperset({1, 2})  # True

# Disjoint (no common elements)
{1, 2}.isdisjoint({3, 4})  # True
```

### Set Comprehensions
```python
# Basic syntax: {expression for item in iterable}
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}

# With condition
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}
```

### Common Use Cases
```python
# Remove duplicates from list
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(numbers))  # [1, 2, 3, 4]

# Find unique characters
text = "hello"
unique_chars = set(text)  # {'h', 'e', 'l', 'o'}

# Check for common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)  # {3, 4}
```

---

## Tuples

### Creating Tuples
```python
# Empty tuple
empty = ()
empty = tuple()

# Tuple with values
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")

# Single element tuple (comma required!)
single = (42,)  # Tuple
not_tuple = (42)  # This is just an int!

# Without parentheses (tuple packing)
coords = 10, 20, 30  # (10, 20, 30)
```

### Accessing Tuples
```python
fruits = ("apple", "banana", "cherry", "date")

# Indexing (same as lists)
fruits[0]   # "apple"
fruits[-1]  # "date"

# Slicing (same as lists)
fruits[1:3]  # ("banana", "cherry")

# Unpacking
name, age, city = ("Wilson", 30, "NYC")
# name = "Wilson", age = 30, city = "NYC"

# Unpacking with *
first, *middle, last = (1, 2, 3, 4, 5)
# first = 1, middle = [2, 3, 4], last = 5
```

### Tuple Methods
```python
numbers = (1, 2, 3, 2, 1, 2)

# Count occurrences
count = numbers.count(2)  # 3

# Find index
index = numbers.index(3)  # 2

# Length
len(numbers)  # 6

# Min/Max/Sum
min(numbers)  # 1
max(numbers)  # 3
sum(numbers)  # 11
```

### Tuples are Immutable
```python
# Cannot modify tuples
coords = (10, 20, 30)
# coords[0] = 15  # TypeError!

# But can create new tuple
new_coords = (15, 20, 30)

# Can concatenate
coords = (10, 20) + (30, 40)  # (10, 20, 30, 40)
```

### When to Use Tuples
```python
# 1. Return multiple values from function
def get_coordinates():
    return (10, 20)  # Or: return 10, 20

x, y = get_coordinates()

# 2. Dictionary keys (tuples are hashable, lists are not)
locations = {
    (0, 0): "origin",
    (10, 20): "point A",
    (30, 40): "point B"
}

# 3. Protect data from modification
DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
```

---

## Linked Lists

### Node Class
```python
class Node:
    """A single node in a linked list"""
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Reference to next node
```

### Linked List Class
```python
class LinkedList:
    """A singly linked list implementation"""

    def __init__(self):
        self.head = None  # First node
        self.tail = None  # Last node

    def is_empty(self):
        """Check if list is empty"""
        return self.head is None

    def append(self, data):
        """Add element to end of list"""
        new_node = Node(data)

        if self.is_empty():
            # If empty, new node is both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Add to end and update tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        """Add element to beginning of list"""
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        """Delete first occurrence of data"""
        if self.is_empty():
            return

        # If head contains the data
        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        # Search for the node
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return
            current = current.next

    def display(self):
        """Print all elements"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def get_at_position(self, position):
        """Get element at specific position (0-indexed)"""
        current = self.head
        index = 0

        while current:
            if index == position:
                return current.data
            current = current.next
            index += 1

        return None  # Position out of range
```

### Using Linked Lists
```python
# Create linked list
ll = LinkedList()

# Add elements
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)

# Display: 5 -> 10 -> 20 -> 30 -> None
ll.display()

# Get element
value = ll.get_at_position(2)  # 20

# Delete element
ll.delete(20)

# Display: 5 -> 10 -> 30 -> None
ll.display()
```

### When to Use Linked Lists
```python
# Advantages:
# - Dynamic size (grows/shrinks as needed)
# - Efficient insertion/deletion at beginning: O(1)
# - No wasted space (no pre-allocation)

# Disadvantages:
# - No random access: O(n) to access element
# - Extra memory for pointers
# - Not cache-friendly

# Use when:
# - Frequent insertions/deletions
# - Unknown size
# - Don't need random access
```

---

## Stacks & Queues

### Stack (LIFO - Last In First Out)
```python
# Using list as stack
stack = []

# Push (add to top)
stack.append(1)
stack.append(2)
stack.append(3)  # [1, 2, 3]

# Pop (remove from top)
item = stack.pop()  # 3, stack is now [1, 2]

# Peek (look at top without removing)
top = stack[-1] if stack else None

# Check if empty
is_empty = len(stack) == 0

# Size
size = len(stack)
```

### Queue (FIFO - First In First Out)
```python
from collections import deque

# Using deque for efficient queue operations
queue = deque()

# Enqueue (add to rear)
queue.append(1)
queue.append(2)
queue.append(3)  # deque([1, 2, 3])

# Dequeue (remove from front)
item = queue.popleft()  # 1, queue is now deque([2, 3])

# Peek (look at front)
front = queue[0] if queue else None

# Check if empty
is_empty = len(queue) == 0

# Size
size = len(queue)
```

---

## Data Structure Comparison

| Operation | List | Dict | Set | Tuple |
|-----------|------|------|-----|-------|
| Ordered | Yes | Yes* | No | Yes |
| Mutable | Yes | Yes | Yes | No |
| Duplicates | Yes | Keys: No<br>Values: Yes | No | Yes |
| Indexing | Yes | By key | No | Yes |
| Add | `.append()` | `[key] = value` | `.add()` | N/A |
| Remove | `.remove()` | `del [key]` | `.remove()` | N/A |
| Lookup Speed | O(n) | O(1) | O(1) | O(n) |

*Dictionaries are ordered as of Python 3.7+

---

## Quick Reference

### List
```python
my_list = [1, 2, 3]
my_list.append(4)              # Add to end
my_list.insert(0, 0)          # Insert at index
my_list.remove(2)             # Remove by value
my_list.pop()                 # Remove from end
my_list[0]                    # Access by index
[x*2 for x in my_list]        # List comprehension
```

### Dictionary
```python
my_dict = {"a": 1, "b": 2}
my_dict["c"] = 3              # Add/update
my_dict.get("a", 0)           # Safe access
del my_dict["b"]              # Remove
my_dict.keys()                # Get keys
my_dict.values()              # Get values
my_dict.items()               # Get key-value pairs
```

### Set
```python
my_set = {1, 2, 3}
my_set.add(4)                 # Add element
my_set.remove(2)              # Remove element
{1, 2} | {2, 3}              # Union: {1, 2, 3}
{1, 2} & {2, 3}              # Intersection: {2}
{1, 2} - {2, 3}              # Difference: {1}
```

### Tuple
```python
my_tuple = (1, 2, 3)
my_tuple[0]                   # Access (immutable!)
a, b, c = my_tuple            # Unpacking
my_tuple.count(2)             # Count occurrences
my_tuple.index(3)             # Find index
```

---
