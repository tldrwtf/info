# Linked Lists and Custom Data Structures in Python

This guide covers the implementation of linear data structures in Python: **Linked Lists**, **Stacks**, and **Queues**. Unlike Python's built-in `list` (which is a dynamic array), these structures are built using `Node` objects linked together.

---

## 1. The Node Class

The building block of all these structures is the `Node`. It contains:
1.  **Data**: The value stored.
2.  **Next**: A pointer (reference) to the next node in the chain.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Initially points to nothing
```

---

## 2. Linked Lists

A Linked List is a chain of nodes. We track the **Head** (start) and often the **Tail** (end) for efficiency.

### Basic Implementation

```python
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        """Add to the end of the list (O(1) if we have tail)"""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        
        # Link current tail to new node
        self.tail.next = new_node
        # Update tail pointer
        self.tail = new_node

    def traverse(self):
        """Print all values"""
        current = self.head
        while current:
            print(current.data)
            current = current.next
```

### Advanced Operations

#### Insert at Position
```python
def insert_at_position(self, position, data):
    new_node = Node(data)
    
    # Case: Insert at head
    if position == 1:
        new_node.next = self.head
        self.head = new_node
        if self.tail is None: self.tail = new_node
        return

    # Traverse to position - 1
    current = self.head
    counter = 1
    while counter < position - 1 and current:
        current = current.next
        counter += 1
    
    if current:
        new_node.next = current.next
        current.next = new_node
```

#### Delete at Position
```python
def delete_at_position(self, position):
    if self.is_empty(): return
    
    # Case: Delete head
    if position == 1:
        self.head = self.head.next
        if self.head is None: self.tail = None
        return

    # Traverse to node before target
    current = self.head
    counter = 1
    while counter < position - 1 and current.next:
        current = current.next
        counter += 1
        
    # Unlink the node
    if current.next:
        if current.next == self.tail:
            self.tail = current
        current.next = current.next.next
```

---

## 3. Stacks (LIFO)

**Last In, First Out.** Think of a stack of plates.
*   **Push**: Add to top (Head).
*   **Pop**: Remove from top (Head).
*   **Peek**: Look at top.

```python
class Stack:
    def __init__(self):
        self.head = None # Top of stack
        self.size = 0

    def push(self, data):
        """Add to Top - O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        """Remove from Top - O(1)"""
        if not self.head: return None
        
        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return item
```

---

## 4. Queues (FIFO)

**First In, First Out.** Think of a line at a store.
*   **Enqueue**: Add to back (Tail).
*   **Dequeue**: Remove from front (Head).

```python
class Queue:
    def __init__(self):
        self.head = None # Front
        self.tail = None # Back
        self.size = 0

    def enqueue(self, data):
        """Add to Back - O(1)"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        """Remove from Front - O(1)"""
        if not self.head: return None
        
        item = self.head.data
        self.head = self.head.next
        if not self.head: self.tail = None
        
        self.size -= 1
        return item
```

---

## 5. Linked List vs Python List

| Feature | Python List (`[]`) | Linked List |
| :--- | :--- | :--- |
| **Underlying Structure** | Dynamic Array (Contiguous Memory) | Nodes (Scattered Memory) |
| **Access by Index** | O(1) - Instant | O(n) - Must traverse |
| **Insert/Delete at Start** | O(n) - Must shift all items | O(1) - Just change head pointer |
| **Insert/Delete at End** | O(1) (Usually) | O(1) (With tail pointer) |
| **Memory Usage** | Lower overhead | Higher (stores data + pointer) |

**When to use Linked Lists?**
*   When you need constant time `O(1)` insertions/deletions at the beginning of the list.
*   When implementing Stacks and Queues manually.
*   When memory fragmentation is a concern (rare in high-level Python).

---

## 6. Real-World Application: Music Playlist

A playlist is a classic Linked List.
*   **Next Song**: `current = current.next`
*   **Previous Song**: Requires a **Doubly Linked List** (nodes have `next` and `prev`).

```python
class MusicPlaylist:
    def __init__(self, name):
        self.songs = LinkedList()
        self.current_pos = 0

    def play_next(self):
        # Logic to move pointer forward
        pass
```

---

## See Also
- **[Data Structures Cheat Sheet](../cheatsheets/Data_Structures_Cheat_Sheet.md)**
- **[Big O Notation Cheat Sheet](../cheatsheets/Big_O_Notation_Cheat_Sheet.md)**