# Library-Api Flask Patterns and Best Practices Guide

## Table of Contents
1. [Application Factory Pattern](#application-factory-pattern)
2. [Blueprint Architecture](#blueprint-architecture)
3. [Rate Limiting with Flask-Limiter](#rate-limiting-with-flask-limiter)
4. [Caching with Flask-Caching](#caching-with-flask-caching)
5. [Pagination Implementation](#pagination-implementation)
6. [Marshmallow Schema Validation](#marshmallow-schema-validation)
7. [JWT Authentication Flow](#jwt-authentication-flow)
8. [SQLAlchemy Model Patterns](#sqlalchemy-model-patterns)
9. [Configuration Management](#configuration-management)
10. [Advanced Route Patterns](#advanced-route-patterns)

---

## 1. Application Factory Pattern

### Overview
The application factory pattern creates Flask applications dynamically, allowing for better testing, multiple instances, and environment-specific configurations.

### Implementation

**File: `app/__init__.py`**
```python
from flask import Flask
from .models import db
from .extensions import ma, limiter, cache
from .blueprints.user import users_bp
from .blueprints.books import books_bp
from .blueprints.loans import loans_bp

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')

    # Initialize my extension onto my Flask app
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)

    # Register blueprints
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(books_bp, url_prefix='/books')
    app.register_blueprint(loans_bp, url_prefix='/loans')

    return app
```

**File: `app.py` (Entry Point)**
```python
from app.models import db
from app import create_app

app = create_app('DevelopmentConfig')

with app.app_context():
    db.create_all()  # Creating our database tables

app.run()
```

### Key Benefits
- Environment-specific configuration (Development, Testing, Production)
- Easy testing with multiple app instances
- Clean separation of concerns
- Delayed extension initialization

### Best Practices
1. Initialize extensions outside of the factory function
2. Use `init_app()` pattern for all Flask extensions
3. Register blueprints with URL prefixes for API versioning
4. Use `app.app_context()` for database operations outside request context

---

## 2. Blueprint Architecture

### Overview
Blueprints organize Flask applications into modular components, each handling specific functionality.

### Structure
```
app/
├── blueprints/
│   ├── books/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   ├── loans/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   └── user/
│       ├── __init__.py
│       ├── routes.py
│       └── schemas.py
```

### Implementation

**File: `app/blueprints/books/__init__.py`**
```python
from flask import Blueprint

books_bp = Blueprint('books_bp', __name__)

from . import routes
```

**File: `app/blueprints/books/routes.py`**
```python
from . import books_bp
from .schemas import book_schema, books_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Books, db
from app.extensions import limiter, cache
from sqlalchemy import select

@books_bp.route('', methods=['POST'])
def create_book():
    try:
        data = book_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_book = Books(**data)
    db.session.add(new_book)
    db.session.commit()
    return book_schema.jsonify(new_book), 201
```

### Registration Pattern
```python
# In create_app()
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(books_bp, url_prefix='/books')
app.register_blueprint(loans_bp, url_prefix='/loans')
```

### Best Practices
1. One blueprint per resource/domain
2. Keep routes, schemas, and business logic together
3. Use URL prefixes for API organization
4. Import routes at the end of `__init__.py` to avoid circular imports
5. Name blueprints descriptively with `_bp` suffix

---

## 3. Rate Limiting with Flask-Limiter

### Overview
Flask-Limiter provides rate limiting functionality to protect API endpoints from abuse.

### Configuration

**File: `app/extensions.py`**
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
```

### Usage Patterns

#### 1. Route-Level Rate Limiting
```python
@books_bp.route('/<int:book_id>', methods=['PUT'])
@limiter.limit("30 per hour")
def update_book(book_id):
    # Update logic
    pass

@books_bp.route('/<int:book_id>', methods=['DELETE'])
@limiter.limit("8 per day")
def delete_book(book_id):
    # Delete logic
    pass
```

#### 2. Override Default Limits
```python
@loans_bp.route('/<int:loan_id>/add-book/<int:book_id>', methods=['PUT'])
@limiter.limit("600 per day", override_defaults=True)
def add_book(loan_id, book_id):
    # Logic
    pass
```

#### 3. Login Protection
```python
@users_bp.route('/login', methods=['POST'])
@limiter.limit("5 per 10 minute")
def login():
    # Login logic
    pass
```

#### 4. Profile Access Rate Limiting
```python
@users_bp.route('/profile', methods=['GET'])
@limiter.limit("15 per hour")
@token_required
def read_user():
    # Profile retrieval logic
    pass
```

### Rate Limit Formats
- `"5 per minute"`
- `"10 per hour"`
- `"100 per day"`
- `"5 per 10 minute"` (custom window)

### Best Practices
1. Set global default limits to protect all endpoints
2. Use stricter limits for sensitive operations (login, delete)
3. Use more relaxed limits for read operations
4. Override defaults when specific endpoints need different limits
5. Use `get_remote_address` for identifying clients by IP
6. Consider authenticated user tracking for more granular control

---

## 4. Caching with Flask-Caching

### Overview
Flask-Caching improves API performance by caching expensive operations and database queries.

### Configuration

**File: `app/extensions.py`**
```python
from flask_caching import Cache

cache = Cache()
```

**File: `config.py`**
```python
class DevelopmentConfig:
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300  # 5 minutes
```

### Usage Patterns

#### 1. Route Caching
```python
@books_bp.route('/popularity', methods=['GET'])
@cache.cached(timeout=90)
def get_popular_books():
    books = db.session.query(Books).all()
    books.sort(key=lambda book: len(book.loans), reverse=True)
    # Return popular books
    return jsonify(output), 200
```

#### 2. Important Note on Pagination
```python
@books_bp.route('', methods=['GET'])
# @cache.cached(timeout=90)  # If you cache paginated routes it will cache a single page
def get_books():
    # Pagination logic
    pass
```

### Cache Types
- `SimpleCache`: In-memory cache (development)
- `RedisCache`: Redis-based cache (production)
- `FileSystemCache`: File-based cache
- `MemcachedCache`: Memcached-based cache

### Best Practices
1. Don't cache paginated endpoints (caches only one page)
2. Use shorter timeouts for frequently updated data
3. Cache expensive computations (aggregations, complex queries)
4. Use Redis or Memcached in production
5. Implement cache invalidation for data updates
6. Monitor cache hit rates

---

## 5. Pagination Implementation

### Overview
Pagination limits the amount of data returned per request, improving performance and user experience.

### Implementation

```python
@books_bp.route('', methods=['GET'])
def get_books():
    try:
        page = int(request.args.get('page'))
        per_page = int(request.args.get('per_page'))
        query = select(Books)
        books = db.paginate(query, page=page, per_page=per_page)
        return books_schema.jsonify(books), 200
    except:
        books = db.session.query(Books).all()
        return books_schema.jsonify(books), 200
```

### Usage
```
GET /books?page=1&per_page=10
GET /books?page=2&per_page=20
```

### Key Components
1. **Query Parameters**: `page` and `per_page`
2. **SQLAlchemy Select**: Using `select()` for modern query building
3. **db.paginate()**: Built-in Flask-SQLAlchemy pagination
4. **Fallback**: Returns all items if pagination params missing

### Pagination Response Structure
```python
# db.paginate() returns object with:
# - items: list of records
# - page: current page number
# - per_page: items per page
# - total: total number of items
# - pages: total number of pages
# - has_next: boolean
# - has_prev: boolean
```

### Best Practices
1. Always validate pagination parameters
2. Set reasonable defaults (e.g., per_page=20)
3. Set maximum limits (e.g., max per_page=100)
4. Include pagination metadata in responses
5. Use cursor-based pagination for large datasets
6. Don't cache paginated endpoints

---

## 6. Marshmallow Schema Validation

### Overview
Marshmallow provides object serialization/deserialization and validation for Flask applications.

### Extension Setup

**File: `app/extensions.py`**
```python
from flask_marshmallow import Marshmallow

ma = Marshmallow()
```

### Schema Patterns

#### 1. Basic SQLAlchemy Auto Schema
```python
from app.extensions import ma
from app.models import Books

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Books

book_schema = BookSchema()
books_schema = BookSchema(many=True)
```

#### 2. Schema with Exclusions
```python
from app.extensions import ma
from app.models import Users

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users

user_schema = UserSchema()
users_schema = UserSchema(many=True)
login_schema = UserSchema(exclude=['first_name', 'last_name', 'role'])
```

### Usage Patterns

#### 1. Request Validation (Deserialization)
```python
@books_bp.route('', methods=['POST'])
def create_book():
    try:
        # Validates data and translates JSON to Python dictionary
        data = book_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_book = Books(**data)
    db.session.add(new_book)
    db.session.commit()
    return book_schema.jsonify(new_book), 201
```

#### 2. Response Serialization (Full Response)
```python
@users_bp.route("", methods=["GET"])
def read_users():
    users = db.session.query(Users).all()
    return users_schema.jsonify(users), 200
```

#### 3. Partial Serialization (dump)
```python
@loans_bp.route('/<int:loan_id>/add-book/<int:book_id>', methods=['PUT'])
def add_book(loan_id, book_id):
    loan = db.session.get(Loans, loan_id)
    book = db.session.get(Books, book_id)

    loan.books.append(book)
    db.session.commit()

    return jsonify({
        'message': f'successfully add {book.title} to loan',
        'loan': loan_schema.dump(loan),  # Use dump for partial responses
        'books': books_schema.dump(loan.books)
    }), 200
```

### Serialization Methods
- `schema.load()`: JSON → Python (deserialization + validation)
- `schema.dump()`: Python → Dict (serialization)
- `schema.jsonify()`: Python → JSON Response (serialization + jsonify)

### Best Practices
1. Use `SQLAlchemyAutoSchema` to auto-generate from models
2. Create separate schemas for different use cases (e.g., login_schema)
3. Use `exclude` or `only` for field control
4. Always handle `ValidationError` exceptions
5. Use `many=True` for collections
6. Use `.load()` for incoming data (with validation)
7. Use `.dump()` for partial serialization in complex responses
8. Use `.jsonify()` for simple endpoint responses

---

## 7. JWT Authentication Flow

### Overview
JWT (JSON Web Tokens) provide stateless authentication for API endpoints.

### Configuration

**File: `app/util/auth.py`**
```python
from datetime import datetime, timedelta, timezone
from jose import jwt
import jose
from functools import wraps
from flask import request, jsonify

SECRET_KEY = 'super secret secrets'
```

### Token Generation

```python
def encode_token(user_id, role="user"):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(days=0, hours=1),
        'iat': datetime.now(timezone.utc),
        'sub': str(user_id),  # IMPORTANT: Convert user ID to string
        'role': role
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token
```

### Token Validation Decorator

```python
def token_required(f):
    @wraps(f)
    def decoration(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            # Extract token from "Bearer <token>"
            token = request.headers['Authorization'].split()[1]

        if not token:
            return jsonify({"error": "token missing from authorization headers"}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.logged_in_user_id = data['sub']
        except jose.exceptions.ExpiredSignatureError:
            return jsonify({'message': 'token is expired'}), 403
        except jose.exceptions.JWTError:
            return jsonify({'message': 'invalid token'}), 401

        return f(*args, **kwargs)

    return decoration
```

### Login Flow

```python
@users_bp.route('/login', methods=['POST'])
@limiter.limit("5 per 10 minute")
def login():
    try:
        data = login_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    user = db.session.query(Users).where(Users.email==data['email']).first()

    if user and check_password_hash(user.password, data['password']):
        token = encode_token(user.id, role=user.role)
        return jsonify({
            "message": f"Welcome {user.first_name}",
            "token": token,
        }), 200
```

### Protected Route Example

```python
@users_bp.route('/profile', methods=['GET'])
@limiter.limit("15 per hour")
@token_required
def read_user():
    user_id = request.logged_in_user_id
    user = db.session.get(Users, user_id)
    return user_schema.jsonify(user), 200

@users_bp.route("", methods=["DELETE"])
@token_required
def delete_user():
    token_id = request.logged_in_user_id
    user = db.session.get(Users, token_id)

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"Successfully deleted user {token_id}"}), 200
```

### Password Hashing

```python
from werkzeug.security import generate_password_hash, check_password_hash

# During registration
data["password"] = generate_password_hash(data["password"])

# During login
if user and check_password_hash(user.password, data['password']):
    # Login success
    pass
```

### JWT Payload Structure
```json
{
  "exp": 1763518014,      // Expiration timestamp
  "iat": 1763514414,      // Issued at timestamp
  "sub": "1",             // Subject (user ID as string)
  "role": "Admin"         // Custom claim (user role)
}
```

### Authorization Header Format
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjM1MTgwMTQsImlhdCI6MTc2MzUxNDQxNCwic3ViIjoiMSIsInJvbGUiOiJBZG1pbiJ9.2gEKkaU_LEQAxEPbj5734khp4k6jKMgJQsayui70iPw
```

### Best Practices
1. Use strong, random SECRET_KEY (store in environment variables)
2. Set reasonable token expiration times (1-24 hours)
3. Always convert user_id to string in payload
4. Store user_id in request object for easy access
5. Combine rate limiting with authentication
6. Use HTTPS in production to protect tokens
7. Implement token refresh mechanism for long sessions
8. Hash passwords with werkzeug.security
9. Handle all JWT exceptions properly
10. Don't store sensitive data in JWT payload

---

## 8. SQLAlchemy Model Patterns

### Overview
Modern SQLAlchemy 2.0+ patterns using Mapped types and declarative base.

### Base Configuration

**File: `app/models.py`**
```python
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Date, Column, ForeignKey, Table
from datetime import date, datetime, timedelta

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
```

### Model Patterns

#### 1. Many-to-Many Association Table
```python
loan_books = Table(
    'loan_books',
    Base.metadata,
    Column('loan_id', ForeignKey('loans.id')),
    Column('book_id', ForeignKey('books.id'))
)
```

#### 2. User Model with Relationships
```python
class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(250), nullable=False)
    last_name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(350), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(150), nullable=False)
    DOB: Mapped[date] = mapped_column(Date, nullable=True)
    address: Mapped[str] = mapped_column(String(500), nullable=True)
    role: Mapped[str] = mapped_column(String(30), nullable=False)

    loans: Mapped[list['Loans']] = relationship('Loans', back_populates='user')
```

#### 3. Loans Model with Foreign Keys
```python
class Loans(Base):
    __tablename__ = 'loans'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    loan_date: Mapped[date] = mapped_column(Date, default=datetime.now())
    deadline: Mapped[date] = mapped_column(Date, default=datetime.now() + timedelta(days=14))
    return_date: Mapped[date] = mapped_column(Date, nullable=True)

    user: Mapped['Users'] = relationship('Users', back_populates='loans')
    books: Mapped[list['Books']] = relationship("Books", secondary=loan_books, back_populates='loans')
```

#### 4. Books Model with Secondary Relationship
```python
class Books(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    genre: Mapped[str] = mapped_column(String(360), nullable=False)
    age_category: Mapped[str] = mapped_column(String(120), nullable=False)
    publish_date: Mapped[date] = mapped_column(Date, nullable=False)
    author: Mapped[str] = mapped_column(String(500), nullable=False)

    loans: Mapped[list['Loans']] = relationship("Loans", secondary=loan_books, back_populates='books')
```

### Database Operations

#### 1. Create
```python
new_book = Books(**data)
db.session.add(new_book)
db.session.commit()
```

#### 2. Read (Query All)
```python
books = db.session.query(Books).all()
```

#### 3. Read (Query by ID)
```python
book = db.session.get(Books, book_id)
```

#### 4. Read (Query with Filter)
```python
user = db.session.query(Users).where(Users.email==data['email']).first()
```

#### 5. Update
```python
book = db.session.get(Books, book_id)
for key, value in data.items():
    setattr(book, key, value)
db.session.commit()
```

#### 6. Delete
```python
book = db.session.get(Books, book_id)
db.session.delete(book)
db.session.commit()
```

#### 7. Many-to-Many Operations
```python
# Add relationship
loan.books.append(book)
db.session.commit()

# Remove relationship
loan.books.remove(book)
db.session.commit()

# Check relationship
if book in loan.books:
    # Book is in loan
    pass
```

### Best Practices
1. Use `Mapped[]` type hints for type safety
2. Use `mapped_column()` instead of `Column()`
3. Define relationships with `back_populates` for bidirectional access
4. Use association tables for many-to-many relationships
5. Set appropriate `nullable`, `unique`, and `default` constraints
6. Use `db.session.get()` for queries by primary key
7. Use `.where()` instead of `.filter()` in modern SQLAlchemy
8. Always commit after modifications
9. Use `datetime.now()` for timestamp defaults
10. Define `__tablename__` explicitly

---

## 9. Configuration Management

### Overview
Environment-specific configuration classes for different deployment stages.

### Configuration Pattern

**File: `config.py`**
```python
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    DEBUG = True
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300

class TestingConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    TESTING = True
    CACHE_TYPE = "SimpleCache"

class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:pass@localhost/dbname'
    DEBUG = False
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_URL = "redis://localhost:6379/0"
```

### Loading Configuration
```python
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    # ...
```

### Common Configuration Options
- `SQLALCHEMY_DATABASE_URI`: Database connection string
- `DEBUG`: Enable/disable debug mode
- `TESTING`: Enable testing mode
- `SECRET_KEY`: Secret key for sessions/JWT
- `CACHE_TYPE`: Cache backend type
- `CACHE_DEFAULT_TIMEOUT`: Default cache timeout in seconds
- `SQLALCHEMY_TRACK_MODIFICATIONS`: Track model changes (usually False)

### Best Practices
1. Use environment variables for secrets
2. Create separate configs for dev, test, prod
3. Never commit sensitive data to version control
4. Use SQLite for development, PostgreSQL for production
5. Disable debug mode in production
6. Use Redis cache in production
7. Set proper cache timeouts per environment

---

## 10. Advanced Route Patterns

### Overview
Common patterns for building robust REST API endpoints.

### 1. CRUD Operations

#### Create
```python
@books_bp.route('', methods=['POST'])
def create_book():
    try:
        data = book_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_book = Books(**data)
    db.session.add(new_book)
    db.session.commit()
    return book_schema.jsonify(new_book), 201
```

#### Read (List)
```python
@books_bp.route('', methods=['GET'])
def get_books():
    books = db.session.query(Books).all()
    return books_schema.jsonify(books), 200
```

#### Read (Single)
```python
@books_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = db.session.get(Books, book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return book_schema.jsonify(book), 200
```

#### Update
```python
@books_bp.route('/<int:book_id>', methods=['PUT'])
@limiter.limit("30 per hour")
def update_book(book_id):
    book = db.session.get(Books, book_id)

    if not book:
        return jsonify("Invalid book_id"), 404

    try:
        data = book_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    for key, value in data.items():
        setattr(book, key, value)

    db.session.commit()
    return book_schema.jsonify(book), 200
```

#### Delete
```python
@books_bp.route('/<int:book_id>', methods=['DELETE'])
@limiter.limit("8 per day")
def delete_book(book_id):
    book = db.session.get(Books, book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify(f"Successfully deleted book {book_id}")
```

### 2. Search Pattern
```python
@books_bp.route('/search', methods=['GET'])
def search_books():
    title = request.args.get('title')
    books = db.session.query(Books).where(Books.title.ilike(f"%{title}%")).all()
    return books_schema.jsonify(books), 200
```

### 3. Aggregation Pattern (Popular Books)
```python
@books_bp.route('/popularity', methods=['GET'])
def get_popular_books():
    books = db.session.query(Books).all()

    # Sort by relationship count
    books.sort(key=lambda book: len(book.loans), reverse=True)

    output = []
    for book in books[:5]:
        book_format = {
            "book": book_schema.dump(book),
            "readers": len(book.loans)
        }
        output.append(book_format)

    return jsonify(output), 200
```

### 4. Nested Resource Pattern
```python
@loans_bp.route('/<int:loan_id>/add-book/<int:book_id>', methods=['PUT'])
@limiter.limit("600 per day", override_defaults=True)
def add_book(loan_id, book_id):
    loan = db.session.get(Loans, loan_id)
    book = db.session.get(Books, book_id)

    if book not in loan.books:
        loan.books.append(book)
        db.session.commit()
        return jsonify({
            'message': f'successfully add {book.title} to loan',
            'loan': loan_schema.dump(loan),
            'books': books_schema.dump(loan.books)
        }), 200

    return jsonify("This book is already on the loan"), 400
```

### 5. Dynamic Query with Fallback
```python
@books_bp.route('', methods=['GET'])
def get_books():
    try:
        page = int(request.args.get('page'))
        per_page = int(request.args.get('per_page'))
        query = select(Books)
        books = db.paginate(query, page=page, per_page=per_page)
        return books_schema.jsonify(books), 200
    except:
        books = db.session.query(Books).all()
        return books_schema.jsonify(books), 200
```

### HTTP Status Code Guide
- `200 OK`: Successful GET, PUT, DELETE
- `201 Created`: Successful POST
- `400 Bad Request`: Validation error
- `401 Unauthorized`: Missing/invalid authentication
- `403 Forbidden`: Expired token, insufficient permissions
- `404 Not Found`: Resource doesn't exist
- `500 Internal Server Error`: Server error

### Best Practices
1. Use appropriate HTTP methods (GET, POST, PUT, DELETE)
2. Return correct HTTP status codes
3. Validate all input data with Marshmallow
4. Handle errors gracefully
5. Use dynamic URL parameters for resource IDs
6. Implement proper error messages
7. Use query parameters for filtering/pagination
8. Combine decorators (limiter, auth) in correct order
9. Use `ilike()` for case-insensitive search
10. Implement relationship checks before modifications

---

## Dependencies

**File: `requirements.txt`**
```
Flask==3.1.2
Flask-SQLAlchemy==3.1.1
Flask-Limiter==4.0.0
Flask-Caching==2.3.1
flask-marshmallow==1.3.0
marshmallow-sqlalchemy==1.4.2
python-jose==3.5.0
Werkzeug==3.1.3
SQLAlchemy==2.0.44
```

---

## Project Structure Summary

```
library-api/
├── app/
│   ├── __init__.py              # Application factory
│   ├── models.py                # SQLAlchemy models
│   ├── extensions.py            # Extension initialization
│   ├── blueprints/
│   │   ├── books/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── schemas.py
│   │   ├── loans/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── schemas.py
│   │   └── user/
│   │       ├── __init__.py
│   │       ├── routes.py
│   │       └── schemas.py
│   └── util/
│       └── auth.py              # JWT utilities
├── app.py                       # Entry point
├── config.py                    # Configuration classes
└── requirements.txt             # Dependencies
```

---

## Quick Reference

### Extension Initialization Pattern
```python
# In extensions.py
extension = Extension()

# In create_app()
extension.init_app(app)
```

### Blueprint Pattern
```python
# In blueprint __init__.py
bp = Blueprint('name', __name__)
from . import routes

# In create_app()
app.register_blueprint(bp, url_prefix='/prefix')
```

### Protected Route Pattern
```python
@bp.route('/endpoint', methods=['POST'])
@limiter.limit("10 per hour")
@token_required
def protected_endpoint():
    user_id = request.logged_in_user_id
    # Logic here
```

### Validation Pattern
```python
try:
    data = schema.load(request.json)
except ValidationError as e:
    return jsonify(e.messages), 400
```

---

## See Also

### Foundation Concepts
- [Flask REST API Development Guide](./Flask_REST_API_Development_Guide.md) - Basic Flask API patterns and fundamentals
- [SQL & SQLAlchemy](./SQL_and_SQLAlchemy_Cheat_Sheet.md) - Database fundamentals and basic ORM operations

### Advanced Patterns
- [Flask Advanced Features Guide](./Flask_Advanced_Features_Guide.md) - Detailed coverage of rate limiting, caching, pagination, and production patterns
- [SQLAlchemy Relationships Guide](./SQLAlchemy_Relationships_Guide.md) - Understanding relationship patterns and configurations
- [SQLAlchemy Advanced Patterns Guide](./SQLAlchemy_Advanced_Patterns_Guide.md) - Session management, query optimization, and production best practices

### Authentication & Security
- [API Authentication Guide](./API_Authentication_Guide.md) - Authentication strategies and security patterns
- [OAuth2 and Token Management Guide](./OAuth2_and_Token_Management_Guide.md) - OAuth2 flows and token lifecycle management
- [Error Handling Cheat Sheet](./Error_Handling_Cheat_Sheet.md) - Exception handling and error management

### Related Topics
- [Library-Api Patterns Summary](./Library-Api_Patterns_Summary.md) - Quick reference summary of patterns in this guide
- [Python CLI Applications Guide](./Python_CLI_Applications_Guide.md) - Building CLI applications with similar patterns
- [Testing and Debugging Cheat Sheet](./Testing_and_Debugging_Cheat_Sheet.md) - Testing Flask applications

[Back to Main](./README.md)
