"""
SQLAlchemy ORM Models for Library Management System.

This module defines the database schema using SQLAlchemy 2.0+ style with:
- Modern Mapped type annotations for type safety
- Declarative base pattern for model definition
- Relationship patterns (One-to-Many, Many-to-Many)
- Foreign key constraints for referential integrity

Database Schema Overview:
┌─────────┐       ┌───────┐       ┌───────┐
│  Users  │───────│ Loans │───────│ Books │
└─────────┘  1:N  └───────┘  M:N  └───────┘

┌─────────┐  1:N  ┌───────┐  N:1  ┌──────────────────┐
│ Orders  │───────│ Items │───────│ ItemDescription  │
└─────────┘       └───────┘       └──────────────────┘

Relationship Types Explained:
- One-to-Many (1:N): One user has many loans
- Many-to-Many (M:N): One loan has many books, one book appears in many loans
- One-to-One: Could be implemented with uselist=False in relationship()
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Date, Column, ForeignKey, Table, DateTime, Float
from datetime import date, datetime, timedelta


# ============================================
# BASE CLASS FOR ORM MODELS
# ============================================
class Base(DeclarativeBase):
    """
    Base class for all ORM models using SQLAlchemy 2.0+ declarative style.

    All model classes inherit from this base to gain SQLAlchemy ORM capabilities.
    This provides:
    - Automatic table creation from class definitions
    - Type-safe column definitions with Mapped[]
    - Query interface for database operations
    - Relationship tracking between models

    The DeclarativeBase pattern is preferred over the older declarative_base()
    function for better IDE support and type checking.
    """
    pass
    # You can add common columns here that all models should have:
    # id: Mapped[int] = mapped_column(primary_key=True)
    # created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


# Initialize SQLAlchemy with our custom base class
# This db object will be used to interact with the database throughout the app
db = SQLAlchemy(model_class=Base)


# ============================================
# ASSOCIATION TABLE FOR MANY-TO-MANY RELATIONSHIP
# ============================================
loan_book = Table(
    "loan_book",  # Table name in database
    Base.metadata,  # Links this table to our Base's metadata
    Column("loan_id", ForeignKey("loans.id")),  # Foreign key to loans table
    Column("book_id", ForeignKey("books.id"))   # Foreign key to books table
)
"""
Association table for Many-to-Many relationship between Loans and Books.

Why use an association table?
- A loan can include multiple books (e.g., checking out 3 books at once)
- A book can appear in multiple loans over time (e.g., same book loaned to different users)
- This creates a Many-to-Many (M:N) relationship, which requires a junction table

Table Structure:
+----------+----------+
| loan_id  | book_id  |
+----------+----------+
|    1     |    5     |  <- Loan #1 includes Book #5
|    1     |    7     |  <- Loan #1 also includes Book #7
|    2     |    5     |  <- Loan #2 includes Book #5 (same book, different loan)
+----------+----------+

This is a "pure" association table with only foreign keys, no additional columns.
If you need extra data (like condition_when_borrowed), consider a full model class instead.

SQLAlchemy Note:
Using Table() instead of a model class for association tables is best practice when
the table only contains foreign keys and no other business logic.
"""


# ============================================
# USER MODEL
# ============================================
class Users(Base):
    """
    Represents a library user (patron or admin).

    This model demonstrates:
    - Primary key definition with mapped_column()
    - Type annotations with Mapped[] for type safety
    - One-to-Many relationship (one user has many loans)
    - Default values (role defaults to "User")

    Attributes:
        id: Unique identifier for each user (auto-incremented)
        first_name: User's first name (max 100 characters)
        last_name: User's last name (max 100 characters)
        email: Unique email address for login/contact (max 350 chars)
        phone: Contact phone number (stored as string to preserve formatting)
        password: Hashed password (never store plain text!)
        role: User role - either "User" or "Admin" (defaults to "User")
        loans: Collection of all loans associated with this user

    Relationships:
        loans: One-to-Many → One user can have multiple loans
               Accessible via user.loans (returns list of Loan objects)
    """
    __tablename__ = 'users'  # Explicit table name in database

    # Primary Key - Auto-incrementing integer
    id: Mapped[int] = mapped_column(primary_key=True)

    # String columns with maximum length constraints
    # Mapped[str] means this column is required (NOT NULL)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(350), unique=True)  # Unique constraint prevents duplicate emails
    phone: Mapped[str] = mapped_column(String(15))

    # Password storage - should always be hashed (e.g., with bcrypt or Werkzeug security)
    # NEVER store plain text passwords in production!
    password: Mapped[str] = mapped_column(String(150))

    # Role-based access control - defaults to "User" if not specified
    role: Mapped[str] = mapped_column(String(50), default="User")  # "User" or "Admin"

    # ===== RELATIONSHIP DEFINITION =====
    # One-to-Many: One user can have many loans
    # back_populates creates bidirectional relationship:
    #   - user.loans gets all loans for this user
    #   - loan.user gets the user who made the loan
    loans: Mapped[list['Loans']] = relationship('Loans', back_populates='user')


# ============================================
# LOANS MODEL
# ============================================
class Loans(Base):
    """
    Represents a book loan transaction.

    This model is the "junction" between Users and Books, demonstrating:
    - Many-to-One relationship with Users (many loans → one user)
    - Many-to-Many relationship with Books (via association table)
    - Foreign key constraints for referential integrity
    - Date fields for tracking loan duration

    Attributes:
        id: Unique loan transaction ID
        return_date: When the books should be returned
        borrow_date: When the books were checked out
        user_id: Foreign key linking to the Users table
        user: The User object who made this loan
        books: Collection of all Book objects included in this loan

    Relationships:
        user: Many-to-One → Many loans belong to one user
        books: Many-to-Many → One loan can have many books,
                              one book can be in many loans (over time)

    Example Usage:
        # Create a loan
        loan = Loans(
            borrow_date=date.today(),
            return_date=date.today() + timedelta(days=14),
            user_id=1
        )
        # Add books to the loan
        loan.books.append(book1)
        loan.books.append(book2)
    """
    __tablename__ = 'loans'

    id: Mapped[int] = mapped_column(primary_key=True)

    # Date fields - using Python's date type
    # SQLAlchemy automatically converts between Python dates and SQL DATE columns
    return_date: Mapped[date] = mapped_column(Date)
    borrow_date: Mapped[date] = mapped_column(Date)

    # ===== FOREIGN KEY TO USERS TABLE =====
    # This creates the Many-to-One relationship
    # Multiple loans can reference the same user_id
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    # ===== RELATIONSHIPS =====
    # Many-to-One: This loan belongs to one user
    # back_populates='loans' links to Users.loans attribute
    user: Mapped['Users'] = relationship('Users', back_populates='loans')

    # Many-to-Many: This loan can include many books
    # secondary='loan_book' references the association table defined above
    # back_populates='loans' links to Books.loans attribute
    books: Mapped[list['Books']] = relationship(secondary=loan_book, back_populates='loans')


# ============================================
# BOOKS MODEL
# ============================================
class Books(Base):
    """
    Represents a book in the library catalog.

    This model demonstrates:
    - Unique constraints (ISBN must be unique)
    - Many-to-Many relationship via association table
    - Simple attribute model (no complex nested data)

    Attributes:
        id: Unique book ID
        title: Book title (max 200 characters)
        author: Author name (max 200 characters)
        isbn: International Standard Book Number (unique, max 20 chars)
        loans: Collection of all Loan transactions this book appears in

    Relationships:
        loans: Many-to-Many → One book can be in many loans over time

    Note on Design:
        In a real library system, you might separate:
        - Book (the abstract work): "Pride and Prejudice"
        - BookCopy (physical/digital instances): 3 copies of "Pride and Prejudice"

        This simplified model treats each Books record as both the work and the copy.
    """
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)

    # Book metadata
    title: Mapped[str] = mapped_column(String(200))
    author: Mapped[str] = mapped_column(String(200))

    # ISBN with unique constraint - no two books can have the same ISBN
    # ISBN is the standard identifier for books (like a barcode)
    isbn: Mapped[str] = mapped_column(String(20), unique=True)

    # ===== RELATIONSHIP =====
    # Many-to-Many: This book can appear in many loans
    # secondary='loan_book' references the association table
    # back_populates='books' links to Loans.books attribute
    loans: Mapped[list['Loans']] = relationship(secondary=loan_book, back_populates='books')


# ============================================
# ORDERS MODEL
# ============================================
class Orders(Base):
    """
    Represents a purchase order in the library's bookstore system.

    This model demonstrates:
    - One-to-Many relationship (one order has many items)
    - Date fields with default values
    - Parent side of a parent-child relationship

    Attributes:
        id: Unique order ID
        order_date: Date the order was placed (defaults to today)
        items: Collection of all Items in this order

    Relationships:
        items: One-to-Many → One order contains many items

    Design Pattern:
        This follows the common Order/OrderItem pattern where:
        - Order: Contains order-level info (date, customer, total)
        - OrderItem (Items): Contains line items (product, quantity, price)
    """
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)

    # Date field with default value - automatically set to today if not specified
    # default= accepts a callable (date.today) that runs when the object is created
    order_date: Mapped[date] = mapped_column(Date, default=date.today())

    # ===== RELATIONSHIP =====
    # One-to-Many: One order has many items
    # back_populates creates bidirectional link:
    #   - order.items gets all items in this order
    #   - item.order gets the order that item belongs to
    items: Mapped[list['Items']] = relationship('Items', back_populates='order')


# ============================================
# ITEMS MODEL
# ============================================
class Items(Base):
    """
    Represents an individual item in an order (line item).

    This model demonstrates:
    - Two Many-to-One relationships (to Orders and ItemDescription)
    - Nullable foreign keys (order_id can be NULL)
    - Boolean fields for status tracking

    Attributes:
        id: Unique item ID
        is_sold: Whether this item has been sold (boolean flag)
        description_id: Foreign key to ItemDescription (what product this is)
        description: The ItemDescription object with product details
        order_id: Foreign key to Orders (which order this item is in, nullable)
        order: The Order object this item belongs to (can be None)

    Relationships:
        description: Many-to-One → Many items reference one ItemDescription
        order: Many-to-One → Many items belong to one Order

    Design Explanation:
        The separation between Items and ItemDescription allows:
        - ItemDescription: Template (product catalog entry)
        - Items: Instance (specific instance of that product)

        Example: ItemDescription = "MacBook Pro 16inch"
                 Items = Individual MacBook instances in inventory
    """
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)

    # Boolean field - tracks whether this item has been sold
    # default=False means new items are unsold by default
    is_sold: Mapped[bool] = mapped_column(default=False)

    # ===== FOREIGN KEY TO ITEM DESCRIPTION =====
    # Required relationship - every item must have a description
    description_id: Mapped[int] = mapped_column(ForeignKey('item_description.id'))

    # ===== FOREIGN KEY TO ORDERS =====
    # Optional relationship - items can exist without being in an order (inventory)
    # nullable=True allows this to be NULL in the database
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'), nullable=True)

    # ===== RELATIONSHIPS =====
    # Many-to-One: Many items share one product description
    description: Mapped['ItemDescription'] = relationship('ItemDescription', back_populates='items')

    # Many-to-One: Many items belong to one order (optional - can be None)
    order: Mapped['Orders'] = relationship('Orders', back_populates='items')


# ============================================
# ITEM DESCRIPTION MODEL
# ============================================
class ItemDescription(Base):
    """
    Represents a product in the catalog (template for items).

    This model demonstrates:
    - One-to-Many relationship (one description, many item instances)
    - Floating-point numbers for prices
    - Separation of product definition from inventory instances

    Attributes:
        id: Unique product ID
        name: Product name
        price: Product price (stored as float for decimal values)
        description: Product description/details
        items: Collection of all Item instances of this product

    Relationships:
        items: One-to-Many → One product description has many inventory items

    Example:
        # Create product definition
        product = ItemDescription(
            name="MacBook Pro 16inch",
            price=2499.99,
            description="16-inch Retina display, M3 Pro chip"
        )

        # Create 5 inventory items of this product
        for i in range(5):
            item = Items(description=product, is_sold=False)
            db.session.add(item)
    """
    __tablename__ = 'item_description'

    id: Mapped[int] = mapped_column(primary_key=True)

    # Product metadata
    name: Mapped[str] = mapped_column(String(200))

    # Price stored as float to handle decimal values (e.g., $19.99)
    # In production, consider using Decimal type for financial data
    # to avoid floating-point precision issues
    price: Mapped[float] = mapped_column(Float)

    description: Mapped[str] = mapped_column(String(500))

    # ===== RELATIONSHIP =====
    # One-to-Many: One product description can have many inventory items
    # back_populates='description' links to Items.description attribute
    items: Mapped[list['Items']] = relationship('Items', back_populates='description')


# ============================================
# KEY SQLALCHEMY CONCEPTS DEMONSTRATED
# ============================================
"""
1. MAPPED TYPE ANNOTATIONS (SQLAlchemy 2.0+):
   - Mapped[int]: Required (NOT NULL) integer column
   - Mapped[Optional[int]]: Optional (NULL allowed) integer column
   - Better IDE support and type checking than old style

2. RELATIONSHIP PATTERNS:

   a) One-to-Many (1:N):
      Parent side:  items: Mapped[list['Items']] = relationship(...)
      Child side:   order: Mapped['Orders'] = relationship(...)

      Database: Child table has foreign key to parent
      Usage: order.items returns list, item.order returns single object

   b) Many-to-Many (M:N):
      Both sides:   relationship(secondary=association_table, ...)

      Database: Requires association (junction) table with two foreign keys
      Usage: Both sides return lists (loan.books and book.loans)

3. BACK_POPULATES:
   Creates bidirectional relationships. Always define on BOTH sides:
   - Parent: relationship('Child', back_populates='parent')
   - Child:  relationship('Parent', back_populates='children')

4. CASCADE BEHAVIORS (not shown but important):
   You can add cascade='all, delete-orphan' to relationships to control
   what happens when parent objects are deleted. Example:
   items: Mapped[list['Items']] = relationship('Items', cascade='all, delete-orphan')
   This means: if an Order is deleted, all its Items are automatically deleted.

5. LAZY LOADING (not shown but important):
   By default, relationships use lazy loading (data loaded when accessed).
   You can change this with lazy= parameter:
   - lazy='select': Default, load when accessed
   - lazy='joined': Load with JOIN query
   - lazy='subquery': Load with subquery
   - lazy='noload': Never load automatically

QUERY EXAMPLES:
    # Get user and their loans
    user = db.session.get(Users, 1)
    user_loans = user.loans  # Automatically fetches related loans

    # Get loan with books
    loan = db.session.get(Loans, 1)
    loan_books = loan.books  # Fetches books through association table

    # Filter and join
    active_loans = db.session.query(Loans)\\
        .join(Users)\\
        .filter(Users.email == 'alice@example.com')\\
        .all()
"""
