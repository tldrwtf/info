# Flask Testing Comprehensive Guide

---

## Table of Contents

1. [Testing Setup & Configuration](#testing-setup--configuration)
2. [pytest Fixtures for Flask](#pytest-fixtures-for-flask)
3. [Testing Flask Routes](#testing-flask-routes)
4. [Testing Authentication](#testing-authentication)
5. [Database Testing](#database-testing)
6. [Testing CRUD Operations](#testing-crud-operations)
7. [Negative Testing](#negative-testing)
8. [Running Tests](#running-tests)
9. [Best Practices](#best-practices)

---

## Testing Setup & Configuration

### Project Structure

```
project/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   └── util/
│       └── auth.py
├── tests/
│   ├── __init__.py
│   ├── test_users.py
│   ├── test_products.py
│   └── conftest.py (optional for pytest)
├── config.py
└── requirements.txt
```

### Testing Configuration

Create a separate testing configuration in `config.py`:

```python
class Config:
    """Base configuration"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'

class DevelopmentConfig(Config):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database
    TESTING = True
    DEBUG = True
```

**Why in-memory database?** Tests run faster, and the database is automatically cleaned up after each test session.

---

## pytest Fixtures for Flask

### Basic unittest Setup (Python's Built-in Testing)

Flask testing works excellently with Python's built-in `unittest` module:

```python
import unittest
from app import create_app
from app.models import Users, db
from werkzeug.security import generate_password_hash
from app.util.auth import encode_token

class TestUsers(unittest.TestCase):

    def setUp(self):
        """Runs before each test method"""
        # Create testing app instance
        self.app = create_app('TestingConfig')

        # Create test user
        self.user = Users(
            first_name="Test",
            last_name="Lasttest",
            email="tester@email.com",
            password=generate_password_hash('12345'),
            role="user"
        )

        # Set up database
        with self.app.app_context():
            db.drop_all()  # Remove lingering tables
            db.create_all()  # Create fresh tables
            db.session.add(self.user)
            db.session.commit()

        # Create test client and auth token
        self.client = self.app.test_client()
        self.token = encode_token(1, 'user')

    def tearDown(self):
        """Runs after each test method (optional)"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
```

### Key Setup Components

1. **`self.app = create_app('TestingConfig')`** - Create app with testing configuration
2. **`db.drop_all()` and `db.create_all()`** - Fresh database for each test
3. **`self.client = self.app.test_client()`** - Test client for making requests
4. **`self.token = encode_token(...)`** - Pre-generate auth token for protected routes

---

## Testing Flask Routes

### Testing GET Requests

```python
def test_get_users(self):
    """Test retrieving all users"""
    response = self.client.get('/users')

    # Assert status code
    self.assertEqual(response.status_code, 200)

    # Assert response data
    self.assertEqual(response.json[0]['email'], 'tester@email.com')
    self.assertIsInstance(response.json, list)
```

### Testing POST Requests

```python
def test_create_user(self):
    """Test creating a new user"""
    user_payload = {
        "email": "test@email.com",
        "first_name": "Test",
        "last_name": "Lasttest",
        "password": "12345",
        "role": "user"
    }

    # Send POST request with JSON body
    response = self.client.post('/users', json=user_payload)

    # Assert successful creation
    self.assertEqual(response.status_code, 201)

    # Assert response contains expected data
    self.assertEqual(response.json['first_name'], "Test")
    self.assertEqual(response.json['email'], "test@email.com")
    self.assertEqual(response.json['role'], "user")

    # Verify password was hashed
    from werkzeug.security import check_password_hash
    self.assertTrue(check_password_hash(response.json['password'], '12345'))

    # Assert nullable fields
    self.assertIsNone(response.json['DOB'])
    self.assertIsNone(response.json['address'])
```

### Testing PUT Requests

```python
def test_update(self):
    """Test updating user information"""
    headers = {"Authorization": "Bearer " + self.token}

    update_payload = {
        "email": "NEW_EMAIL@email.com",
        "first_name": "Tester",
        "last_name": "Lasttest",
        "password": "12345",
        "role": "user"
    }

    response = self.client.put("/users", headers=headers, json=update_payload)

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json["email"], "NEW_EMAIL@email.com")
```

### Testing DELETE Requests

```python
def test_delete(self):
    """Test deleting a user"""
    headers = {"Authorization": "Bearer " + self.token}

    response = self.client.delete("/users", headers=headers)

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json['message'], "Successfully deleted user 1")
```

---

## Testing Authentication

### Testing Login Endpoint

```python
def test_login(self):
    """Test user login with valid credentials"""
    login_creds = {
        "email": "tester@email.com",
        "password": "12345"
    }

    response = self.client.post("/users/login", json=login_creds)

    # Assert successful login
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json['message'], "Welcome Test")

    # Assert token is present in response
    self.assertIn("token", response.json)
    self.assertIsNotNone(response.json['token'])
```

### Testing Protected Routes

```python
def test_protected_route_with_token(self):
    """Test accessing protected route with valid token"""
    headers = {"Authorization": "Bearer " + self.token}

    response = self.client.get("/users/profile", headers=headers)

    self.assertEqual(response.status_code, 200)
    self.assertIn("first_name", response.json)
```

### Testing Unauthorized Access

```python
def test_unauthorized_delete(self):
    """Test that protected routes reject requests without token"""
    # No authorization header
    response = self.client.delete("/users")

    self.assertEqual(response.status_code, 401)
    self.assertEqual(
        response.json['error'],
        "token missing from authorization headers"
    )
```

### Testing Invalid Tokens

```python
def test_invalid_token(self):
    """Test accessing protected route with invalid token"""
    headers = {"Authorization": "Bearer invalid_token_here"}

    response = self.client.delete("/users", headers=headers)

    self.assertEqual(response.status_code, 401)
    self.assertIn("error", response.json)
```

---

## Database Testing

### Testing Database Constraints

```python
def test_nonunique_email(self):
    """Test that duplicate emails are rejected"""
    # First user already exists from setUp
    duplicate_payload = {
        "email": "tester@email.com",  # Duplicate email
        "first_name": "Another",
        "last_name": "User",
        "password": "password",
        "role": "user"
    }

    response = self.client.post('/users', json=duplicate_payload)

    # Should fail due to unique constraint
    self.assertEqual(response.status_code, 400)
    self.assertIn('email', response.json)
```

### Testing Data Persistence

```python
def test_data_persists_across_requests(self):
    """Test that data saved in one request is available in the next"""
    # Create user
    user_payload = {"email": "persist@test.com", "first_name": "Persist", ...}
    create_response = self.client.post('/users', json=user_payload)
    user_id = create_response.json['id']

    # Retrieve user in separate request
    get_response = self.client.get(f'/users/{user_id}')

    self.assertEqual(get_response.status_code, 200)
    self.assertEqual(get_response.json['email'], "persist@test.com")
```

### Testing Relationships

```python
def test_user_orders_relationship(self):
    """Test that user-orders relationship works correctly"""
    # Create user and order
    user_id = self.user.id
    order_payload = {"user_id": user_id, "total": 100.00}

    response = self.client.post('/orders', json=order_payload)
    self.assertEqual(response.status_code, 201)

    # Verify relationship
    user_response = self.client.get(f'/users/{user_id}/orders')
    self.assertEqual(len(user_response.json), 1)
    self.assertEqual(user_response.json[0]['total'], 100.00)
```

---

## Testing CRUD Operations

### Complete CRUD Test Suite

```python
class TestProductCRUD(unittest.TestCase):

    def setUp(self):
        self.app = create_app('TestingConfig')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def test_create_product(self):
        """Test CREATE operation"""
        product = {"name": "Laptop", "price": 999.99, "stock": 10}
        response = self.client.post('/products', json=product)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], "Laptop")

    def test_read_product(self):
        """Test READ operation"""
        # First create a product
        product = {"name": "Mouse", "price": 29.99, "stock": 50}
        create_response = self.client.post('/products', json=product)
        product_id = create_response.json['id']

        # Then read it
        response = self.client.get(f'/products/{product_id}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], "Mouse")

    def test_update_product(self):
        """Test UPDATE operation"""
        # Create product
        product = {"name": "Keyboard", "price": 79.99, "stock": 25}
        create_response = self.client.post('/products', json=product)
        product_id = create_response.json['id']

        # Update product
        update_data = {"name": "Keyboard", "price": 69.99, "stock": 30}
        response = self.client.put(f'/products/{product_id}', json=update_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['price'], 69.99)
        self.assertEqual(response.json['stock'], 30)

    def test_delete_product(self):
        """Test DELETE operation"""
        # Create product
        product = {"name": "Monitor", "price": 299.99, "stock": 15}
        create_response = self.client.post('/products', json=product)
        product_id = create_response.json['id']

        # Delete product
        response = self.client.delete(f'/products/{product_id}')

        self.assertEqual(response.status_code, 200)

        # Verify deletion
        get_response = self.client.get(f'/products/{product_id}')
        self.assertEqual(get_response.status_code, 404)
```

---

## Negative Testing

Negative testing ensures your API handles errors gracefully.

### Testing Invalid Input

```python
def test_invalid_create(self):
    """Test creating user with missing required field"""
    user_payload = {
        # Missing email (required field)
        "first_name": "Test",
        "last_name": "Lasttest",
        "password": "12345",
        "role": "user"
    }

    response = self.client.post('/users', json=user_payload)

    self.assertEqual(response.status_code, 400)
    self.assertIn('email', response.json)  # Error message should mention email
```

### Testing Malformed Data

```python
def test_malformed_json(self):
    """Test handling of malformed JSON"""
    response = self.client.post(
        '/users',
        data='{"invalid json',
        content_type='application/json'
    )

    self.assertEqual(response.status_code, 400)
```

### Testing Not Found

```python
def test_get_nonexistent_user(self):
    """Test retrieving user that doesn't exist"""
    response = self.client.get('/users/99999')

    self.assertEqual(response.status_code, 404)
    self.assertIn('error', response.json)
```

### Testing Invalid Methods

```python
def test_method_not_allowed(self):
    """Test using wrong HTTP method"""
    response = self.client.patch('/users')  # If PATCH not implemented

    self.assertEqual(response.status_code, 405)
```

---

## Running Tests

### Using unittest

```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python -m unittest tests.test_users

# Run specific test class
python -m unittest tests.test_users.TestUsers

# Run specific test method
python -m unittest tests.test_users.TestUsers.test_create_user

# Verbose output
python -m unittest discover tests -v
```

### Using pytest (Alternative)

Install pytest:
```bash
pip install pytest pytest-flask
```

Run tests:
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific file
pytest tests/test_users.py

# Run tests matching pattern
pytest -k "test_create"

# Show print statements
pytest -s
```

### Coverage Reporting

Install coverage:
```bash
pip install coverage
```

Run with coverage:
```bash
# Using unittest
coverage run -m unittest discover tests
coverage report
coverage html  # Generate HTML report

# Using pytest
pytest --cov=app --cov-report=html
```

---

## Best Practices

### 1. Isolate Tests

Each test should be independent and not rely on other tests:

```python
# GOOD: Fresh database for each test
def setUp(self):
    with self.app.app_context():
        db.drop_all()
        db.create_all()

# BAD: Tests depend on execution order
```

### 2. Use Descriptive Test Names

```python
# GOOD: Clear what's being tested
def test_create_user_with_valid_data_returns_201(self):
    ...

# BAD: Vague test name
def test_1(self):
    ...
```

### 3. Test One Thing Per Test

```python
# GOOD: Focused test
def test_login_with_valid_credentials(self):
    ...

def test_login_with_invalid_credentials(self):
    ...

# BAD: Testing multiple scenarios
def test_login(self):
    # Tests both valid and invalid in one test
```

### 4. Use Assertions Effectively

```python
# GOOD: Multiple specific assertions
self.assertEqual(response.status_code, 200)
self.assertIn('token', response.json)
self.assertIsNotNone(response.json['token'])

# BAD: Single vague assertion
self.assertTrue(response.status_code == 200 and 'token' in response.json)
```

### 5. Test Edge Cases

```python
def test_create_user_with_max_length_name(self):
    """Test name at maximum allowed length"""
    user_payload = {
        "first_name": "A" * 100,  # Max length
        ...
    }
    response = self.client.post('/users', json=user_payload)
    self.assertEqual(response.status_code, 201)

def test_create_user_with_exceeding_max_length(self):
    """Test name exceeding maximum length"""
    user_payload = {
        "first_name": "A" * 101,  # Exceeds max
        ...
    }
    response = self.client.post('/users', json=user_payload)
    self.assertEqual(response.status_code, 400)
```

### 6. Clean Up Resources

```python
def tearDown(self):
    """Always clean up after tests"""
    with self.app.app_context():
        db.session.remove()
        db.drop_all()
```

### 7. Use Test Fixtures for Common Data

```python
class TestOrders(unittest.TestCase):

    def setUp(self):
        self.app = create_app('TestingConfig')
        self.client = self.app.test_client()

        # Common test data
        self.test_user = self.create_test_user()
        self.test_product = self.create_test_product()

    def create_test_user(self):
        """Helper to create test user"""
        user = Users(...)
        with self.app.app_context():
            db.session.add(user)
            db.session.commit()
        return user
```

### 8. Test Both Success and Failure

```python
def test_delete_with_authorization(self):
    """Test successful deletion"""
    ...

def test_delete_without_authorization(self):
    """Test unauthorized deletion fails"""
    ...
```

---

## Common Testing Patterns

### Pattern: Testing Pagination

```python
def test_users_pagination(self):
    """Test that pagination works correctly"""
    # Create 25 users
    for i in range(25):
        self.client.post('/users', json={...})

    # Get first page (10 items)
    response = self.client.get('/users?page=1&per_page=10')
    self.assertEqual(len(response.json['items']), 10)

    # Get second page
    response = self.client.get('/users?page=2&per_page=10')
    self.assertEqual(len(response.json['items']), 10)
```

### Pattern: Testing Filters

```python
def test_filter_users_by_role(self):
    """Test filtering users by role"""
    response = self.client.get('/users?role=admin')

    for user in response.json:
        self.assertEqual(user['role'], 'admin')
```

### Pattern: Testing Sorting

```python
def test_sort_products_by_price(self):
    """Test sorting products by price"""
    response = self.client.get('/products?sort=price&order=asc')

    prices = [product['price'] for product in response.json]
    self.assertEqual(prices, sorted(prices))
```

---

## Summary

Flask testing with `unittest` provides a robust framework for ensuring your API works correctly. Key takeaways:

- **Use `setUp()` for test initialization** - Fresh database, test client, auth tokens
- **Test all HTTP methods** - GET, POST, PUT, DELETE
- **Test both success and failure cases** - Positive and negative testing
- **Isolate tests** - Each test should be independent
- **Use meaningful assertions** - Check status codes, response data, database state
- **Clean up after tests** - Use `tearDown()` to remove test data

**Next Steps:**
- Explore [Python API Testing Guide](./Python_API_Testing_Guide.md) for advanced patterns
- Learn about [Flask Patterns](./Library-Api_Flask_Patterns_Guide.md) for testable code
- Check [Flask REST API Guide](./Flask_REST_API_Development_Guide.md) for endpoint design

---

**See Also:**
- [Flask Testing Documentation](https://flask.palletsprojects.com/en/latest/testing/)
- [unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [pytest Documentation](https://docs.pytest.org/)
