# Algorithms and Advanced Data Structures Guide

This guide covers fundamental algorithms and advanced data structures essential for efficient problem-solving. It builds upon basic data structures to explore recursion, searching, sorting, trees, and graphs.

## Table of Contents
1. [Recursion](#recursion)
2. [Searching Algorithms](#searching-algorithms)
3. [Sorting Algorithms](#sorting-algorithms)
4. [Trees & Binary Search Trees](#trees--binary-search-trees)
5. [Graph Algorithms](#graph-algorithms)

## 1. Core Concepts

### 1.1. In-Place vs. Out-of-Place Algorithms

Understanding how algorithms handle memory is crucial for optimization.

*   **In-Place:** Modifies the original data structure directly in memory. It uses less memory because no copy is created.
    *   *Example:* Python's `list.sort()` method.
*   **Out-of-Place:** Creates a copy of the original data, modifies the copy, and returns it. The original data remains unchanged.
    *   *Example:* Python's built-in `sorted(list)` function.

```python
nums = [3, 1, 4, 2]

# Out-of-Place (Original nums remains [3, 1, 4, 2])
new_nums = sorted(nums) 

# In-Place (Original nums becomes [1, 2, 3, 4])
nums.sort() 
```

### 1.2. Recursion

Recursion is a technique where a function calls itself...
### Core Concepts
*   **Base Case:** The condition that stops the recursion. Without it, you risk infinite loops and Stack Overflow errors.
*   **Recursive Step:** The part where the function calls itself with a modified parameter, moving towards the base case.

### Factorial Example
Calculates `n! = n * (n-1) * ... * 1`.

```python
def factorial(n):
    # Base Case: 1! = 1
    if n == 1:
        return 1
    # Recursive Step
    else:
        return n * factorial(n - 1)

print(factorial(5)) # Output: 120
```

### Fibonacci Sequence
Calculates the nth number in the sequence 0, 1, 1, 2, 3, 5...

```python
def fibonacci(n):
    # Base Cases
    if n in {0, 1}:
        return n
    # Recursive Step: Sum of previous two
    return fibonacci(n - 1) + fibonacci(n - 2)

# Generate first 10 numbers
sequence = [fibonacci(n) for n in range(10)]
print(sequence)
```

**Pros & Cons:**
*   **Pros:** Elegant, readable code for complex problems (like tree traversal).
*   **Cons:** Can be memory-intensive due to stack usage; risk of recursion depth errors.

---

## Searching Algorithms

### Linear Search
Checks every element until the target is found.
*   **Time Complexity:** O(n)
*   **Use Case:** Unsorted lists.

```python
def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i # Found at index i
    return -1 # Not found
```

### Binary Search
Efficiently finds a target in a **sorted** list by repeatedly dividing the search interval in half.
*   **Time Complexity:** O(log n)
*   **Use Case:** Sorted lists.

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
```

---

## Sorting Algorithms

### Built-in Sort
Python's `.sort()` and `sorted()` use Timsort (a hybrid of Merge Sort and Insertion Sort).
*   **Time Complexity:** O(n log n)

```python
nums = [5, 2, 9, 1, 5, 6]
nums.sort() # Modifies in-place
print(nums) # [1, 2, 5, 5, 6, 9]
```

### Bubble Sort
Repeatedly steps through the list, swaps adjacent elements if they are in the wrong order. With each pass, the next largest element "bubbles up" to its correct position.
*   **Time Complexity:** O(n^2) - **Inefficient** for large datasets.

```python
def bubble_sort(alist):
    n = len(alist)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist
```

### Merge Sort
A "Divide and Conquer" algorithm that recursively splits the list into halves, sorts them, and merges them back together.
*   **Time Complexity:** O(n log n) - **Very Efficient**.

```python
def merge_sort(list_to_sort):
    if len(list_to_sort) > 1:
        mid = len(list_to_sort) // 2
        left_half = list_to_sort[:mid]
        right_half = list_to_sort[mid:]

        # Recursive calls
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge process
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list_to_sort[k] = left_half[i]
                i += 1
            else:
                list_to_sort[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements
        while i < len(left_half):
            list_to_sort[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            list_to_sort[k] = right_half[j]
            j += 1
            k += 1
```

---

## Trees & Binary Search Trees

A **Binary Search Tree (BST)** is a hierarchical structure where each node has at most two children.
*   **Left Child:** Value < Parent
*   **Right Child:** Value > Parent

### BST Implementation

```python
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
```

### Tree Traversal
*   **In-Order:** Left -> Root -> Right (Returns sorted values in BST)
*   **Pre-Order:** Root -> Left -> Right
*   **Post-Order:** Left -> Right -> Root

---

## Graph Algorithms

Graphs consist of **Vertices** (nodes) connected by **Edges**. They model relationships like maps, social networks, and internet links.

### Adjacency List
A common way to represent graphs where each vertex stores a list of its neighbors.

```python
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
```

### Dijkstra's Algorithm (Shortest Path)
Finds the shortest path from a start node to all other nodes in a weighted graph.

```python
import heapq

def dijkstra(graph, start):
    # Track shortest distance to each node (initially infinity)
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    # Priority queue to store (distance, vertex)
    pq = [(0, start)]
    
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)

        # If we found a shorter path already, skip
        if current_dist > distances[current_vertex]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_dist + weight

            # If shorter path found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# Example Usage
distances = dijkstra(graph, 'A')
print(distances) # {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```
