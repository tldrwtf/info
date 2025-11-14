# Python Error Handling & Exceptions Cheat Sheet

## Quick Reference Card

| Operation | Syntax | Example |
|-----------|--------|---------|
| Try/except | `try: ... except:` | `try: x = 1/0 except: pass` |
| Specific exception | `except TypeError:` | `except ValueError as e:` |
| Multiple exceptions | `except (Type1, Type2):` | `except (ValueError, KeyError):` |
| Catch all | `except Exception as e:` | `except Exception as e:` |
| Else clause | `try: ... else:` | Execute if no exception |
| Finally clause | `try: ... finally:` | Always executes |
| Raise exception | `raise Exception(msg)` | `raise ValueError('Invalid')` |
| Custom exception | `class MyError(Exception):` | Define custom error |
| Context manager | `with ... as:` | `with open('f') as f:` |
| Assert | `assert condition` | `assert x > 0` |

## Table of Contents
1. [Exception Basics](#exception-basics)
2. [Try/Except/Else/Finally](#tryexceptelsefinally)
3. [Common Built-in Exceptions](#common-built-in-exceptions)
4. [Raising Exceptions](#raising-exceptions)
5. [Custom Exceptions](#custom-exceptions)
6. [Exception Chaining](#exception-chaining)
7. [Context Managers](#context-managers)
8. [Best Practices](#best-practices)

---

## Exception Basics

### What Are Exceptions?

```python
# Exceptions are errors detected during execution
# They interrupt normal program flow

# Without exception handling (program crashes)
result = 10 / 0  # ZeroDivisionError: division by zero

# With exception handling (program continues)
try:
    result = 10 / 0
except ZeroDivisionError:
    result = None
    print('Cannot divide by zero')
```

### Basic Exception Handling

```python
# Simple try/except
try:
    number = int('abc')  # ValueError
except ValueError:
    print('Invalid number format')

# Capture exception details
try:
    number = int('abc')
except ValueError as e:
    print(f'Error: {e}')  # Error: invalid literal for int()
```

---

## Try/Except/Else/Finally

### Try/Except Block

```python
# Basic form
try:
    # Code that might raise an exception
    result = 10 / 2
except ZeroDivisionError:
    # Handle the exception
    result = None
    print('Division by zero')
```

### Multiple Except Clauses

```python
# Handle different exceptions differently
try:
    value = int(input('Enter a number: '))
    result = 10 / value
except ValueError:
    print('Invalid input - not a number')
except ZeroDivisionError:
    print('Cannot divide by zero')
except Exception as e:
    print(f'Unexpected error: {e}')
```

### Catching Multiple Exceptions Together

```python
# Same handling for multiple exceptions
try:
    data = {'key': 'value'}
    result = data['missing_key']
    number = int('abc')
except (KeyError, ValueError) as e:
    print(f'Error occurred: {e}')

# Or separately
try:
    process_data()
except (IOError, OSError) as e:
    print(f'File operation failed: {e}')
```

### Else Clause

```python
# Executes if NO exception is raised
try:
    result = 10 / 2
except ZeroDivisionError:
    print('Division by zero')
else:
    print(f'Result: {result}')  # Executes if no error
    # Use else for code that should run only if try succeeds

# Practical example
def read_file(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print(f'File {filename} not found')
        return None
    else:
        # Only read if file was opened successfully
        content = f.read()
        f.close()
        return content
```

### Finally Clause

```python
# ALWAYS executes, even if exception occurs
try:
    file = open('data.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print('File not found')
finally:
    # Always executes - cleanup code
    try:
        file.close()
    except:
        pass
    print('Cleanup complete')
```

### Complete Try/Except/Else/Finally Example

```python
def divide_numbers(a, b):
    """Complete exception handling example"""
    result = None

    try:
        # Try to perform the operation
        result = a / b
    except ZeroDivisionError:
        # Handle specific error
        print('Error: Cannot divide by zero')
    except TypeError:
        # Handle another specific error
        print('Error: Invalid types for division')
    else:
        # Executes if no exception occurred
        print(f'Division successful: {result}')
    finally:
        # Always executes (cleanup)
        print('Division operation completed')

    return result

# Usage
divide_numbers(10, 2)   # Success
divide_numbers(10, 0)   # ZeroDivisionError
divide_numbers(10, 'a') # TypeError
```

---

## Common Built-in Exceptions

### Commonly Used Exceptions

| Exception | When It Occurs | Example |
|-----------|----------------|---------|
| `Exception` | Base class for most exceptions | Generic catch-all |
| `ValueError` | Invalid value for operation | `int('abc')` |
| `TypeError` | Wrong type for operation | `'2' + 2` |
| `KeyError` | Key not found in dictionary | `dict['missing']` |
| `IndexError` | Index out of range | `list[999]` |
| `FileNotFoundError` | File doesn't exist | `open('missing.txt')` |
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `AttributeError` | Attribute doesn't exist | `obj.missing_attr` |
| `ImportError` | Module import fails | `import missing_module` |
| `RuntimeError` | Generic runtime error | Various situations |

### Exception Examples

```python
# ValueError - Invalid value
try:
    number = int('not a number')
except ValueError as e:
    print(f'ValueError: {e}')

# TypeError - Wrong type
try:
    result = '2' + 2  # Can't add string and int
except TypeError as e:
    print(f'TypeError: {e}')

# KeyError - Missing dictionary key
try:
    data = {'name': 'Alice'}
    age = data['age']  # Key doesn't exist
except KeyError as e:
    print(f'KeyError: {e}')

# IndexError - Invalid list index
try:
    items = [1, 2, 3]
    value = items[10]  # Index out of range
except IndexError as e:
    print(f'IndexError: {e}')

# FileNotFoundError - File doesn't exist
try:
    with open('missing_file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print(f'FileNotFoundError: {e}')

# AttributeError - Missing attribute
try:
    value = None
    value.some_method()  # None has no method some_method
except AttributeError as e:
    print(f'AttributeError: {e}')
```

### Exception Hierarchy

```python
# Exception hierarchy (simplified)
# BaseException
#   ├── Exception
#   │   ├── ValueError
#   │   ├── TypeError
#   │   ├── KeyError
#   │   ├── IndexError
#   │   ├── FileNotFoundError
#   │   └── ... (many more)
#   ├── KeyboardInterrupt
#   └── SystemExit

# Catching parent exception catches all children
try:
    value = int('abc')  # Raises ValueError
except Exception as e:  # Catches ValueError (and most others)
    print(f'Caught: {e}')

# Be specific when possible
try:
    value = int('abc')
except ValueError:  # More specific - better
    print('Invalid integer')
except Exception:   # Generic fallback
    print('Some other error')
```

---

## Raising Exceptions

### Raise Built-in Exceptions

```python
# Raise an exception manually
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return a / b

# Raise ValueError for invalid input
def set_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    if age > 150:
        raise ValueError('Age seems unrealistic')
    return age

# Usage
try:
    set_age(-5)
except ValueError as e:
    print(f'Error: {e}')
```

### Raise Without Arguments

```python
# Re-raise the current exception
def process_data(data):
    try:
        result = int(data)
    except ValueError:
        print('Logging error...')
        raise  # Re-raise the same exception

# Usage
try:
    process_data('invalid')
except ValueError as e:
    print(f'Caught re-raised exception: {e}')
```

### Raise Generic Exception

```python
# Raise generic Exception with custom message
def validate_password(password):
    if len(password) < 8:
        raise Exception('Password must be at least 8 characters')
    if not any(c.isdigit() for c in password):
        raise Exception('Password must contain at least one digit')

# Usage
try:
    validate_password('short')
except Exception as e:
    print(f'Validation failed: {e}')
```

---

## Custom Exceptions

### Creating Custom Exceptions

```python
# Basic custom exception
class InvalidAgeError(Exception):
    """Custom exception for invalid age values"""
    pass

# Usage
def set_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(f'Invalid age: {age}')
    return age

try:
    set_age(-5)
except InvalidAgeError as e:
    print(f'Error: {e}')
```

### Custom Exception with Attributes

```python
# Exception with additional data
class InsufficientFundsError(Exception):
    """Exception for insufficient account balance"""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.shortage = amount - balance
        super().__init__(f'Insufficient funds: need ${amount}, have ${balance}')

# Usage
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Error: {e}')
    print(f'Short by: ${e.shortage}')
```

### Exception Hierarchy for Your Application

```python
# Create exception hierarchy
class AppError(Exception):
    """Base exception for application"""
    pass

class DatabaseError(AppError):
    """Database-related errors"""
    pass

class ValidationError(AppError):
    """Validation errors"""
    pass

class AuthenticationError(AppError):
    """Authentication errors"""
    pass

# Usage - can catch all app errors or specific ones
def process_user(user_data):
    if not user_data.get('email'):
        raise ValidationError('Email is required')

    # Database operation
    if not database_available():
        raise DatabaseError('Database connection failed')

try:
    process_user({})
except ValidationError as e:
    print(f'Validation error: {e}')
except DatabaseError as e:
    print(f'Database error: {e}')
except AppError as e:
    print(f'Application error: {e}')
```

---

## Exception Chaining

### From Clause (Explicit Chaining)

```python
# Chain exceptions to preserve context
def load_config():
    try:
        with open('config.json', 'r') as f:
            import json
            return json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError('Configuration file not found') from e
    except json.JSONDecodeError as e:
        raise RuntimeError('Invalid configuration format') from e

# Usage
try:
    config = load_config()
except RuntimeError as e:
    print(f'Error: {e}')
    print(f'Caused by: {e.__cause__}')  # Original exception
```

### Implicit Chaining

```python
# Exceptions during exception handling are automatically chained
def process_data():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        # This exception is implicitly chained to ZeroDivisionError
        undefined_variable  # NameError

try:
    process_data()
except NameError as e:
    print(f'Error: {e}')
    print(f'Context: {e.__context__}')  # Previous exception
```

### Suppressing Chaining

```python
# Suppress exception chaining with 'from None'
def get_value(data, key):
    try:
        return data[key]
    except KeyError:
        # Don't show KeyError in traceback
        raise ValueError(f'Required key "{key}" not found') from None

try:
    get_value({'name': 'Alice'}, 'age')
except ValueError as e:
    print(f'Error: {e}')  # Only shows ValueError, not KeyError
```

---

## Context Managers

### What Are Context Managers?

```python
# Context managers ensure cleanup happens
# Even if exceptions occur

# Without context manager (risky)
file = open('data.txt', 'r')
try:
    content = file.read()
finally:
    file.close()  # Must remember to close

# With context manager (safe)
with open('data.txt', 'r') as file:
    content = file.read()
# File automatically closed, even if exception occurs
```

### Common Context Managers

```python
# File operations
with open('file.txt', 'r') as f:
    content = f.read()

# Database connections
import sqlite3
with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')

# Locks (threading)
from threading import Lock
lock = Lock()
with lock:
    # Critical section
    shared_resource.modify()
```

### Creating Custom Context Managers (Class)

```python
# Using __enter__ and __exit__ methods
class DatabaseConnection:
    """Custom context manager for database"""

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        """Called when entering 'with' block"""
        print(f'Connecting to {self.db_name}')
        self.connection = f'Connection to {self.db_name}'
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        print(f'Closing connection to {self.db_name}')
        if exc_type is not None:
            print(f'Exception occurred: {exc_val}')
        # Return False to propagate exception, True to suppress
        return False

# Usage
with DatabaseConnection('mydb') as conn:
    print(f'Using {conn}')
    # Connection automatically closed after block
```

### Creating Context Managers (Decorator)

```python
from contextlib import contextmanager

@contextmanager
def temporary_file(filename):
    """Context manager using generator"""
    print(f'Creating {filename}')
    f = open(filename, 'w')

    try:
        yield f  # This is what 'as' captures
    finally:
        print(f'Cleaning up {filename}')
        f.close()
        import os
        os.remove(filename)

# Usage
with temporary_file('temp.txt') as f:
    f.write('Temporary data')
# File automatically deleted after block
```

### Practical Context Manager Examples

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name):
    """Measure execution time"""
    start = time.time()
    print(f'{name} started')
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f'{name} took {elapsed:.2f} seconds')

# Usage
with timer('Data processing'):
    # Your code here
    time.sleep(1)
    process_large_dataset()

# Temporary directory
import tempfile
import shutil

@contextmanager
def temp_directory():
    """Create and cleanup temporary directory"""
    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir)

# Usage
with temp_directory() as temp_dir:
    # Use temporary directory
    create_files(temp_dir)
# Directory automatically deleted
```

---

## Best Practices

### Be Specific with Exceptions

```python
# Bad: Catching all exceptions
try:
    result = int(user_input)
except:  # Too broad!
    print('Something went wrong')

# Good: Catch specific exceptions
try:
    result = int(user_input)
except ValueError:
    print('Invalid integer format')
except Exception as e:
    print(f'Unexpected error: {e}')
```

### Don't Use Exceptions for Flow Control

```python
# Bad: Using exceptions for normal flow
try:
    user = users[user_id]
except KeyError:
    user = create_new_user(user_id)

# Good: Use conditional logic
user = users.get(user_id)
if user is None:
    user = create_new_user(user_id)
```

### Provide Helpful Error Messages

```python
# Bad: Generic error message
if age < 0:
    raise ValueError('Invalid value')

# Good: Specific, actionable message
if age < 0:
    raise ValueError(f'Age must be non-negative, got {age}')
```

### Clean Up Resources

```python
# Bad: Manual cleanup
f = open('file.txt', 'r')
content = f.read()
f.close()  # Might not execute if error occurs

# Good: Context manager
with open('file.txt', 'r') as f:
    content = f.read()
# Automatically closed
```

### Log Exceptions Appropriately

```python
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)

def process_data(data):
    try:
        result = complex_operation(data)
        return result
    except ValueError as e:
        logging.error(f'Invalid data: {e}', exc_info=True)
        raise
    except Exception as e:
        logging.exception('Unexpected error in process_data')
        raise
```

### Don't Silence Exceptions

```python
# Bad: Silencing exceptions without handling
try:
    critical_operation()
except:
    pass  # Problems hidden!

# Good: Handle or log appropriately
try:
    critical_operation()
except Exception as e:
    logging.error(f'Critical operation failed: {e}')
    # Re-raise or handle appropriately
    raise
```

### Use Exception Chaining

```python
# Bad: Losing original exception context
try:
    load_config()
except FileNotFoundError:
    raise RuntimeError('Config error')  # Lost original error

# Good: Preserve exception context
try:
    load_config()
except FileNotFoundError as e:
    raise RuntimeError('Config error') from e  # Preserves context
```

### Validate Input Early

```python
def calculate_discount(price, discount_percent):
    """Calculate discount with input validation"""
    # Validate inputs first
    if not isinstance(price, (int, float)):
        raise TypeError('Price must be a number')
    if price < 0:
        raise ValueError('Price cannot be negative')
    if not 0 <= discount_percent <= 100:
        raise ValueError('Discount must be between 0 and 100')

    # Now perform calculation
    return price * (1 - discount_percent / 100)
```

### Comprehensive Example

```python
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)

class FileProcessingError(Exception):
    """Custom exception for file processing"""
    pass

def process_file(filename):
    """Process file with comprehensive error handling"""
    file_path = Path(filename)

    # Validate input
    if not isinstance(filename, (str, Path)):
        raise TypeError('Filename must be a string or Path')

    # Check file exists
    if not file_path.exists():
        raise FileNotFoundError(f'File not found: {filename}')

    # Check file is readable
    if not file_path.is_file():
        raise ValueError(f'Not a file: {filename}')

    # Process file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Process content
        result = content.upper()  # Example processing

        logging.info(f'Successfully processed {filename}')
        return result

    except PermissionError as e:
        logging.error(f'Permission denied: {filename}')
        raise FileProcessingError(f'Cannot read {filename}') from e

    except UnicodeDecodeError as e:
        logging.error(f'Encoding error in {filename}')
        raise FileProcessingError(f'Invalid encoding in {filename}') from e

    except Exception as e:
        logging.exception(f'Unexpected error processing {filename}')
        raise FileProcessingError(f'Failed to process {filename}') from e

# Usage
try:
    result = process_file('data.txt')
    print(result)
except FileNotFoundError as e:
    print(f'File error: {e}')
except FileProcessingError as e:
    print(f'Processing error: {e}')
    if e.__cause__:
        print(f'Caused by: {e.__cause__}')
except Exception as e:
    print(f'Unexpected error: {e}')
```

---

## See Also

- **[File Operations Cheat Sheet](./File_Operations_Cheat_Sheet.md)** - File handling with error handling
- **[Python Basics Cheat Sheet](./Python_Basics_Cheat_Sheet.md)** - Python fundamentals
- **[Testing and Debugging Cheat Sheet](./Testing_and_Debugging_Cheat_Sheet.md)** - Testing exception handling

---

## Summary

Exception handling is crucial for robust Python programs:
- Use **try/except** to handle errors gracefully
- Be **specific** with exception types
- Use **else** for code that runs only if no exception
- Use **finally** for cleanup code that always runs
- Create **custom exceptions** for your application domain
- Use **context managers** for resource management
- **Chain exceptions** to preserve error context
- Provide **helpful error messages**
- **Log exceptions** appropriately
- **Don't silence** exceptions without good reason

---