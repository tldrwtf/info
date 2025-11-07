# Big O Notation & Time Complexity - Complete Reference Guide

## Table of Contents
- [What is Big O?](#what-is-big-o)
- [Common Time Complexities](#common-time-complexities)
- [Analyzing Algorithms](#analyzing-algorithms)
- [Space Complexity](#space-complexity)
- [Data Structure Complexities](#data-structure-complexities)
- [Sorting Algorithms](#sorting-algorithms)
- [Best Practices](#best-practices)

---

## What is Big O?

### Definition
```python
# Big O Notation - Describes how algorithm performance scales
# with input size (n)

# Focuses on:
# - Worst-case scenario (usually)
# - Growth rate as n → infinity
# - Ignores constants and lower-order terms

# Example:
# O(2n + 5) → O(n)  # Drop constant 5, coefficient 2
# O(n² + n) → O(n²) # Keep highest order term
```

### Why Big O Matters
```python
# Compare algorithms for large datasets

# Algorithm A: O(n)     - Linear
# Algorithm B: O(n²)    - Quadratic

# For n = 100:
# A: 100 operations
# B: 10,000 operations   # 100x slower!

# For n = 1,000:
# A: 1,000 operations
# B: 1,000,000 operations  # 1000x slower!
```

---

## Common Time Complexities

### O(1) - Constant Time
```python
# Time doesn't change with input size
# Best possible complexity

# Examples:

# Array/List access by index
def get_first(arr):
    return arr[0]  # O(1) - always one operation

# Dictionary/Hash table lookup
def get_value(dictionary, key):
    return dictionary[key]  # O(1) - constant time lookup

# Simple arithmetic
def add(a, b):
    return a + b  # O(1)

# Setting/getting a variable
x = 5        # O(1)
y = arr[-1]  # O(1)

# Multiple O(1) operations is still O(1)
def multiple_operations(arr):
    first = arr[0]     # O(1)
    last = arr[-1]     # O(1)
    total = first + last  # O(1)
    return total       # O(1)
# Total: O(1)
```

### O(log n) - Logarithmic Time
```python
# Divides problem in half each iteration
# Very efficient for large datasets

# Example: Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# For array of 1,000,000 items:
# Max iterations: log₂(1,000,000) ≈ 20
# Much better than checking all 1,000,000!

# Other O(log n) examples:
# - Finding item in balanced binary search tree
# - Some divide-and-conquer algorithms
```

### O(n) - Linear Time
```python
# Time grows linearly with input size
# Most common complexity

# Examples:

# Loop through array once
def find_max(arr):
    max_val = arr[0]
    for num in arr:  # O(n) - touch each element once
        if num > max_val:
            max_val = num
    return max_val

# Sum all elements
def sum_array(arr):
    total = 0
    for num in arr:  # O(n)
        total += num
    return total

# Count occurrences
def count_occurrences(arr, target):
    count = 0
    for num in arr:  # O(n)
        if num == target:
            count += 1
    return count

# Linear search
def linear_search(arr, target):
    for i, num in enumerate(arr):  # O(n)
        if num == target:
            return i
    return -1
```

### O(n log n) - Linearithmic Time
```python
# Common in efficient sorting algorithms
# Better than O(n²) but worse than O(n)

# Examples:

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide: O(log n) levels
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge: O(n) work at each level
    return merge(left, right)

# Quick Sort (average case)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]    # O(n)
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Python's built-in sort
sorted_arr = sorted(arr)  # O(n log n) - Timsort
arr.sort()               # O(n log n) - in-place
```

### O(n²) - Quadratic Time
```python
# Nested loops over same data
# Becomes slow quickly with large n

# Examples:

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):           # O(n)
        for j in range(n - 1):    # O(n)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
# Total: O(n²)

# Check for duplicates (naive)
def has_duplicates(arr):
    for i in range(len(arr)):      # O(n)
        for j in range(i + 1, len(arr)):  # O(n)
            if arr[i] == arr[j]:
                return True
    return False
# Total: O(n²)

# Better approach: O(n)
def has_duplicates_better(arr):
    seen = set()
    for num in arr:  # O(n)
        if num in seen:  # O(1)
            return True
        seen.add(num)  # O(1)
    return False

# Print all pairs
def print_pairs(arr):
    for i in arr:     # O(n)
        for j in arr:  # O(n)
            print(i, j)
# Total: O(n²)
```

### O(2ⁿ) - Exponential Time
```python
# Doubles with each additional input
# Very slow - avoid if possible!

# Example: Recursive Fibonacci (naive)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# For fibonacci(5):
#           fib(5)
#          /      \
#      fib(4)    fib(3)
#      /   \      /   \
#   fib(3) fib(2) ...
#   ...

# Each call branches into 2 calls
# fibonacci(30) ≈ 2,000,000,000 calls!

# Better approach with memoization: O(n)
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Other O(2ⁿ) examples:
# - Naive recursive solutions
# - Generating all subsets of a set
# - Some brute-force algorithms
```

### O(n!) - Factorial Time
```python
# Extremely slow - only viable for tiny inputs
# Each element multiplies the work

# Example: Generate all permutations
def permutations(arr):
    if len(arr) <= 1:
        return [arr]

    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for p in permutations(rest):
            result.append([arr[i]] + p)

    return result

# For n elements: n! permutations
# n = 5:  120 permutations
# n = 10: 3,628,800 permutations
# n = 15: 1,307,674,368,000 permutations

# Use cases:
# - Traveling Salesman Problem (brute force)
# - Generating all permutations
# - Some cryptographic problems
```

---

## Analyzing Algorithms

### Drop Constants
```python
# Big O ignores constant factors

# O(2n) → O(n)
def print_twice(arr):
    for item in arr:  # O(n)
        print(item)
    for item in arr:  # O(n)
        print(item)
# Total: O(2n) → O(n)

# O(n + 100) → O(n)
def function(arr):
    # 100 operations: O(1)
    for i in range(100):
        print(i)

    # n operations: O(n)
    for item in arr:
        print(item)
# Total: O(n + 100) → O(n)
```

### Keep Dominant Terms
```python
# Keep only the fastest-growing term

# O(n² + n) → O(n²)
def nested_with_single(arr):
    for i in arr:       # O(n)
        for j in arr:    # O(n)
            print(i, j)
    for item in arr:    # O(n)
        print(item)
# Total: O(n² + n) → O(n²)

# O(n log n + n) → O(n log n)
# O(2ⁿ + n²) → O(2ⁿ)
```

### Different Inputs
```python
# Be careful with multiple inputs!

# O(a + b) - NOT O(n)
def process_two_arrays(arr_a, arr_b):
    for item in arr_a:  # O(a)
        print(item)
    for item in arr_b:  # O(b)
        print(item)
# Total: O(a + b)

# O(a * b) - NOT O(n²)
def nested_two_arrays(arr_a, arr_b):
    for a in arr_a:     # O(a)
        for b in arr_b:  # O(b)
            print(a, b)
# Total: O(a * b)
```

### Best, Average, Worst Case
```python
# Quick Sort example:

def quick_sort(arr):
    # Best case: O(n log n)
    # - Pivot always divides array evenly

    # Average case: O(n log n)
    # - Random pivot selection

    # Worst case: O(n²)
    # - Pivot is always smallest/largest
    # - Already sorted array with poor pivot choice
    pass

# When discussing Big O, usually means worst case
# unless specified otherwise
```

---

## Space Complexity

### What is Space Complexity?
```python
# Memory usage as function of input size

# O(1) Space - Constant
def sum_array(arr):
    total = 0  # Single variable
    for num in arr:
        total += num
    return total
# Space: O(1) - only 'total' variable

# O(n) Space - Linear
def copy_array(arr):
    new_arr = []
    for item in arr:
        new_arr.append(item)  # Creating new array
    return new_arr
# Space: O(n) - new array of size n

# O(n) Space - Recursive
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
# Space: O(n) - n recursive calls on call stack
```

### Time vs Space Tradeoffs
```python
# Fibonacci: Time-optimized with space
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
# Time: O(n), Space: O(n) - store results

# Fibonacci: Space-optimized
def fibonacci_iterative(n):
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
# Time: O(n), Space: O(1) - only 2 variables
```

---

## Data Structure Complexities

### Arrays/Lists
```python
# Access
arr[5]              # O(1) - direct index access

# Search
5 in arr            # O(n) - must check each element
arr.index(5)        # O(n) - linear search

# Insert/Delete
arr.append(5)       # O(1) - add to end
arr.insert(0, 5)    # O(n) - shift all elements
arr.pop()           # O(1) - remove from end
arr.pop(0)          # O(n) - shift all elements
del arr[0]          # O(n) - shift all elements

# Other operations
arr.sort()          # O(n log n) - Timsort
arr.reverse()       # O(n) - reverse in place
```

### Dictionaries/Hash Tables
```python
# All operations assume good hash function

# Access
d[key]              # O(1) average
d.get(key)          # O(1) average

# Insert/Update
d[key] = value      # O(1) average

# Delete
del d[key]          # O(1) average
d.pop(key)          # O(1) average

# Search
key in d            # O(1) average - hash lookup

# Iteration
for k in d:         # O(n) - iterate all keys
for v in d.values(): # O(n) - iterate all values
```

### Sets
```python
# Add/Remove
s.add(5)            # O(1) average
s.remove(5)         # O(1) average

# Search
5 in s              # O(1) average - hash lookup

# Set operations
s1 | s2             # O(len(s1) + len(s2)) - union
s1 & s2             # O(min(len(s1), len(s2))) - intersection
s1 - s2             # O(len(s1)) - difference
```

### Linked Lists
```python
# Access
# list[5]           # O(n) - must traverse

# Search
# 5 in list         # O(n) - must check each node

# Insert/Delete
# list.prepend(5)   # O(1) - add to head
# list.append(5)    # O(1) - add to tail (if have tail pointer)
# list.insert_at(i) # O(n) - must traverse to position
# list.delete_head()# O(1) - remove head
# list.delete(5)    # O(n) - must find node
```

---

## Sorting Algorithms

### Comparison of Sort Algorithms
```python
# Bubble Sort
# Time: O(n²), Space: O(1)
# Simple but slow

# Selection Sort
# Time: O(n²), Space: O(1)
# Simple but slow

# Insertion Sort
# Time: O(n²), Space: O(1)
# Good for small or nearly sorted arrays

# Merge Sort
# Time: O(n log n), Space: O(n)
# Consistent performance, uses extra space

# Quick Sort
# Time: O(n log n) average, O(n²) worst, Space: O(log n)
# Fast average case, in-place

# Heap Sort
# Time: O(n log n), Space: O(1)
# Consistent, in-place

# Python's sort() / sorted()
# Time: O(n log n), Space: O(n)
# Timsort - hybrid of merge and insertion sort
# Best choice in most cases
```

---

## Best Practices

### Optimization Tips
```python
# 1. Use appropriate data structures
# Bad: O(n) lookup
def find_user(users_list, user_id):
    for user in users_list:
        if user['id'] == user_id:
            return user
    return None

# Good: O(1) lookup
users_dict = {user['id']: user for user in users_list}
def find_user(users_dict, user_id):
    return users_dict.get(user_id)


# 2. Avoid nested loops when possible
# Bad: O(n²)
def find_common(list1, list2):
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                common.append(item1)
    return common

# Good: O(n + m)
def find_common_better(list1, list2):
    set1 = set(list1)  # O(n)
    common = []
    for item in list2:  # O(m)
        if item in set1:  # O(1)
            common.append(item)
    return common


# 3. Use built-ins (they're optimized)
# Slower
result = []
for x in arr:
    if x > 0:
        result.append(x * 2)

# Faster (comprehension uses optimized C code)
result = [x * 2 for x in arr if x > 0]


# 4. Cache expensive computations
# Bad: Recalculate every time
def expensive_function(n):
    # Some expensive operation
    return sum(range(n))

for i in range(1000):
    result = expensive_function(100)

# Good: Cache the result
cached_result = expensive_function(100)
for i in range(1000):
    result = cached_result
```

### Common Patterns
```python
# Two Pointers: O(n)
def remove_duplicates_sorted(arr):
    if not arr:
        return 0

    write = 1
    for read in range(1, len(arr)):
        if arr[read] != arr[read - 1]:
            arr[write] = arr[read]
            write += 1
    return write

# Sliding Window: O(n)
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Hash Map for O(1) lookup
def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
```

---

## Complexity Cheat Sheet

### Time Complexity Ranking
```
Excellent:  O(1)      Constant
Good:       O(log n)  Logarithmic
Fair:       O(n)      Linear
OK:         O(n log n) Linearithmic
Bad:        O(n²)     Quadratic
Horrible:   O(2ⁿ)     Exponential
Avoid:      O(n!)     Factorial
```

### Quick Reference Table
| Big O | Name | Example |
|-------|------|---------|
| O(1) | Constant | Array access, hash lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Loop through array |
| O(n log n) | Linearithmic | Efficient sorting |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Recursive fibonacci |
| O(n!) | Factorial | Permutations |

### Growth Comparison
```
n = 10:
O(1):      1
O(log n):  3
O(n):      10
O(n log n): 30
O(n²):     100
O(2ⁿ):     1,024
O(n!):     3,628,800

n = 100:
O(1):      1
O(log n):  7
O(n):      100
O(n log n): 700
O(n²):     10,000
O(2ⁿ):     1.27 × 10³⁰
O(n!):     9.33 × 10¹⁵⁷
```

---

## Common Interview Questions

### Recognize These Patterns
```python
# Single loop → O(n)
for i in arr:
    print(i)

# Nested loops (same array) → O(n²)
for i in arr:
    for j in arr:
        print(i, j)

# Dividing in half → O(log n)
while n > 1:
    n = n // 2

# Divide and conquer → O(n log n)
# merge_sort, quick_sort

# Recursive with multiple calls → O(2ⁿ)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```

---
