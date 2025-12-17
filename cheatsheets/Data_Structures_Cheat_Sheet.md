# Python Data Structures - Complete Reference Guide

This guide provides a comprehensive overview of fundamental Python data structures: Lists, Dictionaries, Sets, and Tuples. Understanding these structures is crucial for efficient data organization and manipulation in Python programming.

## Quick Reference Card

| Data Structure | Creation                  | Add                | Remove               | Access     | Mutable? | Ordered?* | Unique Elements? |
| :------------- | :------------------------ | :----------------- | :------------------- | :--------- | :------- | :-------- | :--------------- |
| **List**       | `[1, 2, 3]`               | `.append(x)`       | `.remove(x)`         | `list[0]`  | Yes      | Yes       | No               |
| **Dictionary** | `{"a": 1}`                | `dict["key"] = val`| `del dict["key"]`    | `dict["key"]` | Yes      | Yes       | Keys Only        |
| **Set**        | `{1, 2, 3}` / `set()`     | `.add(x)`          | `.remove(x)`         | N/A        | Yes      | No        | Yes              |
| **Tuple**      | `(1, 2, 3)` / `(x,)`      | N/A (immutable)    | N/A (immutable)      | `tuple[0]` | No       | Yes       | No               |

*Dictionaries are ordered as of Python 3.7+ (insertion order).

## Table of Contents
- [Lists](#lists)
- [Dictionaries](#dictionaries)
- [Sets](#sets)
- [Tuples](#tuples)
- [Linked Lists](#linked-lists)
- [Stacks & Queues](#stacks--queues)

---

## 1. Lists

Lists are ordered, mutable collections that can hold items of different data types.

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

---

## 2. Dictionaries

Dictionaries are unordered (ordered by insertion as of Python 3.7+), mutable collections of key-value pairs. Keys must be unique and immutable.

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

# Using dict() constructor with keyword arguments
user = dict(name="Charlie", age=35)

# From lists of tuples
items = [("apple", 1), ("banana", 2)]
fruit_counts = dict(items) # {"apple": 1, "banana": 2}
```

### Accessing Values
```python
person = {"name": "Wilson", "age": 30, "city": "NYC"}

# Direct access (raises KeyError if key doesn't exist)
name = person["name"]  # "Wilson"

# Safe access with get() (returns None if key doesn't exist, or a default value)
email = person.get("email")      # None
email = person.get("email", "no-email@example.com")  # "no-email@example.com"

# Check if key exists
if "age" in person:
    print(person["age"])
```

### Modifying Dictionaries
```python
person = {"name": "Wilson", "age": 30}

# Add or update a key-value pair
person["email"] = "Wilson@example.com"  # Adds new key
person["age"] = 31                      # Updates existing key

# Update multiple items using .update()
person.update({"city": "NYC", "phone": "555-1234"})

# Remove items
del person["city"]                   # Removes specific key
email = person.pop("email")          # Removes and returns value for key
email = person.pop("email", None)    # Safe removal, returns None if key not found

# Remove last inserted item (Python 3.7+ - guaranteed to be last)
item = person.popitem()

# Clear all items
person.clear()
```

### Looping Through Dictionaries
```python
person = {"name": "Wilson", "age": 30, "city": "NYC"}

# Loop through keys (default)
for key in person:
    print(key)

for key in person.keys(): # Explicitly loop keys
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
# Syntax: {key_expr: value_expr for item in iterable if condition}

# Create dict from list of numbers
numbers = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in numbers}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition (only even numbers)
evens_squared = {x: x**2 for x in numbers if x % 2 == 0} # {2: 4, 4: 16}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}  # {1: "a", 2: "b", 3: "c"}
```

### Nested Dictionaries
Dictionaries can contain other dictionaries (or lists, sets, tuples) as values.

```python
users = {
    "user1": {"name": "Alice", "age": 30, "email": "alice@example.com"},
    "user2": {"name": "Bob", "age": 25, "email": "bob@example.com"}
}

# Access nested values
alice_email = users["user1"]["email"] # "alice@example.com"

# Add a new contact (example from new data)
contact = {}
name = "Charlie"
phone = "555-1111"
email = "charlie@example.com"

contact[name] = {
    "phone": phone,
    "email": email
}
print(contact) # {'Charlie': {'phone': '555-1111', 'email': 'charlie@example.com'}}
```

---

## 3. Sets

Sets are unordered, mutable collections of *unique* elements. They are useful for membership testing and eliminating duplicate entries.

### Creating Sets
```python
# Empty set (must use set(), {} creates an empty dictionary)
my_set = set()

# Set with values (duplicates are automatically removed)
numbers = {1, 2, 3, 4, 5, 2, 3} # {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}

# From a list (removes duplicates)
duplicate_list = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(duplicate_list) # {1, 2, 3, 4}
```

### Set Operations
```python
numbers = {1, 2, 3}

# Add a single element
numbers.add(4) # {1, 2, 3, 4}

# Add multiple elements from an iterable
numbers.update([5, 6, 7]) # {1, 2, 3, 4, 5, 6, 7}

# Remove an element
numbers.remove(3) # Removes 3. Raises KeyError if not found.
numbers.discard(2) # Removes 2. No error if not found.

# Remove and return an arbitrary element
item = numbers.pop()

# Clear all elements
numbers.clear()

# Membership testing (very efficient)
is_present = 3 in {1, 2, 3} # True
```

### Set Mathematics (Comparison Operations)
```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union (all unique elements from both sets)
union_set = a | b          # {1, 2, 3, 4, 5, 6, 7, 8}
union_set_method = a.union(b)

# Intersection (elements common to both sets)
intersection_set = a & b   # {4, 5}
intersection_set_method = a.intersection(b)

# Difference (elements in a but not in b)
difference_set = a - b     # {1, 2, 3}
difference_set_method = a.difference(b)

# Symmetric difference (elements in a or b, but not in both)
sym_difference_set = a ^ b # {1, 2, 3, 6, 7, 8}
sym_difference_set_method = a.symmetric_difference(b)

# Subset: check if all elements of one set are in another
is_subset = {1, 2}.issubset({1, 2, 3}) # True

# Superset: check if one set contains all elements of another
is_superset = {1, 2, 3}.issuperset({1, 2}) # True

# Disjoint: check if two sets have no elements in common
is_disjoint = {1, 2}.isdisjoint({3, 4}) # True
```

### Set Comprehensions
```python
# Syntax: {expression for item in iterable if condition}
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}

# With condition
evens = {x for x in range(10) if x % 2 == 0} # {0, 2, 4, 6, 8}
```

---

## 4. Tuples

Tuples are ordered, *immutable* collections. Once a tuple is created, its elements cannot be changed, added, or removed. They are often used for fixed collections of items or as dictionary keys.

### Creating Tuples
```python
# Empty tuple
empty_tuple = ()
empty_tuple_alt = tuple()

# Tuple with values
numbers_tuple = (1, 2, 3, 4, 5)
fruits_tuple = ("apple", "banana", "cherry")

# Single element tuple (comma is crucial!)
single_item_tuple = (42,) # This is a tuple
not_a_tuple = (42)        # This is just an integer inside parentheses

# Tuple packing (without parentheses)
coordinates = 10, 20, 30 # (10, 20, 30)
```

### Accessing Tuples
```python
fruits_tuple = ("apple", "banana", "cherry", "date")

# Indexing (0-based, same as lists)
print(fruits_tuple[0])   # "apple"
print(fruits_tuple[-1])  # "date"

# Slicing (same as lists)
print(fruits_tuple[1:3]) # ("banana", "cherry")

# Unpacking (assigning tuple elements to individual variables)
name, age, city = ("Alice", 30, "New York")
print(f"Name: {name}, Age: {age}, City: {city}")

# Unpacking with * (for variable number of elements)
first, *middle, last = (1, 2, 3, 4, 5)
print(f"First: {first}, Middle: {middle}, Last: {last}")
# Output: First: 1, Middle: [2, 3, 4], Last: 5
```

### Tuple Methods
Since tuples are immutable, they have fewer methods than lists.

```python
numbers_tuple = (1, 2, 3, 2, 1, 2)

# count(): Returns the number of times a specified value occurs in a tuple.
print(numbers_tuple.count(2)) # Output: 3

# index(): Searches the tuple for a specified value and returns the position of where it was found.
print(numbers_tuple.index(3)) # Output: 2

# len(): Returns the number of items in the tuple.
print(len(numbers_tuple)) # Output: 6

# min(), max(), sum(): Works similarly to lists.
print(min(numbers_tuple)) # Output: 1
print(max(numbers_tuple)) # Output: 3
print(sum(numbers_tuple)) # Output: 11
```

### Immutability of Tuples
Once created, elements of a tuple cannot be changed.

```python
my_tuple = (10, 20, 30)
# my_tuple[0] = 15 # This would raise a TypeError!

# You can reassign the variable to a new tuple, but not modify the original.
my_tuple = (15, 20, 30)
```

### When to Use Tuples

*   **Fixed Data Collections:** For data that should not change throughout the program's execution (e.g., coordinates, RGB color values).
*   **Function Return Values:** Functions can return multiple values as a tuple, which can then be unpacked.
*   **Dictionary Keys:** Because tuples are immutable, they can be used as keys in dictionaries (unlike lists).
*   **Performance:** Tuples can sometimes be slightly faster than lists for iteration over small collections, and they consume less memory.

---

## 5. Linked Lists

A Linked List is a linear data structure where elements are not stored at contiguous memory locations. Instead, each element (node) is a separate object that contains a reference (or link) to the next node in the sequence.

### Node Class
```python
class Node:
    """Represents a single node in a linked list."""
    def __init__(self, data):
        self.data = data  # The value this node holds
        self.next = None  # Pointer to the next node
```

### LinkedList Class (Singly Linked List)
```python
class LinkedList:
    """A basic singly linked list implementation."""

    def __init__(self):
        self.head = None  # The first node in the list
        self.tail = None  # The last node in the list (for O(1) appends)

    def is_empty(self):
        """Checks if the linked list is empty."""
        return self.head is None

    def append(self, data):
        """Adds a new node with the given data to the end of the list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        """Adds a new node with the given data to the beginning of the list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        """Deletes the first occurrence of a node with the given data."""
        if self.is_empty():
            return

        # Case 1: Head node is the one to be deleted
        if self.head.data == data:
            self.head = self.head.next
            if self.head is None: # If list becomes empty after deletion
                self.tail = None
            return

        # Case 2: Node to be deleted is elsewhere in the list
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next # Skip over the node to delete
                if current.next is None: # If we deleted the tail
                    self.tail = current
                return
            current = current.next

    def display(self):
        """Prints all elements in the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    def get_at_position(self, position):
        """Retrieves the data of the node at a specific 0-indexed position."""
        if position < 0:
            return None # Invalid position

        current = self.head
        count = 0
        while current:
            if count == position:
                return current.data
            current = current.next
            count += 1
        return None # Position out of bounds
```

### Using Linked Lists
```python
# Create a linked list instance
my_linked_list = LinkedList()

# Append elements
my_linked_list.append(10)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.display() # Output: 10 -> 20 -> 30 -> None

# Prepend an element
my_linked_list.prepend(5)
my_linked_list.display() # Output: 5 -> 10 -> 20 -> 30 -> None

# Get element at a position
print(f"Element at position 2: {my_linked_list.get_at_position(2)}") # Output: Element at position 2: 20

# Delete an element
my_linked_list.delete(20)
my_linked_list.display() # Output: 5 -> 10 -> 30 -> None

my_linked_list.delete(5) # Delete head
my_linked_list.display() # Output: 10 -> 30 -> None

my_linked_list.delete(30) # Delete tail
my_linked_list.display() # Output: 10 -> None

my_linked_list.delete(10) # Delete last element
my_linked_list.display() # Output: None
```

---

## 6. Stacks & Queues

Stacks and Queues are abstract data types (ADTs) that define how elements can be added and removed from a collection.

### Stack (LIFO - Last In First Out)
In a stack, the last element added is the first one to be removed. Think of a stack of plates.

```python
# Python lists can be used as stacks (efficient for append/pop from end)
stack = []

# Push (add element to the top of the stack)
stack.append("plate1")
stack.append("plate2")
stack.append("plate3")
print(f"Stack after pushes: {stack}") # Output: ['plate1', 'plate2', 'plate3']

# Pop (remove and return the top element)
top_item = stack.pop()
print(f"Popped item: {top_item}") # Output: plate3
print(f"Stack after pop: {stack}") # Output: ['plate1', 'plate2']

# Peek (view the top element without removing it)
peek_item = stack[-1] if stack else None
print(f"Peeked item: {peek_item}") # Output: plate2

# Check if empty
is_empty = len(stack) == 0
print(f"Is stack empty? {is_empty}") # Output: False

# Size
size = len(stack)
print(f"Stack size: {size}") # Output: 2
```

### Queue (FIFO - First In First Out)
In a queue, the first element added is the first one to be removed. Think of a line at a store.
For efficient queue operations, Python's `collections.deque` is preferred over a standard list because `pop(0)` from a list is O(n), while `popleft()` from a `deque` is O(1).

```python
from collections import deque

queue = deque()

# Enqueue (add element to the rear of the queue)
queue.append("person1")
queue.append("person2")
queue.append("person3")
print(f"Queue after enqueues: {queue}") # Output: deque(['person1', 'person2', 'person3'])

# Dequeue (remove and return the front element)
front_item = queue.popleft()
print(f"Dequeued item: {front_item}") # Output: person1
print(f"Queue after dequeue: {queue}") # Output: deque(['person2', 'person3'])

# Peek (view the front element without removing it)
peek_item = queue[0] if queue else None
print(f"Peeked item: {peek_item}") # Output: person2

# Check if empty
is_empty = len(queue) == 0
print(f"Is queue empty? {is_empty}") # Output: False

# Size
size = len(queue)
print(f"Queue size: {size}") # Output: 2
```

---

## 7. Trees

A **Tree** is a hierarchical data structure consisting of nodes connected by edges.

*   **Node:** An entity containing a key or value.
*   **Root:** The topmost node (no parent).
*   **Leaf:** A node with no children.
*   **Edge:** The link between two nodes.

### Binary Tree
Each node has at most two children (Left and Right).

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode("Book1")
root.left = TreeNode("Book2")
root.right = TreeNode("Book3")
```

---

## 8. Graphs

A **Graph** is a non-linear data structure consisting of **Vertices** (nodes) and **Edges** (connections). Used for maps, social networks, and routing.

### Key Concepts
*   **Directed Graph:** Edges have a direction (A -> B). Like a one-way street.
*   **Undirected Graph:** Edges have no direction (A <-> B). Like a two-way street.
*   **Weighted Graph:** Edges have values (weights), representing distance or cost.

### Representations

**1. Adjacency Matrix**
A 2D array (table) where `matrix[i][j]` represents an edge from `i` to `j`. Good for dense graphs.

```python
# 0: No connection, 1: Connection
matrix = [
    [0, 1, 0], # Node 0 connects to 1
    [1, 0, 1], # Node 1 connects to 0 and 2
    [0, 1, 0]  # Node 2 connects to 1
]
```

**2. Adjacency List**
A dictionary where each key is a vertex and its value is a list of connected vertices. Good for sparse graphs (most common).

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
```

---

## 9. Data Structure Comparison

| Operation      | List          | Dictionary     | Set             | Tuple         |
| :------------- | :------------ | :------------- | :-------------- | :------------ |
| **Ordered**    | Yes           | Yes (Python 3.7+) | No           | Yes           |
| **Mutable**    | Yes           | Yes            | Yes             | No            |
| **Duplicates** | Yes           | Keys: No, Values: Yes | No          | Yes           |
| **Indexing**   | Yes (by int)  | Yes (by key)   | No              | Yes (by int)  |
| **Add**        | `.append()`   | `dict[key] = val` | `.add()`        | N/A           |
| **Remove**     | `.remove()`   | `del dict[key]`   | `.remove()`     | N/A           |
| **Lookup Speed**| O(n) Avg/Worst | O(1) Avg/Worst | O(1) Avg/Worst | O(n) Avg/Worst |

---

## See Also

-   **[Python Basics Cheat Sheet](../cheatsheets/Python_Basics_Cheat_Sheet.md)** - Essential Python syntax and concepts.
-   **[Standard Library Essentials Cheat Sheet](../cheatsheets/Standard_Library_Essentials_Cheat_Sheet.md)** - More on Python's built-in tools.
-   **[Iterators and Generators Cheat Sheet](../cheatsheets/Iterators_and_Generators_Cheat_Sheet.md)** - How to efficiently process data collections.
-   **[Big O Notation Cheat Sheet](../cheatsheets/Big_O_Notation_Cheat_Sheet.md)** - Understanding the performance characteristics of data structures and algorithms.
-   **[Linked Lists and Custom Data Structures Guide](../guides/Linked_Lists_and_Custom_Data_Structures_Guide.md)** - Detailed guide on implementing and using linked lists.