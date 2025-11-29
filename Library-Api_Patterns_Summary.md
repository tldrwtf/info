# Library-Api Flask Patterns - Quick Summary
---

## Table of Contents
1. [Application Factory Pattern](#1-application-factory-pattern)
2. [Blueprint Architecture](#2-blueprint-architecture)
3. [Rate Limiting (Flask-Limiter)](#3-rate-limiting-flask-limiter)
4. [Caching (Flask-Caching)](#4-caching-flask-caching)
5. [Pagination](#5-pagination)
6. [Marshmallow Schema Validation](#6-marshmallow-schema-validation)
7. [JWT Authentication](#7-jwt-authentication)
8. [SQLAlchemy Model Patterns (Modern 2.0+)](#8-sqlalchemy-model-patterns-modern-20)
9. [Configuration Management](#9-configuration-management)
10. [Advanced Route Patterns](#10-advanced-route-patterns)
11. [Common HTTP Status Codes](#common-http-status-codes)
12. [Decorator Stacking Order](#decorator-stacking-order)
13. [Extension Initialization Pattern](#extension-initialization-pattern)
14. [Project Structure Template](#project-structure-template)
15. [Key Dependencies](#key-dependencies)
16. [Best Practices Checklist](#best-practices-checklist)
17. [Quick Start Template](#quick-start-template)
18. [See Also](#see-also)

---

## 1. Application Factory Pattern

**Purpose**: Create Flask apps dynamically with environment-specific configs

**Key Code**:
```python
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')

    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)

    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(books_bp, url_prefix='/books')

    return app
```

**Benefits**: Testing, multiple instances, environment isolation

---

## 2. Blueprint Architecture

**Purpose**: Modular application organization

**Structure**:
```
app/blueprints/
├── books/
│   ├── __init__.py    # Blueprint definition
│   ├── routes.py      # Endpoint handlers
│   └── schemas.py     # Marshmallow schemas
```

**Blueprint Definition**:
```python
books_bp = Blueprint('books_bp', __name__)
from . import routes
```

**Registration**:
```python
app.register_blueprint(books_bp, url_prefix='/books')
```

---

## 3. Rate Limiting (Flask-Limiter)

**Setup**:
```python
limiter = Limiter(
    get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
```

**Usage Examples**:
```python
@limiter.limit("5 per 10 minute")  # Login protection
@limiter.limit("30 per hour")      # Update operations
@limiter.limit("8 per day")        # Delete operations
@limiter.limit("600 per day", override_defaults=True)  # Override
```

---

## 4. Caching (Flask-Caching)

**Setup**:
```python
cache = Cache()

# In config
CACHE_TYPE = "SimpleCache"
CACHE_DEFAULT_TIMEOUT = 300
```

**Usage**:
```python
@cache.cached(timeout=90)
def expensive_operation():
    # Cached for 90 seconds
    pass
```

**Warning**: Don't cache paginated routes (caches single page only)

---

## 5. Pagination

**Implementation**:
```python
@books_bp.route('', methods=['GET'])
def get_books():
    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))
    query = select(Books)
    books = db.paginate(query, page=page, per_page=per_page)
    return books_schema.jsonify(books), 200
```

**Usage**: `GET /books?page=1&per_page=10`

---

## 6. Marshmallow Schema Validation

**Schema Definition**:
```python
class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Books

book_schema = BookSchema()
books_schema = BookSchema(many=True)
```

**Methods**:
- `schema.load()`: JSON → Python + validation
- `schema.dump()`: Python → Dict
- `schema.jsonify()`: Python → JSON response

**Validation Pattern**:
```python
try:
    data = book_schema.load(request.json)
except ValidationError as e:
    return jsonify(e.messages), 400
```

---

## 7. JWT Authentication

**Token Generation**:
```python
def encode_token(user_id, role="user"):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1),
        'iat': datetime.now(timezone.utc),
        'sub': str(user_id),  # String conversion important!
        'role': role
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
```

**Token Validation Decorator**:
```python
def token_required(f):
    @wraps(f)
    def decoration(*args, **kwargs):
        token = request.headers['Authorization'].split()[1]
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        request.logged_in_user_id = data['sub']
        return f(*args, **kwargs)
    return decoration
```

**Protected Route**:
```python
@users_bp.route('/profile', methods=['GET'])
@token_required
def read_user():
    user_id = request.logged_in_user_id
    user = db.session.get(Users, user_id)
    return user_schema.jsonify(user), 200
```

**Password Hashing**:
```python
from werkzeug.security import generate_password_hash, check_password_hash

# Registration
data["password"] = generate_password_hash(data["password"])

# Login
if check_password_hash(user.password, data['password']):
    # Success
```

---

## 8. SQLAlchemy Model Patterns (Modern 2.0+)

**Base Setup**:
```python
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
```

**Model with Relationships**:
```python
class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(350), unique=True)
    password: Mapped[str] = mapped_column(String(150))

    loans: Mapped[list['Loans']] = relationship('Loans', back_populates='user')
```

**Many-to-Many Association**:
```python
loan_books = Table(
    'loan_books',
    Base.metadata,
    Column('loan_id', ForeignKey('loans.id')),
    Column('book_id', ForeignKey('books.id'))
)

class Loans(Base):
    books: Mapped[list['Books']] = relationship(
        "Books",
        secondary=loan_books,
        back_populates='loans'
    )
```

**Database Operations**:
```python
# Create
new_book = Books(**data)
db.session.add(new_book)
db.session.commit()

# Read
book = db.session.get(Books, book_id)
books = db.session.query(Books).all()
user = db.session.query(Users).where(Users.email==email).first()

# Update
for key, value in data.items():
    setattr(book, key, value)
db.session.commit()

# Delete
db.session.delete(book)
db.session.commit()

# Many-to-Many
loan.books.append(book)  # Add relationship
loan.books.remove(book)  # Remove relationship
```

---

## 9. Configuration Management

**Config Classes**:
```python
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    DEBUG = True
    CACHE_TYPE = "SimpleCache"

class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql://...'
    DEBUG = False
    CACHE_TYPE = "RedisCache"
```

**Loading**:
```python
app.config.from_object(f'config.{config_name}')
```

---

## 10. Advanced Route Patterns

### CRUD Operations

**Create**:
```python
@bp.route('', methods=['POST'])
def create():
    data = schema.load(request.json)
    item = Model(**data)
    db.session.add(item)
    db.session.commit()
    return schema.jsonify(item), 201
```

**Read**:
```python
@bp.route('', methods=['GET'])
def read_all():
    items = db.session.query(Model).all()
    return schema.jsonify(items), 200

@bp.route('/<int:id>', methods=['GET'])
def read_one(id):
    item = db.session.get(Model, id)
    return schema.jsonify(item), 200
```

**Update**:
```python
@bp.route('/<int:id>', methods=['PUT'])
def update(id):
    item = db.session.get(Model, id)
    data = schema.load(request.json)
    for key, value in data.items():
        setattr(item, key, value)
    db.session.commit()
    return schema.jsonify(item), 200
```

**Delete**:
```python
@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    item = db.session.get(Model, id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Deleted"}), 200
```

### Search Pattern
```python
@bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    items = db.session.query(Model).where(
        Model.field.ilike(f"%{query}%")
    ).all()
    return schema.jsonify(items), 200
```

### Aggregation Pattern
```python
@bp.route('/popular', methods=['GET'])
def popular():
    items = db.session.query(Model).all()
    items.sort(key=lambda x: len(x.relationships), reverse=True)
    return jsonify(items[:10]), 200
```

### Nested Resources
```python
@bp.route('/<int:parent_id>/children/<int:child_id>', methods=['PUT'])
def add_child(parent_id, child_id):
    parent = db.session.get(Parent, parent_id)
    child = db.session.get(Child, child_id)
    parent.children.append(child)
    db.session.commit()
    return jsonify({"message": "Added"}), 200
```

---

## Common HTTP Status Codes

- `200 OK`: Successful operation
- `201 Created`: Successful creation
- `400 Bad Request`: Validation error
- `401 Unauthorized`: Missing/invalid auth
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

---

## Decorator Stacking Order

```python
@bp.route('/endpoint', methods=['POST'])
@limiter.limit("10 per hour")      # Rate limiting first
@cache.cached(timeout=60)          # Caching second
@token_required                     # Auth last
def protected_cached_endpoint():
    pass
```

---

## Extension Initialization Pattern

**In extensions.py**:
```python
ma = Marshmallow()
limiter = Limiter(get_remote_address, default_limits=[...])
cache = Cache()
```

**In create_app()**:
```python
ma.init_app(app)
limiter.init_app(app)
cache.init_app(app)
```

---

## Project Structure Template

```
project/
├── app/
│   ├── __init__.py         # create_app()
│   ├── models.py           # SQLAlchemy models
│   ├── extensions.py       # Extension instances
│   ├── blueprints/
│   │   └── resource/
│   │       ├── __init__.py
│   │       ├── routes.py
│   │       └── schemas.py
│   └── util/
│       └── auth.py         # JWT utilities
├── app.py                  # Entry point
├── config.py               # Config classes
└── requirements.txt
```

---

## Key Dependencies

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

## Best Practices Checklist

- [ ] Use application factory pattern
- [ ] Organize code with blueprints
- [ ] Validate all inputs with Marshmallow
- [ ] Implement rate limiting on sensitive endpoints
- [ ] Cache expensive operations (but not paginated routes)
- [ ] Use JWT for stateless authentication
- [ ] Hash passwords with werkzeug.security
- [ ] Use modern SQLAlchemy 2.0 syntax (Mapped, mapped_column)
- [ ] Implement proper error handling
- [ ] Return appropriate HTTP status codes
- [ ] Use environment-specific configurations
- [ ] Never commit secrets to version control
- [ ] Implement pagination for large datasets
- [ ] Use HTTPS in production
- [ ] Set proper CORS headers if needed
- [ ] Log important operations
- [ ] Write tests for all endpoints
- [ ] Document API with OpenAPI/Swagger

---

## Quick Start Template

```python
# 1. Create extensions (extensions.py)
ma = Marshmallow()
limiter = Limiter(get_remote_address, default_limits=["200/day"])
cache = Cache()

# 2. Create blueprint (blueprints/resource/__init__.py)
resource_bp = Blueprint('resource_bp', __name__)
from . import routes

# 3. Create schema (blueprints/resource/schemas.py)
class ResourceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Resource
resource_schema = ResourceSchema()

# 4. Create routes (blueprints/resource/routes.py)
@resource_bp.route('', methods=['POST'])
@limiter.limit("30 per hour")
def create_resource():
    data = resource_schema.load(request.json)
    resource = Resource(**data)
    db.session.add(resource)
    db.session.commit()
    return resource_schema.jsonify(resource), 201

# 5. Create app (app/__init__.py)
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')

    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)

    app.register_blueprint(resource_bp, url_prefix='/resources')

    return app

# 6. Run app (app.py)
app = create_app('DevelopmentConfig')
with app.app_context():
    db.create_all()
app.run()
```

---

## See Also

- [Library-Api Flask Patterns Guide](./Library-Api_Flask_Patterns_Guide.md) - Full detailed guide with explanations and examples
- [Flask REST API Development Guide](./Flask_REST_API_Development_Guide.md) - Foundational Flask API concepts
- [Flask Advanced Features Guide](./Flask_Advanced_Features_Guide.md) - Advanced patterns and production best practices
- [SQLAlchemy Advanced Patterns Guide](./SQLAlchemy_Advanced_Patterns_Guide.md) - Database optimization and session management
- [API Authentication Guide](./API_Authentication_Guide.md) - Authentication strategies

[Back to Main](./README.md)

