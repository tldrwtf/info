# Linked Lists and Custom Data Structures Guide

[Back to Main](./README.md)

---

## Table of Contents

1. [Introduction to Linked Lists](#introduction-to-linked-lists)
2. [Node Implementation](#node-implementation)
3. [LinkedList Class](#linkedlist-class)
4. [LinkedList Operations](#linkedlist-operations)
5. [Stack Implementation (LIFO)](#stack-implementation-lifo)
6. [Queue Implementation (FIFO)](#queue-implementation-fifo)
7. [Time Complexity Analysis](#time-complexity-analysis)
8. [Practical Applications](#practical-applications)
9. [Optimization Techniques](#optimization-techniques)
10. [Python Built-in Alternatives](#python-built-in-alternatives)
11. [When to Use Each Structure](#when-to-use-each-structure)

---

## Introduction to Linked Lists

A **linked list** is a linear data structure where elements are stored in nodes. Each node contains data and a reference (pointer) to the next node in the sequence.

### Linked List vs Array (Python List)

| Feature | Linked List | Python List |
|---------|-------------|-------------|
| Access by index | O(n) | O(1) |
| Insert at beginning | O(1) | O(n) |
| Insert at end | O(1) with tail / O(n) without | O(1) amortized |
| Insert in middle | O(n) | O(n) |
| Delete at beginning | O(1) | O(n) |
| Memory | Extra pointer per element | Contiguous block |

### Visual Representation

```
    Head                                Tail
     |                                   |
     v                                   v
[Data|Next] -> [Data|Next] -> [Data|Next] -> None
```

---

## Node Implementation

A node is the building block of a linked list, containing data and a reference to the next node.

### Basic Node Class

```python
class Node:
    def __init__(self, data):
        """
        Initialize a node.

        Args:
            data: The value to store in the node
        """
        self.data = data  # The cargo/value of the node
        self.next = None  # Pointer to the next node (initially None)
```

### Using Nodes

```python
# Create individual nodes
blue = Node("blue")
red = Node("red")
purple = Node("purple")

# Link nodes together
blue.next = red
red.next = purple

# Traverse manually
print(blue.data)           # "blue"
print(blue.next.data)      # "red"
print(blue.next.next.data) # "purple"
```

### Manual Traversal

```python
# Traverse all nodes starting from head
current = blue
while current is not None:
    print(current.data)
    current = current.next

# Output:
# blue
# red
# purple
```

---

## LinkedList Class

A LinkedList class manages nodes and provides methods for common operations.

### Basic LinkedList Structure

```python
class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None  # First node in the list
        self.tail = None  # Last node in the list (for optimization)

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None
```

### Complete LinkedList Implementation

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
        """Check if list is empty."""
        return self.head is None

    def append(self, data):
        """Add a new node to the end of the list (O(1) with tail)."""
        new_node = Node(data)

        # If list is empty, new node becomes both head and tail
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        # Otherwise, add to end and update tail
        self.tail.next = new_node
        self.tail = new_node

    def traverse(self):
        """Print all elements in the list."""
        print("========== List Contents ==========")

        if self.is_empty():
            print("List is empty")
            return

        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def insert_at_position(self, position, data):
        """
        Insert a node at a specific position (1-indexed).

        Args:
            position: 1-based index where to insert
            data: Value for the new node
        """
        new_node = Node(data)

        # Case 1: Insert at beginning (position 1)
        if position == 1:
            new_node.next = self.head
            self.head = new_node

            # If list was empty, update tail too
            if self.tail is None:
                self.tail = new_node
            return

        # Case 2: Insert elsewhere
        current = self.head
        counter = 1

        # Move to the node just before the desired position
        while counter < position - 1 and current is not None:
            current = current.next
            counter += 1

        if current is None:
            print("Position out of bounds")
            return

        # Insert the new node
        new_node.next = current.next
        current.next = new_node

        # If inserted at end, update tail
        if new_node.next is None:
            self.tail = new_node

    def delete_at_position(self, position):
        """
        Delete a node at a specific position (1-indexed).

        Args:
            position: 1-based index of node to delete

        Returns:
            The deleted node, or None if position invalid
        """
        if self.is_empty():
            print("List is empty. Nothing to delete")
            return None

        # Case 1: Delete head (first node)
        if position == 1:
            deleted_node = self.head
            self.head = self.head.next

            # If list becomes empty, reset tail
            if self.head is None:
                self.tail = None

            return deleted_node

        # Case 2: Delete at other position
        current = self.head
        counter = 1

        # Move to node just before the one to delete
        while counter < position - 1 and current.next is not None:
            current = current.next
            counter += 1

        if current.next is None:
            print("Position out of bounds")
            return None

        # Save node to delete
        deleted_node = current.next

        # If deleting tail, update tail pointer
        if deleted_node == self.tail:
            self.tail = current

        # Remove node from chain
        current.next = deleted_node.next

        return deleted_node

    def get_at_position(self, position):
        """
        Get data at a specific position (1-indexed).

        Args:
            position: 1-based index

        Returns:
            Data at position, or None if out of bounds
        """
        counter = 1
        current = self.head

        while counter < position:
            if current is None or current.next is None:
                print("Position out of bounds")
                return None
            current = current.next
            counter += 1

        return current.data if current else None
```

---

## LinkedList Operations

### Append (Add to End)

**Without Tail Pointer (O(n)):**
```python
def append_without_tail(self, data):
    """Add to end - must traverse entire list."""
    new_node = Node(data)

    if self.is_empty():
        self.head = new_node
        return

    # Traverse to end (O(n))
    current = self.head
    while current.next:
        current = current.next

    current.next = new_node
```

**With Tail Pointer (O(1)):**
```python
def append_with_tail(self, data):
    """Add to end - direct access via tail."""
    new_node = Node(data)

    if self.is_empty():
        self.head = new_node
        self.tail = new_node
        return

    # Direct access to tail (O(1))
    self.tail.next = new_node
    self.tail = new_node
```

### Insert at Position

```python
# Usage examples
my_list = LinkedList()
my_list.append("A")
my_list.append("B")
my_list.append("D")

# Insert "C" at position 3 (between B and D)
my_list.insert_at_position(3, "C")

# Result: A -> B -> C -> D

# Insert at beginning
my_list.insert_at_position(1, "Start")

# Result: Start -> A -> B -> C -> D
```

### Delete at Position

```python
# Delete at position 3
deleted = my_list.delete_at_position(3)
print(f"Deleted: {deleted.data}")

# Delete first node
my_list.delete_at_position(1)

# Delete last node
my_list.delete_at_position(my_list.get_length())
```

### Traverse (Print All)

```python
my_list = LinkedList()
my_list.append("Apple")
my_list.append("Banana")
my_list.append("Cherry")

my_list.traverse()
# Output:
# ========== List Contents ==========
# Apple
# Banana
# Cherry
```

---

## Stack Implementation (LIFO)

A **stack** is a Last-In-First-Out (LIFO) data structure. The last element added is the first one removed.

### Stack Operations

- **push**: Add element to top
- **pop**: Remove and return top element
- **peek**: View top element without removing
- **is_empty**: Check if stack is empty

### Complete Stack Implementation

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
        """Check if stack is empty."""
        return self.head is None

    def push(self, item):
        """
        Add item to top of stack (O(1)).

        Args:
            item: Value to add
        """
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # Add to head (top of stack)
            new_node.next = self.head
            self.head = new_node

        self.size += 1
        print(f"Pushed {item} onto stack")

    def pop(self):
        """
        Remove and return top item (O(1)).

        Returns:
            The item from top of stack, or None if empty
        """
        if self.is_empty():
            print("Stack is empty!")
            return None

        # Remove from head
        item = self.head.data
        self.head = self.head.next

        # If stack becomes empty, reset tail
        if self.head is None:
            self.tail = None

        self.size -= 1
        return item

    def peek(self):
        """
        View top item without removing (O(1)).

        Returns:
            Top item, or None if empty
        """
        if self.is_empty():
            print("Stack is empty")
            return None

        return self.head.data

    def get_size(self):
        """Get number of items in stack."""
        return self.size
```

### Stack Usage Example

```python
# Create stack
stack = Stack()

# Push items
stack.push("First")
stack.push("Second")
stack.push("Third")

# View top
print(f"Top: {stack.peek()}")  # "Third"

# Pop items (LIFO order)
print(stack.pop())  # "Third"
print(stack.pop())  # "Second"
print(stack.pop())  # "First"
print(stack.pop())  # Stack is empty! (returns None)
```

### Real-World Stack Applications

```python
# Undo functionality
class TextEditor:
    def __init__(self):
        self.undo_stack = Stack()
        self.current_text = ""

    def type_text(self, text):
        """Add text and save state for undo."""
        self.undo_stack.push(self.current_text)
        self.current_text += text

    def undo(self):
        """Undo last change."""
        if not self.undo_stack.is_empty():
            self.current_text = self.undo_stack.pop()
        else:
            print("Nothing to undo")

# Usage
editor = TextEditor()
editor.type_text("Hello")
editor.type_text(" World")
print(editor.current_text)  # "Hello World"

editor.undo()
print(editor.current_text)  # "Hello"

editor.undo()
print(editor.current_text)  # ""
```

---

## Queue Implementation (FIFO)

A **queue** is a First-In-First-Out (FIFO) data structure. The first element added is the first one removed.

### Queue Operations

- **enqueue**: Add element to rear
- **dequeue**: Remove and return front element
- **front**: View front element without removing
- **rear**: View rear element without removing
- **is_empty**: Check if queue is empty

### Complete Queue Implementation

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None  # Front of queue
        self.tail = None  # Rear of queue
        self.size_count = 0

    def is_empty(self):
        """Check if queue is empty."""
        return self.head is None

    def enqueue(self, item):
        """
        Add item to rear of queue (O(1)).

        Args:
            item: Value to add
        """
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # Add to tail (rear of queue)
            self.tail.next = new_node
            self.tail = new_node

        self.size_count += 1
        print(f"Enqueued {item}")

    def dequeue(self):
        """
        Remove and return front item (O(1)).

        Returns:
            Item from front of queue

        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")

        # Remove from head (front)
        item = self.head.data
        self.head = self.head.next

        # If queue becomes empty, reset tail
        if self.head is None:
            self.tail = None

        self.size_count -= 1
        return item

    def front(self):
        """
        View front item without removing (O(1)).

        Returns:
            Front item, or None if empty
        """
        if self.is_empty():
            print("Queue is empty")
            return None

        return self.head.data

    def rear(self):
        """
        View rear item without removing (O(1)).

        Returns:
            Rear item, or None if empty
        """
        if self.is_empty():
            print("Queue is empty")
            return None

        return self.tail.data

    def get_size(self):
        """Get number of items in queue."""
        return self.size_count
```

### Queue Usage Example

```python
# Create queue
queue = Queue()

# Enqueue items
queue.enqueue("First")
queue.enqueue("Second")
queue.enqueue("Third")

# View front and rear
print(f"Front: {queue.front()}")  # "First"
print(f"Rear: {queue.rear()}")    # "Third"

# Dequeue items (FIFO order)
print(queue.dequeue())  # "First"
print(queue.dequeue())  # "Second"
print(queue.dequeue())  # "Third"
```

### Real-World Queue Applications

```python
# Print job queue
class PrintQueue:
    def __init__(self):
        self.queue = Queue()

    def add_print_job(self, document):
        """Add document to print queue."""
        self.queue.enqueue(document)
        print(f"Added '{document}' to print queue")

    def process_next_job(self):
        """Process next document in queue."""
        if not self.queue.is_empty():
            doc = self.queue.dequeue()
            print(f"Printing: {doc}")
        else:
            print("No documents to print")

    def view_next_job(self):
        """See what will print next."""
        next_doc = self.queue.front()
        if next_doc:
            print(f"Next: {next_doc}")

# Usage
printer = PrintQueue()
printer.add_print_job("Report.pdf")
printer.add_print_job("Invoice.pdf")
printer.add_print_job("Letter.pdf")

printer.view_next_job()      # "Next: Report.pdf"
printer.process_next_job()   # "Printing: Report.pdf"
printer.process_next_job()   # "Printing: Invoice.pdf"
```

---

## Time Complexity Analysis

### LinkedList Operations

| Operation | Time Complexity | Explanation |
|-----------|----------------|-------------|
| `append()` with tail | O(1) | Direct access to tail |
| `append()` without tail | O(n) | Must traverse to end |
| `insert_at_position()` | O(n) | Must traverse to position |
| `delete_at_position()` | O(n) | Must traverse to position |
| `get_at_position()` | O(n) | Must traverse to position |
| `traverse()` | O(n) | Visit each node once |
| `is_empty()` | O(1) | Check head pointer |

### Stack Operations

| Operation | Time Complexity | Explanation |
|-----------|----------------|-------------|
| `push()` | O(1) | Add to head |
| `pop()` | O(1) | Remove from head |
| `peek()` | O(1) | Read head data |
| `is_empty()` | O(1) | Check head pointer |

### Queue Operations

| Operation | Time Complexity | Explanation |
|-----------|----------------|-------------|
| `enqueue()` | O(1) | Add to tail |
| `dequeue()` | O(1) | Remove from head |
| `front()` | O(1) | Read head data |
| `rear()` | O(1) | Read tail data |
| `is_empty()` | O(1) | Check head pointer |

### Space Complexity

- **Linked List**: O(n) - Each node requires storage for data + pointer
- **Stack**: O(n) - Linear with number of elements
- **Queue**: O(n) - Linear with number of elements

---

## Practical Applications

### Music Playlist Manager

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
        self.current_position = 1

    def add_song(self, title, artist, duration):
        """Add song to playlist."""
        song = Song(title, artist, duration)
        self.songs.append(song)

    def display(self):
        """Show all songs in playlist."""
        print(f"========== {self.name} ==========")

        if self.songs.is_empty():
            print("Playlist is empty")
            return

        current = self.songs.head
        counter = 1

        while current is not None:
            song = current.data
            print(f"{counter}. {song.title} - {song.artist} ({song.duration}s)")
            current = current.next
            counter += 1

    def play_song_at_position(self, position):
        """Play song at specific position."""
        song = self.songs.get_at_position(position)
        if song:
            self.current_position = position
            print(f"Now playing: {song.title} by {song.artist}")
        else:
            print("Song not found")

    def next_song(self):
        """Play next song in playlist."""
        next_position = self.current_position + 1
        next_song = self.songs.get_at_position(next_position)

        if next_song:
            self.current_position = next_position
            print(f"Now playing: {next_song.title}")
        else:
            print("End of playlist")

    def previous_song(self):
        """Play previous song in playlist."""
        if self.current_position > 1:
            prev_position = self.current_position - 1
            prev_song = self.songs.get_at_position(prev_position)
            self.current_position = prev_position
            print(f"Now playing: {prev_song.title}")
        else:
            print("At beginning of playlist")

    def remove_current_song(self):
        """Remove currently playing song."""
        removing = self.songs.delete_at_position(self.current_position)
        if removing:
            print(f"Removed: {removing.data.title}")

# Usage
playlist = MusicPlaylist("My Favorites")
playlist.add_song("Thriller", "Michael Jackson", 358)
playlist.add_song("Dreams", "Fleetwood Mac", 257)
playlist.add_song("Bohemian Rhapsody", "Queen", 354)

playlist.display()
playlist.play_song_at_position(1)
playlist.next_song()
playlist.next_song()
playlist.previous_song()
```

### Browser History (Stack)

```python
class BrowserHistory:
    def __init__(self):
        self.history = Stack()
        self.current_page = None

    def visit(self, url):
        """Visit a new page."""
        if self.current_page:
            self.history.push(self.current_page)
        self.current_page = url
        print(f"Visiting: {url}")

    def back(self):
        """Go back to previous page."""
        if not self.history.is_empty():
            previous_page = self.history.pop()
            print(f"Going back to: {previous_page}")
            self.current_page = previous_page
        else:
            print("No history to go back to")

# Usage
browser = BrowserHistory()
browser.visit("google.com")
browser.visit("github.com")
browser.visit("stackoverflow.com")
browser.back()  # Returns to github.com
browser.back()  # Returns to google.com
```

### Task Queue (Queue)

```python
class TaskQueue:
    def __init__(self):
        self.queue = Queue()

    def add_task(self, task_name, priority="normal"):
        """Add task to queue."""
        task = {"name": task_name, "priority": priority}
        self.queue.enqueue(task)

    def process_next_task(self):
        """Process next task in queue."""
        if not self.queue.is_empty():
            task = self.queue.dequeue()
            print(f"Processing: {task['name']} (Priority: {task['priority']})")
            return task
        else:
            print("No tasks in queue")
            return None

    def view_next_task(self):
        """See next task without processing."""
        next_task = self.queue.front()
        if next_task:
            print(f"Next task: {next_task['name']}")

# Usage
tasks = TaskQueue()
tasks.add_task("Send emails", "high")
tasks.add_task("Update documentation", "normal")
tasks.add_task("Code review", "high")

tasks.view_next_task()
tasks.process_next_task()
tasks.process_next_task()
```

---

## Optimization Techniques

### 1. Tail Pointer Optimization

**Performance Impact:** O(n) → O(1) for append operations

```python
# Without tail - O(n)
def append_slow(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return

    current = self.head
    while current.next:  # Traverse entire list
        current = current.next
    current.next = new_node

# With tail - O(1)
def append_fast(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        self.tail = new_node
        return

    self.tail.next = new_node
    self.tail = new_node
```

### 2. Size Tracking

Track size as attribute instead of counting nodes.

```python
class OptimizedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # Track size

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1  # O(1) increment

    def get_length(self):
        return self.size  # O(1) instead of O(n)
```

### 3. Boundary Condition Handling

Always handle edge cases properly.

```python
def delete_at_position(self, position):
    # Check empty list
    if self.is_empty():
        return None

    # Handle deleting head
    if position == 1:
        deleted = self.head
        self.head = self.head.next
        if self.head is None:  # List became empty
            self.tail = None
        return deleted

    # Handle deleting tail
    current = self.head
    counter = 1
    while counter < position - 1 and current.next:
        current = current.next
        counter += 1

    if not current.next:
        return None

    deleted = current.next
    if deleted == self.tail:  # Update tail if necessary
        self.tail = current

    current.next = deleted.next
    return deleted
```

---

## Python Built-in Alternatives

### Stack using Python List

```python
# Python list as stack
stack = []

# Push (O(1))
stack.append("First")
stack.append("Second")
stack.append("Third")

# Pop (O(1))
top = stack.pop()  # "Third"

# Peek (O(1))
if stack:
    top = stack[-1]  # View without removing

# Check if empty
is_empty = len(stack) == 0
```

### Queue using collections.deque

```python
from collections import deque

# Create queue
queue = deque()

# Enqueue (O(1))
queue.append("First")
queue.append("Second")
queue.append("Third")

# Dequeue (O(1))
front = queue.popleft()  # "First"

# Front/rear
front = queue[0] if queue else None
rear = queue[-1] if queue else None

# Check if empty
is_empty = len(queue) == 0
```

**Why not use list for Queue?**
- `list.pop(0)` is O(n) - shifts all elements
- `deque.popleft()` is O(1) - optimized for both ends

---

## When to Use Each Structure

### Use Linked Lists When:

- Frequent insertions/deletions at beginning or middle
- Don't need random access by index
- Size changes frequently
- Memory overhead acceptable

**Examples:** Undo/redo, music playlists, browser history

### Use Stacks When:

- Need LIFO (Last-In-First-Out) behavior
- Tracking state for backtracking
- Reversing order

**Examples:**
- Function call stack
- Undo functionality
- Expression evaluation
- Browser back button
- Depth-first search

### Use Queues When:

- Need FIFO (First-In-First-Out) behavior
- Process items in order received
- Fair scheduling

**Examples:**
- Print job queues
- Task scheduling
- Breadth-first search
- Message queues
- Customer service tickets

### Use Python Lists When:

- Need fast random access (O(1))
- Mostly reading data
- Size relatively stable
- Indexing important

**Examples:** Storing data for analysis, lookup tables

### Comparison Table

| Use Case | Best Structure | Reason |
|----------|---------------|---------|
| Undo functionality | Stack | LIFO for recent changes |
| Print queue | Queue | FIFO for fair ordering |
| Music playlist | Linked List | Easy insert/delete of songs |
| Recent items | Stack | Access most recent first |
| Task scheduling | Queue | Process in order received |
| Array indexing | Python List | O(1) random access |
| Frequent beginning inserts | Linked List | O(1) vs O(n) for lists |

---

## Summary

### Key Concepts

1. **Linked Lists**: Sequential nodes with pointers
2. **Stacks**: LIFO structure (push/pop from same end)
3. **Queues**: FIFO structure (add rear, remove front)
4. **Time Complexity**: Know O(1) vs O(n) operations
5. **Optimization**: Use tail pointer for O(1) append

### Implementation Checklist

- [ ] Implement Node class with data and next pointer
- [ ] Create LinkedList with head and tail
- [ ] Add append method (O(1) with tail)
- [ ] Implement insert/delete at position
- [ ] Add traversal method
- [ ] Handle edge cases (empty list, single node)
- [ ] Track size for O(1) length queries
- [ ] Implement Stack with push/pop/peek
- [ ] Implement Queue with enqueue/dequeue
- [ ] Test all boundary conditions

### Related Resources

- [Data Structures](./Data_Structures_Cheat_Sheet.md) - Overview of built-in structures
- [Big O Notation](./Big_O_Notation_Cheat_Sheet.md) - Time complexity analysis
- [OOP](./OOP_Cheat_Sheet.md) - Object-oriented programming concepts
- [Standard Library Essentials](./Standard_Library_Essentials_Cheat_Sheet.md) - Using collections.deque

[Back to Main](./README.md)
