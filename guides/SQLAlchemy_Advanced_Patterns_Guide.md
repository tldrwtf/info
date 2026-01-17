# SQLAlchemy Advanced Patterns Guide

---

## Table of Contents

1. [Session Management Patterns](#session-management-patterns)
2. [Query Optimization](#query-optimization)
3. [Complex Relationships](#complex-relationships)
4. [Association Objects vs Association Tables](#association-objects-vs-association-tables)
5. [Self-Referential Relationships](#self-referential-relationships)
6. [Lazy Loading Strategies](#lazy-loading-strategies)
7. [Cascade Operations](#cascade-operations)
8. [Transaction Handling](#transaction-handling)
9. [Session Lifecycle Best Practices](#session-lifecycle-best-practices)
10. [Production Patterns](#production-patterns)

---

## Session Management Patterns

### Basic Session Setup

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create engine
engine = create_engine('sqlite:///database.db', echo=False)

# Create session factory
Session = sessionmaker(bind=engine)

# Create session instance
session = Session()
```

### Session Lifecycle in CRUD Operations

**CREATE:**
```python
def create_user(user_data):
    """Create new user with proper session handling."""
    try:
        new_user = Users(**user_data)
        session.add(new_user)
        session.commit()
        return new_user
    except Exception as e:
        session.rollback()  # IMPORTANT: Roll back on error
        print(f"Error creating user: {e}")
        return None
```

### Using flush() vs commit()

Understanding when to use flush() instead of commit() is critical for working with auto-generated IDs and multi-step transactions.

#### The Difference

**commit():**
- Sends SQL to database AND commits the transaction
- Makes changes permanent
- Releases locks
- Cannot be rolled back

**flush():**
- Sends SQL to database but does NOT commit
- Makes auto-generated IDs available (id, created_at, etc.)
- Keeps transaction open
- Can still be rolled back

#### Pattern: Accessing Auto-Generated IDs

Common scenario: Create a user and immediately create their cart using the user's ID.

```python
from sqlalchemy.orm import Session
from models import User, Cart

def register_user_with_cart(session: Session, user_data):
    """Register user and create cart in same transaction."""
    try:
        # Create user
        user = User(**user_data)
        session.add(user)

        # flush() to get auto-generated user.id
        session.flush()

        # Now user.id is available!
        new_cart = Cart(user_id=user.id)
        session.add(new_cart)

        # Commit both together
        session.commit()

        return user
    except Exception as e:
        session.rollback()
        raise e
```

#### Why This Matters

Without flush(), trying to access `user.id` before commit would fail:

```python
# WRONG - This fails!
user = User(username="alice")
session.add(user)
cart = Cart(user_id=user.id)  # ERROR: user.id is None!
```

#### Common Use Cases

1. **Multi-entity creation with foreign keys**
   ```python
   order = Order(user_id=current_user.id)
   session.add(order)
   session.flush()  # Get order.id

   item1 = OrderItem(order_id=order.id, product_id=1)
   item2 = OrderItem(order_id=order.id, product_id=2)
   session.add_all([item1, item2])
   session.commit()
   ```

2. **Enforcing database constraints before final commit**
   ```python
   user = User(email="test@example.com")
   session.add(user)
   session.flush()  # Check unique constraint immediately
   # If constraint violated, exception raised here
   ```

3. **Logging or audit trails**
   ```python
   record = AuditRecord(action="create_user")
   session.add(record)
   session.flush()  # Get timestamp and ID

   # Use record.id for related entries
   detail = AuditDetail(audit_id=record.id, field="email")
   session.add(detail)
   session.commit()
   ```

#### Best Practices

- Use flush() when you need auto-generated values mid-transaction
- Always follow flush() with commit() eventually
- Handle exceptions to rollback properly
- Don't overuse - commit() when the transaction is complete

#### Key Differences Table

| Aspect | flush() | commit() |
|--------|---------|----------|
| Sends SQL to DB | Yes | Yes |
| Commits transaction | No | Yes |
| Makes changes permanent | No | Yes |
| Auto-generated IDs available | Yes | Yes |
| Can rollback after | Yes | No |
| Typical use | Mid-transaction | End of transaction |

**READ:**
```python
# Get by primary key (most efficient)
user = session.get(Users, user_id)

# Query with filter
user = session.query(Users).where(Users.email == email).first()

# Query all
all_users = session.query(Users).all()

# Query with multiple conditions
active_admins = session.query(Users).where(
    Users.is_active == True,
    Users.role == 'admin'
).all()
```

**UPDATE:**
```python
def update_user(user_id, updates):
    """Update user with transaction safety."""
    try:
        user = session.get(Users, user_id)
        if not user:
            return None

        # Update attributes
        for key, value in updates.items():
            if hasattr(user, key):
                setattr(user, key, value)

        session.commit()
        return user
    except Exception as e:
        session.rollback()
        print(f"Error updating user: {e}")
        return None
```

**DELETE:**
```python
def delete_user(user_id):
    """Delete user with confirmation."""
    try:
        user = session.get(Users, user_id)
        if not user:
            return False

        session.delete(user)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Error deleting user: {e}")
        return False
```

### Context Manager Pattern (Recommended)

```python
from contextlib import contextmanager

@contextmanager
def get_db_session():
    """Provide transactional scope with automatic cleanup."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

# Usage
def create_user(user_data):
    with get_db_session() as session:
        new_user = Users(**user_data)
        session.add(new_user)
    # Auto-commit, auto-rollback, auto-close
    return new_user
```

---

## Query Optimization

### N+1 Query Problem

**Problem:**
```python
# This generates N+1 queries!
owner = session.get(Owners, 1)  # Query 1

for pet in owner.pets:  # Query 2, 3, 4... for each pet
    print(pet.name)
    for appointment in pet.appointments:  # Even more queries!
        print(appointment.status)
```

**Solution 1: Joined Load (Single Query)**
```python
from sqlalchemy.orm import joinedload

# Load everything in one query with JOINs
owner = session.query(Owners).options(
    joinedload(Owners.pets).joinedload(Pets.appointments)
).get(1)

# No additional queries needed
for pet in owner.pets:
    for appointment in pet.appointments:
        print(appointment.status)
```

**Solution 2: Select In Load (Two Queries)**
```python
from sqlalchemy.orm import selectinload

# Load with SELECT IN for better performance with many relationships
owners = session.query(Owners).options(
    selectinload(Owners.pets).selectinload(Pets.appointments)
).all()
```

### Query Optimization Techniques

**1. Use `.first()` for Single Results:**
```python
# Good - stops after finding first match
user = session.query(Users).where(Users.email == email).first()

# Bad - loads all matching rows
user = session.query(Users).where(Users.email == email).all()[0]
```

**2. Select Specific Columns:**
```python
# Only load needed columns
usernames = session.query(Users.username, Users.email).all()

# vs loading entire objects
users = session.query(Users).all()  # Loads all columns
```

**3. Use Pagination:**
```python
def get_paginated_users(page=1, per_page=20):
    """Get paginated results."""
    offset = (page - 1) * per_page
    return session.query(Users).limit(per_page).offset(offset).all()
```

**4. Count Efficiently:**
```python
from sqlalchemy import func

# Efficient count
user_count = session.query(func.count(Users.id)).scalar()

# vs inefficient count
user_count = len(session.query(Users).all())  # Loads all records!
```

**5. Bulk Operations:**
```python
# Bulk insert (more efficient than individual commits)
users = [
    Users(username=f"user{i}", email=f"user{i}@example.com")
    for i in range(1000)
]
session.bulk_save_objects(users)
session.commit()

# Bulk update
session.query(Users).filter(Users.is_active == False).update(
    {"status": "inactive"},
    synchronize_session=False
)
session.commit()
```

---

## Complex Relationships

### One-to-Many Relationships

```python
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Owners(Base):
    __tablename__ = 'owners'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True)

    # One-to-many: One owner has many pets
    pets: Mapped[list["Pets"]] = relationship(
        "Pets",
        back_populates="owner"
    )

class Pets(Base):
    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    species: Mapped[str] = mapped_column(String(50))
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('owners.id'))

    # Many-to-one: Many pets belong to one owner
    owner: Mapped["Owners"] = relationship(
        "Owners",
        back_populates="pets"
    )
```

**Usage:**
```python
# Navigate from owner to pets
owner = session.get(Owners, 1)
for pet in owner.pets:
    print(f"{pet.name} ({pet.species})")

# Navigate from pet to owner
pet = session.get(Pets, 1)
print(f"Owner: {pet.owner.name}")

# Add pet to owner
new_pet = Pets(name="Fluffy", species="Cat")
owner.pets.append(new_pet)
session.commit()
```

### Many-to-Many Relationships

**Simple Many-to-Many (Association Table):**
```python
from sqlalchemy import Table, Column, Integer, ForeignKey

# Association table (no additional data)
student_clubs = Table(
    "student_clubs",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("club_id", Integer, ForeignKey("clubs.id"))
)

class Students(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))

    # Many-to-many relationship
    clubs: Mapped[list["Clubs"]] = relationship(
        "Clubs",
        secondary=student_clubs,
        back_populates="students"
    )

class Clubs(Base):
    __tablename__ = "clubs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(500))

    students: Mapped[list["Students"]] = relationship(
        "Students",
        secondary=student_clubs,
        back_populates="clubs"
    )
```

**Usage:**
```python
# Add student to club
student = session.get(Students, 1)
club = session.get(Clubs, 1)

student.clubs.append(club)
session.commit()

# Remove student from club
student.clubs.remove(club)
session.commit()

# Access student's clubs
for club in student.clubs:
    print(club.name)

# Access club's students
for student in club.students:
    print(f"{student.first_name} {student.last_name}")
```

---

## Association Objects vs Association Tables

### When to Use Association Tables

Use for **simple many-to-many** with no additional metadata:

```python
# Just linking users and posts (likes)
likes = Table(
    "likes",
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('post_id', Integer, ForeignKey('posts.id'))
)

class Users(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    liked_posts: Mapped[list["Posts"]] = relationship(
        "Posts",
        secondary="likes",
        back_populates="liked_by"
    )

# Usage: Simple append/remove
user.liked_posts.append(post)
user.liked_posts.remove(post)
```

### When to Use Association Objects

Use for **rich many-to-many** with additional attributes:

```python
from datetime import datetime

class Enrollments(Base):
    """Association object with extra metadata."""
    __tablename__ = "enrollments"

    id: Mapped[int] = mapped_column(primary_key=True)

    # Foreign keys
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("students.id"))
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey('courses.id'))

    # Additional metadata about the relationship
    enrolled_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    grade: Mapped[str] = mapped_column(String(2), nullable=True)
    notes: Mapped[str] = mapped_column(String(500), nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="active")

    # Relationships
    student: Mapped["Students"] = relationship(
        "Students",
        back_populates='enrollments'
    )
    course: Mapped["Courses"] = relationship(
        "Courses",
        back_populates='enrollments'
    )

class Students(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))

    enrollments: Mapped[list["Enrollments"]] = relationship(
        "Enrollments",
        back_populates="student"
    )

class Courses(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))

    enrollments: Mapped[list["Enrollments"]] = relationship(
        "Enrollments",
        back_populates="course"
    )
```

**Usage:**
```python
# Enroll student in course with metadata
enrollment = Enrollments(
    student_id=student.id,
    course_id=course.id,
    grade="A",
    notes="Excellent participation"
)
session.add(enrollment)
session.commit()

# Access enrollment metadata
for enrollment in student.enrollments:
    print(f"Course: {enrollment.course.title}")
    print(f"Grade: {enrollment.grade}")
    print(f"Enrolled: {enrollment.enrolled_date}")

# Update grade
enrollment = session.query(Enrollments).where(
    Enrollments.student_id == student_id,
    Enrollments.course_id == course_id
).first()
enrollment.grade = "A+"
session.commit()
```

---

### Real-World Example: Shopping Cart with Association Object

Association objects are needed when the many-to-many relationship itself has attributes. This example shows when and how to use them.

#### The Scenario

**Requirement:** Users can add products to their cart
- Many carts can contain many products
- BUT we need to track HOW MANY of each product

**Wrong Approach - Simple Association Table:**

```python
# This only tracks which products are in which carts
cart_products = Table('cart_products',
    Column('cart_id', ForeignKey('carts.id')),
    Column('product_id', ForeignKey('products.id'))
)
```

**Problem:** Where do we store quantity? We can't add columns to a relationship table.

#### The Solution - Association Object Pattern

Create a full model class for the relationship:

```python
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, UniqueConstraint

class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    # Relationship to items (association objects)
    items: Mapped[list["CartItem"]] = relationship(
        "CartItem",
        back_populates="cart",
        cascade="all, delete-orphan"  # Delete items when cart is deleted
    )

    # Convenience property to get products directly
    @property
    def products(self):
        return [item.product for item in self.items]

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[float]

    # Relationship back to cart items
    cart_items: Mapped[list["CartItem"]] = relationship(
        "CartItem",
        back_populates="product"
    )

class CartItem(Base):  # ASSOCIATION OBJECT
    """
    Represents one product in a cart with quantity.
    This is NOT a simple Table - it's a full model.
    """
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True)

    # Foreign keys to both sides
    cart_id: Mapped[int] = mapped_column(ForeignKey('carts.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))

    # EXTRA ATTRIBUTE - This is why we need association object!
    quantity: Mapped[int] = mapped_column(Integer, default=1)

    # Relationships to both sides
    cart: Mapped["Cart"] = relationship("Cart", back_populates="items")
    product: Mapped["Product"] = relationship("Product", back_populates="cart_items")

    # Prevent duplicate products in same cart
    __table_args__ = (
        UniqueConstraint('cart_id', 'product_id', name='_cart_product_uc'),
    )

    def __repr__(self):
        return f"<CartItem cart={self.cart_id} product={self.product_id} qty={self.quantity}>"
```

#### Using the Association Object

**Add product to cart:**

```python
from sqlalchemy.orm import Session

def add_to_cart(session: Session, cart_id: int, product_id: int, quantity: int = 1):
    """Add product to cart or update quantity."""

    # Check if item already in cart
    existing = session.query(CartItem)\
        .filter_by(cart_id=cart_id, product_id=product_id)\
        .first()

    if existing:
        # Update quantity
        existing.quantity += quantity
    else:
        # Create new cart item
        item = CartItem(
            cart_id=cart_id,
            product_id=product_id,
            quantity=quantity
        )
        session.add(item)

    session.commit()
```

**View cart with details:**

```python
def get_cart_total(session: Session, cart_id: int):
    """Calculate cart total price."""
    cart = session.get(Cart, cart_id)

    total = 0
    for item in cart.items:
        item_total = item.product.price * item.quantity
        print(f"{item.product.name}: ${item.product.price} x {item.quantity} = ${item_total}")
        total += item_total

    print(f"Total: ${total}")
    return total

# Example output:
# Laptop: $999.99 x 2 = $1999.98
# Mouse: $24.99 x 5 = $124.95
# Total: $2124.93
```

**Remove item from cart:**

```python
def remove_from_cart(session: Session, cart_id: int, product_id: int):
    """Remove product from cart."""
    item = session.query(CartItem)\
        .filter_by(cart_id=cart_id, product_id=product_id)\
        .first()

    if item:
        session.delete(item)
        session.commit()
```

#### When to Use Association Object vs Table

| Use Association **Table** | Use Association **Object** |
|---------------------------|----------------------------|
| **Simple linking only** | **Need extra attributes** |
| No timestamps needed | Track created_at, updated_at |
| No status/state tracking | Store status, notes, metadata |
| No quantity/count | Track quantity, score, rating |
| **Examples:** | **Examples:** |
| - Student enrolls in courses | - Student in course (with grade) |
| - User likes posts | - Product in cart (with quantity) |
| - User follows user | - User rates movie (with rating) |
| - Tags on articles | - Order items (with price snapshot) |

**Decision Tree:**

```
Do you need to store data ABOUT the relationship?
    │
    ├─ No  → Use Association Table (Table object)
    │
    └─ Yes → Use Association Object (Model class)
           │
           └─ Examples of "data about relationship":
              - Quantity (how many in cart)
              - Grade (what score in course)
              - Timestamp (when was relationship created)
              - Status (active/inactive relationship)
              - Metadata (notes, tags on relationship)
```

#### Advanced Pattern: Price Snapshots in Orders

Association objects are critical for e-commerce order items:

```python
class OrderItem(Base):
    """
    Order item with price snapshot.
    Stores price AT TIME OF PURCHASE, not current product price.
    """
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))

    quantity: Mapped[int]
    price_at_purchase: Mapped[float]  # Snapshot! Important for historical accuracy

    order: Mapped["Order"] = relationship("Order", back_populates="items")
    product: Mapped["Product"] = relationship("Product")

    @property
    def subtotal(self):
        return self.quantity * self.price_at_purchase
```

**Why price snapshot matters:**

```python
# Create order
order = Order(user_id=user.id)
item = OrderItem(
    order=order,
    product=laptop,
    quantity=1,
    price_at_purchase=laptop.price  # $999 today
)

db.session.add_all([order, item])
db.session.commit()

# 1 year later, price changes
laptop.price = 1299  # Price increased

# Order still shows original price
print(item.price_at_purchase)  # $999 (correct historical record)
print(item.product.price)      # $1299 (current price)
```

#### Common Patterns Summary

1. **cart_items:** quantity
2. **order_items:** quantity, price_at_purchase
3. **student_courses:** grade, enrolled_date
4. **user_ratings:** rating_value, review_text, created_at
5. **project_memberships:** role, joined_date, permissions

---

## Self-Referential Relationships

Self-referential relationships allow a model to relate to itself (e.g., users following users).

### Implementation

```python
# Association table for followers
following = Table(
    'following',
    Base.metadata,
    Column('follower_id', Integer, ForeignKey('users.id')),
    Column('followed_id', Integer, ForeignKey('users.id'))
)

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    bio: Mapped[str] = mapped_column(String(300))

    # Self-referential many-to-many
    following: Mapped[list['Users']] = relationship(
        'Users',
        secondary="following",
        primaryjoin="Users.id==following.c.follower_id",
        secondaryjoin="Users.id==following.c.followed_id",
        backref='followers'
    )
```

**Understanding the Joins:**

- `primaryjoin`: How to join from current instance to association table
  - `Users.id==following.c.follower_id` matches user ID with follower_id
- `secondaryjoin`: How to join from association table to related instances
  - `Users.id==following.c.followed_id` matches user ID with followed_id
- `backref='followers'`: Creates reverse relationship automatically

**Usage:**
```python
# Get users
alice = session.query(Users).where(Users.username == "alice").first()
bob = session.query(Users).where(Users.username == "bob").first()

# Alice follows Bob
alice.following.append(bob)
session.commit()

# Who does Alice follow?
for user in alice.following:
    print(f"Alice follows {user.username}")

# Who follows Bob? (using backref)
for follower in bob.followers:
    print(f"{follower.username} follows Bob")

# Check if following
if bob in alice.following:
    print("Alice follows Bob")

# Unfollow
alice.following.remove(bob)
session.commit()
```

---

## Lazy Loading Strategies

SQLAlchemy offers multiple strategies for loading related data.

### Loading Strategy Options

**1. `select` (default) - Lazy Loading:**
```python
class Owners(Base):
    __tablename__ = 'owners'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # Default lazy='select' - loads on access
    pets: Mapped[list["Pets"]] = relationship("Pets", lazy='select')

# Triggers separate query when accessing pets
owner = session.get(Owners, 1)
for pet in owner.pets:  # Query executed here
    print(pet.name)
```

**2. `joined` - Eager Loading with JOIN:**
```python
# Define at model level
pets: Mapped[list["Pets"]] = relationship("Pets", lazy='joined')

# Or use at query level
owner = session.query(Owners).options(
    joinedload(Owners.pets)
).get(1)
```

**3. `selectin` - Eager Loading with SELECT IN:**
```python
# More efficient for collections
owners = session.query(Owners).options(
    selectinload(Owners.pets)
).all()
```

**4. `subquery` - Eager Loading with Subquery:**
```python
owners = session.query(Owners).options(
    subqueryload(Owners.pets)
).all()
```

**5. `noload` - Never Load:**
```python
# Don't load relationship at all
owner = session.query(Owners).options(
    noload(Owners.pets)
).get(1)
```

**6. `raise` - Raise Error on Access:**
```python
# Helpful for catching unintended access
pets: Mapped[list["Pets"]] = relationship("Pets", lazy='raise')
```

### Choosing the Right Strategy

```python
# Use selectinload for one-to-many
owners = session.query(Owners).options(
    selectinload(Owners.pets)
).all()

# Use joinedload for many-to-one
pets = session.query(Pets).options(
    joinedload(Pets.owner)
).all()

# Nested loading
owners = session.query(Owners).options(
    selectinload(Owners.pets).joinedload(Pets.appointments)
).all()
```

---

## Cascade Operations

Cascades define what happens to related objects when operations are performed on a parent.

### Cascade Options

```python
class Owners(Base):
    __tablename__ = 'owners'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # With cascades
    pets: Mapped[list["Pets"]] = relationship(
        "Pets",
        back_populates="owner",
        cascade="all, delete-orphan"
    )
```

**Available Cascades:**

- `save-update` (default): Add parent → add children
- `delete`: Delete parent → delete children
- `delete-orphan`: Remove from collection → delete
- `merge`: Merge parent → merge children
- `refresh`: Refresh parent → refresh children
- `expunge`: Expunge parent → expunge children
- `all`: Shorthand for save-update, merge, refresh, expunge, delete

### Cascade Examples

**Strong Ownership (all, delete-orphan):**
```python
class Owners(Base):
    pets: Mapped[list["Pets"]] = relationship(
        "Pets",
        cascade="all, delete-orphan"
    )

# Delete owner deletes all pets
owner = session.get(Owners, 1)
session.delete(owner)
session.commit()  # Pets automatically deleted

# Remove from collection deletes pet
owner.pets.remove(pet)
session.commit()  # Pet deleted from database
```

**Weak Ownership (delete only):**
```python
class BlogPost(Base):
    comments: Mapped[list["Comment"]] = relationship(
        "Comment",
        cascade="delete"
    )

# Delete post deletes comments
# But removing from collection doesn't delete
```

**No Cascade (independent entities):**
```python
class Appointments(Base):
    # Vet is independent - no cascade
    vet: Mapped["Vets"]] = relationship("Vets")

# Deleting appointment doesn't delete vet
```

---

## Transaction Handling

### Basic Transaction Pattern

```python
def transfer_pet_ownership(pet_id, old_owner_id, new_owner_id):
    """Transfer pet with transactional safety."""
    try:
        # All operations in one transaction
        pet = session.get(Pets, pet_id)
        old_owner = session.get(Owners, old_owner_id)
        new_owner = session.get(Owners, new_owner_id)

        # Verify ownership
        if pet.owner_id != old_owner_id:
            raise ValueError("Pet doesn't belong to old owner")

        # Transfer
        pet.owner_id = new_owner_id

        # Commit all changes together
        session.commit()
        return True

    except Exception as e:
        session.rollback()  # Rollback on any error
        print(f"Transfer failed: {e}")
        return False
```

### Nested Transactions (Savepoints)

```python
def create_user_with_profile():
    """Create user with optional profile using savepoints."""
    try:
        # Main transaction
        user = Users(username="alice")
        session.add(user)

        # Nested transaction (savepoint)
        savepoint = session.begin_nested()
        try:
            # Try to add profile
            profile = Profiles(user=user, bio="Hello")
            session.add(profile)
        except Exception as e:
            # Roll back only the profile
            savepoint.rollback()
            print(f"Profile creation failed: {e}")

        # User is still added even if profile fails
        session.commit()

    except Exception as e:
        session.rollback()
        print(f"User creation failed: {e}")
```

### Context Manager for Transactions

```python
@contextmanager
def transaction_scope():
    """Provide transactional scope."""
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise

# Usage
def create_user_and_posts(user_data, posts_data):
    with transaction_scope():
        user = Users(**user_data)
        session.add(user)

        for post_data in posts_data:
            post = Posts(user=user, **post_data)
            session.add(post)

        # All committed together or all rolled back
```

---

## Session Lifecycle Best Practices

### Anti-Pattern: Global Session

```python
# DON'T DO THIS
Session = sessionmaker(bind=engine)
session = Session()  # Global session - problems!

# Problems:
# - Not thread-safe
# - Never closed
# - Holds connections indefinitely
# - Accumulates objects
```

### Pattern 1: Scoped Session (Thread-Safe)

```python
from sqlalchemy.orm import scoped_session

# Thread-local session
Session = scoped_session(sessionmaker(bind=engine))

def get_user(user_id):
    session = Session()
    try:
        user = session.get(Users, user_id)
        return user
    finally:
        Session.remove()  # Clean up thread-local session
```

### Pattern 2: Session per Request (Web Apps)

```python
# Flask example
from flask import g

def get_session():
    """Get session for current request."""
    if 'session' not in g:
        g.session = Session()
    return g.session

@app.teardown_appcontext
def cleanup(exception=None):
    """Clean up session after request."""
    session = g.pop('session', None)
    if session is not None:
        session.close()
```

### Pattern 3: Context Manager (Best Practice)

```python
@contextmanager
def get_db_session():
    """Context manager for database sessions."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

# Usage
def create_user(user_data):
    with get_db_session() as session:
        new_user = Users(**user_data)
        session.add(new_user)
        # Auto-commit, auto-rollback, auto-close
    return new_user
```

---

## Production Patterns

### Complete Production-Ready Session Manager

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import QueuePool
from contextlib import contextmanager
import logging

logger = logging.getLogger(__name__)

class DatabaseManager:
    """Production-ready database manager."""

    def __init__(self, database_url, echo=False):
        """
        Initialize database manager.

        Args:
            database_url: Database connection string
            echo: Whether to log SQL queries
        """
        # Create engine with connection pooling
        self.engine = create_engine(
            database_url,
            echo=echo,
            poolclass=QueuePool,
            pool_size=10,
            max_overflow=20,
            pool_pre_ping=True  # Verify connections before use
        )

        # Create session factory
        session_factory = sessionmaker(
            bind=self.engine,
            expire_on_commit=False  # Don't expire objects after commit
        )

        # Thread-safe scoped session
        self.Session = scoped_session(session_factory)

    @contextmanager
    def session_scope(self):
        """Provide transactional scope with proper error handling."""
        session = self.Session()
        try:
            yield session
            session.commit()
            logger.debug("Transaction committed successfully")
        except Exception as e:
            session.rollback()
            logger.error(f"Transaction rolled back: {e}")
            raise
        finally:
            session.close()
            logger.debug("Session closed")

    def create_tables(self, base):
        """Create all tables."""
        base.metadata.create_all(self.engine)
        logger.info("Database tables created")

    def drop_tables(self, base):
        """Drop all tables."""
        base.metadata.drop_all(self.engine)
        logger.warning("All database tables dropped")

    def cleanup(self):
        """Clean up database connections."""
        self.Session.remove()
        self.engine.dispose()
        logger.info("Database connections cleaned up")

# Usage
db_manager = DatabaseManager("sqlite:///app.db")

def create_user(user_data):
    with db_manager.session_scope() as session:
        user = Users(**user_data)
        session.add(user)
    return user
```

### Error Handling with Specific Exceptions

```python
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

def safe_create_user(user_data):
    """Create user with specific error handling."""
    try:
        with db_manager.session_scope() as session:
            user = Users(**user_data)
            session.add(user)
        return user, None

    except IntegrityError as e:
        # Duplicate username/email
        logger.warning(f"Integrity error: {e}")
        return None, "User with this email already exists"

    except SQLAlchemyError as e:
        # Other database errors
        logger.error(f"Database error: {e}")
        return None, "Database error occurred"

    except Exception as e:
        # Unexpected errors
        logger.exception(f"Unexpected error: {e}")
        return None, "An unexpected error occurred"
```

---

## Summary

### Best Practices Checklist

- [ ] Use context managers for session lifecycle
- [ ] Always rollback on exceptions
- [ ] Use eager loading to prevent N+1 queries
- [ ] Configure cascades appropriately
- [ ] Use specific exception handling
- [ ] Close sessions after use
- [ ] Use connection pooling in production
- [ ] Log database operations
- [ ] Test transaction rollback scenarios
- [ ] Profile queries for performance

### Related Resources

- [SQL & SQLAlchemy](../cheatsheets/SQL_and_SQLAlchemy_Cheat_Sheet.md) - Basic SQLAlchemy operations
- [SQLAlchemy Relationships](SQLAlchemy_Relationships_Guide.md) - Relationship fundamentals
- [Error Handling](../cheatsheets/Error_Handling_Cheat_Sheet.md) - Exception handling patterns
- [Flask REST API Development](Flask_REST_API_Development_Guide.md) - Using SQLAlchemy with Flask

[Back to Main](../README.md)