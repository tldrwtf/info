# Flask REST API Development Guide

## Quick Reference Card

| Component | Purpose | Example |
|-----------|---------|---------|
| **App Factory** | Create configurable app instance | `create_app(config_name)` |
| **Blueprint** | Organize routes & views | `bp = Blueprint('name', __name__)` |
| **Model** | Database table definition | `class User(db.Model):` |
| **Schema** | Serialization/Validation | `class UserSchema(ma.SQLAlchemyAutoSchema):` |
| **Route** | Define API endpoint | `@bp.route('/users', methods=['POST'])` |
| **Request** | Access incoming data | `request.get_json()` |
| **Response** | Return data to client | `jsonify(data), 200` |
| **Session** | Database transaction | `db.session.add(obj); db.session.commit()` |

## Table of Contents

1. [Project Structure](#project-structure)
2. [Application Factory Pattern](#application-factory-pattern)
3. [Blueprints & modularity](#blueprints--modularity)
4. [Database Models (SQLAlchemy)](#database-models-sqlalchemy)
5. [Schemas (Marshmallow)](#schemas-marshmallow)
6. [Routes & Controllers](#routes--controllers)
7. [Authentication (JWT)](#authentication-jwt)
8. [Rate Limiting & Caching](#rate-limiting--caching)
9. [Documentation (Swagger/OpenAPI)](#documentation-swaggeropenapi)
10. [Configuration Management](#configuration-management)

---

## Project Structure

A production-ready Flask application should be modular. Here is the standard structure used in our **Library API**:

```
project/
├── app/
│   ├── __init__.py            # Application Factory
│   ├── extensions.py          # Initialize db, ma, limiter, etc.
│   ├── models.py              # SQLAlchemy Models
│   ├── util/
│   │   └── auth.py            # Authentication decorators
│   ├── blueprints/
│   │   ├── user/
│   │   │   ├── __init__.py    # Blueprint setup
│   │   │   ├── routes.py      # Route logic
│   │   │   └── schemas.py     # Marshmallow schemas
│   │   ├── books/
│   │   ├── loans/
│   │   └── ...
│   └── static/
│       └── swagger.yaml       # API Documentation
├── config.py                  # Environment configurations
├── app.py                     # Entry point
└── requirements.txt           # Dependencies
```

---

## Application Factory Pattern

Instead of creating a global `app` object, we use a function to create it. This allows for easier testing and multiple configurations.

```python
# app/__init__.py
from flask import Flask
from .models import db
from .extensions import ma, limiter, cache
from .blueprints.user import users_bp
# ... import other blueprints

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')

    # Initialize Extensions
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)

    # Register Blueprints
    app.register_blueprint(users_bp, url_prefix='/users')
    # ... register others

    return app
```

---

## Blueprints & Modularity

Blueprints allow you to organize your application into distinct components.

```python
# app/blueprints/user/__init__.py
from flask import Blueprint

users_bp = Blueprint('users_bp', __name__)

from . import routes
```

### Organizing Routes
Routes are defined within the blueprint, keeping `app/__init__.py` clean.

```python
# app/blueprints/user/routes.py
from . import users_bp
from flask import request, jsonify

@users_bp.route('/login', methods=['POST'])
def login():
    # Login logic here
    pass
```

---

## Database Models (SQLAlchemy)

Define your data structure using SQLAlchemy models. Use relationships to link tables.

```python
# app/models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Users(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(350), unique=True, nullable=False)
    
    # Relationships
    orders: Mapped[list['Orders']] = relationship('Orders', back_populates='user')
```

---

## Schemas (Marshmallow)

Marshmallow is used for:
1.  **Serialization**: Converting Objects -> JSON (for responses).
2.  **Deserialization**: Converting JSON -> Objects (for requests).
3.  **Validation**: Ensuring input data is correct.

```python
# app/blueprints/user/schemas.py
from app.extensions import ma
from app.models import Users

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_instance = True # Optional: deserialize directly to model instance

user_schema = UserSchema()
users_schema = UserSchema(many=True)
login_schema = UserSchema(only=['email', 'password']) # Partial schema
```

---

## Routes & Controllers

The core logic of your API.

### Creating Data (POST)
```python
@books_bp.route('', methods=['POST'])
def create_book():
    try:
        # 1. Deserialize & Validate
        data = book_schema.load(request.json) 
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    # 2. Create Object
    new_book = Books(**data)
    
    # 3. Save to DB
    db.session.add(new_book)
    db.session.commit()
    
    # 4. Return Response
    return book_schema.jsonify(new_book), 201
```

### Reading Data (GET) with Pagination
```python
@books_bp.route('', methods=['GET'])
def get_books():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Use SQLAlchemy paginate
    pagination = db.select(Books).paginate(page=page, per_page=per_page)
    
    return books_schema.jsonify(pagination.items), 200
```

---

## Authentication (JWT)

Secure your API using JSON Web Tokens (JWT).

### 1. Generating Tokens
```python
# app/util/auth.py
import jwt
from datetime import datetime, timedelta, timezone

def encode_token(user_id, role="user"):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1),
        'iat': datetime.now(timezone.utc),
        'sub': str(user_id),
        'role': role
    }
    return jwt.encode(payload, 'SECRET_KEY', algorithm='HS256')
```

### 2. Protecting Routes (Decorator)
```python
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            # Format: "Bearer <token>"
            token = request.headers['Authorization'].split()[1]
        
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
            
        try:
            data = jwt.decode(token, 'SECRET_KEY', algorithms=['HS256'])
            request.logged_in_user_id = data['sub'] # Pass user ID to route
        except:
            return jsonify({'message': 'Token is invalid'}), 401
            
        return f(*args, **kwargs)
    return decorated
```

---

## Rate Limiting & Caching

Use `Flask-Limiter` and `Flask-Caching` to optimize and protect your API.

### Rate Limiting
Prevent abuse by limiting requests.
```python
# Global limit in extensions.py
limiter = Limiter(key_func=get_remote_address, default_limits=["200 per day"])

# Route-specific limit
@users_bp.route('/login', methods=['POST'])
@limiter.limit("5 per 10 minute")
def login():
    # ...
```

### Caching
Cache expensive GET requests to improve performance.
```python
@books_bp.route('', methods=['GET'])
@cache.cached(timeout=60) # Cache result for 60 seconds
def get_books():
    # ... expensive database query ...
```

---

## Documentation (Swagger/OpenAPI)

Use `flask-swagger-ui` to serve standard OpenAPI documentation.

1.  Create `static/swagger.yaml` following OpenAPI 2.0 or 3.0 specs.
2.  Register the blueprint in `app/__init__.py`.

```yaml
# swagger.yaml example
paths:
  /users/login:
    post:
      tags: [Users]
      summary: Login endpoint
      parameters:
        - in: body
          name: body
          schema:
            $ref: '#/definitions/LoginCredentials'
      responses:
        200:
          description: Success
```

---

## Configuration Management

Use a `config.py` file to manage different environments (Dev, Test, Prod).

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
```

Load it in `app.py` or `__init__.py`:
```python
app.config.from_object('config.DevelopmentConfig')
```