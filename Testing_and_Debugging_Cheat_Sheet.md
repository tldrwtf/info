# Python Testing & Debugging Cheat Sheet

## Quick Reference Card

| Operation | Syntax | Example |
|-----------|--------|---------|
| Unit test class | `class Test(unittest.TestCase):` | Define test class |
| Test method | `def test_something(self):` | Must start with test_ |
| Assert equal | `self.assertEqual(a, b)` | Check equality |
| Pytest test | `def test_something():` | Simple function |
| Pytest assert | `assert a == b` | Simple assertion |
| Run pytest | `pytest` | Run all tests |
| Mock object | `Mock()` | Create mock |
| Patch function | `@patch('module.func')` | Replace function |
| Fixture | `@pytest.fixture` | Setup/teardown |
| Breakpoint | `breakpoint()` | Start debugger (Python 3.7+) |
| Debug command | `python -m pdb script.py` | Debug script |

> **Note:** For Python versions older than 3.7, use `import pdb; pdb.set_trace()` to start the debugger.
## Table of Contents
1. [Testing Basics](#testing-basics)
2. [unittest Module](#unittest-module)
3. [pytest Framework](#pytest-framework)
4. [Mocking and Patching](#mocking-and-patching)
5. [Test Coverage](#test-coverage)
6. [Debugging with pdb](#debugging-with-pdb)
7. [Debugging Techniques](#debugging-techniques)
8. [Best Practices](#best-practices)

---

## Testing Basics

### Why Test?

```python
# Testing helps:
# - Catch bugs early
# - Document expected behavior
# - Enable refactoring with confidence
# - Improve code design

# Example: Function to test
def add(a, b):
    """Add two numbers"""
    return a + b

# Manual testing (bad)
print(add(2, 3))  # 5
print(add(-1, 1))  # 0

# Automated testing (good)
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

### Types of Tests

```python
# Unit tests - Test individual functions/methods
def test_calculate_discount():
    assert calculate_discount(100, 10) == 90

# Integration tests - Test components together
def test_user_registration_flow():
    user = register_user('alice@example.com')
    assert user.email == 'alice@example.com'
    assert user in database.users

# End-to-end tests - Test entire system
def test_complete_purchase_flow():
    # Login -> Browse -> Add to cart -> Checkout
    pass
```

### Test Structure (AAA Pattern)

```python
def test_user_creation():
    # Arrange - Setup test data
    username = 'alice'
    email = 'alice@example.com'

    # Act - Execute the function
    user = create_user(username, email)

    # Assert - Verify results
    assert user.username == username
    assert user.email == email
    assert user.is_active == True
```

---

## unittest Module

### Basic unittest Test

```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    """Test case for math functions"""

    def test_add_positive(self):
        """Test adding positive numbers"""
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        """Test adding negative numbers"""
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        """Test adding zero"""
        self.assertEqual(add(5, 0), 5)

if __name__ == '__main__':
    unittest.main()
```

### Common Assertions

```python
import unittest

class TestAssertions(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(1, 1)
        self.assertNotEqual(1, 2)

    def test_truthiness(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_none(self):
        self.assertIsNone(None)
        self.assertIsNotNone(42)

    def test_membership(self):
        self.assertIn(1, [1, 2, 3])
        self.assertNotIn(4, [1, 2, 3])

    def test_types(self):
        self.assertIsInstance('hello', str)
        self.assertNotIsInstance('hello', int)

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            int('not a number')

        with self.assertRaises(ZeroDivisionError):
            1 / 0

    def test_approximate_equality(self):
        self.assertAlmostEqual(1.0, 1.0001, places=3)

    def test_greater_less(self):
        self.assertGreater(10, 5)
        self.assertLess(5, 10)
        self.assertGreaterEqual(10, 10)
        self.assertLessEqual(5, 5)
```

### setUp and tearDown

```python
import unittest

class TestDatabase(unittest.TestCase):

    def setUp(self):
        """Run before each test"""
        self.db = Database()
        self.db.connect()
        print('Setup complete')

    def tearDown(self):
        """Run after each test"""
        self.db.disconnect()
        print('Teardown complete')

    def test_insert(self):
        """Test database insert"""
        self.db.insert('user', {'name': 'Alice'})
        result = self.db.query('user', {'name': 'Alice'})
        self.assertEqual(len(result), 1)

    def test_delete(self):
        """Test database delete"""
        self.db.insert('user', {'name': 'Bob'})
        self.db.delete('user', {'name': 'Bob'})
        result = self.db.query('user', {'name': 'Bob'})
        self.assertEqual(len(result), 0)
```

### Class-level Setup

```python
import unittest

class TestExpensiveSetup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Run once before all tests in class"""
        cls.resource = acquire_expensive_resource()
        print('Class setup complete')

    @classmethod
    def tearDownClass(cls):
        """Run once after all tests in class"""
        cls.resource.cleanup()
        print('Class teardown complete')

    def test_one(self):
        # Use self.resource
        pass

    def test_two(self):
        # Use self.resource
        pass
```

### Skipping Tests

```python
import unittest
import sys

class TestSkipping(unittest.TestCase):

    @unittest.skip('Not implemented yet')
    def test_future_feature(self):
        pass

    @unittest.skipIf(sys.version_info < (3, 8), 'Requires Python 3.8+')
    def test_new_feature(self):
        pass

    @unittest.skipUnless(sys.platform.startswith('win'), 'Windows only')
    def test_windows_feature(self):
        pass

    def test_conditional_skip(self):
        if not database_available():
            self.skipTest('Database not available')
        # Test continues if database available
```

---

## pytest Framework

### Basic pytest Test

```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    """Simple pytest test"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Run with: pytest test_math.py
```

### pytest Assertions

```python
def test_assertions():
    # Simple assertions
    assert 1 == 1
    assert 'hello' in 'hello world'
    assert [1, 2, 3] == [1, 2, 3]

    # With custom messages
    x = 5
    assert x > 0, f'x should be positive, got {x}'

def test_exceptions():
    import pytest

    # Test that exception is raised
    with pytest.raises(ValueError):
        int('not a number')

    # Test exception message
    with pytest.raises(ValueError, match='invalid literal'):
        int('not a number')

    # Capture exception for inspection
    with pytest.raises(ZeroDivisionError) as exc_info:
        1 / 0
    assert 'division by zero' in str(exc_info.value)
```

### pytest Fixtures

```python
import pytest

@pytest.fixture
def sample_data():
    """Fixture provides test data"""
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    """Test uses fixture"""
    assert sum(sample_data) == 15

def test_len(sample_data):
    """Another test using same fixture"""
    assert len(sample_data) == 5

# Fixture with setup and teardown
@pytest.fixture
def database():
    """Setup and teardown database"""
    db = Database()
    db.connect()
    yield db  # Test runs here
    db.disconnect()  # Cleanup

def test_query(database):
    result = database.query('SELECT * FROM users')
    assert len(result) > 0
```

### Fixture Scopes

```python
import pytest

@pytest.fixture(scope='function')  # Default - runs for each test
def function_fixture():
    return 'function'

@pytest.fixture(scope='class')  # Once per test class
def class_fixture():
    return 'class'

@pytest.fixture(scope='module')  # Once per module
def module_fixture():
    return 'module'

@pytest.fixture(scope='session')  # Once per test session
def session_fixture():
    return 'session'
```

### Parametrized Tests

```python
import pytest

@pytest.mark.parametrize('input,expected', [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25),
])
def test_square(input, expected):
    """Test runs for each parameter set"""
    assert input ** 2 == expected

@pytest.mark.parametrize('a,b,expected', [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
])
def test_add(a, b, expected):
    assert a + b == expected
```

### pytest Marks

```python
import pytest

@pytest.mark.slow
def test_slow_operation():
    """Mark test as slow"""
    time.sleep(5)
    assert True

@pytest.mark.integration
def test_database_integration():
    """Mark test as integration test"""
    pass

@pytest.mark.skip(reason='Not implemented')
def test_future_feature():
    pass

@pytest.mark.skipif(sys.version_info < (3, 8), reason='Requires Python 3.8+')
def test_new_feature():
    pass

@pytest.mark.xfail(reason='Known bug')
def test_known_bug():
    """Test expected to fail"""
    assert False

# Run specific marks:
# pytest -m slow
# pytest -m "not slow"
```

---

## Mocking and Patching

### Why Mock?

```python
# Mock external dependencies to:
# - Test in isolation
# - Avoid slow operations (API calls, database queries)
# - Simulate error conditions
# - Make tests deterministic

# Example: Function with external dependency
import requests

def get_user_data(user_id):
    """Fetch user from API"""
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()

# Problem: Test requires network and external API
# Solution: Mock the API call
```

### Mock Basics

```python
from unittest.mock import Mock

# Create mock object
mock_obj = Mock()

# Mock has any attribute/method you access
mock_obj.some_method()  # Works
mock_obj.some_attribute  # Works

# Configure return value
mock_obj.some_method.return_value = 42
result = mock_obj.some_method()
assert result == 42

# Check if method was called
mock_obj.some_method()
assert mock_obj.some_method.called
assert mock_obj.some_method.call_count == 1

# Check call arguments
mock_obj.some_method(1, 2, key='value')
mock_obj.some_method.assert_called_with(1, 2, key='value')
```

### Patching Functions

```python
from unittest.mock import patch
import requests

def get_user_name(user_id):
    """Get username from API"""
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()['name']

# Patch with decorator
@patch('requests.get')
def test_get_user_name(mock_get):
    """Test with mocked API call"""
    # Configure mock response
    mock_response = Mock()
    mock_response.json.return_value = {'name': 'Alice'}
    mock_get.return_value = mock_response

    # Call function
    name = get_user_name(123)

    # Assertions
    assert name == 'Alice'
    mock_get.assert_called_once_with('https://api.example.com/users/123')

# Patch with context manager
def test_get_user_name_context():
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {'name': 'Bob'}
        mock_get.return_value = mock_response

        name = get_user_name(456)
        assert name == 'Bob'
```

### Patching Methods

```python
from unittest.mock import patch

class Database:
    def get_user(self, user_id):
        # Expensive database query
        return {'id': user_id, 'name': 'Alice'}

def get_user_email(user_id):
    db = Database()
    user = db.get_user(user_id)
    return f"{user['name'].lower()}@example.com"

@patch.object(Database, 'get_user')
def test_get_user_email(mock_get_user):
    """Mock database method"""
    mock_get_user.return_value = {'id': 1, 'name': 'Bob'}

    email = get_user_email(1)

    assert email == 'bob@example.com'
    mock_get_user.assert_called_once_with(1)
```

### Mock Side Effects

```python
from unittest.mock import Mock

# Return different values on successive calls
mock = Mock()
mock.side_effect = [1, 2, 3]
assert mock() == 1
assert mock() == 2
assert mock() == 3

# Raise exceptions
mock = Mock()
mock.side_effect = ValueError('Invalid input')
try:
    mock()
except ValueError as e:
    assert str(e) == 'Invalid input'

# Use function for complex behavior
def custom_behavior(arg):
    if arg < 0:
        raise ValueError('Negative not allowed')
    return arg * 2

mock = Mock()
mock.side_effect = custom_behavior
assert mock(5) == 10
```

### pytest Mocking

```python
import pytest
from unittest.mock import Mock, patch

def test_with_mocker(mocker):
    """pytest-mock provides mocker fixture"""
    # Patch with mocker
    mock_get = mocker.patch('requests.get')
    mock_response = Mock()
    mock_response.json.return_value = {'name': 'Alice'}
    mock_get.return_value = mock_response

    # Test your code
    result = get_user_name(123)
    assert result == 'Alice'
```

---

## Test Coverage

### Measuring Coverage

```python
# Install coverage tool
# pip install coverage

# Run tests with coverage
# coverage run -m pytest

# Generate report
# coverage report

# Generate HTML report
# coverage html
# open htmlcov/index.html

# Example output:
# Name                  Stmts   Miss  Cover
# -----------------------------------------
# myapp.py                 20      4    80%
# myapp_test.py            15      0   100%
# -----------------------------------------
# TOTAL                    35      4    89%
```

### Coverage Configuration

```python
# .coveragerc file
[run]
source = src
omit =
    */tests/*
    */venv/*
    */__pycache__/*

[report]
precision = 2
exclude_lines =
    pragma: no cover
    def __repr__
    raise NotImplementedError
    if __name__ == .__main__.:
```

---

## Debugging with pdb

### Starting Debugger

```python
# Method 1: Set breakpoint in code
import pdb

def buggy_function(x):
    result = x * 2
    pdb.set_trace()  # Execution pauses here
    return result + 10

# Method 2: Run script with debugger
# python -m pdb script.py

# Method 3: Python 3.7+ built-in
def another_function(x):
    result = x * 2
    breakpoint()  # Built-in debugger
    return result + 10
```

### pdb Commands

```python
# Common pdb commands:
# h (help) - Show help
# l (list) - Show code around current line
# n (next) - Execute next line
# s (step) - Step into function
# c (continue) - Continue execution
# r (return) - Continue until function returns
# p variable - Print variable value
# pp variable - Pretty-print variable
# a (args) - Show function arguments
# w (where) - Show stack trace
# u (up) - Move up stack frame
# d (down) - Move down stack frame
# q (quit) - Quit debugger

# Example debug session:
def calculate(x, y):
    breakpoint()
    result = x + y
    result = result * 2
    return result

# Run and interact:
calculate(5, 3)
# > (Pdb) p x
# 5
# > (Pdb) p y
# 3
# > (Pdb) n
# > (Pdb) p result
# 8
# > (Pdb) c
# 16
```

### Conditional Breakpoints

```python
import pdb

def process_items(items):
    for i, item in enumerate(items):
        # Only break on specific condition
        if item < 0:
            pdb.set_trace()
        process(item)

# Or use pdb's conditional breakpoint
# (Pdb) b 10, item < 0
```

### Post-Mortem Debugging

```python
import pdb

def buggy_code():
    x = 10
    y = 0
    return x / y  # Will crash

try:
    buggy_code()
except:
    pdb.post_mortem()  # Debug at point of exception
```

---

## Debugging Techniques

### Print Debugging

```python
# Simple but effective
def calculate_discount(price, percent):
    print(f'DEBUG: price={price}, percent={percent}')  # Debug print
    discount = price * (percent / 100)
    print(f'DEBUG: discount={discount}')
    final_price = price - discount
    print(f'DEBUG: final_price={final_price}')
    return final_price
```

### Logging for Debugging

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def process_data(data):
    logging.debug(f'Processing data: {data}')

    try:
        result = complex_operation(data)
        logging.debug(f'Operation successful: {result}')
        return result
    except Exception as e:
        logging.error(f'Operation failed: {e}', exc_info=True)
        raise
```

### Assertions for Debugging

```python
def calculate_average(numbers):
    """Calculate average with debug assertions"""
    assert isinstance(numbers, list), 'numbers must be a list'
    assert len(numbers) > 0, 'numbers cannot be empty'

    total = sum(numbers)
    assert isinstance(total, (int, float)), 'sum should be numeric'

    average = total / len(numbers)
    assert average >= min(numbers), 'average should be >= minimum'
    assert average <= max(numbers), 'average should be <= maximum'

    return average
```

### Debugging with repr

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        """Helpful debug representation"""
        return f'User(name={self.name!r}, email={self.email!r})'

# When debugging
user = User('Alice', 'alice@example.com')
print(user)  # User(name='Alice', email='alice@example.com')
```

### Timing Code

```python
import time

def debug_timing(func):
    """Decorator to time function execution"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start:.4f} seconds')
        return result
    return wrapper

@debug_timing
def slow_function():
    time.sleep(1)
    return 'done'
```

---

## Best Practices

### Write Testable Code

```python
# Bad: Hard to test (hidden dependencies)
def process_user():
    db = Database()  # Hidden dependency
    user = db.get_user(1)
    return user.name

# Good: Easy to test (dependency injection)
def process_user(database):
    user = database.get_user(1)
    return user.name

# Can easily test with mock database
def test_process_user():
    mock_db = Mock()
    mock_db.get_user.return_value = Mock(name='Alice')
    result = process_user(mock_db)
    assert result == 'Alice'
```

### Test One Thing Per Test

```python
# Bad: Testing multiple things
def test_user_operations():
    user = create_user('alice')
    assert user.name == 'alice'
    user.update_email('alice@example.com')
    assert user.email == 'alice@example.com'
    user.delete()
    assert user.is_deleted

# Good: Separate tests
def test_user_creation():
    user = create_user('alice')
    assert user.name == 'alice'

def test_user_email_update():
    user = create_user('alice')
    user.update_email('alice@example.com')
    assert user.email == 'alice@example.com'

def test_user_deletion():
    user = create_user('alice')
    user.delete()
    assert user.is_deleted
```

### Use Descriptive Test Names

```python
# Bad
def test_user():
    pass

def test_1():
    pass

# Good
def test_create_user_with_valid_email():
    pass

def test_create_user_raises_error_for_invalid_email():
    pass

def test_user_can_update_password():
    pass
```

### Don't Test Implementation Details

```python
# Bad: Testing implementation
def test_sort_uses_quicksort():
    # Don't test internal algorithm
    pass

# Good: Test behavior
def test_sort_returns_ordered_list():
    result = sort([3, 1, 2])
    assert result == [1, 2, 3]
```

### Keep Tests Fast

```python
# Use mocks to avoid slow operations
@patch('requests.get')
def test_api_call(mock_get):
    mock_get.return_value = Mock(status_code=200)
    # Fast test - no real API call
    result = fetch_data()
    assert result.status_code == 200
```

### Clean Up After Tests

```python
import pytest
import tempfile
import os

@pytest.fixture
def temp_file():
    """Create and cleanup temporary file"""
    fd, path = tempfile.mkstemp()
    yield path
    os.close(fd)
    os.unlink(path)  # Cleanup

def test_file_operations(temp_file):
    # Use temp_file
    # Automatically cleaned up after test
    pass
```

---

## See Also

- **Error_Handling_Cheat_Sheet.md** - Exception handling for tests
- **Decorators_Cheat_Sheet.md** - Decorators for test fixtures
- **File_Operations_Cheat_Sheet.md** - Testing file operations

---

## Summary

Testing and debugging are essential for quality Python code:
- **unittest** provides traditional xUnit-style testing
- **pytest** offers simpler, more powerful testing
- Use **fixtures** for test setup and teardown
- **Mock** external dependencies for isolated tests
- Measure **test coverage** to find untested code
- Use **pdb** for interactive debugging
- **Print/log** debugging for quick investigation
- Write **testable code** with clear dependencies
- Keep tests **fast, focused, and independent**
- Use **descriptive test names** that explain intent

---
