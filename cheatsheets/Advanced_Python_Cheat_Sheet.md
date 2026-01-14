# Advanced Python - Complete Reference Guide

This guide covers advanced Python concepts for building robust, maintainable, and performant applications. From metaclasses to async patterns, these tools help you write cleaner code and solve complex problems elegantly.

## Quick Reference Card

| Concept | Purpose | Syntax | Use When |
|:--------|:--------|:-------|:---------|
| Metaclass | Customize class creation | `class Meta(type):` | Building frameworks, enforcing patterns |
| Descriptor | Control attribute access | `__get__`, `__set__`, `__delete__` | Validation, lazy loading, computed properties |
| Context Manager | Resource cleanup | `with statement:` | File I/O, locks, transactions |
| Generator | Lazy iteration | `def func(): yield` | Large datasets, infinite sequences |
| Decorator | Function modification | `@decorator` | Logging, timing, validation |
| Async/Await | Concurrent I/O | `async def`, `await` | Network requests, file I/O |
| Type Hints | Static type checking | `def func(x: int) -> str:` | Large codebases, API contracts |
| Protocol | Structural subtyping | `class P(Protocol):` | Duck typing with type safety |
| Dataclass | Auto-generate methods | `@dataclass` | Data containers, DTOs |
| ABC | Abstract interfaces | `class C(ABC):` | Defining contracts, plugin systems |

---

## Table of Contents

1. [Metaclasses and Type System](#metaclasses-and-type-system)
2. [Descriptors and Properties](#descriptors-and-properties)
3. [Context Managers](#context-managers)
4. [Advanced Generators and Iterators](#advanced-generators-and-iterators)
5. [Advanced Decorators](#advanced-decorators)
6. [Async/Await and Concurrency](#asyncawait-and-concurrency)
7. [Type Hints and Protocols](#type-hints-and-protocols)
8. [Performance Patterns](#performance-patterns)

---

## Metaclasses and Type System

### What Are Metaclasses?

Metaclasses are classes that create classes. They control how classes are constructed and behave.

```python
# Classes are instances of their metaclass
# type is the default metaclass

class MyClass:
    pass

print(type(MyClass))  # <class 'type'>
print(type(type))     # <class 'type'>
```

### Creating a Simple Metaclass

```python
class SingletonMeta(type):
    """Metaclass that ensures only one instance of a class exists."""

    _instances: dict[type, object] = {}

    def __call__(cls, *args, **kwargs):
        """
        Override instance creation to return existing instance.

        Args:
            *args: Positional arguments for __init__
            **kwargs: Keyword arguments for __init__

        Returns:
            The single instance of the class
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    """Database connection that should only exist once."""

    def __init__(self, connection_string: str) -> None:
        self.connection_string = connection_string
        print(f"Connecting to {connection_string}")


# Only one instance created
db1 = Database("postgresql://localhost/db")
db2 = Database("postgresql://localhost/db")

print(db1 is db2)  # True - same instance!
# Output: Connecting to postgresql://localhost/db (only printed once)
```

### Enforcing Class Structure

```python
class RequiredMethodsMeta(type):
    """Metaclass that enforces required methods on subclasses."""

    required_methods = ["save", "load"]

    def __new__(mcs, name, bases, namespace):
        """
        Validate that required methods are implemented.

        Args:
            mcs: The metaclass itself
            name: Name of the class being created
            bases: Base classes
            namespace: Class attributes and methods

        Returns:
            The new class

        Raises:
            TypeError: If required methods are missing
        """
        # Skip validation for the base class itself
        if name == "Model":
            return super().__new__(mcs, name, bases, namespace)

        # Check for required methods
        for method in mcs.required_methods:
            if method not in namespace:
                raise TypeError(
                    f"{name} must implement {method}() method"
                )

        return super().__new__(mcs, name, bases, namespace)


class Model(metaclass=RequiredMethodsMeta):
    """Base model class that enforces save/load methods."""
    pass


# BAD: This will raise TypeError
try:
    class User(Model):
        def __init__(self, name: str) -> None:
            self.name = name
        # Missing save() and load() methods!
except TypeError as e:
    print(f"Error: {e}")


# GOOD: All required methods implemented
class User(Model):
    def __init__(self, name: str) -> None:
        self.name = name

    def save(self) -> None:
        """Save user to database."""
        print(f"Saving {self.name}")

    def load(self, user_id: int) -> None:
        """Load user from database."""
        print(f"Loading user {user_id}")
```

### Class Registration Pattern

```python
class RegistryMeta(type):
    """Metaclass that automatically registers classes in a registry."""

    registry: dict[str, type] = {}

    def __new__(mcs, name, bases, namespace):
        """
        Create class and register it.

        Args:
            mcs: The metaclass
            name: Class name
            bases: Base classes
            namespace: Class dictionary

        Returns:
            The new registered class
        """
        cls = super().__new__(mcs, name, bases, namespace)

        # Don't register the base class
        if name != "Plugin":
            mcs.registry[name] = cls

        return cls


class Plugin(metaclass=RegistryMeta):
    """Base plugin class with auto-registration."""
    pass


class EmailPlugin(Plugin):
    """Email sending plugin."""
    pass


class SMSPlugin(Plugin):
    """SMS sending plugin."""
    pass


# All plugins automatically registered
print(RegistryMeta.registry)
# {'EmailPlugin': <class '__main__.EmailPlugin'>,
#  'SMSPlugin': <class '__main__.SMSPlugin'>}

# Factory pattern using registry
def create_plugin(name: str) -> Plugin:
    """
    Create plugin instance from registry.

    Args:
        name: Plugin class name

    Returns:
        New plugin instance

    Raises:
        KeyError: If plugin not found
    """
    plugin_class = RegistryMeta.registry[name]
    return plugin_class()


email = create_plugin("EmailPlugin")
sms = create_plugin("SMSPlugin")
```

### When to Use Metaclasses

**GOOD use cases:**
- Framework development (Django models, SQLAlchemy)
- Enforcing coding standards across many classes
- Automatic registration patterns
- Singleton patterns
- API client generation

**BAD use cases:**
- Simple validation (use `__init_subclass__` instead)
- One-off customization (just override `__init__`)
- Most application code (metaclasses are complex)

**Alternative: `__init_subclass__`** (Simpler in most cases)

```python
class Plugin:
    """Base plugin with automatic registration (no metaclass needed)."""

    registry: dict[str, type] = {}

    def __init_subclass__(cls, **kwargs) -> None:
        """
        Register subclass automatically.

        Args:
            **kwargs: Additional arguments
        """
        super().__init_subclass__(**kwargs)
        cls.registry[cls.__name__] = cls


class EmailPlugin(Plugin):
    """Email plugin - automatically registered."""
    pass


print(Plugin.registry)  # {'EmailPlugin': <class '__main__.EmailPlugin'>}
```

---

## Descriptors and Properties

### What Are Descriptors?

Descriptors control how attributes are accessed, set, and deleted. They power `@property`, methods, and many Python internals.

### Descriptor Protocol

```python
class Descriptor:
    """Basic descriptor implementing all three methods."""

    def __get__(self, instance, owner):
        """
        Called when attribute is accessed.

        Args:
            instance: The instance accessing the attribute (or None if accessed from class)
            owner: The owner class

        Returns:
            The attribute value
        """
        print(f"__get__ called on {instance}")
        return self.value

    def __set__(self, instance, value):
        """
        Called when attribute is set.

        Args:
            instance: The instance setting the attribute
            value: The new value
        """
        print(f"__set__ called on {instance} with value {value}")
        self.value = value

    def __delete__(self, instance):
        """
        Called when attribute is deleted.

        Args:
            instance: The instance deleting the attribute
        """
        print(f"__delete__ called on {instance}")
        del self.value
```

### Validation Descriptor

```python
class ValidatedString:
    """Descriptor that validates string attributes."""

    def __init__(self, min_length: int = 0, max_length: int = 100) -> None:
        """
        Initialize validator.

        Args:
            min_length: Minimum allowed string length
            max_length: Maximum allowed string length
        """
        self.min_length = min_length
        self.max_length = max_length
        self.data: dict[int, str] = {}  # Store values per instance

    def __set_name__(self, owner, name):
        """
        Called when descriptor is assigned to class attribute.

        Args:
            owner: The class containing this descriptor
            name: The attribute name
        """
        self.name = name

    def __get__(self, instance, owner):
        """
        Get the validated string value.

        Args:
            instance: The instance (or None for class access)
            owner: The owner class

        Returns:
            The string value or self for class access
        """
        if instance is None:
            return self
        return self.data.get(id(instance), "")

    def __set__(self, instance, value: str) -> None:
        """
        Set and validate the string value.

        Args:
            instance: The instance setting the value
            value: The new string value

        Raises:
            TypeError: If value is not a string
            ValueError: If string length is invalid
        """
        if not isinstance(value, str):
            raise TypeError(f"{self.name} must be a string")

        if len(value) < self.min_length:
            raise ValueError(
                f"{self.name} must be at least {self.min_length} characters"
            )

        if len(value) > self.max_length:
            raise ValueError(
                f"{self.name} must be at most {self.max_length} characters"
            )

        self.data[id(instance)] = value


class User:
    """User with validated attributes."""

    username = ValidatedString(min_length=3, max_length=20)
    email = ValidatedString(min_length=5, max_length=100)

    def __init__(self, username: str, email: str) -> None:
        """
        Initialize user.

        Args:
            username: User's username
            email: User's email address
        """
        self.username = username  # Validation happens here
        self.email = email


# GOOD: Valid user
user = User("alice", "alice@example.com")
print(user.username)  # alice

# BAD: Username too short
try:
    user = User("ab", "alice@example.com")
except ValueError as e:
    print(f"Error: {e}")
    # Error: username must be at least 3 characters
```

### Type-Checking Descriptor

```python
class TypedAttribute:
    """Descriptor that enforces type checking."""

    def __init__(self, expected_type: type) -> None:
        """
        Initialize type checker.

        Args:
            expected_type: The required type for this attribute
        """
        self.expected_type = expected_type
        self.data: dict[int, object] = {}

    def __set_name__(self, owner, name):
        """Store the attribute name."""
        self.name = name

    def __get__(self, instance, owner):
        """Get the typed value."""
        if instance is None:
            return self
        return self.data.get(id(instance))

    def __set__(self, instance, value) -> None:
        """
        Set value with type checking.

        Args:
            instance: The instance
            value: The new value

        Raises:
            TypeError: If value type doesn't match expected type
        """
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} must be {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )
        self.data[id(instance)] = value


class Point:
    """Point with type-checked coordinates."""

    x = TypedAttribute(int)
    y = TypedAttribute(int)

    def __init__(self, x: int, y: int) -> None:
        """
        Initialize point.

        Args:
            x: X coordinate
            y: Y coordinate
        """
        self.x = x
        self.y = y


# GOOD: Integer coordinates
p = Point(10, 20)

# BAD: Float coordinates
try:
    p = Point(10.5, 20.5)
except TypeError as e:
    print(f"Error: {e}")
    # Error: x must be int, got float
```

### Property Decorator (Syntactic Sugar for Descriptors)

```python
class Temperature:
    """Temperature with computed Fahrenheit conversion."""

    def __init__(self, celsius: float) -> None:
        """
        Initialize temperature.

        Args:
            celsius: Temperature in Celsius
        """
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        """
        Get temperature in Celsius.

        Returns:
            Temperature in Celsius
        """
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """
        Set temperature in Celsius.

        Args:
            value: Temperature in Celsius

        Raises:
            ValueError: If temperature is below absolute zero
        """
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """
        Get temperature in Fahrenheit.

        Returns:
            Temperature in Fahrenheit
        """
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        """
        Set temperature using Fahrenheit.

        Args:
            value: Temperature in Fahrenheit
        """
        self.celsius = (value - 32) * 5/9


temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0

temp.fahrenheit = 68
print(temp.celsius)     # 20.0
```

### Lazy Property Pattern

```python
class LazyProperty:
    """Descriptor for lazy-loaded properties (computed once, cached)."""

    def __init__(self, func):
        """
        Initialize lazy property.

        Args:
            func: Function to compute the value
        """
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        """
        Get value, computing it on first access.

        Args:
            instance: The instance (or None)
            owner: The owner class

        Returns:
            The computed (and cached) value
        """
        if instance is None:
            return self

        # Compute value and cache it on the instance
        value = self.func(instance)
        setattr(instance, self.name, value)
        return value


class DataProcessor:
    """Process large dataset with lazy loading."""

    def __init__(self, filename: str) -> None:
        """
        Initialize processor.

        Args:
            filename: Path to data file
        """
        self.filename = filename

    @LazyProperty
    def data(self) -> list[str]:
        """
        Load data from file (expensive operation, done once).

        Returns:
            List of data lines
        """
        print(f"Loading data from {self.filename}...")
        with open(self.filename, 'r') as f:
            return f.readlines()


processor = DataProcessor("data.txt")
# Data not loaded yet

lines = processor.data  # Loads now
# Output: Loading data from data.txt...

lines = processor.data  # Uses cached value, no loading
```

---

## Context Managers

### What Are Context Managers?

Context managers ensure cleanup code runs even when exceptions occur. They're essential for managing resources like files, network connections, and locks.

### Using Context Managers

```python
# BAD: Manual resource management (risky)
file = open('data.txt', 'r')
try:
    content = file.read()
    process(content)
finally:
    file.close()  # Must remember to close


# GOOD: Context manager (automatic cleanup)
with open('data.txt', 'r') as file:
    content = file.read()
    process(content)
# File automatically closed, even if exception occurs
```

### Creating Context Managers (Class-Based)

```python
class DatabaseConnection:
    """Custom context manager for database connections."""

    def __init__(self, connection_string: str) -> None:
        """
        Initialize connection parameters.

        Args:
            connection_string: Database connection string
        """
        self.connection_string = connection_string
        self.connection = None

    def __enter__(self):
        """
        Called when entering 'with' block.

        Returns:
            The connection object
        """
        print(f"Connecting to {self.connection_string}")
        self.connection = f"Connection({self.connection_string})"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Called when exiting 'with' block.

        Args:
            exc_type: Exception type (or None)
            exc_val: Exception value (or None)
            exc_tb: Exception traceback (or None)

        Returns:
            False to propagate exceptions, True to suppress
        """
        print(f"Closing connection to {self.connection_string}")

        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
            # Log error, rollback transaction, etc.

        # Return False to propagate exceptions
        return False


# Usage
with DatabaseConnection("postgresql://localhost/db") as conn:
    print(f"Using {conn}")
    # Connection automatically closed after block
```

### Creating Context Managers (Function-Based)

```python
from contextlib import contextmanager
import tempfile
import os


@contextmanager
def temporary_file(filename: str):
    """
    Create temporary file that's deleted after use.

    Args:
        filename: Name for temporary file

    Yields:
        Open file object

    Example:
        >>> with temporary_file('temp.txt') as f:
        ...     f.write('temporary data')
    """
    print(f"Creating {filename}")
    f = open(filename, 'w')

    try:
        yield f
    finally:
        print(f"Cleaning up {filename}")
        f.close()
        os.remove(filename)


# Usage
with temporary_file('temp.txt') as f:
    f.write('Temporary data')
    process_file(f)
# File automatically deleted
```

### Practical Context Manager Examples

```python
import time
from contextlib import contextmanager


@contextmanager
def timer(name: str):
    """
    Measure and print execution time.

    Args:
        name: Name of the operation being timed

    Yields:
        None

    Example:
        >>> with timer('Data processing'):
        ...     process_large_dataset()
        Data processing took 2.34 seconds
    """
    start = time.time()
    print(f"{name} started")

    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name} took {elapsed:.2f} seconds")


# Usage
with timer("Database query"):
    # Your code here
    time.sleep(1)
    results = db.execute_complex_query()


@contextmanager
def suppress_stdout():
    """
    Temporarily suppress stdout output.

    Yields:
        None

    Example:
        >>> with suppress_stdout():
        ...     print("This won't be visible")
    """
    import sys
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')

    try:
        yield
    finally:
        sys.stdout.close()
        sys.stdout = original_stdout


# Usage
with suppress_stdout():
    print("This is hidden")
    noisy_function()
```

### Nested Context Managers

```python
# Multiple context managers
with open('input.txt', 'r') as infile:
    with open('output.txt', 'w') as outfile:
        content = infile.read()
        outfile.write(content.upper())


# Cleaner syntax (Python 3.1+)
with open('input.txt', 'r') as infile, \
     open('output.txt', 'w') as outfile:
    content = infile.read()
    outfile.write(content.upper())
```

### Context Manager for State Management

```python
@contextmanager
def temporary_setting(config: dict, key: str, temp_value):
    """
    Temporarily change a configuration value.

    Args:
        config: Configuration dictionary
        key: Setting key
        temp_value: Temporary value

    Yields:
        None

    Example:
        >>> config = {'debug': False}
        >>> with temporary_setting(config, 'debug', True):
        ...     print(config['debug'])  # True
        >>> print(config['debug'])  # False
    """
    original_value = config.get(key)
    config[key] = temp_value

    try:
        yield
    finally:
        if original_value is None:
            config.pop(key, None)
        else:
            config[key] = original_value


# Usage
config = {'debug': False, 'timeout': 30}

with temporary_setting(config, 'debug', True):
    print(config['debug'])  # True
    run_debug_code()

print(config['debug'])  # False (restored)
```

---

## Advanced Generators and Iterators

### Generator vs Iterator

```python
# Iterator: Implement __iter__() and __next__()
class Counter:
    """Iterator that counts from start to end."""

    def __init__(self, start: int, end: int) -> None:
        """
        Initialize counter.

        Args:
            start: Starting number
            end: Ending number (exclusive)
        """
        self.current = start
        self.end = end

    def __iter__(self):
        """Return iterator object (self)."""
        return self

    def __next__(self) -> int:
        """
        Get next number.

        Returns:
            The next number in sequence

        Raises:
            StopIteration: When sequence is exhausted
        """
        if self.current >= self.end:
            raise StopIteration

        self.current += 1
        return self.current - 1


# Generator: Use yield keyword
def counter(start: int, end: int):
    """
    Generate numbers from start to end.

    Args:
        start: Starting number
        end: Ending number (exclusive)

    Yields:
        Numbers in sequence

    Example:
        >>> for num in counter(1, 5):
        ...     print(num)
        1
        2
        3
        4
    """
    current = start
    while current < end:
        yield current
        current += 1


# Both work the same way
for num in Counter(1, 5):
    print(num)  # 1, 2, 3, 4

for num in counter(1, 5):
    print(num)  # 1, 2, 3, 4
```

### Generator Expressions

```python
# List comprehension: Creates entire list in memory
squares_list = [x**2 for x in range(1000000)]  # Large memory usage

# Generator expression: Creates values on demand
squares_gen = (x**2 for x in range(1000000))   # Small memory usage


# Memory comparison
import sys
print(sys.getsizeof(squares_list))  # ~8MB
print(sys.getsizeof(squares_gen))   # 112 bytes


# Using generator expressions
evens = (x for x in range(100) if x % 2 == 0)
for num in evens:
    print(num)  # 0, 2, 4, 6, ...


# Chaining generator expressions
numbers = range(100)
evens = (x for x in numbers if x % 2 == 0)
squares = (x**2 for x in evens)
large = (x for x in squares if x > 1000)

print(list(large))  # [1024, 1156, 1296, ...]
```

### Advanced Generator Patterns

```python
def fibonacci(n: int):
    """
    Generate first n Fibonacci numbers.

    Args:
        n: Number of Fibonacci numbers to generate

    Yields:
        Fibonacci numbers

    Example:
        >>> list(fibonacci(10))
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def infinite_sequence(start: int = 0):
    """
    Generate infinite sequence of numbers.

    Args:
        start: Starting number

    Yields:
        Numbers counting up from start

    Warning:
        This generator never ends. Use with care.

    Example:
        >>> gen = infinite_sequence()
        >>> [next(gen) for _ in range(5)]
        [0, 1, 2, 3, 4]
    """
    num = start
    while True:
        yield num
        num += 1


def take(n: int, iterable):
    """
    Take first n items from iterable.

    Args:
        n: Number of items to take
        iterable: Source iterable

    Yields:
        First n items

    Example:
        >>> list(take(5, infinite_sequence()))
        [0, 1, 2, 3, 4]
    """
    for i, item in enumerate(iterable):
        if i >= n:
            break
        yield item
```

### Generator Delegation with yield from

```python
def flatten(nested_list):
    """
    Flatten nested list using yield from.

    Args:
        nested_list: List of lists to flatten

    Yields:
        Individual items from nested lists

    Example:
        >>> nested = [[1, 2], [3, 4], [5, 6]]
        >>> list(flatten(nested))
        [1, 2, 3, 4, 5, 6]
    """
    for sublist in nested_list:
        yield from sublist


# Without yield from (more verbose)
def flatten_verbose(nested_list):
    """Flatten nested list without yield from."""
    for sublist in nested_list:
        for item in sublist:
            yield item


nested = [[1, 2], [3, 4], [5, 6]]
print(list(flatten(nested)))  # [1, 2, 3, 4, 5, 6]
```

### Generator Pipelines

```python
def read_file(filename: str):
    """
    Read file line by line.

    Args:
        filename: Path to file

    Yields:
        Lines from file
    """
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()


def filter_comments(lines):
    """
    Filter out comment lines.

    Args:
        lines: Iterator of lines

    Yields:
        Non-comment lines
    """
    for line in lines:
        if not line.startswith('#'):
            yield line


def parse_data(lines):
    """
    Parse data lines.

    Args:
        lines: Iterator of data lines

    Yields:
        Parsed data dictionaries
    """
    for line in lines:
        if '=' in line:
            key, value = line.split('=', 1)
            yield {key.strip(): value.strip()}


# Build processing pipeline
lines = read_file('config.txt')
filtered = filter_comments(lines)
parsed = parse_data(filtered)

for item in parsed:
    print(item)
```

---

## Advanced Decorators

### Decorator with Arguments (Factory Pattern)

```python
from functools import wraps
import time


def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    Retry decorator with configurable attempts and delay.

    Args:
        max_attempts: Maximum retry attempts
        delay: Delay between attempts in seconds

    Returns:
        Decorator function

    Example:
        >>> @retry(max_attempts=3, delay=2.0)
        ... def unstable_api_call():
        ...     return make_request()
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Wrapper that implements retry logic.

            Args:
                *args: Positional arguments for wrapped function
                **kwargs: Keyword arguments for wrapped function

            Returns:
                Result from wrapped function

            Raises:
                Last exception if all attempts fail
            """
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator


@retry(max_attempts=3, delay=2.0)
def unstable_function():
    """Function that might fail and needs retry logic."""
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success"
```

### Class-Based Decorators

```python
class CountCalls:
    """Decorator that counts function calls."""

    def __init__(self, func):
        """
        Initialize call counter.

        Args:
            func: Function to decorate
        """
        self.func = func
        self.count = 0
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        """
        Increment counter and call function.

        Args:
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Result from wrapped function
        """
        self.count += 1
        print(f"Call {self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)


@CountCalls
def greet(name: str) -> str:
    """
    Greet someone.

    Args:
        name: Person to greet

    Returns:
        Greeting message
    """
    return f"Hello, {name}!"


greet("Alice")  # Call 1 to greet
greet("Bob")    # Call 2 to greet
print(greet.count)  # 2
```

### Decorator that Modifies Function Behavior

```python
def memoize(func):
    """
    Cache function results for speed.

    Args:
        func: Function to memoize

    Returns:
        Memoized function

    Example:
        >>> @memoize
        ... def fibonacci(n):
        ...     if n < 2:
        ...         return n
        ...     return fibonacci(n-1) + fibonacci(n-2)
    """
    cache = {}

    @wraps(func)
    def wrapper(*args):
        """
        Wrapper that caches results.

        Args:
            *args: Arguments (must be hashable)

        Returns:
            Cached or computed result
        """
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    wrapper.cache = cache  # Expose cache for testing
    return wrapper


@memoize
def fibonacci(n: int) -> int:
    """
    Calculate nth Fibonacci number.

    Args:
        n: Position in sequence

    Returns:
        Fibonacci number at position n
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Much faster with memoization
print(fibonacci(100))  # Instant, even for large n
```

### Stacking Multiple Decorators

```python
@timer
@retry(max_attempts=3)
@memoize
def expensive_api_call(url: str) -> dict:
    """
    Make API call with retry, memoization, and timing.

    Args:
        url: API endpoint

    Returns:
        API response data
    """
    import requests
    response = requests.get(url)
    return response.json()


# Decorators applied bottom-up:
# 1. memoize wraps expensive_api_call
# 2. retry wraps memoized function
# 3. timer wraps retried function
```

---

## Async/Await and Concurrency

### Basic Async Functions

```python
import asyncio


async def fetch_data(url: str) -> dict:
    """
    Asynchronously fetch data from URL.

    Args:
        url: URL to fetch

    Returns:
        Response data

    Example:
        >>> data = await fetch_data('https://api.example.com/users')
    """
    print(f"Fetching {url}")
    await asyncio.sleep(1)  # Simulate network delay
    return {'url': url, 'status': 'success'}


async def main():
    """Main async function."""
    # Sequential execution (slow)
    data1 = await fetch_data('https://api.example.com/users')
    data2 = await fetch_data('https://api.example.com/posts')

    print(data1, data2)


# Run async function
asyncio.run(main())
```

### Concurrent Execution with asyncio.gather

```python
async def fetch_all_data(urls: list[str]) -> list[dict]:
    """
    Fetch multiple URLs concurrently.

    Args:
        urls: List of URLs to fetch

    Returns:
        List of response data

    Example:
        >>> urls = ['https://api.example.com/1', 'https://api.example.com/2']
        >>> results = await fetch_all_data(urls)
    """
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results


async def main():
    """Fetch multiple URLs concurrently."""
    urls = [
        'https://api.example.com/users',
        'https://api.example.com/posts',
        'https://api.example.com/comments'
    ]

    results = await fetch_all_data(urls)
    print(f"Fetched {len(results)} URLs")


asyncio.run(main())
```

### Async Context Managers

```python
class AsyncDatabaseConnection:
    """Async context manager for database connections."""

    def __init__(self, connection_string: str) -> None:
        """
        Initialize connection.

        Args:
            connection_string: Database connection string
        """
        self.connection_string = connection_string
        self.connection = None

    async def __aenter__(self):
        """
        Async enter method.

        Returns:
            Database connection
        """
        print(f"Connecting to {self.connection_string}")
        await asyncio.sleep(0.1)  # Simulate async connection
        self.connection = f"AsyncConnection({self.connection_string})"
        return self.connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Async exit method.

        Args:
            exc_type: Exception type
            exc_val: Exception value
            exc_tb: Exception traceback

        Returns:
            False to propagate exceptions
        """
        print(f"Closing {self.connection_string}")
        await asyncio.sleep(0.1)  # Simulate async cleanup
        return False


async def main():
    """Use async context manager."""
    async with AsyncDatabaseConnection("postgresql://localhost/db") as conn:
        print(f"Using {conn}")
        # Connection automatically closed


asyncio.run(main())
```

### Async Generators

```python
async def async_range(count: int):
    """
    Async generator that yields numbers.

    Args:
        count: Number of values to generate

    Yields:
        Numbers from 0 to count-1

    Example:
        >>> async for num in async_range(5):
        ...     print(num)
    """
    for i in range(count):
        await asyncio.sleep(0.1)  # Simulate async work
        yield i


async def main():
    """Consume async generator."""
    async for num in async_range(5):
        print(num)


asyncio.run(main())
```

### Error Handling in Async Code

```python
async def risky_operation(url: str) -> dict:
    """
    Operation that might fail.

    Args:
        url: URL to fetch

    Returns:
        Response data

    Raises:
        ValueError: If operation fails
    """
    await asyncio.sleep(0.5)
    if 'invalid' in url:
        raise ValueError(f"Invalid URL: {url}")
    return {'url': url, 'status': 'success'}


async def main():
    """Handle errors in async code."""
    urls = [
        'https://api.example.com/valid',
        'https://api.example.com/invalid',
        'https://api.example.com/another'
    ]

    tasks = [risky_operation(url) for url in urls]

    # Gather with return_exceptions=True
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for url, result in zip(urls, results):
        if isinstance(result, Exception):
            print(f"Error for {url}: {result}")
        else:
            print(f"Success for {url}: {result}")


asyncio.run(main())
```

---

## Type Hints and Protocols

### Basic Type Hints

```python
from typing import List, Dict, Tuple, Optional, Union


def process_names(names: List[str]) -> Dict[str, int]:
    """
    Count name lengths.

    Args:
        names: List of names

    Returns:
        Dictionary mapping names to lengths

    Example:
        >>> process_names(['Alice', 'Bob'])
        {'Alice': 5, 'Bob': 3}
    """
    return {name: len(name) for name in names}


def find_user(user_id: int) -> Optional[Dict[str, str]]:
    """
    Find user by ID.

    Args:
        user_id: User ID to search for

    Returns:
        User data or None if not found
    """
    users = {1: {'name': 'Alice', 'email': 'alice@example.com'}}
    return users.get(user_id)


def parse_value(value: Union[str, int]) -> int:
    """
    Parse value as integer.

    Args:
        value: String or integer value

    Returns:
        Integer value
    """
    if isinstance(value, str):
        return int(value)
    return value
```

### Generic Types

```python
from typing import TypeVar, Generic, List


T = TypeVar('T')


class Stack(Generic[T]):
    """Generic stack implementation."""

    def __init__(self) -> None:
        """Initialize empty stack."""
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """
        Push item onto stack.

        Args:
            item: Item to push
        """
        self._items.append(item)

    def pop(self) -> T:
        """
        Pop item from stack.

        Returns:
            Top item from stack

        Raises:
            IndexError: If stack is empty
        """
        return self._items.pop()


# Type checker knows these are different types
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)

str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")
```

### Protocol (Structural Subtyping)

```python
from typing import Protocol


class Drawable(Protocol):
    """Protocol for drawable objects."""

    def draw(self) -> None:
        """Draw the object."""
        ...


class Circle:
    """Circle that implements Drawable protocol."""

    def draw(self) -> None:
        """Draw circle."""
        print("Drawing circle")


class Square:
    """Square that implements Drawable protocol."""

    def draw(self) -> None:
        """Draw square."""
        print("Drawing square")


def render(obj: Drawable) -> None:
    """
    Render drawable object.

    Args:
        obj: Any object with a draw() method
    """
    obj.draw()


# Both work without explicit inheritance
render(Circle())  # Drawing circle
render(Square())  # Drawing square
```

### Dataclasses

```python
from dataclasses import dataclass, field
from typing import List


@dataclass
class Point:
    """Point in 2D space."""

    x: int
    y: int


@dataclass
class User:
    """User with auto-generated methods."""

    name: str
    email: str
    age: int = 0
    tags: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate after initialization."""
        if self.age < 0:
            raise ValueError("Age cannot be negative")


# Auto-generated __init__, __repr__, __eq__
user = User(name="Alice", email="alice@example.com", age=30)
print(user)  # User(name='Alice', email='alice@example.com', age=30, tags=[])

user2 = User(name="Alice", email="alice@example.com", age=30)
print(user == user2)  # True
```

### Abstract Base Classes

```python
from abc import ABC, abstractmethod


class Storage(ABC):
    """Abstract base class for storage backends."""

    @abstractmethod
    def save(self, key: str, value: str) -> None:
        """
        Save value with key.

        Args:
            key: Storage key
            value: Value to store
        """
        pass

    @abstractmethod
    def load(self, key: str) -> str:
        """
        Load value by key.

        Args:
            key: Storage key

        Returns:
            Stored value
        """
        pass


class FileStorage(Storage):
    """File-based storage implementation."""

    def save(self, key: str, value: str) -> None:
        """Save to file."""
        with open(f"{key}.txt", 'w') as f:
            f.write(value)

    def load(self, key: str) -> str:
        """Load from file."""
        with open(f"{key}.txt", 'r') as f:
            return f.read()


class MemoryStorage(Storage):
    """In-memory storage implementation."""

    def __init__(self) -> None:
        """Initialize storage."""
        self.data: Dict[str, str] = {}

    def save(self, key: str, value: str) -> None:
        """Save to memory."""
        self.data[key] = value

    def load(self, key: str) -> str:
        """Load from memory."""
        return self.data[key]


# BAD: Cannot instantiate abstract class
try:
    storage = Storage()
except TypeError as e:
    print(f"Error: {e}")


# GOOD: Use concrete implementations
file_storage = FileStorage()
memory_storage = MemoryStorage()
```

---

## Performance Patterns

### Slots for Memory Optimization

```python
# BAD: Regular class (uses __dict__)
class RegularPoint:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


# GOOD: Using __slots__ (no __dict__)
class OptimizedPoint:
    __slots__ = ['x', 'y']

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


# Memory comparison
import sys

regular = RegularPoint(1, 2)
optimized = OptimizedPoint(1, 2)

print(sys.getsizeof(regular.__dict__))  # 112 bytes
print(sys.getsizeof(optimized))         # 48 bytes

# 50% memory reduction for objects with fixed attributes
```

### Local Variable Optimization

```python
# BAD: Repeated global lookups
import math

def calculate_distances(points):
    """Slow: Looks up math.sqrt every iteration."""
    distances = []
    for x, y in points:
        distance = math.sqrt(x**2 + y**2)
        distances.append(distance)
    return distances


# GOOD: Cache global as local
def calculate_distances_fast(points):
    """Fast: math.sqrt is local variable."""
    sqrt = math.sqrt  # Cache as local
    distances = []
    for x, y in points:
        distance = sqrt(x**2 + y**2)
        distances.append(distance)
    return distances


# Even better: Use list comprehension
def calculate_distances_fastest(points):
    """Fastest: List comprehension with cached lookup."""
    sqrt = math.sqrt
    return [sqrt(x**2 + y**2) for x, y in points]
```

### Generator for Memory Efficiency

```python
# BAD: Load entire file into memory
def process_file_slow(filename: str) -> int:
    """Load entire file into memory (high memory usage)."""
    with open(filename, 'r') as f:
        lines = f.readlines()  # Entire file in memory
        return sum(1 for line in lines if line.startswith('ERROR'))


# GOOD: Process line by line
def process_file_fast(filename: str) -> int:
    """Process file line by line (low memory usage)."""
    count = 0
    with open(filename, 'r') as f:
        for line in f:  # One line at a time
            if line.startswith('ERROR'):
                count += 1
    return count


# Even better: Generator expression
def process_file_fastest(filename: str) -> int:
    """Process file with generator expression."""
    with open(filename, 'r') as f:
        return sum(1 for line in f if line.startswith('ERROR'))
```

---

## See Also

- **[Python Basics Cheat Sheet](Python_Basics_Cheat_Sheet.md)** - Python fundamentals and basic concepts
- **[OOP Cheat Sheet](OOP_Cheat_Sheet.md)** - Object-oriented programming principles
- **[Decorators Cheat Sheet](Decorators_Cheat_Sheet.md)** - Comprehensive decorator patterns
- **[Iterators and Generators Cheat Sheet](Iterators_and_Generators_Cheat_Sheet.md)** - Iteration protocols in depth
- **[Functional Programming Cheat Sheet](Functional_Programming_Cheat_Sheet.md)** - map, filter, reduce, and lambda
- **[Error Handling Cheat Sheet](Error_Handling_Cheat_Sheet.md)** - Exception handling best practices
- **[Data Structures Cheat Sheet](Data_Structures_Cheat_Sheet.md)** - Lists, dicts, sets, and tuples
- **[Big O Notation Cheat Sheet](Big_O_Notation_Cheat_Sheet.md)** - Algorithm complexity analysis
