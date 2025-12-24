# ==========================================
# DATA STRUCTURES - PRACTICE SOLUTIONS
# ==========================================
"""
Python data structures exercises demonstrating lists, dictionaries, nested structures, and sets.

Core concepts covered:
- Function parameters and return values
- Lists: ordered, mutable collections
- Dictionaries: key-value pairs for fast lookup
- Nested data structures: dicts within dicts
- Sets: unordered collections of unique elements
- Set operations: intersection, union, difference

These are Python's most commonly used built-in data structures. Understanding
when to use each one is crucial for writing efficient, readable code.
"""

from typing import Dict, List, Optional, Set


# ==========================================
# TASK 3.1: Basic Functions
# ==========================================
def greet(name: str) -> None:
    """
    Print a greeting message for the given name.

    Args:
        name: The person's name to greet

    Returns:
        None: Prints directly to console

    Example:
        >>> greet("Alice")
        Hello Alice
    """
    print(f"Hello {name}")


def rectangle_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Area formula: length × width

    Args:
        length: The length of the rectangle (any numeric value)
        width: The width of the rectangle (any numeric value)

    Returns:
        The calculated area as a float

    Example:
        >>> rectangle_area(5, 3)
        15.0
        >>> rectangle_area(2.5, 4.0)
        10.0
    """
    return length * width


def add(num1: float, num2: float) -> float:
    """
    Add two numbers together.

    Args:
        num1: First number
        num2: Second number

    Returns:
        Sum of num1 and num2

    Example:
        >>> add(5, 3)
        8
        >>> add(2.5, 1.5)
        4.0
    """
    return num1 + num2


# ==========================================
# TASK 3.2: Converter
# ==========================================
def celcius_to_farenheit(c: float) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.

    Formula: F = (C × 9/5) + 32

    The formula works because:
    - Celsius scale: 0° (freezing) to 100° (boiling) = 100 degrees
    - Fahrenheit scale: 32° (freezing) to 212° (boiling) = 180 degrees
    - Ratio: 180/100 = 9/5

    Args:
        c: Temperature in Celsius

    Returns:
        Temperature converted to Fahrenheit

    Example:
        >>> celcius_to_farenheit(0)
        32.0
        >>> celcius_to_farenheit(100)
        212.0
        >>> celcius_to_farenheit(37)  # Human body temperature
        98.6
    """
    return (c * 9/5) + 32


# ==========================================
# TASK 3.3: List Statistics
# ==========================================
def list_statistics(numbers: List[float]) -> Optional[Dict[str, float]]:
    """
    Calculate statistical measures for a list of numbers.

    Demonstrates:
    - Guard clause pattern (early return for empty list)
    - Dictionary construction with multiple key-value pairs
    - Built-in aggregate functions (max, min, sum, len)
    - Dictionary as structured return value

    Args:
        numbers: List of numeric values to analyze

    Returns:
        Dictionary containing 'max', 'min', 'avg', and 'sum' keys,
        or None if the input list is empty

    Example:
        >>> list_statistics([10, 20, 30, 40])
        {'max': 40, 'min': 10, 'avg': 25.0, 'sum': 100}
        >>> list_statistics([])
        None

    Best Practice:
        Returning a dictionary allows the caller to access specific
        statistics by name (e.g., result['avg']) rather than relying
        on positional access of a tuple.
    """
    # Guard clause: Check if list is empty first
    # Using 'not' on an empty list evaluates to True
    if not numbers:
        return None

    # Return dictionary with computed statistics
    # Built-in functions make this concise and readable
    return {
        "max": max(numbers),      # Largest value
        "min": min(numbers),      # Smallest value
        "avg": sum(numbers) / len(numbers),  # Mean (average)
        "sum": sum(numbers)       # Total of all values
    }


# ==========================================
# TASK 4.1: Student Dictionary
# ==========================================
# Module-level dictionary demonstrating key-value pairs
# Key: student name (string), Value: score (integer)
students: Dict[str, int] = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}


def process_students() -> None:
    """
    Demonstrate three ways to iterate over dictionary data.

    Dictionary iteration methods:
    1. for key in dict: Iterates over keys only
    2. for value in dict.values(): Iterates over values only
    3. for key, value in dict.items(): Iterates over key-value pairs

    This function also demonstrates the .get() method for safe dictionary access,
    which returns a default value if the key doesn't exist (instead of raising KeyError).

    Returns:
        None: Prints dictionary contents in various formats

    Example Output:
        --- Names ---
        Alice
        Bob
        Charlie

        --- Scores ---
        85
        92
        78

        --- Pairs ---
        Alice: 85
        Bob: 92
        Charlie: 78

        --- Safe Check ---
        David's score: Not Found

    Best Practice:
        Use .get(key, default) instead of dict[key] when you're not sure
        if the key exists. This prevents KeyError exceptions.
    """
    # Method 1: Iterate over keys (default behavior)
    print("\n--- Names ---")
    for name in students:  # Same as: for name in students.keys()
        print(name)

    # Method 2: Iterate over values only
    print("\n--- Scores ---")
    for score in students.values():
        print(score)

    # Method 3: Iterate over key-value pairs (most common pattern)
    print("\n--- Pairs ---")
    for name, score in students.items():
        # Tuple unpacking: items() returns (key, value) tuples
        print(f"{name}: {score}")

    # Safe dictionary access with .get()
    print("\n--- Safe Check ---")
    # .get('David', 'Not Found') returns 'Not Found' if 'David' key doesn't exist
    # This is safer than students['David'] which would raise KeyError
    print(f"David's score: {students.get('David', 'Not Found')}")


# ==========================================
# TASK 4.2: Inventory System (Nested Dicts)
# ==========================================
# Nested dictionary demonstrating complex data structures
# Structure: Category -> Item -> Properties (price, stock)
inventory: Dict[str, Dict[str, Dict[str, int]]] = {
    "Electronics": {
        "Laptop": {"price": 1000, "stock": 5},
        "Mouse": {"price": 20, "stock": 50}
    },
    "Furniture": {
        "Chair": {"price": 100, "stock": 10}
    }
}


def manage_inventory() -> None:
    """
    Demonstrate operations on nested dictionary structures.

    Operations shown:
    1. Multi-level access: dict[key1][key2][key3]
    2. In-place modification: -= operator
    3. Adding new items to nested structure
    4. Nested iteration to aggregate data

    Nested dictionaries are useful for representing hierarchical data
    like catalogs, organizational structures, or configuration settings.

    Returns:
        None: Prints inventory operations and results

    Example Output:
        Laptop Price: 1000
        Total Inventory Value: $11450

    Best Practice:
        When working with deeply nested structures, consider:
        1. Using .get() for safe access: inventory.get('Electronics', {})
        2. Extracting nested access to variables for readability
        3. Using dataclasses or named tuples for better structure
    """
    # 1. Access nested value through multiple levels
    # Syntax: dict[outer_key][inner_key][property_key]
    laptop_price = inventory['Electronics']['Laptop']['price']
    print(f"Laptop Price: {laptop_price}")

    # 2. Update nested value (simulating a sale)
    # The -= operator modifies the value in place
    inventory['Electronics']['Laptop']['stock'] -= 1
    # After this operation, Laptop stock becomes 4

    # 3. Add new item to existing category
    # We're adding a new inner dictionary to the Electronics category
    inventory['Electronics']['Keyboard'] = {"price": 50, "stock": 20}

    # 4. Calculate total inventory value across all items
    total = 0

    # Outer loop: iterate through categories (Electronics, Furniture)
    for category in inventory.values():
        # Inner loop: iterate through items in each category
        for item in category.values():
            # Calculate value: price × quantity
            total += item['price'] * item['stock']

    print(f"Total Inventory Value: ${total}")


# ==========================================
# TASK 4.3: Clean Usernames
# ==========================================
def clean_usernames(raw_list: List[str]) -> List[str]:
    """
    Normalize a list of usernames by removing whitespace and converting to lowercase.

    This demonstrates the accumulator pattern: build a new list by transforming
    each element of an input list.

    Common data cleaning operations:
    - .strip(): Remove leading/trailing whitespace
    - .lower(): Convert to lowercase for case-insensitive comparison

    Args:
        raw_list: List of raw username strings (may have inconsistent formatting)

    Returns:
        New list with cleaned usernames (lowercase, no extra whitespace)

    Example:
        >>> clean_usernames(["  Bob  ", "ALICE", "  charlie  "])
        ['bob', 'alice', 'charlie']

    Alternative Implementation (List Comprehension):
        return [name.strip().lower() for name in raw_list]

    This would be more Pythonic and concise, but the loop version
    is more explicit for learning purposes.
    """
    # Initialize empty list to accumulate results
    cleaned = []

    # Iterate through each raw username
    for name in raw_list:
        # Chain string methods: first strip whitespace, then lowercase
        # Method chaining works left-to-right: name.strip() returns a string,
        # then .lower() is called on that result
        cleaned_name = name.strip().lower()
        cleaned.append(cleaned_name)

    return cleaned


# ==========================================
# TASK 4.4: Set Operations
# ==========================================
def set_hobbies() -> None:
    """
    Demonstrate mathematical set operations with Python sets.

    Sets are unordered collections of unique elements. They're perfect for:
    - Removing duplicates from a list: set([1, 2, 2, 3]) → {1, 2, 3}
    - Membership testing: 'coding' in wilson → True
    - Mathematical set operations (shown below)

    Set operations (mathematical concepts):
    - Intersection (∩): Elements in BOTH sets
    - Union (∪): Elements in EITHER set (combined, no duplicates)
    - Difference (−): Elements in first set but NOT in second

    Returns:
        None: Prints results of set operations

    Example Output:
        Common: {'gaming'}
        All Unique: {'coding', 'gaming', 'reading', 'hiking', 'cooking'}
        Wilson Only: {'coding', 'reading'}

    Real-World Use Cases:
        - Find common interests between users (intersection)
        - Merge tags from multiple sources (union)
        - Find unique features of a product (difference)

    Note:
        Sets use curly braces {} like dictionaries, but contain only values,
        not key-value pairs. Empty set must be created with set(), not {},
        because {} creates an empty dictionary.
    """
    # Create two sets of hobbies
    # Sets automatically eliminate duplicates if any exist
    wilson = {"coding", "gaming", "reading"}
    friend = {"gaming", "hiking", "cooking"}

    # Intersection: What hobbies do both people share?
    # Result: {'gaming'} - only hobby in both sets
    print(f"Common: {wilson.intersection(friend)}")
    # Alternative syntax: wilson & friend

    # Union: What are all hobbies combined (no duplicates)?
    # Result: All unique hobbies from both sets
    print(f"All Unique: {wilson.union(friend)}")
    # Alternative syntax: wilson | friend

    # Difference: What hobbies does Wilson have that friend doesn't?
    # Result: {'coding', 'reading'} - Wilson's unique hobbies
    print(f"Wilson Only: {wilson.difference(friend)}")
    # Alternative syntax: wilson - friend


# Script entry point
if __name__ == "__main__":
    """
    Run demonstrations of all functions.
    """
    # Test list statistics
    print(list_statistics([10, 20, 30, 40]))

    # Demonstrate dictionary operations
    process_students()

    # Show nested dictionary management
    manage_inventory()

    # Display username cleaning
    print(clean_usernames(["  Bob  ", "ALICE", "  charlie  "]))

    # Illustrate set operations
    set_hobbies()
