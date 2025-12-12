# Python Decorators Cheat Sheet

## Quick Reference Card

| Operation | Syntax | Example |
|-----------|--------|---------|
| Basic decorator | `@decorator` | `@timer` |
| Decorator function | `def decorator(func):` | Define decorator |
| Call wrapped function | `return func(*args, **kwargs)` | Execute original |
| Decorator with args | `@decorator(arg)` | `@retry(times=3)` |
| Class decorator | `@classmethod` | Built-in class decorator |
| Property decorator | `@property` | Make method a property |
| Static method | `@staticmethod` | No self parameter |
| Preserve metadata | `@wraps(func)` | From functools |
| Multiple decorators | Stack decorators | Apply bottom-up |
| Class as decorator | `class Decorator:` | Use class instance |

## Table of Contents
1. [Decorator Basics](#decorator-basics)
2. [Function Decorators](#function-decorators)
3. [Decorators with Arguments](#decorators-with-arguments)
4. [Class Decorators](#class-decorators)
5. [Built-in Decorators](#built-in-decorators)
6. [functools Decorators](#functools-decorators)
7. [Practical Decorator Examples](#practical-decorator-examples)
8. [Best Practices](#best-practices)

---

## Decorator Basics

### What Are Decorators?

```python
# Decorators modify or enhance functions/classes
# Without changing their source code

# Without decorator
def say_hello():
    return 'Hello!'

say_hello = logger(say_hello)  # Manually wrap

# With decorator
@logger
def say_hello():
    return 'Hello!'

# @ is syntactic sugar for wrapping
```

### How Decorators Work

```python
# Decorators are functions that take a function and return a new function

def my_decorator(func):
    """Basic decorator structure"""
    def wrapper():
        print('Before function call')
        result = func()  # Call original function
        print('After function call')
        return result
    return wrapper

# Apply decorator
@my_decorator
def say_hello():
    print('Hello!')

# When called:
say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

### First-Class Functions

```python
# Functions are objects in Python
def greet(name):
    return f'Hello, {name}!'

# Assign to variable
say_hi = greet
print(say_hi('Alice'))  # Hello, Alice!

# Pass as argument
def execute(func, value):
    return func(value)

result = execute(greet, 'Bob')  # Hello, Bob!

# Return from function
def get_greeting_function():
    def greet(name):
        return f'Hi, {name}!'
    return greet

greeting = get_greeting_function()
print(greeting('Charlie'))  # Hi, Charlie!
```

---

## Function Decorators

### Simple Function Decorator

```python
def simple_decorator(func):
    """Most basic decorator"""
    def wrapper():
        print('Decorator executed')
        return func()
    return wrapper

@simple_decorator
def say_hello():
    return 'Hello!'

print(say_hello())
# Output:
# Decorator executed
# Hello!
```

### Decorator with Arguments

```python
# Decorator that handles function arguments
def log_arguments(func):
    """Log function arguments"""
    def wrapper(*args, **kwargs):
        print(f'Arguments: {args}, {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@log_arguments
def add(a, b):
    return a + b

result = add(5, 3)
# Output: Arguments: (5, 3), {}
# Returns: 8

@log_arguments
def greet(name, greeting='Hello'):
    return f'{greeting}, {name}!'

result = greet('Alice', greeting='Hi')
# Output: Arguments: ('Alice',), {'greeting': 'Hi'}
# Returns: Hi, Alice!
```

### Preserving Function Metadata

```python
from functools import wraps

# Without @wraps
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def my_function():
    """This is my function"""
    pass

print(my_function.__name__)  # 'wrapper' - Wrong!
print(my_function.__doc__)   # None - Lost!

# With @wraps (correct way)
def good_decorator(func):
    @wraps(func)  # Preserves metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def my_function():
    """This is my function"""
    pass

print(my_function.__name__)  # 'my_function' - Correct!
print(my_function.__doc__)   # 'This is my function' - Preserved!
```

### Multiple Decorators

```python
from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

# Applied bottom-up (decorator2 first, then decorator1)
@decorator1
@decorator2
def say_hello():
    print('Hello!')

say_hello()
# Output:
# Decorator 1
# Decorator 2
# Hello!
```

---

## Decorators with Arguments

### Decorator Factory Pattern

```python
from functools import wraps

def repeat(times):
    """Decorator that repeats function execution"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    return f'Hello, {name}!'

result = greet('Alice')
print(result)
# ['Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!']
```

### Parametrized Decorator Examples

```python
from functools import wraps
import time

def delay(seconds):
    """Add delay before function execution"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay(seconds=2)
def say_hello():
    return 'Hello!'

# Waits 2 seconds before executing
result = say_hello()

# Retry decorator with arguments
def retry(max_attempts=3, delay_seconds=1):
    """Retry function on exception"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f'Attempt {attempt + 1} failed: {e}')
                    time.sleep(delay_seconds)
        return wrapper
    return decorator

@retry(max_attempts=3, delay_seconds=2)
def unstable_api_call():
    # Might fail, will retry
    return make_request()
```

### Optional Arguments Decorator

```python
from functools import wraps

def smart_decorator(arg=None):
    """Decorator that works with or without arguments"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Decorator arg: {arg}')
            return func(*args, **kwargs)
        return wrapper

    # Called without arguments
    if callable(arg):
        return decorator(arg)

    # Called with arguments
    return decorator

# Without arguments
@smart_decorator
def func1():
    return 'Function 1'

# With arguments
@smart_decorator(arg='custom')
def func2():
    return 'Function 2'

func1()  # Decorator arg: None
func2()  # Decorator arg: custom
```

---

## Class Decorators

### Decorating Classes

```python
def add_string_method(cls):
    """Add __str__ method to class"""
    def to_string(self):
        return f'{cls.__name__} instance'
    cls.__str__ = to_string
    return cls

@add_string_method
class MyClass:
    pass

obj = MyClass()
print(obj)  # MyClass instance
```

### Using Classes as Decorators

```python
class CallCounter:
    """Decorator class that counts function calls"""

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f'Call {self.count} to {self.func.__name__}')
        return self.func(*args, **kwargs)

@CallCounter
def say_hello():
    return 'Hello!'

say_hello()  # Call 1 to say_hello
say_hello()  # Call 2 to say_hello
say_hello()  # Call 3 to say_hello
print(say_hello.count)  # 3
```

### Class Decorator with Arguments

```python
class Repeat:
    """Class decorator with arguments"""

    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(self.times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper

@Repeat(times=3)
def greet(name):
    return f'Hello, {name}!'

result = greet('Alice')
# ['Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!']
```

---

## Built-in Decorators

### @property

```python
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        """Getter - access like an attribute"""
        return f'{self._first_name} {self._last_name}'

    @property
    def email(self):
        """Computed property"""
        return f'{self._first_name.lower()}.{self._last_name.lower()}@email.com'

person = Person('John', 'Doe')
print(person.full_name)  # John Doe
print(person.email)      # john.doe@email.com
```

### @property with Setter

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius"""
        if value < -273.15:
            raise ValueError('Temperature below absolute zero')
        self._celsius = value

    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit"""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit"""
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0
temp.fahrenheit = 68
print(temp.celsius)     # 20.0
```

### @staticmethod

```python
class MathUtils:
    """Static methods don't access instance or class"""

    @staticmethod
    def add(a, b):
        """No self or cls parameter"""
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

# Call without instance
result = MathUtils.add(5, 3)  # 8
print(MathUtils.is_even(4))   # True

# Can also call from instance (but unusual)
utils = MathUtils()
result = utils.add(2, 3)  # 5
```

### @classmethod

```python
class Person:
    """Class methods receive class as first argument"""
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Alternative constructor"""
        current_year = 2024
        age = current_year - birth_year
        return cls(name, age)

    @classmethod
    def get_population(cls):
        """Access class variables"""
        return cls.population

# Normal constructor
p1 = Person('Alice', 30)

# Alternative constructor using @classmethod
p2 = Person.from_birth_year('Bob', 1995)
print(p2.age)  # 29

# Access class method
print(Person.get_population())  # 2
```

### Combining @property, @classmethod, @staticmethod

```python
class BankAccount:
    """Comprehensive example using all three decorators"""
    interest_rate = 0.05  # Class variable

    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        """Property getter"""
        return self._balance

    @balance.setter
    def balance(self, value):
        """Property setter with validation"""
        if value < 0:
            raise ValueError('Balance cannot be negative')
        self._balance = value

    @classmethod
    def set_interest_rate(cls, rate):
        """Modify class variable"""
        cls.interest_rate = rate

    @classmethod
    def from_dict(cls, data):
        """Alternative constructor"""
        return cls(data['owner'], data['balance'])

    @staticmethod
    def validate_account_number(number):
        """Utility function"""
        return len(str(number)) == 10

# Usage
account = BankAccount('Alice', 1000)
print(account.balance)  # 1000

BankAccount.set_interest_rate(0.06)
print(BankAccount.interest_rate)  # 0.06

data = {'owner': 'Bob', 'balance': 500}
account2 = BankAccount.from_dict(data)

is_valid = BankAccount.validate_account_number(1234567890)
```

---

## functools Decorators

### @wraps

```python
from functools import wraps

# Covered earlier - preserves function metadata
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### @lru_cache

```python
from functools import lru_cache

# Least Recently Used cache - speeds up repeated calls
@lru_cache(maxsize=128)
def fibonacci(n):
    """Cached Fibonacci - much faster!"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# First call - calculates
print(fibonacci(100))  # Fast due to caching

# Check cache info
print(fibonacci.cache_info())
# CacheInfo(hits=98, misses=101, maxsize=128, currsize=101)

# Clear cache
fibonacci.cache_clear()
```

### @lru_cache with Arguments

```python
from functools import lru_cache
import time

@lru_cache(maxsize=32)
def expensive_operation(x, y):
    """Simulate expensive computation"""
    time.sleep(1)  # Slow operation
    return x + y

# First call - slow (1 second)
result = expensive_operation(2, 3)

# Second call with same arguments - instant!
result = expensive_operation(2, 3)

# Different arguments - slow again
result = expensive_operation(4, 5)

# Unlimited cache size
@lru_cache(maxsize=None)
def unlimited_cache(x):
    return x ** 2
```

### @singledispatch

```python
from functools import singledispatch

# Generic function
@singledispatch
def process(data):
    """Default implementation"""
    return f'Processing unknown type: {type(data)}'

# Register implementation for int
@process.register(int)
def _(data):
    return f'Processing integer: {data * 2}'

# Register implementation for str
@process.register(str)
def _(data):
    return f'Processing string: {data.upper()}'

# Register implementation for list
@process.register(list)
def _(data):
    return f'Processing list of {len(data)} items'

# Usage
print(process(42))           # Processing integer: 84
print(process('hello'))      # Processing string: HELLO
print(process([1, 2, 3]))    # Processing list of 3 items
print(process(3.14))         # Processing unknown type: <class 'float'>
```

### @total_ordering

```python
from functools import total_ordering

@total_ordering
class Person:
    """Define only __eq__ and __lt__, get others for free"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

# All comparison operators now work!
p1 = Person('Alice', 30)
p2 = Person('Bob', 25)

print(p1 > p2)   # True (derived from __lt__)
print(p1 <= p2)  # False (derived from __lt__ and __eq__)
print(p1 >= p2)  # True (derived from __lt__ and __eq__)
print(p1 != p2)  # True (derived from __eq__)
```

---

## Practical Decorator Examples

### Timer Decorator

```python
from functools import wraps
import time

def timer(func):
    """Measure function execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start:.4f} seconds')
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return 'Done'

result = slow_function()
# Output: slow_function took 1.0001 seconds
```

### Debug Decorator

```python
from functools import wraps

def debug(func):
    """Print function calls and returns"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')

        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result!r}')
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

result = add(5, 3)
# Output:
# Calling add(5, 3)
# add returned 8
```

### Rate Limiter Decorator

```python
from functools import wraps
import time

def rate_limit(max_calls, period):
    """Limit function calls to max_calls per period (seconds)"""
    calls = []

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()

            # Remove old calls
            calls[:] = [c for c in calls if c > now - period]

            if len(calls) >= max_calls:
                sleep_time = period - (now - calls[0])
                print(f'Rate limit reached. Waiting {sleep_time:.2f} seconds')
                time.sleep(sleep_time)
                calls[:] = []

            calls.append(time.time())
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=3, period=10)
def api_call():
    print('Making API call')
    return 'Success'

# First 3 calls execute immediately
# 4th call waits until period expires
```

### Validation Decorator

```python
from functools import wraps

def validate_types(**type_checks):
    """Validate function argument types"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get function signature
            import inspect
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)

            # Check types
            for param_name, expected_type in type_checks.items():
                if param_name in bound.arguments:
                    value = bound.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f'{param_name} must be {expected_type.__name__}, '
                            f'got {type(value).__name__}'
                        )

            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(name=str, age=int)
def create_user(name, age):
    return {'name': name, 'age': age}

# Valid
user = create_user('Alice', 30)

# Invalid - raises TypeError
user = create_user('Bob', '25')  # age should be int
```

### Memoization Decorator

```python
from functools import wraps

def memoize(func):
    """Cache function results"""
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    # Add cache inspection
    wrapper.cache = cache
    return wrapper

@memoize
def expensive_calculation(n):
    print(f'Calculating for {n}')
    return n ** 2

result = expensive_calculation(5)  # Calculates
# Output: Calculating for 5

result = expensive_calculation(5)  # Uses cache
# No output - cached

print(expensive_calculation.cache)  # {(5,): 25}
```

### Authentication Decorator

```python
from functools import wraps

def require_auth(func):
    """Require authentication before executing"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Assume we have a way to check authentication
        if not is_authenticated():
            raise PermissionError('Authentication required')
        return func(*args, **kwargs)
    return wrapper

def require_role(role):
    """Require specific role"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not user_has_role(role):
                raise PermissionError(f'Role {role} required')
            return func(*args, **kwargs)
        return wrapper
    return decorator

@require_auth
def view_profile():
    return 'Profile data'

@require_role('admin')
def delete_user(user_id):
    return f'Deleted user {user_id}'
```

---

## Best Practices

### Always Use @wraps

```python
from functools import wraps

# Good practice
def my_decorator(func):
    @wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### Make Decorators Generic

```python
from functools import wraps

# Good: Accepts any arguments
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Handle any function
        return func(*args, **kwargs)
    return wrapper
```

### Document Decorators

```python
def my_decorator(func):
    """
    Decorator that does X, Y, and Z.

    Args:
        func: Function to decorate

    Returns:
        Decorated function

    Example:
        @my_decorator
        def my_function():
            pass
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### Keep Decorators Simple

```python
# Bad: Too much logic in decorator
def complex_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 50 lines of complex logic
        result = func(*args, **kwargs)
        # 50 more lines
        return result
    return wrapper

# Good: Extract logic into helper functions
def process_before():
    # Logic here
    pass

def process_after(result):
    # Logic here
    return result

def simple_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        process_before()
        result = func(*args, **kwargs)
        return process_after(result)
    return wrapper
```

### Order Matters with Multiple Decorators

```python
# Decorators applied bottom-up
@decorator1  # Applied second
@decorator2  # Applied first
def my_function():
    pass

# Equivalent to:
my_function = decorator1(decorator2(my_function))
```

---

## See Also

- **[Functional Programming Cheat Sheet](Functional_Programming_Cheat_Sheet.md)** - Lambda functions and functional concepts
- **[OOP Cheat Sheet](OOP_Cheat_Sheet.md)** - Class methods and properties
- **[Python Basics Cheat Sheet](Python_Basics_Cheat_Sheet.md)** - Function fundamentals

---
