# Python Iterators & Generators Cheat Sheet

## Quick Reference Card

| Operation | Syntax | Example |
|-----------|--------|---------|
| Iterator protocol | `__iter__()`, `__next__()` | Implement both methods |
| Get iterator | `iter(object)` | `iter([1, 2, 3])` |
| Get next item | `next(iterator)` | `next(it)` |
| Generator function | `def func(): yield` | Use yield keyword |
| Generator expression | `(x for x in range(10))` | Like list comprehension |
| Yield value | `yield value` | Pause and return value |
| Yield from | `yield from iterable` | Delegate to sub-iterator |
| Iterator exhausted | `StopIteration` | Raised when done |
| Infinite iterator | `itertools.count()` | Never stops |
| Chain iterators | `itertools.chain()` | Combine multiple |

## Table of Contents
1. [Iterator Basics](#iterator-basics)
2. [Creating Iterators](#creating-iterators)
3. [Generator Functions](#generator-functions)
4. [Generator Expressions](#generator-expressions)
5. [Advanced Generator Patterns](#advanced-generator-patterns)
6. [itertools Module](#itertools-module)
7. [Practical Examples](#practical-examples)
8. [Best Practices](#best-practices)

---

## Iterator Basics

### What Is an Iterator?

```python
# Iterators are objects that can be iterated (looped) upon
# They implement two methods: __iter__() and __next__()

# Lists, tuples, strings are iterables (can create iterators)
my_list = [1, 2, 3]

# Get iterator from iterable
my_iterator = iter(my_list)

# Get items one by one
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3

# When exhausted, raises StopIteration
try:
    print(next(my_iterator))
except StopIteration:
    print('No more items')
```

### Iterables vs Iterators

```python
# Iterable: Object that can return an iterator
# Has __iter__() method

# Iterator: Object that produces values one at a time
# Has __iter__() and __next__() methods

my_list = [1, 2, 3]  # Iterable

# Check if iterable
from collections.abc import Iterable, Iterator

print(isinstance(my_list, Iterable))   # True
print(isinstance(my_list, Iterator))   # False

# Get iterator
my_iter = iter(my_list)
print(isinstance(my_iter, Iterator))   # True
```

### How For Loops Work

```python
# For loops use iterators behind the scenes

# This:
for item in [1, 2, 3]:
    print(item)

# Is equivalent to:
iterator = iter([1, 2, 3])
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
```

---

## Creating Iterators

### Iterator Class

```python
class Counter:
    """Simple iterator that counts from start to end"""

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        """Return the iterator object (self)"""
        return self

    def __next__(self):
        """Return the next value"""
        if self.current >= self.end:
            raise StopIteration

        self.current += 1
        return self.current - 1

# Usage
counter = Counter(1, 5)
for num in counter:
    print(num)  # 1, 2, 3, 4

# Manual iteration
counter = Counter(1, 4)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
# next(counter) would raise StopIteration
```

### Iterator with State

```python
class Fibonacci:
    """Iterator for Fibonacci sequence"""

    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration

        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

# Usage
fib = Fibonacci(10)
for num in fib:
    print(num, end=' ')
# Output: 0 1 1 2 3 5 8 13 21 34
```

### Reverse Iterator

```python
class ReverseIterator:
    """Iterator that goes through sequence backwards"""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# Usage
rev = ReverseIterator([1, 2, 3, 4, 5])
for item in rev:
    print(item, end=' ')
# Output: 5 4 3 2 1
```

### Iterable Class (Contains Iterator)

```python
class PowersOfTwo:
    """Iterable class that creates iterator"""

    def __init__(self, max_exponent):
        self.max_exponent = max_exponent

    def __iter__(self):
        """Return a new iterator each time"""
        return PowersOfTwoIterator(self.max_exponent)

class PowersOfTwoIterator:
    """Iterator for powers of two"""

    def __init__(self, max_exponent):
        self.max_exponent = max_exponent
        self.exponent = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.exponent >= self.max_exponent:
            raise StopIteration

        result = 2 ** self.exponent
        self.exponent += 1
        return result

# Usage - can iterate multiple times
powers = PowersOfTwo(5)

for p in powers:
    print(p, end=' ')  # 1 2 4 8 16

print()

for p in powers:
    print(p, end=' ')  # 1 2 4 8 16 (works again!)
```

---

## Generator Functions

### Basic Generator

```python
def simple_generator():
    """Generator function using yield"""
    print('First yield')
    yield 1

    print('Second yield')
    yield 2

    print('Third yield')
    yield 3

# Create generator
gen = simple_generator()

# Generator is an iterator
print(next(gen))
# Output:
# First yield
# 1

print(next(gen))
# Output:
# Second yield
# 2

print(next(gen))
# Output:
# Third yield
# 3
```

### Generator vs Regular Function

```python
# Regular function - returns once
def regular_function():
    return [1, 2, 3]

# Generator function - yields multiple times
def generator_function():
    yield 1
    yield 2
    yield 3

# Regular function returns entire list
result = regular_function()
print(result)  # [1, 2, 3]

# Generator function returns generator object
gen = generator_function()
print(gen)  # <generator object>

# Get values one at a time
for value in gen:
    print(value)  # 1, 2, 3
```

### Generator with Loop

```python
def count_up_to(max):
    """Generate numbers from 1 to max"""
    count = 1
    while count <= max:
        yield count
        count += 1

# Usage
for num in count_up_to(5):
    print(num)  # 1, 2, 3, 4, 5

# Memory efficient for large ranges
# Only one number in memory at a time
for num in count_up_to(1000000):
    if num > 10:
        break
    print(num)
```

### Generator with State

```python
def fibonacci(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Usage
for num in fibonacci(10):
    print(num, end=' ')
# Output: 0 1 1 2 3 5 8 13 21 34
```

### Infinite Generators

```python
def infinite_counter(start=0):
    """Generate infinite sequence"""
    count = start
    while True:
        yield count
        count += 1

# Usage - be careful with infinite generators!
counter = infinite_counter()
for i in range(5):
    print(next(counter))  # 0, 1, 2, 3, 4

# Take first n items
def take(n, iterable):
    """Take first n items from iterable"""
    for i, item in enumerate(iterable):
        if i >= n:
            break
        yield item

# Use with infinite generator
counter = infinite_counter(10)
for num in take(5, counter):
    print(num)  # 10, 11, 12, 13, 14
```

---

## Generator Expressions

### Basic Generator Expression

```python
# Generator expression - like list comprehension but with ()
# Memory efficient - generates values on demand

# List comprehension - creates entire list in memory
squares_list = [x**2 for x in range(1000000)]

# Generator expression - creates values one at a time
squares_gen = (x**2 for x in range(1000000))

# Generator expressions are iterators
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4

# Can iterate over generator expression
squares = (x**2 for x in range(5))
for square in squares:
    print(square)  # 0, 1, 4, 9, 16
```

### Generator Expression vs List Comprehension

```python
# List comprehension - all in memory
numbers_list = [x for x in range(1000000)]
print(type(numbers_list))  # <class 'list'>

# Generator expression - lazy evaluation
numbers_gen = (x for x in range(1000000))
print(type(numbers_gen))  # <class 'generator'>

# Memory usage comparison
import sys
print(sys.getsizeof(numbers_list))  # Large size
print(sys.getsizeof(numbers_gen))   # Small size (just generator object)
```

### Filtering with Generator Expressions

```python
# Filter even numbers
evens = (x for x in range(10) if x % 2 == 0)
for num in evens:
    print(num)  # 0, 2, 4, 6, 8

# Complex filtering
# Only positive squares of even numbers
result = (x**2 for x in range(-10, 11) if x % 2 == 0 and x > 0)
print(list(result))  # [4, 16, 36, 64, 100]
```

### Nested Generator Expressions

```python
# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = (item for sublist in nested for item in sublist)
print(list(flat))  # [1, 2, 3, 4, 5, 6]

# Create coordinate pairs
coords = ((x, y) for x in range(3) for y in range(3))
for coord in coords:
    print(coord)
# Output: (0,0), (0,1), (0,2), (1,0), (1,1), etc.
```

### Generator Expressions in Functions

```python
# Can pass generator expression directly to functions
# No need for extra parentheses

# Sum of squares
result = sum(x**2 for x in range(10))
print(result)  # 285

# Maximum of cubes
result = max(x**3 for x in range(5))
print(result)  # 64

# Any/all
result = any(x > 5 for x in [1, 2, 3, 4, 5])
print(result)  # False

result = all(x > 0 for x in [1, 2, 3, 4, 5])
print(result)  # True
```

---

## Advanced Generator Patterns

### Generator with Send

```python
def echo_generator():
    """Generator that receives values via send()"""
    while True:
        received = yield
        print(f'Received: {received}')

gen = echo_generator()
next(gen)  # Prime the generator
gen.send('Hello')  # Received: Hello
gen.send('World')  # Received: World
```

### Generator with Return Value

```python
def generator_with_return():
    """Generator can have a return value"""
    yield 1
    yield 2
    yield 3
    return 'Finished!'

gen = generator_with_return()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

try:
    print(next(gen))
except StopIteration as e:
    print(e.value)  # Finished!
```

### Yield From (Delegation)

```python
def generator1():
    yield 1
    yield 2

def generator2():
    yield 3
    yield 4

def combined():
    """Delegate to multiple generators"""
    yield from generator1()
    yield from generator2()

for value in combined():
    print(value)  # 1, 2, 3, 4

# More practical example
def read_files(filenames):
    """Read lines from multiple files"""
    for filename in filenames:
        with open(filename, 'r') as f:
            yield from f  # Yield each line
```

### Generator Pipeline

```python
# Chain generators for data processing pipeline

def read_numbers(filename):
    """Generator 1: Read numbers from file"""
    with open(filename) as f:
        for line in f:
            yield int(line.strip())

def filter_positive(numbers):
    """Generator 2: Filter positive numbers"""
    for num in numbers:
        if num > 0:
            yield num

def square_numbers(numbers):
    """Generator 3: Square each number"""
    for num in numbers:
        yield num ** 2

# Build pipeline
numbers = read_numbers('numbers.txt')
positive = filter_positive(numbers)
squared = square_numbers(positive)

# Process data efficiently
for result in squared:
    print(result)

# Or chain in one expression
result = square_numbers(filter_positive(read_numbers('numbers.txt')))
```

### Coroutines with Generators

```python
def running_average():
    """Coroutine that maintains running average"""
    total = 0
    count = 0

    while True:
        value = yield (total / count if count > 0 else 0)
        total += value
        count += 1

# Usage
avg = running_average()
next(avg)  # Prime the generator

print(avg.send(10))  # 10.0
print(avg.send(20))  # 15.0
print(avg.send(30))  # 20.0
```

---

## itertools Module

### Infinite Iterators

```python
import itertools

# count(start, step) - infinite counting
counter = itertools.count(10, 2)
print(next(counter))  # 10
print(next(counter))  # 12
print(next(counter))  # 14

# Take first n values
for i, val in enumerate(itertools.count()):
    if i >= 5:
        break
    print(val)  # 0, 1, 2, 3, 4

# cycle(iterable) - infinite repetition
colors = itertools.cycle(['red', 'green', 'blue'])
for i in range(7):
    print(next(colors))  # red, green, blue, red, green, blue, red

# repeat(value, times) - repeat value
for val in itertools.repeat('Hello', 3):
    print(val)  # Hello, Hello, Hello
```

### Combinatoric Iterators

```python
import itertools

# combinations(iterable, r) - all combinations of length r
letters = ['A', 'B', 'C']
for combo in itertools.combinations(letters, 2):
    print(combo)
# ('A', 'B'), ('A', 'C'), ('B', 'C')

# permutations(iterable, r) - all permutations
for perm in itertools.permutations(letters, 2):
    print(perm)
# ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')

# product(*iterables) - Cartesian product
for prod in itertools.product([1, 2], ['A', 'B']):
    print(prod)
# (1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')

# combinations_with_replacement
for combo in itertools.combinations_with_replacement('AB', 2):
    print(combo)
# ('A', 'A'), ('A', 'B'), ('B', 'B')
```

### Terminating Iterators

```python
import itertools

# chain(*iterables) - chain multiple iterables
for val in itertools.chain([1, 2], [3, 4], [5, 6]):
    print(val)  # 1, 2, 3, 4, 5, 6

# compress(data, selectors) - filter based on selectors
data = ['A', 'B', 'C', 'D']
selectors = [1, 0, 1, 0]  # 1=keep, 0=skip
result = itertools.compress(data, selectors)
print(list(result))  # ['A', 'C']

# dropwhile(predicate, iterable) - drop while predicate is true
numbers = [1, 2, 3, 4, 1, 2]
result = itertools.dropwhile(lambda x: x < 3, numbers)
print(list(result))  # [3, 4, 1, 2]

# takewhile(predicate, iterable) - take while predicate is true
result = itertools.takewhile(lambda x: x < 3, numbers)
print(list(result))  # [1, 2]

# islice(iterable, start, stop, step) - slice an iterator
result = itertools.islice(range(10), 2, 8, 2)
print(list(result))  # [2, 4, 6]
```

### Grouping and Accumulating

```python
import itertools

# groupby(iterable, key) - group consecutive elements
data = [('A', 1), ('A', 2), ('B', 1), ('B', 2), ('A', 3)]
for key, group in itertools.groupby(data, lambda x: x[0]):
    print(f'{key}: {list(group)}')
# A: [('A', 1), ('A', 2)]
# B: [('B', 1), ('B', 2)]
# A: [('A', 3)]

# accumulate(iterable, func) - cumulative operation
numbers = [1, 2, 3, 4, 5]
result = itertools.accumulate(numbers)
print(list(result))  # [1, 3, 6, 10, 15] (cumulative sum)

# With custom function
import operator
result = itertools.accumulate(numbers, operator.mul)
print(list(result))  # [1, 2, 6, 24, 120] (cumulative product)
```

---

## Practical Examples

### Reading Large Files

```python
def read_large_file(filename):
    """Memory-efficient file reading"""
    with open(filename, 'r') as f:
        for line in f:  # File object is an iterator
            yield line.strip()

# Process huge file line by line
for line in read_large_file('huge_file.txt'):
    process(line)  # Only one line in memory at a time
```

### Processing Data in Batches

```python
def batch_iterator(iterable, batch_size):
    """Yield data in batches"""
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []

    # Yield remaining items
    if batch:
        yield batch

# Usage
data = range(10)
for batch in batch_iterator(data, 3):
    print(batch)
# [0, 1, 2], [3, 4, 5], [6, 7, 8], [9]
```

### Sliding Window

```python
from collections import deque

def sliding_window(iterable, n):
    """Yield sliding window of size n"""
    it = iter(iterable)
    window = deque(maxlen=n)

    # Fill initial window
    for _ in range(n):
        try:
            window.append(next(it))
        except StopIteration:
            return

    yield tuple(window)

    # Slide window
    for item in it:
        window.append(item)
        yield tuple(window)

# Usage
for window in sliding_window([1, 2, 3, 4, 5], 3):
    print(window)
# (1, 2, 3), (2, 3, 4), (3, 4, 5)
```

### Fibonacci Sequence

```python
def fibonacci():
    """Infinite Fibonacci generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 Fibonacci numbers
fib = fibonacci()
result = [next(fib) for _ in range(10)]
print(result)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Prime Numbers

```python
def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes():
    """Generate prime numbers"""
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

# Get first 10 primes
prime_gen = primes()
result = [next(prime_gen) for _ in range(10)]
print(result)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

### Tree Traversal

```python
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

def traverse_depth_first(node):
    """Depth-first tree traversal generator"""
    yield node.value
    for child in node.children:
        yield from traverse_depth_first(child)

# Build tree
root = Node(1, [
    Node(2, [Node(4), Node(5)]),
    Node(3, [Node(6)])
])

# Traverse
for value in traverse_depth_first(root):
    print(value)  # 1, 2, 4, 5, 3, 6
```

---

## Best Practices

### Use Generators for Large Data

```python
# Bad: Load everything into memory
def read_all_lines(filename):
    with open(filename) as f:
        return f.readlines()  # Entire file in memory

# Good: Process one line at a time
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()  # One line at a time
```

### Generator Expressions for Simple Cases

```python
# Bad: Unnecessary function for simple generator
def squares(n):
    for i in range(n):
        yield i ** 2

# Good: Use generator expression
squares = (i**2 for i in range(n))
```

### Iterators for Complex State

```python
# Bad: Try to cram complex logic into generator expression
# (Hard to read)

# Good: Use iterator class for complex state
class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.state = {}

    def __iter__(self):
        return self

    def __next__(self):
        # Complex processing logic
        pass
```

### Don't Reuse Exhausted Generators

```python
# Generators are single-use
gen = (x for x in range(5))
list1 = list(gen)  # [0, 1, 2, 3, 4]
list2 = list(gen)  # [] - Generator exhausted!

# Solution: Use list or create new generator
data = list(x for x in range(5))
list1 = data
list2 = data  # Both have data
```

### Use itertools for Common Patterns

```python
import itertools

# Instead of reimplementing
def my_chain(iter1, iter2):
    for item in iter1:
        yield item
    for item in iter2:
        yield item

# Use built-in
combined = itertools.chain(iter1, iter2)
```

### Close Generators with Try/Finally

```python
def resource_generator():
    """Generator that manages resources"""
    resource = acquire_resource()
    try:
        while True:
            data = resource.get_data()
            yield data
    finally:
        resource.close()  # Cleanup when generator closed
```

---

## See Also

- **[Functional Programming Cheat Sheet](Functional_Programming_Cheat_Sheet.md)** - Map, filter, and functional concepts
- **[Data Structures Cheat Sheet](Data_Structures_Cheat_Sheet.md)** - Lists and data structures
- **[Python Basics Cheat Sheet](Python_Basics_Cheat_Sheet.md)** - Loops and control flow

---