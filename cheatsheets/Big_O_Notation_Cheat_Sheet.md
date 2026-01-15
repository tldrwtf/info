# Big O Notation & Time Complexity - Complete Reference Guide

Big O Notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. In computer science, it is used to classify algorithms according to how their running time or space requirements grow as the input size grows.

## Quick Reference Card

| Complexity | Name           | Description                                  | Example Operation             | Growth Rate |
| :--------- | :------------- | :------------------------------------------- | :---------------------------- | :---------- |
| **O(1)**   | Constant       | Time is independent of input size.           | Array/List access by index, hash map lookup | Best        |
| **O(log n)**| Logarithmic    | Time grows proportional to the logarithm of the input size. | Binary search                 | Excellent   |
| **O(n)**   | Linear         | Time grows linearly with the input size.     | Simple loop over an array, linear search | Good        |
| **O(n log n)**| Linearithmic   | Time grows proportional to n multiplied by the logarithm of n. | Efficient sorting algorithms (Merge Sort, Quick Sort) | Fair        |
| **O(n²)**  | Quadratic      | Time grows proportionally to the square of the input size. | Nested loops over the same input | Poor        |
| **O(2ⁿ)**  | Exponential    | Time doubles with each additional input.     | Recursive Fibonacci (naive), generating subsets | Very Bad    |
| **O(n!)**  | Factorial      | Time grows by a factor of n for each additional input. | Traveling Salesman (naive), permutations | Worst       |

---

## Table of Contents
- [1. What is Big O Notation?](#1-what-is-big-o-notation)
- [2. Practical Time Complexity Examples](#2-practical-time-complexity-examples)
- [3. Common Time Complexities](#3-common-time-complexities)
    - [O(1) - Constant Time](#o1---constant-time)
    - [O(log n) - Logarithmic Time](#olog-n---logarithmic-time)
    - [O(n) - Linear Time](#on---linear-time)
    - [O(n log n) - Linearithmic Time](#on-log-n---linearithmic-time)
    - [O(n²) - Quadratic Time](#on²---quadratic-time)
    - [O(2ⁿ) - Exponential Time](#o2ⁿ---exponential-time)
    - [O(n!) - Factorial Time](#on---factorial-time)
- [4. Analyzing Algorithm Complexity](#4-analyzing-algorithm-complexity)
- [5. Space Complexity](#5-space-complexity)
- [6. Data Structure Operation Complexities](#6-data-structure-operation-complexities)
- [7. Best Practices for Optimization](#7-best-practices-for-optimization)

---

## 1. What is Big O Notation?

Big O Notation is a way to describe the efficiency of an algorithm, indicating how the runtime or space requirements scale with the input size. It provides a high-level understanding of an algorithm's performance characteristic.

### Definition
*   **Focuses on worst-case scenario**: Usually, Big O describes the upper bound of an algorithm's growth rate.
*   **Growth rate**: It's concerned with how the number of operations (or memory usage) grows as the input size (`n`) approaches infinity.
*   **Ignores constants and lower-order terms**: For example, `O(2n + 10)` simplifies to `O(n)`. `O(n^2 + n)` simplifies to `O(n^2)`.

### Why Big O Matters
Understanding Big O helps in:
*   **Comparing algorithms**: Determining which algorithm is faster or uses less memory for large inputs.
*   **Identifying bottlenecks**: Pinpointing parts of the code that will become slow as data grows.
*   **Designing scalable systems**: Choosing efficient approaches from the outset.

---

## 2. Practical Time Complexity Examples

Before diving into theoretical complexity classes, let's see how Big O impacts real-world performance with concrete examples.

### Dictionary Operations (O(1) - Constant Time)

```python
# O(1) - Dictionary access
user_dict = {"alice": 25, "bob": 30, "charlie": 28}
age = user_dict["alice"]  # Instant lookup, no matter how many users

# O(1) - Dictionary membership check
if "alice" in user_dict:  # Fast check using hash table
    print("Found!")

# Why this matters: Even with 1,000,000 users, lookup is still instant
```

**Why this matters**: Dictionaries use hash tables for O(1) access regardless of size. With 1 million items, dictionary lookup takes the same time as with 10 items.

### List Operations Comparison

```python
# O(1) - Append to list (amortized)
numbers = [1, 2, 3]
numbers.append(4)  # Fast! Just adds to the end

# O(n) - Insert at beginning
numbers.insert(0, 0)  # Slow! Must shift all elements right
# [0, 1, 2, 3, 4]  All elements had to move

# Performance Impact:
# List with 1,000 items:
# - append(x): ~0.0001ms
# - insert(0, x): ~0.05ms  (500x slower!)
```

### Real-World Optimization Example

```python
# BAD: O(n) membership check with list
def check_membership_slow(item, items_list):
    """Check if item exists in list - O(n)"""
    return item in items_list  # Linear search through entire list

# GOOD: O(1) membership check with set
def check_membership_fast(item, items_set):
    """Check if item exists in set - O(1)"""
    return item in items_set  # Hash lookup, instant

# Performance Comparison:
items_list = list(range(1_000_000))  # 1 million items
items_set = set(range(1_000_000))

# List lookup (worst case - item not in list):
# Average time: ~50ms  (checks all 1,000,000 items)

# Set lookup (any case):
# Average time: ~0.0001ms  (hash table lookup)

# Speedup: 500,000x faster!
```

### Dictionary vs List for Data Lookup

```python
# Scenario: Find user by ID from 10,000 users

# BAD: O(n) - List of dictionaries
users_list = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    # ... 10,000 users
]

def find_user_slow(user_id):
    for user in users_list:  # O(n) - scans entire list
        if user["id"] == user_id:
            return user
    return None

# Average lookups per second: ~2,000

# GOOD: O(1) - Dictionary by ID
users_dict = {
    1: {"id": 1, "name": "Alice"},
    2: {"id": 2, "name": "Bob"},
    # ... 10,000 users
}

def find_user_fast(user_id):
    return users_dict.get(user_id)  # O(1) - hash lookup

# Average lookups per second: ~1,000,000 (500x faster!)
```

### Time Complexity Practice Problems

Try optimizing these common scenarios:

1. **Find duplicate numbers in a list** (Hint: use a set for O(n) instead of nested loops O(n²))
2. **Count word frequency in text** (Hint: use a dictionary for O(n) counting)
3. **Remove duplicates from list while preserving order** (Hint: set for tracking, list for order)

**Solutions:**

```python
# Problem 1: Find duplicates - O(n) solution
def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:  # O(1) lookup
            duplicates.add(num)
        seen.add(num)  # O(1) insertion
    return list(duplicates)
# Time: O(n), Space: O(n)

# Problem 2: Word frequency - O(n) solution
def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:  # O(n) loop
        frequency[word] = frequency.get(word, 0) + 1  # O(1) operations
    return frequency
# Time: O(n), Space: O(n)

# Problem 3: Remove duplicates preserving order - O(n) solution
def remove_duplicates_ordered(items):
    seen = set()
    result = []
    for item in items:  # O(n) loop
        if item not in seen:  # O(1) check
            seen.add(item)  # O(1) insertion
            result.append(item)  # O(1) amortized append
    return result
# Time: O(n), Space: O(n)
```

### Key Takeaway

**Choosing the right data structure matters!**
- Lists: Great for ordered data, append operations
- Dictionaries/Sets: Great for lookups, uniqueness checks
- The difference can be 100x-500,000x faster

---

## 3. Common Time Complexities

This section details the most common Big O time complexities, ordered from most efficient to least efficient.

### O(1) - Constant Time

The execution time or space required does not change as the input size grows. This is the ideal efficiency.

```python
# Accessing an element in a list by index
my_list = [10, 20, 30, 40, 50]
first_element = my_list[0] # O(1)
last_element = my_list[-1] # O(1)

# Accessing a value in a dictionary by key
my_dict = {"name": "Alice", "age": 30}
user_name = my_dict["name"] # O(1) on average

# Basic arithmetic operations
result = 5 + 3 # O(1)

# Assigning a value to a variable
x = 10 # O(1)
```

### O(log n) - Logarithmic Time

The execution time grows proportionally to the logarithm of the input size. This typically occurs in algorithms that repeatedly halve the problem size.

```python
# Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid # Found it!
        elif guess < target:
            low = mid + 1 # Guess was too low, discard left half
        else:
            high = mid + 1 # Guess was too high, discard right half
    return -1 # Not found

sorted_numbers = [1, 5, 7, 10, 15, 20, 25, 30]
print(binary_search(sorted_numbers, 20)) # Output: 5
print(binary_search(sorted_numbers, 13)) # Output: -1

# Why log n? If you have 1,000,000 items, it takes about log2(1,000,000) ~= 20 steps to find an item.
```

### O(n) - Linear Time

The execution time grows linearly with the input size. If the input doubles, the time roughly doubles.

```python
# Iterating through a list (linear search)
def find_item_linear(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1

my_list = [1, 5, 2, 8, 3]
print(find_item_linear(my_list, 8)) # Output: 3

# Summing all elements in a list
def sum_list(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Printing each element in a list
def print_elements(arr):
    for element in arr:
        print(element)
```

### Practical Example: Stacked vs. Nested Loops

It's important to distinguish between **stacked** loops (which remain linear) and **nested** loops (which become quadratic).

```python
# O(n) - Linear Time
def double_split(list):
    evens = []
    odds = []

    # Loop 1: O(n)
    for num in list:
        if num % 2 == 0:
            evens.append(num * 2)
    
    # Loop 2: O(n)
    for num in list:
        if num % 2 == 1:
            odds.append(num * 2)

    return (evens, odds)
    # Total: O(n) + O(n) = O(2n) -> O(n)

# O(n^2) - Quadratic Time
def find_pairs(list):
    # Nested Loop
    for i in list:          # O(n)
        for j in list:      # O(n) inside O(n)
            print(i, j)
    # Total: O(n) * O(n) = O(n^2)
```

### O(n log n) - Linearithmic Time

The execution time grows proportionally to `n * log n`. This is typically seen in efficient sorting algorithms.

```python
# Merge Sort (conceptual Python-like snippet)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merging two sorted halves takes O(n) time
    return merge(left_half, right_half)

def merge(left, right):
    # This function combines two sorted lists into one
    # Actual implementation is more complex, but its time complexity is O(n)
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Python's built-in sort (Timsort) is O(n log n)
my_unsorted_list = [34, 1, 56, 2, 89, 12]
sorted_list = sorted(my_unsorted_list)
print(sorted_list) # Output: [1, 2, 12, 34, 56, 89]
```

### O(n²) - Quadratic Time

The execution time grows proportionally to the square of the input size. This often occurs when iterating through a data structure with nested loops.

```python
# Nested loops (e.g., Bubble Sort, selection sort, checking all pairs)
def print_all_pairs(arr):
    for i in arr:           # Outer loop: O(n)
        for j in arr:       # Inner loop: O(n)
            print(f"{i}, {j}")
# Total complexity: O(n * n) = O(n²)

my_items = ["A", "B", "C"]
# print_all_pairs(my_items)
# Output:
# A, A
# A, B
# A, C
# B, A
# B, B
# B, C
# C, A
# C, B
# C, C

# Simple (naive) check for duplicates
def has_duplicates_naive(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

numbers_with_duplicates = [1, 2, 3, 4, 2]
print(has_duplicates_naive(numbers_with_duplicates)) # Output: True

# A more efficient way to check for duplicates is O(n) using a set:
def has_duplicates_better(arr):
    seen = set()
    for num in arr:
        if num in seen: # Set lookup is O(1)
            return True
        seen.add(num)
    return False
print(has_duplicates_better(numbers_with_duplicates)) # Output: True
```

### O(2ⁿ) - Exponential Time

The execution time doubles for every additional element in the input. These algorithms are typically very inefficient and become unusable for even moderately sized inputs.

```python
# Naive Recursive Fibonacci
def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

# fibonacci_naive(1) = 1
# fibonacci_naive(2) = 1
# fibonacci_naive(3) = 2
# fibonacci_naive(4) = 3
# fibonacci_naive(5) = 5
# fibonacci_naive(30) takes millions of operations.

# This repeated calculation can be optimized using memoization (dynamic programming) to O(n)
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

# Generating all subsets of a set (power set) is also O(2^n)
```

### O(n!) - Factorial Time

The execution time grows proportionally to the factorial of the input size. These algorithms are extremely slow and are only practical for very small inputs (n < 10-15).

```python
# Generating all permutations of a list (conceptual example)
def get_permutations(arr):
    if len(arr) == 0:
        return [[]]
    if len(arr) == 1:
        return [arr]

    permutations = []
    for i in range(len(arr)):
        m = arr[i]
        rem_list = arr[:i] + arr[i+1:]
        for p in get_permutations(rem_list):
            permutations.append([m] + p)
    return permutations

# print(get_permutations([1, 2, 3]))
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] (3! = 6 permutations)

# This complexity is often encountered in brute-force solutions for problems like the Traveling Salesman.
```

---

## 4. Analyzing Algorithm Complexity

### Drop Constants
Constant factors are ignored in Big O Notation because as `n` grows very large, their impact becomes negligible.

```python
# O(2n) -> O(n)
def print_list_twice(arr):
    for item in arr: # O(n)
        print(item)
    for item in arr: # O(n)
        print(item)
# Total time is 2n, but Big O is O(n)
```

### Keep Dominant Terms
Only the term with the highest growth rate is kept. Lower-order terms and constants are dropped.

```python
# O(n^2 + n) -> O(n^2)
def nested_loop_and_single_loop(arr):
    for i in arr:      # O(n)
        for j in arr:  # O(n)
            print(i, j)
    for item in arr:   # O(n)
        print(item)
# The O(n^2) term dominates the O(n) term as n grows large.
```

### Different Inputs
When an algorithm depends on multiple independent input sizes, each should be represented by a different variable.

```python
# O(a + b) (Not O(n))
def process_two_arrays(arr_a, arr_b):
    for item in arr_a: # O(a)
        print(item)
    for item in arr_b: # O(b)
        print(item)
# Total complexity depends on sizes of arr_a and arr_b independently.

# O(a * b) (Not O(n^2))
def nested_two_arrays(arr_a, arr_b):
    for a in arr_a:    # O(a)
        for b in arr_b: # O(b)
            print(a, b)
# Total complexity depends on the product of their sizes.
```

### Best, Average, and Worst Case
Big O usually refers to the worst-case scenario unless specified.
*   **Best Case**: Minimum time an algorithm can take (e.g., finding item at first position in linear search).
*   **Average Case**: Expected time behavior with typical input.
*   **Worst Case**: Maximum time an algorithm can take (e.g., finding item at last position or not at all in linear search).

For example, Quick Sort has an average time complexity of O(n log n), but a worst-case time complexity of O(n²).

---

## 5. Space Complexity

Space complexity describes the amount of memory an algorithm needs to run as a function of the input size `n`.

### O(1) Space - Constant Space
The memory usage does not change with the input size.

```python
def sum_array_space_o1(arr):
    total = 0 # Only one variable, regardless of arr size
    for num in arr:
        total += num
    return total
# Space complexity: O(1)
```

### O(n) Space - Linear Space
The memory usage grows linearly with the input size.

```python
def copy_array_space_on(arr):
    new_arr = [] # Creates a new list that grows with 'arr'
    for item in arr:
        new_arr.append(item)
    return new_arr
# Space complexity: O(n)

# Recursive functions can also consume O(n) space on the call stack
def factorial_recursive_space_on(n):
    if n == 0:
        return 1
    return n * factorial_recursive_space_on(n - 1)
# Space complexity: O(n) due to n function calls on the call stack
```

### Time vs. Space Trade-offs
Often, you can reduce time complexity by using more space, and vice-versa.

```python
# Example: Fibonacci (Time-optimized with O(n) Space)
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]
# Time: O(n), Space: O(n) (for memoization dictionary)

# Example: Fibonacci (Space-optimized with O(1) Space)
def fibonacci_iterative_space_o1(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
# Time: O(n), Space: O(1)
```

---

## 6. Data Structure Operation Complexities

Understanding the Big O of basic operations on common data structures is crucial for writing efficient algorithms.

### Python Lists (Dynamic Arrays)

| Operation        | Average Case | Worst Case   | Notes                                           |
| :--------------- | :----------- | :----------- | :---------------------------------------------- |
| Access (by index)| O(1)         | O(1)         |                                                 |
| Search (by value)| O(n)         | O(n)         | Needs to scan the list                          |
| Append           | O(1)         | O(1)         | List has pre-allocated space, amortized O(1)    |
| Insert (at beginning/middle) | O(n)         | O(n)         | Requires shifting elements                      |
| Delete (from beginning/middle)| O(n)         | O(n)         | Requires shifting elements                      |
| Pop (from end)   | O(1)         | O(1)         |                                                 |
| Sort (`.sort()`) | O(n log n)   | O(n log n)   | Timsort algorithm                               |

### Python Dictionaries & Sets (Hash Tables)

| Operation        | Average Case | Worst Case   | Notes                                           |
| :--------------- | :----------- | :----------- | :---------------------------------------------- |
| Access (by key)  | O(1)         | O(n)         | Hash collisions can lead to O(n) in worst case  |
| Insert/Add       | O(1)         | O(n)         | Hash collisions can lead to O(n) in worst case  |
| Delete           | O(1)         | O(n)         | Hash collisions can lead to O(n) in worst case  |
| Search (by key/value)| O(1)         | O(n)         | Hash collisions can lead to O(n) in worst case  |
| Iteration        | O(n)         | O(n)         | Needs to visit all elements                     |

### Linked Lists

| Operation        | Average Case | Worst Case   | Notes                                           |
| :--------------- | :----------- | :----------- | :---------------------------------------------- |
| Access (by index)| O(n)         | O(n)         | Requires traversing from head                   |
| Search (by value)| O(n)         | O(n)         | Requires traversing from head                   |
| Insert (at head) | O(1)         | O(1)         | Simple pointer re-assignment                    |
| Insert (at tail) | O(1) (with tail pointer) | O(1) (with tail pointer) | If no tail pointer, O(n)          |
| Insert (at middle)| O(n)         | O(n)         | Requires traversing to position                 |
| Delete (from head)| O(1)         | O(1)         | Simple pointer re-assignment                    |
| Delete (from middle/tail)| O(n)         | O(n)         | Requires traversing to previous node            |

---

## 7. Best Practices for Optimization

### Choose the Right Data Structure
The choice of data structure significantly impacts algorithm performance. Always consider the complexity of the operations you'll perform most frequently.

```python
# Bad: O(n) lookup for users
users_list = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
def find_user_by_id_list(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# Good: O(1) average lookup for users using a dictionary
users_dict = {user["id"]: user for user in users_list} # O(n) to build
def find_user_by_id_dict(users_map, user_id):
    return users_map.get(user_id)
```

### Avoid Unnecessary Nested Loops
Nested loops often lead to quadratic (O(n²)) or higher complexities. Look for ways to flatten loops or use more efficient data structures.

```python
# Bad: O(n^2) for finding common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = []
for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            common_elements.append(item1)
# print(common_elements)

# Good: O(n + m) using sets
set1 = set(list1) # O(n)
common_elements_better = []
for item in list2: # O(m)
    if item in set1: # O(1) average
        common_elements_better.append(item)
# print(common_elements_better)
```

### Utilize Built-in Functions and Libraries
Python's built-in functions and standard library are often implemented in C and highly optimized. Use them whenever possible.

```python
# Bad: Manual sum
def manual_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

# Good: Built-in sum (more efficient)
numbers = [1, 2, 3, 4, 5]
efficient_sum = sum(numbers)
```

### Memoization / Caching
For recursive algorithms with overlapping subproblems (like Fibonacci), memoization (caching results) can drastically reduce time complexity.

```python
# From O(2^n) to O(n)
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]
```

---

## See Also

-   **[Python Basics Cheat Sheet](../cheatsheets/Python_Basics_Cheat_Sheet.md)** - For foundational Python concepts used in algorithms.
-   **[Data Structures Cheat Sheet](../cheatsheets/Data_Structures_Cheat_Sheet.md)** - Detailed information on various data structures and their properties.
-   **[Algorithms Guide](../guides/Algorithms_Guide.md)** - (If created) for deeper dives into specific algorithms and their implementations.
-   **[Testing and Debugging Cheat Sheet](../cheatsheets/Testing_and_Debugging_Cheat_Sheet.md)** - Tools and techniques for profiling and measuring code performance.