# Library-Api Advanced Architecture Guide

---

## Quick Reference Card

| Module      | Purpose                        | Key Components                                       |
| ----------- | ------------------------------ | ---------------------------------------------------- |
| **Orders**  | E-commerce style checkout flow | `create_order`, `add_item`, `checkout`               |
| **Items**   | Inventory/Asset management     | `ItemDescription` (Product), `Items` (Instance)      |
| **Auth**    | Security & Role management     | `token_required`, `admin_required` decorators        |
| **Testing** | Automated QA                   | `pytest` (fixtures, parametrization), fast discovery |
| **Docs**    | API Documentation              | `swagger.yaml`, `flask_swagger_ui`                   |

---

## Table of Contents

- [Library-Api Advanced Architecture Guide](#library-api-advanced-architecture-guide)
  - [Quick Reference Card](#quick-reference-card)
  - [Table of Contents](#table-of-contents)
  - [1. Inventory Management Pattern](#1-inventory-management-pattern)
    - [Structure](#structure)
    - [Implementation Analysis](#implementation-analysis)
  - [2. Order Processing Flow](#2-order-processing-flow)
    - [Workflow](#workflow)
    - [Code Structure](#code-structure)
  - [3. Testing Strategy](#3-testing-strategy)
    - [Test Class Structure](#test-class-structure)
  - [4. Security Architecture](#4-security-architecture)
    - [Decorator Pattern](#decorator-pattern)
  - [5. Practice Scenarios](#5-practice-scenarios)

---

## 1. Inventory Management Pattern

**Concept**: Separating the "Product Definition" from the "Physical Instance". This is crucial for tracking individual assets (like library books or warehouse items) that share common attributes.

### Structure

- **ItemDescription**: Holds shared data (Name, Description, SKU, Base Price).
- **Items**: Represents a physical unit. Links back to `ItemDescription`.

### Implementation 
```python
# 1. Create the Definition first
@items_bp.route('/description', methods=['POST'])
def create_item_description():
    # Creates the "Catalog Entry"
    pass

# 2. Add Physical Inventory
@items_bp.route('/<int:description_id>/instance', methods=['POST'])
def create_item(description_id):
    # Creates a specific unit linked to the description
    # Useful for tracking condition or unique serial numbers
    pass
```

**When to Use:**

- When you have multiple copies of the same product.
- When you need to track the status (lost, damaged, borrowed) of individual units.

---

## 2. Order Processing Flow

**Concept**: A transactional flow allowing users to build a cart (Order) and finalize it (Checkout). This differs from the direct "Loan" model by introducing a "Pending" state.

### Workflow

1.  **Create Order**: Initialize a new order session.
2.  **Add Items**: Link specific `Items` or `ItemDescriptions` to the order.
3.  **Checkout**: Finalize the transaction, lock items, and process payment/loan.

### Code Structure

```python
# Step 1: Initialize
def create_order():
    # Creates an Order record with status="Pending"
    pass

# Step 2: Build Cart
def add_item(order_id, description_id):
    # Adds items to the order relationship
    pass

# Step 3: Finalize
def checkout(order_id):
    # 1. Verify stock
    # 2. Update order status to "Completed"
    # 3. Deduct inventory / Assign ownership
    pass
```

---

## 3. Testing Strategy

Concept: Use `pytest` with fixtures for reliable, readable, and fast tests. The project follows a "Arrange -> Act -> Assert" pattern and relies on fixtures for setup/teardown and dependency injection.

**Key Takeaways**

- Use fixtures to keep tests DRY and isolated.
- Prefer small, focused tests that assert behavior rather than implementation details.

### Example: pytest-style tests with fixtures

Use a session-local or function-scoped fixture that creates the app, pushes the app context, and prepares the test database. Tests then receive a `client` fixture and operate with simple `assert` statements.

```python
import pytest
from app import create_app
from app.models import db, Users

@pytest.fixture
def client():
    app = create_app('TestingConfig')
    ctx = app.app_context()
    ctx.push()
    db.create_all()
    client = app.test_client()
    yield client
    db.session.remove()
    db.drop_all()
    ctx.pop()

def test_create_user(client):
    payload = {"username": "test", "email": "test@test.com"}
    resp = client.post('/users', json=payload)
    assert resp.status_code == 201

def test_invalid_create(client):
    resp = client.post('/users', json={})
    assert resp.status_code == 400
```

Key Takeaways:

- Isolation: Fixtures (like `client`) ensure each test runs in a clean state.
- Readability: `pytest` encourages small test functions and direct `assert` statements.
- Parametrization: Use `@pytest.mark.parametrize` to cover many inputs succinctly.

---

## 4. Security Architecture

**Concept**: Role-Based Access Control (RBAC) using JWTs and custom decorators.

### Decorator Pattern

```python
def token_required(f):
    @wraps(f)
    def decoration(*args, **kwargs):
        # 1. Check for Authorization header
        # 2. Decode JWT
        # 3. Attach user info to request
        return f(*args, **kwargs)
    return decoration

def admin_required(f):
    @wraps(f)
    def decoration(*args, **kwargs):
        # 1. Run token_required logic first
        # 2. Check if role == 'Admin'
        if role != 'Admin':
            return jsonify({"message": "Unauthorized"}), 403
        return f(*args, **kwargs)
    return decoration
```
**Useful Links:**

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
