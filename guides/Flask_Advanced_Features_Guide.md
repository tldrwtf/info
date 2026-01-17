# Flask Advanced Features Guide

## Table of Contents

1. [Rate Limiting with Flask-Limiter](#rate-limiting-with-flask-limiter)
2. [Caching with Flask-Caching](#caching-with-flask-caching)
3. [Pagination Patterns](#pagination-patterns)
4. [Advanced Blueprint Architecture](#advanced-blueprint-architecture)
5. [Request Validation](#request-validation)
6. [Error Handling](#error-handling)
7. [Application Factory Pattern](#application-factory-pattern)
8. [JWT Authentication](#jwt-authentication)
9. [CORS Configuration](#cors-configuration)
10. [Production Best Practices](#production-best-practices)

---

## Rate Limiting with Flask-Limiter

Rate limiting prevents abuse by restricting the number of requests a client can make.

### Installation

```bash
pip install Flask-Limiter
```

### Basic Setup

```python
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Initialize limiter
limiter = Limiter(
    app=app,
    key_func=get_remote_address,  # Use IP address as key
    default_limits=["200 per day", "50 per hour"],  # Global limits
    storage_uri="redis://localhost:6379"  # For distributed systems
)
```

### Applying Rate Limits

**Global Limits:**
```python
# Applied to all routes via default_limits in config
limiter = Limiter(
    app=app,
    default_limits=["200 per day", "50 per hour"]
)
```

**Per-Route Limits:**
```python
@app.route('/api/search')
@limiter.limit("5 per minute")  # Override global limit
def search():
    return {"results": []}

@app.route('/api/expensive-operation')
@limiter.limit("1 per hour")  # Very restrictive
def expensive_operation():
    return {"status": "processing"}
```

**Multiple Limits:**
```python
@app.route('/api/posts')
@limiter.limit("10 per minute")
@limiter.limit("100 per hour")
@limiter.limit("1000 per day")
def get_posts():
    """Enforces all three limits."""
    return {"posts": []}
```

### Dynamic Rate Limits

```python
def get_user_tier():
    """Determine rate limit based on user tier."""
    user = get_current_user()
    if user and user.tier == 'premium':
        return "1000 per hour"
    elif user and user.tier == 'standard':
        return "100 per hour"
    return "10 per hour"  # Free tier

@app.route('/api/data')
@limiter.limit(get_user_tier)
def get_data():
    return {"data": []}
```

### Exempt Routes

```python
@app.route('/health')
@limiter.exempt  # No rate limiting
def health_check():
    return {"status": "healthy"}
```

### Custom Key Functions

```python
from flask import request

def get_user_id():
    """Use user ID instead of IP for authenticated requests."""
    token = request.headers.get('Authorization')
    if token:
        user = decode_token(token)
        return f"user:{user.id}"
    return get_remote_address()

limiter = Limiter(
    app=app,
    key_func=get_user_id
)
```

### Rate Limit Response

```python
@app.errorhandler(429)
def ratelimit_handler(e):
    """Custom response for rate limit exceeded."""
    return {
        "error": "Rate limit exceeded",
        "message": str(e.description),
        "retry_after": e.description.split()[-1]
    }, 429
```

### Complete Example

```python
from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Configure limiter
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"  # Use Redis in production
)

@app.route('/api/books')
@limiter.limit("10 per minute")
def get_books():
    """Get books with rate limiting."""
    books = [
        {"id": 1, "title": "1984"},
        {"id": 2, "title": "Brave New World"}
    ]
    return jsonify(books)

@app.route('/api/books/<int:book_id>')
@limiter.limit("30 per minute")  # More generous for single item
def get_book(book_id):
    """Get single book with higher rate limit."""
    book = {"id": book_id, "title": "Example Book"}
    return jsonify(book)

@app.errorhandler(429)
def ratelimit_error(e):
    return jsonify(error="Rate limit exceeded", message=str(e.description)), 429

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Caching with Flask-Caching

Caching stores frequently accessed data to reduce database queries and improve performance.

### Installation

```bash
pip install Flask-Caching
```

### Basic Setup

```python
from flask import Flask
from flask_caching import Cache

app = Flask(__name__)

# Configure cache
app.config['CACHE_TYPE'] = 'SimpleCache'  # Memory cache
app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # 5 minutes

# Or use Redis for production
app.config['CACHE_TYPE'] = 'RedisCache'
app.config['CACHE_REDIS_HOST'] = 'localhost'
app.config['CACHE_REDIS_PORT'] = 6379
app.config['CACHE_REDIS_DB'] = 0

# Initialize cache
cache = Cache(app)
```

### Caching Routes

**Basic Route Caching:**
```python
@app.route('/api/popular-books')
@cache.cached(timeout=600)  # Cache for 10 minutes
def get_popular_books():
    """Expensive query - cache the result."""
    books = Book.query.order_by(Book.views.desc()).limit(10).all()
    return jsonify([book.to_dict() for book in books])
```

**Conditional Caching:**
```python
@app.route('/api/books')
@cache.cached(timeout=300, unless=lambda: request.args.get('nocache'))
def get_books():
    """Cache unless nocache parameter is present."""
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])
```

**Cache with Query Parameters:**
```python
@app.route('/api/books')
@cache.cached(timeout=300, query_string=True)
def get_books():
    """Different cache for different query parameters."""
    page = request.args.get('page', 1, type=int)
    books = Book.query.paginate(page=page, per_page=20)
    return jsonify([book.to_dict() for book in books.items])
```

### Memoization (Function Caching)

```python
@cache.memoize(timeout=600)
def get_user_books(user_id):
    """Cache result based on user_id argument."""
    books = Book.query.filter_by(user_id=user_id).all()
    return [book.to_dict() for book in books]

@app.route('/api/users/<int:user_id>/books')
def user_books(user_id):
    """Use memoized function."""
    books = get_user_books(user_id)
    return jsonify(books)
```

### Cache Invalidation

**Delete Specific Cache:**
```python
@app.route('/api/books', methods=['POST'])
def create_book():
    """Create book and invalidate cache."""
    # Create book
    book = Book(**request.json)
    db.session.add(book)
    db.session.commit()

    # Invalidate cached book lists
    cache.delete('view//api/books')
    cache.delete('view//api/popular-books')

    return jsonify(book.to_dict()), 201
```

**Delete Memoized Cache:**
```python
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """Update book and clear its cache."""
    book = Book.query.get_or_404(book_id)
    book.title = request.json.get('title', book.title)
    db.session.commit()

    # Clear memoized cache for this book
    cache.delete_memoized(get_user_books, book.user_id)

    return jsonify(book.to_dict())
```

**Clear All Cache:**
```python
@app.route('/admin/clear-cache', methods=['POST'])
@admin_required
def clear_cache():
    """Clear entire cache."""
    cache.clear()
    return jsonify({"message": "Cache cleared"}), 200
```

### Pagination with Caching

```python
@app.route('/api/books')
@cache.cached(timeout=300, query_string=True)
def get_books_paginated():
    """Cache paginated results."""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)

    # Be careful with caching paginated routes
    # Consider: cache.cached() may not be ideal if data changes frequently
    pagination = Book.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return jsonify({
        'books': [book.to_dict() for book in pagination.items],
        'page': page,
        'pages': pagination.pages,
        'total': pagination.total
    })
```

### Caching Pagination: Common Pitfalls and Solutions

Caching paginated routes is one of the most common Flask mistakes. This section explains the problem and provides solutions.

#### The Problem

When you cache a paginated route, you're caching a **single page snapshot**, not the entire dataset:

```python
# ANTI-PATTERN - Don't do this!
@app.route('/api/books')
@cache.cached(timeout=300, query_string=True)  # 5 minute cache
def get_books_paginated():
    page = request.args.get('page', 1, type=int)

    pagination = Book.query.paginate(page=page, per_page=20)

    return jsonify({
        'books': [book.to_dict() for book in pagination.items],
        'page': page,
        'total_pages': pagination.pages,
        'total_books': pagination.total
    })
```

**What goes wrong:**

1. **User adds new book** → Total count increases to 101
2. **Page 1 is still cached** → Shows total_books: 100 (stale)
3. **Page 6 doesn't exist yet** → Cache shows it exists
4. **Inconsistent data across pages**

#### Warning Signs

- Total count differs between pages
- New items don't appear until cache expires
- Deleted items still appear in some pages
- Page count incorrect after data changes

#### Solution 1: Don't Cache Pagination (Recommended)

For frequently changing data, skip caching entirely:

```python
@app.route('/api/books')
def get_books_paginated():
    """No caching for dynamic data."""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)

    pagination = Book.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return jsonify({
        'books': [book.to_dict() for book in pagination.items],
        'page': page,
        'pages': pagination.pages,
        'total': pagination.total
    })
```

**Use database query optimization instead:**
- Add indexes on filter/sort columns
- Use `select_related` for foreign keys
- Limit fields returned with `only()`

#### Solution 2: Very Short TTL

For semi-static data that changes occasionally:

```python
@app.route('/api/books')
@cache.cached(timeout=10, query_string=True)  # Only 10 seconds
def get_books_paginated():
    # ... pagination code ...
    return jsonify(response)
```

**Good for:**
- News articles (updates every few minutes)
- Product catalogs (updates hourly)
- Read-heavy endpoints with occasional writes

#### Solution 3: Cache Individual Items, Not Pages

Cache the expensive part (individual book data), not the page:

```python
@cache.memoize(timeout=300)
def get_book_data(book_id):
    """Cache individual book lookups."""
    book = Book.query.get(book_id)
    return book.to_dict()

@app.route('/api/books')
def get_books_paginated():
    """Pagination without caching, but items are cached."""
    page = request.args.get('page', 1, type=int)
    per_page = 20

    # Get page of IDs (fast query, not cached)
    book_ids = db.session.query(Book.id)\
        .order_by(Book.created_at.desc())\
        .limit(per_page)\
        .offset((page - 1) * per_page)\
        .all()

    # Fetch each book (cached individually)
    books = [get_book_data(book_id) for book_id, in book_ids]

    # Get total count (can cache this separately)
    total = Book.query.count()

    return jsonify({
        'books': books,
        'page': page,
        'total': total
    })
```

**Benefits:**
- Individual items cached across pages
- Page structure always fresh
- Adding/removing items doesn't break cache

#### Solution 4: Smart Cache Invalidation

Invalidate all page caches when data changes:

```python
def invalidate_books_cache():
    """Clear all cached book pages."""
    # Get max page number
    total_books = Book.query.count()
    max_pages = (total_books // 20) + 1

    # Clear cache for each page
    for page in range(1, max_pages + 1):
        cache.delete(f'view//api/books?page={page}&per_page=20')

@app.route('/api/books', methods=['POST'])
def create_book():
    """Create book and invalidate cache."""
    book = Book(**request.json)
    db.session.add(book)
    db.session.commit()

    # Invalidate all page caches
    invalidate_books_cache()

    return jsonify(book.to_dict()), 201
```

**Warning:** This can be expensive for many pages. Consider Solution 3 instead.

#### Solution 5: Separate Metadata Cache

Cache metadata (total count, page count) separately from data:

```python
@cache.cached(timeout=60, key_prefix='books_metadata')
def get_books_metadata():
    """Cache metadata for 1 minute."""
    return {
        'total_books': Book.query.count(),
        'total_pages': (Book.query.count() // 20) + 1
    }

@app.route('/api/books')
def get_books_paginated():
    page = request.args.get('page', 1, type=int)

    # Get uncached data
    books = Book.query.paginate(page=page, per_page=20)

    # Get cached metadata
    metadata = get_books_metadata()

    return jsonify({
        'books': [b.to_dict() for b in books.items],
        'page': page,
        **metadata  # Cached total/pages
    })
```

#### Decision Matrix

| Data Characteristics | Recommended Solution |
|---------------------|---------------------|
| Changes frequently (social feeds, dashboards) | Solution 1: No caching |
| Updates every few minutes | Solution 2: Short TTL (10-30s) |
| Expensive item lookups | Solution 3: Cache items, not pages |
| Occasional writes, many reads | Solution 5: Separate metadata cache |
| Complete control over invalidation | Solution 4: Manual invalidation |

#### Production Pattern

For most applications, combine strategies:

```python
# Cache individual items
@cache.memoize(timeout=300)
def get_book_details(book_id):
    return Book.query.get(book_id).to_dict()

# Cache metadata briefly
@cache.memoize(timeout=30)
def get_books_count():
    return Book.query.count()

# Don't cache pagination
@app.route('/api/books')
def get_books_paginated():
    page = request.args.get('page', 1, type=int)

    # Fresh pagination
    book_ids = db.session.query(Book.id)\
        .limit(20).offset((page-1)*20).all()

    # Cached details
    books = [get_book_details(id) for id, in book_ids]

    # Cached count
    total = get_books_count()

    return jsonify({'books': books, 'total': total})
```

#### Testing Cache Behavior

Always test pagination caching:

```python
def test_pagination_cache():
    # Get page 1
    response1 = client.get('/api/books?page=1')
    total_before = response1.json['total']

    # Add new book
    client.post('/api/books', json={'title': 'New Book'})

    # Get page 1 again
    response2 = client.get('/api/books?page=1')
    total_after = response2.json['total']

    # Should reflect new total
    assert total_after == total_before + 1
```

---

## Pagination Patterns

### Basic Pagination

```python
from flask import request, jsonify

@app.route('/api/books')
def get_books():
    """Paginated book list."""
    # Get pagination parameters
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)

    # Validate parameters
    if per_page > 100:
        per_page = 100  # Max items per page

    # Query with pagination
    pagination = Book.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False  # Don't raise 404 for invalid page
    )

    # Build response
    return jsonify({
        'items': [book.to_dict() for book in pagination.items],
        'pagination': {
            'page': page,
            'per_page': per_page,
            'total_pages': pagination.pages,
            'total_items': pagination.total,
            'has_next': pagination.has_next,
            'has_prev': pagination.has_prev,
            'next_page': page + 1 if pagination.has_next else None,
            'prev_page': page - 1 if pagination.has_prev else None
        }
    })
```

### Pagination with Links

```python
from urllib.parse import urlencode

def build_pagination_links(pagination, endpoint):
    """Build next/prev/first/last links."""
    def build_url(page):
        args = request.args.copy()
        args['page'] = page
        return f"{request.base_url}?{urlencode(args)}"

    links = {
        'self': build_url(pagination.page),
        'first': build_url(1),
        'last': build_url(pagination.pages)
    }

    if pagination.has_next:
        links['next'] = build_url(pagination.page + 1)

    if pagination.has_prev:
        links['prev'] = build_url(pagination.page - 1)

    return links

@app.route('/api/books')
def get_books():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)

    pagination = Book.query.paginate(page=page, per_page=per_page)

    return jsonify({
        'items': [book.to_dict() for book in pagination.items],
        'links': build_pagination_links(pagination, 'get_books'),
        'meta': {
            'page': page,
            'per_page': per_page,
            'total': pagination.total
        }
    })
```

### Cursor-Based Pagination

For better performance with large datasets:

```python
@app.route('/api/books')
def get_books_cursor():
    """Cursor-based pagination (more efficient for large datasets)."""
    cursor = request.args.get('cursor', type=int)
    limit = request.args.get('limit', 20, type=int)

    # Query items after cursor
    query = Book.query.order_by(Book.id)

    if cursor:
        query = query.filter(Book.id > cursor)

    books = query.limit(limit + 1).all()

    # Check if there are more items
    has_more = len(books) > limit
    if has_more:
        books = books[:limit]

    # Build response
    response = {
        'items': [book.to_dict() for book in books],
        'has_more': has_more
    }

    if has_more:
        response['next_cursor'] = books[-1].id

    return jsonify(response)
```

---

## Advanced Blueprint Architecture

### Modular Blueprint Structure

```
app/
├── __init__.py          # Application factory
├── models.py            # Database models
├── config.py            # Configuration
├── auth/
│   ├── __init__.py
│   ├── routes.py        # Auth routes
│   └── utils.py         # Auth utilities
├── books/
│   ├── __init__.py
│   ├── routes.py        # Book routes
│   └── schemas.py       # Marshmallow schemas
└── users/
    ├── __init__.py
    ├── routes.py        # User routes
    └── schemas.py       # Marshmallow schemas
```

### Blueprint Definition

**auth/__init__.py:**
```python
from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

from . import routes  # Import routes to register them
```

**auth/routes.py:**
```python
from flask import request, jsonify
from . import auth_bp
from .utils import generate_token, verify_password
from app.models import User

@auth_bp.route('/login', methods=['POST'])
def login():
    """User login endpoint."""
    data = request.get_json()

    user = User.query.filter_by(email=data['email']).first()

    if not user or not verify_password(data['password'], user.password_hash):
        return jsonify({"error": "Invalid credentials"}), 401

    token = generate_token(user)
    return jsonify({"token": token}), 200

@auth_bp.route('/register', methods=['POST'])
def register():
    """User registration endpoint."""
    data = request.get_json()

    # Registration logic
    user = User(**data)
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201
```

### Registering Blueprints

**app/__init__.py:**
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app(config_name='development'):
    """Application factory pattern."""
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(f'app.config.{config_name.capitalize()}Config')

    # Initialize extensions
    db.init_app(app)
    CORS(app)

    # Register blueprints
    from app.auth import auth_bp
    from app.books import books_bp
    from app.users import users_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(users_bp)

    return app
```

### Blueprint with Decorators

```python
from functools import wraps
from flask import request, jsonify
from . import books_bp

def token_required(f):
    """Decorator to require authentication."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({"error": "Token required"}), 401

        try:
            # Verify token logic
            user = verify_token(token)
            return f(current_user=user, *args, **kwargs)
        except Exception as e:
            return jsonify({"error": "Invalid token"}), 401

    return decorated

@books_bp.route('/books', methods=['POST'])
@token_required
def create_book(current_user):
    """Create book - requires authentication."""
    data = request.get_json()
    book = Book(user_id=current_user.id, **data)
    db.session.add(book)
    db.session.commit()

    return jsonify(book.to_dict()), 201
```

---

## Request Validation

### Using Marshmallow for Validation

```python
from marshmallow import Schema, fields, validate, ValidationError

class BookSchema(Schema):
    """Schema for book validation."""
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    author = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    isbn = fields.Str(validate=validate.Regexp(r'^\d{10}(\d{3})?$'))
    published_year = fields.Int(validate=validate.Range(min=1000, max=2100))
    genre = fields.Str(validate=validate.OneOf(['Fiction', 'Non-Fiction', 'Science', 'History']))
    price = fields.Float(validate=validate.Range(min=0))

    class Meta:
        ordered = True

book_schema = BookSchema()
books_schema = BookSchema(many=True)
```

### Using Schemas in Routes

```python
@app.route('/api/books', methods=['POST'])
def create_book():
    """Create book with validation."""
    try:
        # Validate and deserialize input
        data = book_schema.load(request.get_json())

        # Create book
        book = Book(**data)
        db.session.add(book)
        db.session.commit()

        # Serialize and return
        return jsonify(book_schema.dump(book)), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
```

### Custom Validation

```python
from marshmallow import validates, ValidationError

class UserSchema(Schema):
    email = fields.Email(required=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    password = fields.Str(required=True, load_only=True)

    @validates('username')
    def validate_username(self, value):
        """Custom validation for username."""
        if User.query.filter_by(username=value).first():
            raise ValidationError('Username already exists')

    @validates('email')
    def validate_email(self, value):
        """Custom validation for email."""
        if User.query.filter_by(email=value).first():
            raise ValidationError('Email already registered')
```

---

## Error Handling

### Global Error Handlers

```python
from werkzeug.exceptions import HTTPException

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return jsonify({
        "error": "Not Found",
        "message": "The requested resource was not found"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    db.session.rollback()  # Rollback any failed transactions
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred"
    }), 500

@app.errorhandler(ValidationError)
def validation_error(error):
    """Handle Marshmallow validation errors."""
    return jsonify({
        "error": "Validation Error",
        "messages": error.messages
    }), 400

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle all HTTP exceptions."""
    return jsonify({
        "error": e.name,
        "message": e.description
    }), e.code

### Custom 404 Behavior (SPA Pattern)

In Single Page Applications (SPAs) like React or Vue, you often want the backend to ignore unknown routes and let the frontend handle them.

```python
from flask import redirect, url_for

@app.errorhandler(404)
def handle_404(e):
    """Redirect unknown routes to the home page (SPA entry point)."""
    # For APIs, you usually return JSON.
    # For SPAs, you might want to redirect to the frontend route.
    return redirect(url_for('home'))
```
```

### Custom Exceptions

```python
class APIError(Exception):
    """Base class for API exceptions."""
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

class ResourceNotFoundError(APIError):
    """Raised when resource is not found."""
    status_code = 404

class UnauthorizedError(APIError):
    """Raised when user is not authorized."""
    status_code = 401

@app.errorhandler(APIError)
def handle_api_error(error):
    """Handle custom API errors."""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# Usage in routes
@app.route('/api/books/<int:book_id>')
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        raise ResourceNotFoundError(f"Book with id {book_id} not found")
    return jsonify(book.to_dict())
```

---

## Application Factory Pattern

### Complete Application Factory

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
limiter = Limiter(key_func=get_remote_address)
cache = Cache()

def create_app(config_name='development'):
    """
    Application factory.

    Args:
        config_name: Configuration to use (development, production, testing)

    Returns:
        Configured Flask application
    """
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(f'app.config.{config_name.capitalize()}Config')

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    limiter.init_app(app)
    cache.init_app(app)

    # Register blueprints
    from app.auth import auth_bp
    from app.books import books_bp
    from app.users import users_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(books_bp, url_prefix='/api/books')
    app.register_blueprint(users_bp, url_prefix='/api/users')

    # Register error handlers
    register_error_handlers(app)

    # Register CLI commands
    register_commands(app)

    return app

def register_error_handlers(app):
    """Register error handlers."""
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return jsonify({"error": "Internal server error"}), 500

def register_commands(app):
    """Register CLI commands."""
    @app.cli.command()
    def init_db():
        """Initialize the database."""
        db.create_all()
        print("Database initialized")

    @app.cli.command()
    def seed_db():
        """Seed the database with sample data."""
        # Seeding logic
        print("Database seeded")
```

### Configuration

**config.py:**
```python
import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Rate limiting
    RATELIMIT_STORAGE_URL = os.getenv('REDIS_URL', 'memory://')

    # Caching
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DEV_DATABASE_URL',
        'sqlite:///dev.db'
    )
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    # Redis for caching and rate limiting
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_URL = os.getenv('REDIS_URL')
    RATELIMIT_STORAGE_URL = os.getenv('REDIS_URL')

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
```

---

## JWT Authentication

### Setup

```bash
pip install python-jose[cryptography]
```

### Token Generation and Verification

```python
from jose import jwt, JWTError
from datetime import datetime, timedelta
from flask import current_app

def generate_token(user):
    """Generate JWT token for user."""
    payload = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(hours=24),
        'iat': datetime.utcnow()
    }

    token = jwt.encode(
        payload,
        current_app.config['SECRET_KEY'],
        algorithm='HS256'
    )

    return token

def verify_token(token):
    """Verify JWT token."""
    try:
        # Remove "Bearer " prefix if present
        if token.startswith('Bearer '):
            token = token[7:]

        payload = jwt.decode(
            token,
            current_app.config['SECRET_KEY'],
            algorithms=['HS256']
        )

        return payload['user_id']

    except JWTError:
        return None
```

### Authentication Decorator

```python
from functools import wraps
from flask import request, jsonify

def token_required(f):
    """Decorator to require valid JWT token."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        user_id = verify_token(token)

        if not user_id:
            return jsonify({"error": "Invalid or expired token"}), 401

        # Load user
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 401

        # Pass user to route function
        return f(current_user=user, *args, **kwargs)

    return decorated_function

# Usage
@app.route('/api/profile')
@token_required
def get_profile(current_user):
    return jsonify(current_user.to_dict())
```

---

## CORS Configuration

### Basic CORS Setup

```python
from flask_cors import CORS

app = Flask(__name__)

# Allow all origins (development only)
CORS(app)

# Restrict to specific origins (production)
CORS(app, origins=['https://example.com', 'https://app.example.com'])

# Configure per resource
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://example.com"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})
```

### Blueprint-Specific CORS

```python
from flask_cors import cross_origin

@books_bp.route('/books', methods=['GET'])
@cross_origin(origins=['https://example.com'])
def get_books():
    return jsonify([])
```

---

## Production Best Practices

### Environment Variables

**.env:**
```
FLASK_APP=run.py
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost/dbname
REDIS_URL=redis://localhost:6379/0
```

### Logging Configuration

```python
import logging
from logging.handlers import RotatingFileHandler
import os

def configure_logging(app):
    """Configure application logging."""
    if not app.debug:
        # Create logs directory
        if not os.path.exists('logs'):
            os.mkdir('logs')

        # File handler
        file_handler = RotatingFileHandler(
            'logs/app.log',
            maxBytes=10240000,  # 10MB
            backupCount=10
        )

        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'
        ))

        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Application startup')

# In create_app()
configure_logging(app)
```

### Health Check Endpoint

```python
@app.route('/health')
@limiter.exempt
def health_check():
    """Health check endpoint for load balancers."""
    try:
        # Check database
        db.session.execute('SELECT 1')

        return jsonify({
            "status": "healthy",
            "database": "connected",
            "timestamp": datetime.utcnow().isoformat()
        }), 200

    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500
```

---

## Summary

### Key Takeaways

1. **Rate Limiting**: Protect your API from abuse
2. **Caching**: Improve performance by caching expensive operations
3. **Pagination**: Handle large datasets efficiently
4. **Blueprints**: Organize code into modular components
5. **Validation**: Use schemas for request validation
6. **Error Handling**: Provide consistent error responses
7. **Factory Pattern**: Use for flexible application configuration
8. **JWT Auth**: Secure routes with token-based authentication

### Best Practices Checklist

- [ ] Implement rate limiting on public endpoints
- [ ] Cache expensive database queries
- [ ] Use pagination for list endpoints
- [ ] Organize routes into blueprints
- [ ] Validate all request data
- [ ] Handle errors consistently
- [ ] Use application factory pattern
- [ ] Implement JWT authentication
- [ ] Configure CORS appropriately
- [ ] Set up proper logging
- [ ] Add health check endpoint
- [ ] Use environment variables for config

### Related Resources

- [Flask REST API Development](Flask_REST_API_Development_Guide.md) - Basic Flask API patterns
- [API Authentication](API_Authentication_Guide.md) - Authentication strategies
- [OAuth2 and Token Management](OAuth2_and_Token_Management_Guide.md) - OAuth2 implementation
- [SQLAlchemy Advanced Patterns](SQLAlchemy_Advanced_Patterns_Guide.md) - Database optimization
- [Error Handling](../cheatsheets/Error_Handling_Cheat_Sheet.md) - Exception handling

---

[Back to Main](../README.md)
