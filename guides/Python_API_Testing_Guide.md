# Python API Testing Guide: TDD & Mocking

This guide covers Test-Driven Development (TDD) principles and implementation using Python's `unittest`, `pytest`, and `faker` libraries.

## Table of Contents
1.  [The TDD Cycle](#the-tdd-cycle)
2.  [Testing Frameworks](#testing-frameworks)
3.  [Generating Fake Data](#generating-fake-data)
4.  [Mocking Dependencies](#mocking-dependencies)

---

## The TDD Cycle

Test-Driven Development follows the **Red-Green-Refactor** cycle:

1.  **Red:** Write a failing test for functionality that doesn't exist yet.
2.  **Green:** Write the *minimum* amount of code required to make the test pass.
3.  **Refactor:** Clean up the code (optimize, deduplicate) while ensuring tests still pass.

---

## Testing Frameworks

### 1. `unittest` (Standard Library)
Class-based testing framework inspired by Java's JUnit.

```python
import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        # Create a test client before each test
        self.app = app.test_client()
    
    def test_sum_endpoint(self):
        payload = {'num1': 10, 'num2': 5}
        response = self.app.post('/sum', json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['result'], 15)

if __name__ == '__main__':
    unittest.main()
```

### 2. `pytest` (Third-Party)
A more concise, powerful framework that supports fixtures and plugins.

```python
import pytest
from app import app

@pytest.fixture
def client():
    # Fixture to provide a test client
    with app.test_client() as client:
        yield client

def test_sum(client):
    payload = {'num1': 2, 'num2': 3}
    response = client.post('/sum', json=payload)
    assert response.get_json()['result'] == 5
```

---

## Generating Fake Data

Use the `Faker` library to generate realistic test data, avoiding hardcoded values.

```python
from faker import Faker

def test_dynamic_sum(client):
    fake = Faker()
    # Generate random numbers
    num1 = fake.random_number(digits=3)
    num2 = fake.random_number(digits=3)
    
    payload = {"num1": num1, "num2": num2}
    response = client.post('/sum', json=payload)
    
    # Assert against the dynamic expected value
    assert response.get_json()['result'] == num1 + num2
```

---

## Mocking Dependencies

Mocking allows you to isolate the code under test by replacing external dependencies (like DB calls or APIs) with simulated objects.

### Using `pytest-mock`

```python
def test_external_api_call(client, mocker):
    # Mock the 'requests.get' method inside 'app.services'
    # Force it to return a specific JSON response
    mock_response = mocker.Mock()
    mock_response.json.return_value = {'id': 1, 'name': 'Mocked User'}
    mock_response.status_code = 200
    
    mocker.patch('app.services.requests.get', return_value=mock_response)

    # Now when the app calls the external API, it gets our mock
    response = client.get('/users/1')
    assert response.get_json()['name'] == 'Mocked User'
```
