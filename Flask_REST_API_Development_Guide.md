# Flask REST API Development Guide

## Quick Reference Card

| Component | Purpose | Example |
|-----------|---------|---------|
| Flask app factory | Create configurable app | `create_app(config_name)` |
| Blueprint | Organize routes | `users_bp = Blueprint('users', __name__)` |
| Route decorator | Define endpoint | `@users_bp.route('/users', methods=['POST'])` |
| Request data | Get JSON payload | `data = request.get_json()` |
| Marshmallow schema | Validate/serialize | `user_schema.load(data)` |
| SQLAlchemy model | Database table | `class User(db.Model):` |
| CRUD operations | Create, Read, Update, Delete | See examples below |
| JSON response | Return data | `jsonify(user_schema.dump(user))` |
| Error handling | Return errors | `return jsonify({'error': 'message'}), 400` |
| Database session | Commit changes | `db.session.commit()` |

**HTTP Status Codes:** 200 (OK), 201 (Created), 400 (Bad Request), 404 (Not Found), 500 (Server Error)

## Table of Contents
1. [Project Structure](#project-structure)
2. [Flask Application Factory Pattern](#flask-application-factory-pattern)
3. [Database Configuration](#database-configuration)
4. [SQLAlchemy Models](#sqlalchemy-models)
5. [Marshmallow Schemas](#marshmallow-schemas)
6. [Blueprints](#blueprints)
7. [CRUD Operations](#crud-operations)
8. [Error Handling](#error-handling)
9. [Testing Your API](#testing-your-api)
10. [Best Practices](#best-practices)

---

## Project Structure

### Recommended Flask API Structure
```
library-api/
├── app.py                      # Entry point
├── config.py                   # Configuration classes
├── requirements.txt            # Dependencies
├── app/
│   ├── __init__.py            # App factory
│   ├── models.py              # Database models
│   ├── extensions.py          # Flask extensions
│   └── blueprints/
│       └── user/
│           ├── __init__.py    # Blueprint registration
│           ├── routes.py      # Route handlers
│           └── schemas.py     # Marshmallow schemas
```

### Why This Structure?
```python
# Benefits:
# - Separation of concerns
# - Easy to test
# - Scalable (add new blueprints easily)
# - Configuration management
# - Reusable components
```

---

## Flask Application Factory Pattern

### Creating the App Factory
```python
# app/__init__.py
from flask import Flask
from .models import db
from .extensions import ma
from .blueprints.user import users_bp

def create_app(config_name):
    """
    Application factory pattern
    Creates and configures the Flask app
    """
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(f'config.{config_name}')

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    # Register blueprints
    app.register_blueprint(users_bp, url_prefix='/api')

    # Create tables
    with app.app_context():
        db.create_all()

    return app
```

### Entry Point
```python
# app.py
from app.models import db
from app import create_app

app = create_app('DevelopmentConfig')

if __name__ == '__main__':
    app.run(debug=True)
```

### Benefits of App Factory
```python
# 1. Multiple configurations
dev_app = create_app('DevelopmentConfig')
test_app = create_app('TestingConfig')
prod_app = create_app('ProductionConfig')

# 2. Easy testing
def test_something():
    app = create_app('TestingConfig')
    with app.test_client() as client:
        response = client.get('/api/users')
        assert response.status_code == 200

# 3. Avoid circular imports
# Extensions initialized separately from app creation
```

---

## Database Configuration

### Configuration Classes
```python
# config.py
import os

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///library_dev.db'

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///library_test.db'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
```

### Extensions Setup
```python
# app/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize extensions (without app)
db = SQLAlchemy()
ma = Marshmallow()
```

---

## SQLAlchemy Models

### Basic Model
```python
# app/models.py
from .extensions import db
from datetime import datetime

class User(db.Model):
    """User model"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'
```

### Model with Relationships
```python
class Book(db.Model):
    """Book model"""
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(13), unique=True)
    available = db.Column(db.Boolean, default=True)

    # Relationship to loans
    loans = db.relationship('Loan', backref='book', lazy=True)

class Loan(db.Model):
    """Loan model (links users and books)"""
    __tablename__ = 'loans'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    loan_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime, nullable=True)

    # Relationships
    user = db.relationship('User', backref='loans')
```

---

## Marshmallow Schemas

### Basic Schema
```python
# app/blueprints/user/schemas.py
from app.extensions import ma
from app.models import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    """User schema for serialization/deserialization"""

    class Meta:
        model = User
        load_instance = True
        include_fk = True

# Create schema instances
user_schema = UserSchema()        # For single user
users_schema = UserSchema(many=True)  # For multiple users
```

### Schema with Validation
```python
from marshmallow import fields, validates, ValidationError

class UserSchema(ma.SQLAlchemyAutoSchema):
    """User schema with validation"""

    # Custom fields
    email = fields.Email(required=True)
    age = fields.Integer(required=False)

    class Meta:
        model = User
        load_instance = True

    @validates('age')
    def validate_age(self, value):
        """Validate age is positive"""
        if value < 0 or value > 150:
            raise ValidationError('Age must be between 0 and 150')

    @validates('email')
    def validate_email(self, value):
        """Validate email is unique"""
        existing = User.query.filter_by(email=value).first()
        if existing:
            raise ValidationError('Email already exists')
```

### Nested Schemas
```python
class LoanSchema(ma.SQLAlchemyAutoSchema):
    """Loan schema with nested user and book"""

    class Meta:
        model = Loan
        include_fk = True

    # Nested schemas
    user = fields.Nested(UserSchema)
    book = fields.Nested(BookSchema)

# Usage
loan_schema = LoanSchema()
result = loan_schema.dump(loan)
# Returns: {'id': 1, 'user': {'id': 1, 'name': 'Alice'}, 'book': {'id': 1, 'title': '1984'}}
```

---

## Blueprints

### Creating a Blueprint
```python
# app/blueprints/user/__init__.py
from flask import Blueprint

users_bp = Blueprint('users', __name__)

from . import routes  # Import routes after blueprint creation
```

### Registering Blueprints
```python
# app/__init__.py
from .blueprints.user import users_bp

def create_app(config_name):
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(users_bp, url_prefix='/api/users')

    return app
```

### Blueprint Structure
```python
# Why use blueprints?
# 1. Organize routes by resource
#    - /api/users -> users_bp
#    - /api/books -> books_bp
#    - /api/loans -> loans_bp

# 2. Reusable across projects
# 3. Easy to add/remove features
# 4. Better testing
```

---

## CRUD Operations

### CREATE - POST Request
```python
# app/blueprints/user/routes.py
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import User, db
from app.blueprints.user import users_bp
from .schemas import user_schema, users_schema

@users_bp.route('', methods=['POST'])
def create_user():
    """
    Create a new user
    POST /api/users
    Body: {"first_name": "John", "last_name": "Doe", "email": "john@example.com"}
    """
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate and deserialize input data
        new_user = user_schema.load(data)

        # Add to database
        db.session.add(new_user)
        db.session.commit()

        # Return created user
        return jsonify(user_schema.dump(new_user)), 201

    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
```

### READ - GET Requests
```python
@users_bp.route('', methods=['GET'])
def read_users():
    """
    Get all users
    GET /api/users
    """
    users = User.query.all()
    return jsonify(users_schema.dump(users)), 200

@users_bp.route('/<int:user_id>', methods=['GET'])
def read_user(user_id):
    """
    Get a single user by ID
    GET /api/users/1
    """
    user = User.query.get_or_404(user_id)
    return jsonify(user_schema.dump(user)), 200
```

### UPDATE - PUT/PATCH Requests
```python
@users_bp.route('/<int:user_id>', methods=['PUT', 'PATCH'])
def update_user(user_id):
    """
    Update a user
    PUT /api/users/1
    Body: {"first_name": "Jane", "email": "jane@example.com"}
    """
    try:
        # Get user from database
        user = User.query.get_or_404(user_id)

        # Get update data
        data = request.get_json()

        # Validate and update
        updated_user = user_schema.load(data, instance=user, partial=True)

        # Commit changes
        db.session.commit()

        return jsonify(user_schema.dump(updated_user)), 200

    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
```

### DELETE - DELETE Request
```python
@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user
    DELETE /api/users/1
    """
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': f'User {user_id} deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
```

---

## Error Handling

### Global Error Handlers
```python
# app/__init__.py
def create_app(config_name):
    app = Flask(__name__)

    # ... other setup ...

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'error': 'Bad request'}), 400

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return jsonify({'error': 'Internal server error'}), 500

    return app
```

### Custom Exceptions
```python
class APIException(Exception):
    """Base API exception"""
    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

class ResourceNotFound(APIException):
    """Resource not found exception"""
    status_code = 404

class ValidationFailed(APIException):
    """Validation failed exception"""
    status_code = 400

# Register exception handler
@app.errorhandler(APIException)
def handle_api_exception(error):
    response = {
        'error': error.message,
        'status_code': error.status_code
    }
    return jsonify(response), error.status_code
```

---

## Testing Your API

### Using Postman
```python
# Example Postman requests:

# 1. Create User (POST)
# URL: http://localhost:5000/api/users
# Method: POST
# Headers: Content-Type: application/json
# Body:
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com"
}

# 2. Get All Users (GET)
# URL: http://localhost:5000/api/users
# Method: GET

# 3. Get Single User (GET)
# URL: http://localhost:5000/api/users/1
# Method: GET

# 4. Update User (PUT)
# URL: http://localhost:5000/api/users/1
# Method: PUT
# Body:
{
    "email": "newemail@example.com"
}

# 5. Delete User (DELETE)
# URL: http://localhost:5000/api/users/1
# Method: DELETE
```

### Using Python Requests
```python
import requests

BASE_URL = 'http://localhost:5000/api/users'

# Create user
data = {
    'first_name': 'Alice',
    'last_name': 'Smith',
    'email': 'alice@example.com'
}
response = requests.post(BASE_URL, json=data)
print(response.json())

# Get all users
response = requests.get(BASE_URL)
print(response.json())

# Get single user
user_id = 1
response = requests.get(f'{BASE_URL}/{user_id}')
print(response.json())

# Update user
updates = {'email': 'newemail@example.com'}
response = requests.put(f'{BASE_URL}/{user_id}', json=updates)
print(response.json())

# Delete user
response = requests.delete(f'{BASE_URL}/{user_id}')
print(response.json())
```

### Unit Testing
```python
import unittest
from app import create_app
from app.models import db, User

class UserTestCase(unittest.TestCase):
    """Test case for User API"""

    def setUp(self):
        """Set up test client and database"""
        self.app = create_app('TestingConfig')
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """Clean up after tests"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user(self):
        """Test creating a user"""
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com'
        }
        response = self.client.post('/api/users', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('email', response.json)

    def test_get_users(self):
        """Test getting all users"""
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
```

---

## Best Practices

### 1. Use Environment Variables
```python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
```

### 2. Pagination for Large Datasets
```python
@users_bp.route('', methods=['GET'])
def read_users():
    """Get users with pagination"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    pagination = User.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return jsonify({
        'users': users_schema.dump(pagination.items),
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    }), 200
```

### 3. Input Validation
```python
@users_bp.route('', methods=['POST'])
def create_user():
    """Create user with validation"""
    data = request.get_json()

    # Validate required fields
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    required_fields = ['first_name', 'last_name', 'email']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    # Use schema validation
    try:
        new_user = user_schema.load(data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(user_schema.dump(new_user)), 201
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
```

### 4. Database Transactions
```python
@users_bp.route('/batch', methods=['POST'])
def create_batch_users():
    """Create multiple users in a transaction"""
    try:
        users_data = request.get_json()
        new_users = []

        for user_data in users_data:
            user = user_schema.load(user_data)
            db.session.add(user)
            new_users.append(user)

        # Commit all or none
        db.session.commit()

        return jsonify(users_schema.dump(new_users)), 201

    except Exception as e:
        db.session.rollback()  # Rollback if any error
        return jsonify({'error': str(e)}), 500
```

### 5. API Versioning
```python
# app/__init__.py
def create_app(config_name):
    app = Flask(__name__)

    # Version 1
    app.register_blueprint(users_bp_v1, url_prefix='/api/v1/users')

    # Version 2
    app.register_blueprint(users_bp_v2, url_prefix='/api/v2/users')

    return app
```

### 6. CORS Configuration
```python
from flask_cors import CORS

def create_app(config_name):
    app = Flask(__name__)

    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    return app
```

---

## Complete Example: Library API

### Requirements
```txt
Flask==2.3.0
Flask-SQLAlchemy==3.0.3
Flask-Marshmallow==0.15.0
marshmallow-sqlalchemy==0.29.0
python-dotenv==1.0.0
```

### Project Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### API Endpoints Summary
```
POST   /api/users          - Create a new user
GET    /api/users          - Get all users
GET    /api/users/<id>     - Get a specific user
PUT    /api/users/<id>     - Update a user
DELETE /api/users/<id>     - Delete a user

POST   /api/books          - Create a new book
GET    /api/books          - Get all books
GET    /api/books/<id>     - Get a specific book
PUT    /api/books/<id>     - Update a book
DELETE /api/books/<id>     - Delete a book

POST   /api/loans          - Create a loan
GET    /api/loans          - Get all loans
PUT    /api/loans/<id>     - Return a book
```

---

## See Also

- **[APIs and Requests Cheat Sheet](./APIs_and_Requests_Cheat_Sheet.md)** - HTTP methods and requests
- **[SQL and SQLAlchemy Cheat Sheet](./SQL_and_SQLAlchemy_Cheat_Sheet.md)** - Database operations
- **[OOP Cheat Sheet](./OOP_Cheat_Sheet.md)** - Classes for models and schemas
- **[Error Handling Cheat Sheet](./Error_Handling_Cheat_Sheet.md)** - Exception handling
- **[Testing and Debugging Cheat Sheet](./Testing_and_Debugging_Cheat_Sheet.md)** - Testing your API

---

## Summary

Flask REST API development combines multiple concepts:
- **App Factory Pattern** for flexible configuration
- **Blueprints** for organizing routes by resource
- **SQLAlchemy** for database operations
- **Marshmallow** for serialization and validation
- **CRUD operations** for complete resource management
- **Error handling** for robust applications
- **Testing** for reliable code

---