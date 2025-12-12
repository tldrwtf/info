# Flask AI Tools Integration Guide

This guide explores the architecture and implementation of a Flask application designed for potential integration with AI tools. It showcases a structured approach using Blueprints, SQLAlchemy ORM, Marshmallow for serialization, and custom JWT authentication.

---

## 1. Project Overview

This Flask application serves as a backend API for an e-commerce or inventory management system. It's built with scalability and maintainability in mind, making it suitable for extending with AI-powered features such as recommendation engines, smart inventory management, or conversational interfaces.

### Key Features
*   **Modular Design:** Utilizes Flask Blueprints for organized API endpoints.
*   **Database Integration:** Uses SQLAlchemy ORM for interacting with a relational database.
*   **Data Serialization:** Employs Marshmallow for request validation and response serialization.
*   **Authentication:** Custom JWT (JSON Web Token) implementation for secure access.
*   **Rate Limiting & Caching:** (Implied by dependencies and common Flask patterns).
*   **Product Catalog:** Manages product descriptions and individual product items.
*   **User Management:** Handles user registration, login, and profiles.
*   **Shopping Cart & Orders:** Functionality for managing user carts and processing orders.

---

## 2. Core Application Structure

The application follows an Application Factory pattern, promoting flexible configuration and testability.

### `app.py` - Application Entry Point

This file initializes and runs the Flask application, setting up the application context and database.

```python
from app import create_app
from app.models import db

app = create_app('DevelopmentConfig') # Creates the Flask app instance

with app.app_context():
    db.create_all() # Ensures all database tables are created based on models

if __name__ == '__main__':
    app.run() # Starts the Flask development server
```

### `app/__init__.py` - The Application Factory

The `create_app` function is the core of the Application Factory pattern. It configures the Flask app and registers extensions and blueprints.

```python
from flask import Flask
from .models import db
from .extensions import ma # Marshmallow extension
from .blueprints.users import users_bp
from .blueprints.product_descriptions import product_descriptions_bp
from .blueprints.carts import carts_bp
from .blueprints.products import products_bp
from .blueprints.orders import orders_bp

def create_app(config_name):
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object(f'config.{config_name}')

    # Initialize extensions with the app
    db.init_app(app)
    ma.init_app(app)

    # Register Blueprints
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(product_descriptions_bp, url_prefix='/product-descriptions')
    app.register_blueprint(carts_bp, url_prefix='/carts')
    app.register_blueprint(products_bp, url_prefix='/products')
    app.register_blueprint(orders_bp, url_prefix='/orders')

    return app
```

### `config.py` - Configuration Management

Manages different configurations (development, testing, production) for the application, such as database URIs and debug settings.

```python
class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class TestingConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' # In-memory database for tests

class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.db'
    DEBUG = False
```

### `requirements.txt` - Project Dependencies

Lists all Python packages required for the project.

```
Flask==3.0.0
SQLAlchemy==2.0.23
Flask-SQLAlchemy==3.1.1
marshmallow==3.20.1
flask-marshmallow==1.2.1
python-jose==3.3.0
Werkzeug==3.0.1
```

---

## 3. Database Models (`app/models.py`)

SQLAlchemy models define the structure of the database tables and their relationships.

```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, Date, ForeignKey, UniqueConstraint
from datetime import date
from flask_sqlalchemy import SQLAlchemy

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(360), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(360), nullable=False)
    email: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    address: Mapped[str] = mapped_column(String(250))
    first_name: Mapped[str] = mapped_column(String(150))
    last_name: Mapped[str] = mapped_column(String(150))

    orders: Mapped[list["Order"]] = relationship("Order", back_populates="user")
    cart: Mapped["Cart"] = relationship("Cart", back_populates="user", uselist=False)

class ProductDescription(Base):
    __tablename__ = "product_descriptions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(1000))
    price: Mapped[float] = mapped_column(Float, nullable=False)

    products: Mapped[list["Product"]] = relationship("Product", back_populates="description")
    cart_items: Mapped[list["CartItem"]] = relationship("CartItem", back_populates="description")

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    serial_number: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    desc_id: Mapped[int] = mapped_column(ForeignKey('product_descriptions.id'), nullable=False)

    description: Mapped["ProductDescription"] = relationship("ProductDescription", back_populates="products")

    def generate_serial_number(self):
        # Placeholder for serial number generation logic
        return f"SN-{self.id}-{self.desc_id}"

class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="cart")
    items: Mapped[list["CartItem"]] = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")

class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    cart_id: Mapped[int] = mapped_column(ForeignKey('carts.id'), nullable=False)
    desc_id: Mapped[int] = mapped_column(ForeignKey('product_descriptions.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1)

    cart: Mapped["Cart"] = relationship("Cart", back_populates="items")
    description: Mapped["ProductDescription"] = relationship("ProductDescription", back_populates="cart_items")

    __table_args__ = (UniqueConstraint('cart_id', 'desc_id', name='_cart_desc_uc'),)

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    order_date: Mapped[date] = mapped_column(Date, nullable=False)
    delivery_date: Mapped[date] = mapped_column(Date)
    total: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default='pending') # pending, shipped, delivered, cancelled

    user: Mapped["User"] = relationship("User", back_populates="orders")
```

---

## 4. Authentication (`app/utils/auth.py`)

A custom JWT implementation handles user authentication for API endpoints, securing sensitive routes.

```python
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from functools import wraps
from flask import request, jsonify

SECRET_KEY = "your-super-secret-key" # In production, load this from environment variables
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 60

def encode_token(user_id: int) -> str:
    """Encodes a user ID into a JWT token."""
    payload = {
        "sub": str(user_id), # Subject of the token (user ID)
        "exp": datetime.now(timezone.utc) + timedelta(minutes=EXPIRATION_MINUTES),
        "iat": datetime.now(timezone.utc)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def token_required(f):
    """
    Decorator to protect API routes, requiring a valid JWT token.
    Extracts user ID from token and attaches it to the request object.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        # Check for Authorization header
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1] # Extract token after "Bearer "

        if not token:
            return jsonify({"message": "Authorization token is missing!"}), 401
        
        try:
            # Decode and verify the token
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            request.logged_in_user_id = payload['sub'] # Attach user ID to request

        except jose.exceptions.ExpiredSignatureError:
            return jsonify({'message':'Token has expired!'}), 403
        except jose.exceptions.JWTError:
            return jsonify({'message':'Invalid token!'}), 401
        except Exception as e:
            return jsonify({'message':f'Authentication error: {e}'}), 401
        
        return f(*args, **kwargs)
    
    return decorated_function
```

---

## 5. Blueprints (API Endpoints)

The application is organized into several Flask Blueprints, each managing a specific resource or set of related functionalities.

### User Management (`app/blueprints/users/routes.py`)

Handles user-related operations like registration, login, and profile management.

```python
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Cart, db, User
from app.extensions import ma # Marshmallow instance
from app.utils.auth import encode_token, token_required
from marshmallow import ValidationError

users_bp = Blueprint('users_bp', __name__)

# User schema (defined elsewhere, e.g., app/blueprints/users/schemas.py)
# user_schema = UserSchema()
# login_schema = UserSchema(only=("password", "email"))

@users_bp.route("/register", methods=["POST"])
def register():
    """Register a new user and create an associated shopping cart."""
    try:
        # Load and validate data using Marshmallow schema
        user_data = user_schema.load(request.json)
    except ValidationError as err:
        return jsonify({"message": err.messages}), 400

    # Hash the password before saving
    user_data["password"] = generate_password_hash(user_data["password"])

    user = User(**user_data) # Create new user instance
    db.session.add(user)
    db.session.flush() # Flush to get user.id before commit

    # Create a shopping cart for the new user
    new_cart = Cart(user_id=user.id)
    db.session.add(new_cart)
    
    db.session.commit() # Save user and cart to DB

    return user_schema.jsonify(user), 201

@users_bp.route("/login", methods=["POST"])
def login():
    """Authenticate user and return a JWT token."""
    try:
        credentials = login_schema.load(request.json)
    except ValidationError as err:
        return jsonify({"message": err.messages}), 400

    user = db.session.query(User).filter_by(email=credentials["email"]).first()

    if user and check_password_hash(user.password, credentials["password"]):
        token = encode_token(user.id) # Encode user ID into JWT
        return jsonify({"access_token": token}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@users_bp.route("/profile", methods=["GET"])
@token_required # Protect this route with JWT
def get_profile():
    """Retrieve the profile of the logged-in user."""
    user_id = request.logged_in_user_id
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return user_schema.jsonify(user), 200

@users_bp.route("/profile", methods=["PUT"])
@token_required
def update_profile():
    """Update the profile of the logged-in user."""
    user_id = request.logged_in_user_id
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    
    try:
        updated_data = user_schema.load(request.json, partial=True) # partial=True allows incomplete data
    except ValidationError as err:
        return jsonify({"message": err.messages}), 400

    # Update user attributes
    for key, value in updated_data.items():
        if key == "password":
            user.password = generate_password_hash(value)
        else:
            setattr(user, key, value)
    
    db.session.commit()
    return user_schema.jsonify(user), 200

@users_bp.route("/profile", methods=["DELETE"])
@token_required
def delete_profile():
    """Delete the profile of the logged-in user."""
    user_id = request.logged_in_user_id
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 204
```

### Product Catalog (`app/blueprints/product_descriptions/routes.py`, `app/blueprints/products/routes.py`)

Manages the catalog of product descriptions and individual physical product items.

**`app/blueprints/product_descriptions/routes.py`**
```python
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.models import db, ProductDescription
from app.extensions import ma # Marshmallow instance
from app.utils.auth import token_required

product_descriptions_bp = Blueprint('product_descriptions_bp', __name__)

# Product description schemas (defined elsewhere)
# product_description_schema = ProductDescriptionSchema()
# product_descriptions_schema = ProductDescriptionSchema(many=True)

@product_descriptions_bp.route("/", methods=["GET"])
def get_all_product_descriptions():
    """Retrieve all available product descriptions."""
    products = db.session.query(ProductDescription).all()
    return product_descriptions_schema.jsonify(products), 200

@product_descriptions_bp.route("/<int:id>", methods=["GET"])
def get_product_description(id):
    """Retrieve a single product description by its ID."""
    product = db.session.get(ProductDescription, id)
    if not product:
        return jsonify({"message": "Product description not found"}), 404
    return product_description_schema.jsonify(product), 200

@product_descriptions_bp.route("/", methods=["POST"])
@token_required # Assuming only authenticated users can create product descriptions
def create_product_description():
    """Create a new product description."""
    try:
        product_data = product_description_schema.load(request.json)
    except ValidationError as err:
        return jsonify({"message": err.messages}), 400
    
    new_product_description = ProductDescription(**product_data)
    db.session.add(new_product_description)
    db.session.commit()
    return product_description_schema.jsonify(new_product_description), 201

@product_descriptions_bp.route("/<int:id>", methods=["PUT"])
@token_required # Assuming only authenticated users can update product descriptions
def update_product_description(id):
    """Update an existing product description by its ID."""
    product = db.session.get(ProductDescription, id)
    if not product:
        return jsonify({"message": "Product description not found"}), 404

    try:
        updated_data = product_description_schema.load(request.json, partial=True)
    except ValidationError as err:
        return jsonify({"message": err.messages}), 400

    for key, value in updated_data.items():
        setattr(product, key, value)
    
    db.session.commit()
    return product_description_schema.jsonify(product), 200

@product_descriptions_bp.route("/<int:id>", methods=["DELETE"])
@token_required # Assuming only authenticated users can delete product descriptions
def delete_product_description(id):
    """Delete a product description by its ID."""
    product = db.session.get(ProductDescription, id)
    if not product:
        return jsonify({"message": "Product description not found"}), 404
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product description deleted successfully"}), 204
```

**`app/blueprints/products/routes.py`**
```python
from flask import Blueprint, request, jsonify
from app.models import db, Product, ProductDescription
from app.utils.auth import token_required
import uuid # For generating unique serial numbers

products_bp = Blueprint('products_bp', __name__)

@products_bp.route("/create/<int:desc_id>", methods=["POST"])
@token_required # Assuming only authenticated users can add new physical products
def create_product(desc_id):
    """Create a new physical product item based on a product description."""
    product_desc = db.session.get(ProductDescription, desc_id)
    if not product_desc:
        return jsonify({"message": "Product description not found"}), 404

    # Generate a unique serial number for the new product
    serial_number = str(uuid.uuid4()) 
    product = Product(desc_id=desc_id, serial_number=serial_number)
    
    db.session.add(product)
    db.session.commit()

    return jsonify({
        "message": "Product item created",
        "serial_number": product.serial_number,
        "desc_id": product.desc_id
    }), 201
```

### Shopping Cart & Orders (`app/blueprints/carts/routes.py`, `app/blueprints/orders/routes.py`)

Manages user shopping carts and the process of placing orders.

**`app/blueprints/carts/routes.py`**
```python
from flask import Blueprint, request, jsonify
from app.models import db, Cart, CartItem, ProductDescription
from app.extensions import ma # Marshmallow instance
from app.utils.auth import token_required

carts_bp = Blueprint('carts_bp', __name__)

# Schemas would be defined in app/blueprints/carts/schemas.py
# product_descriptions_schema = ProductDescriptionSchema(many=True) # For displaying cart items

@carts_bp.route("/my-cart", methods=["GET"])
@token_required
def view_my_cart():
    """Retrieve the logged-in user's shopping cart contents."""
    user_id = request.logged_in_user_id
    cart = db.session.query(Cart).filter_by(user_id=user_id).first()
    if not cart:
        # Create a cart if one doesn't exist for the user (or handle as error)
        return jsonify({"message": "Cart not found for user"}), 404

    # Get product descriptions for items in the cart
    cart_items = db.session.query(CartItem).filter_by(cart_id=cart.id).all()
    # Assuming ProductDescriptionSchema can jsonify these
    products_in_cart = [item.description for item in cart_items]

    return product_descriptions_schema.jsonify(products_in_cart), 200

@carts_bp.route("/add-item/<int:desc_id>", methods=["POST"])
@token_required
def add_to_cart(desc_id):
    """Add a product description to the logged-in user's cart."""
    user_id = request.logged_in_user_id
    cart = db.session.query(Cart).filter_by(user_id=user_id).first()
    if not cart:
        # Create cart if it doesn't exist
        cart = Cart(user_id=user_id)
        db.session.add(cart)
        db.session.flush() # To get cart ID

    product_desc = db.session.get(ProductDescription, desc_id)
    if not product_desc:
        return jsonify({"message": "Product description not found"}), 404

    # Check if item already in cart, update quantity or add new
    cart_item = db.session.query(CartItem).filter_by(cart_id=cart.id, desc_id=desc_id).first()
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = CartItem(cart_id=cart.id, desc_id=desc_id, quantity=1)
        db.session.add(cart_item)
    
    db.session.commit()
    return jsonify({"message": f"Item {product_desc.name} added/updated in cart"}), 200

@carts_bp.route("/remove-item/<int:desc_id>", methods=["DELETE"])
@token_required
def remove_from_cart(desc_id):
    """Remove a product description from the logged-in user's cart."""
    user_id = request.logged_in_user_id
    cart = db.session.query(Cart).filter_by(user_id=user_id).first()
    if not cart:
        return jsonify({"message": "Cart not found for user"}), 404
    
    cart_item = db.session.query(CartItem).filter_by(cart_id=cart.id, desc_id=desc_id).first()
    if not cart_item:
        return jsonify({"message": "Item not in cart"}), 404

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        db.session.commit()
        return jsonify({"message": f"Quantity of {cart_item.description.name} decreased in cart"}), 200
    else:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({"message": f"Item {cart_item.description.name} removed from cart"}), 204
```

**`app/blueprints/orders/routes.py`**
```python
from flask import Blueprint, request, jsonify
from datetime import date, timedelta
from app.models import db, User, Order, Product, CartItem
from app.extensions import ma # Marshmallow instance
from app.utils.auth import token_required

orders_bp = Blueprint('orders_bp', __name__)

# Order schema (defined elsewhere)
# order_schema = OrderSchema()

@orders_bp.route("/create", methods=["POST"])
@token_required
def create_order():
    """Create a new order from the logged-in user's shopping cart."""
    user_id = request.logged_in_user_id
    user = db.session.get(User, user_id)
    if not user or not user.cart:
        return jsonify({"message": "User or cart not found"}), 404

    cart_items = user.cart.items
    if not cart_items:
        return jsonify({"message": "Cart is empty, cannot create order"}), 400

    total_amount = sum(item.description.price * item.quantity for item in cart_items)

    new_order = Order(
        user_id=user.id,
        order_date=date.today(),
        delivery_date=date.today() + timedelta(days=7), # Estimated 7 day delivery
        total=total_amount,
        status='pending'
    )
    db.session.add(new_order)
    db.session.flush() # Get new_order.id

    # For each item in cart, convert it into a sold product or clear from cart
    # This example simply clears cart and links the order
    for cart_item in cart_items:
        # Example: Link existing products to the order
        # Or, create new 'OrderItem' entries, etc.
        # This implementation just empties the cart and records total
        db.session.delete(cart_item) # Remove cart item once ordered

    db.session.commit()
    return jsonify({"message": f"Order {new_order.id} placed successfully!"}), 201
```

---

## See Also

-   **[Flask REST API Development Guide](../guides/Flask_REST_API_Development_Guide.md)** - For building scalable web APIs with Flask.
-   **[API Authentication Guide](../guides/API_Authentication_Guide.md)** - Detailed guide on API security with JWT.
-   **[SQL and SQLAlchemy Cheat Sheet](../cheatsheets/SQL_and_SQLAlchemy_Cheat_Sheet.md)** - For database setup and ORM details.
-   **[Data Structures Cheat Sheet](../cheatsheets/Data_Structures_Cheat_Sheet.md)** - For understanding data models.