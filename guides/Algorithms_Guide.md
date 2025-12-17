# Algorithms and Advanced Data Structures Guide

This guide covers fundamental algorithms and advanced data structures essential for efficient problem-solving. It builds upon basic data structures to explore recursion, searching, sorting, trees, and graphs.

## Table of Contents
1. [Recursion](#recursion)
2. [Searching Algorithms](#searching-algorithms)
3. [Sorting Algorithms](#sorting-algorithms)
4. [Trees & Binary Search Trees](#trees--binary-search-trees)
5. [Graph Algorithms](#graph-algorithms)

---

## Recursion

Recursion is a technique where a function calls itself to solve a problem by breaking it down into smaller, self-similar sub-problems.

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

### Bubble Sort (Conceptual)
Repeatedly steps through the list, swaps adjacent elements if they are in the wrong order.
*   **Time Complexity:** O(n^2) - **Inefficient** for large datasets.

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
