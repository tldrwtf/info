# Library-Api Advanced Architecture Guide

---

## Quick Reference Card

| Module | Purpose | Key Components |
|--------|---------|----------------|
| **Orders** | E-commerce style checkout flow | `create_order`, `add_item`, `checkout` |
| **Items** | Inventory/Asset management | `ItemDescription` (Product), `Items` (Instance) |
| **Auth** | Security & Role management | `token_required`, `admin_required` decorators |
| **Testing** | Automated QA | `unittest.TestCase`, `setUp`, Negative Testing |
| **Docs** | API Documentation | `swagger.yaml`, `flask_swagger_ui` |

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

### Implementation Analysis
*Inferred from `app/blueprints/items/routes.py`*

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
*Based on `app/blueprints/orders/routes.py`*

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

**Concept**: Using `unittest` to ensure API reliability. The project follows a strict "Setup -> Execute -> Assert" pattern.

### Test Class Structure
*Analysis of [tests/test_users.py](./library_api_code/tests/test_users.py)*

```python
import unittest
from app import create_app

class TestUsers(unittest.TestCase):
    
    def setUp(self):
        # Runs BEFORE every single test method
        # 1. Create a fresh app instance
        # 2. Create a temporary database
        # 3. Push app context
        self.app = create_app('TestingConfig')
        self.client = self.app.test_client()
        
    def test_create_user(self):
        # Positive Test: Should succeed
        payload = {"username": "test", "email": "test@test.com"}
        response = self.client.post('/users', json=payload)
        self.assertEqual(response.status_code, 201)

    def test_invalid_create(self):
        # Negative Test: Should fail gracefully
        payload = {} # Missing data
        response = self.client.post('/users', json=payload)
        self.assertEqual(response.status_code, 400)
```

**Key Takeaways:**
- **Isolation**: Every test starts with a clean state (`setUp`).
- **Coverage**: Tests cover both Success (201) and Failure (400/401) scenarios.
- **Naming**: All test methods must start with `test_`.

---

## 4. Security Architecture

**Concept**: Role-Based Access Control (RBAC) using JWTs and custom decorators.

### Decorator Pattern
*From [app/util/auth.py](./library_api_code/app/util/auth.py)*

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

---

## 5. Practice Scenarios

The repository includes specific challenges (`mechanic.txt`) to test your understanding. Try implementing these:

1.  **Customer Search**: Create a route to search for a user by email (`GET /users/search?email=...`).
2.  **Analytics Endpoint**: Find which staff member (e.g., Mechanic/Librarian) has processed the most tickets/loans.
3.  **Pagination Upgrade**: Convert an existing "List All" route (like `get_tickets`) to use pagination parameters (`page`, `per_page`).

**Goal**: These tasks reinforce the use of **Query Parameters**, **Aggregation Queries**, and **Pagination Logic**.

**Solutions:**
- [Mechanic Shop Solutions](./Practice_Solutions/Mechanic_Shop_Solutions.py)
- [Inventory & Order Solutions](./Practice_Solutions/Inventory_Order_Solutions.py)

**Useful Links:**
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)