# SQLAlchemy CRUD Guide

This guide provides a comprehensive overview of Create, Read, Update, and Delete (CRUD) operations using SQLAlchemy, Python's SQL toolkit and Object Relational Mapper (ORM). It focuses on practical examples, demonstrating how to interact with a database through Python objects.

---

## 1. Introduction to SQLAlchemy CRUD

SQLAlchemy is a powerful ORM that allows developers to interact with relational databases using Python objects instead of raw SQL. This simplifies database operations and makes code more maintainable and Pythonic. CRUD operations are the four basic functions of persistent storage:
*   **Create**: Adding new data records.
*   **Read**: Retrieving existing data records.
*   **Update**: Modifying existing data records.
*   **Delete**: Removing data records.

---

## 2. Model Definition

First, let's define the SQLAlchemy models for a simple social media application. These models map Python classes to database tables.

```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship
from datetime import datetime

# Database setup
engine = create_engine('sqlite:///social_media.db')
Base = declarative_base() # Base class for declarative models
Session = sessionmaker(bind=engine)
session = Session() # Create a session to interact with the DB

# Association table for many-to-many relationship (User-User followers)
followers = Table(
    'followers', Base.metadata,
    Column('follower_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('followed_id', Integer, ForeignKey('users.id'), primary_key=True)
)

# Association table for many-to-many relationship (User-Post likes)
likes = Table(
    'likes', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True)
)

class Users(Base):
    """SQLAlchemy model for a User in a social media application."""
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False) # Store hashed password in real app
    bio: Mapped[str] = mapped_column(String(200), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    posts: Mapped[list["Posts"]] = relationship("Posts", back_populates="user", cascade="all, delete-orphan")

    # Many-to-many self-referential relationship for following
    following: Mapped[list["Users"]] = relationship(
        "Users", secondary=followers,
        primaryjoin=id==followers.c.follower_id,
        secondaryjoin=id==followers.c.followed_id,
        back_populates="followers"
    )
    followers: Mapped[list["Users"]] = relationship(
        "Users", secondary=followers,
        primaryjoin=id==followers.c.followed_id,
        secondaryjoin=id==followers.c.follower_id,
        back_populates="following"
    )
    
    # Many-to-many relationship for liked posts
    liked_posts: Mapped[list["Posts"]] = relationship(
        "Posts", secondary=likes, back_populates="liked_by_users"
    )

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"


class Posts(Base):
    """SQLAlchemy model for a Post in a social media application."""
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    content: Mapped[str] = mapped_column(String(500), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    user: Mapped["Users"] = relationship("Users", back_populates="posts")
    liked_by_users: Mapped[list["Users"]] = relationship(
        "Users", secondary=likes, back_populates="liked_posts"
    )

    def __repr__(self):
        return f"<Post(id={self.id}, user_id={self.user_id}, content='{self.content[:20]}...')>"

# Create all tables in the database
Base.metadata.create_all(engine)
```

---

## 3. Create Operations

Creating new records involves instantiating your model classes and adding them to the session.

### Adding a Single Object

```python
# Create a new user
new_user = Users(username="alice_smith", email="alice@example.com", password="hashed_password", bio="Loves Python")
session.add(new_user)
session.commit()
print(f"Created user: {new_user}")

# Create a post for this user
new_post = Posts(user_id=new_user.id, content="Hello World, first post!")
session.add(new_post)
session.commit()
print(f"Created post: {new_post}")
```

### Adding Multiple Objects (Batch Insert)

```python
# Create more users
bob = Users(username="bob_builder", email="bob@example.com", password="hashed_password", bio="Can he fix it?")
charlie = Users(username="charlie_chaplin", email="charlie@example.com", password="hashed_password", bio="Silent film star")
session.add_all([bob, charlie])
session.commit()
print("Added Bob and Charlie.")
```

---

## 4. Read Operations

Retrieving data from the database is done using the session's `query()` method.

### Querying All Objects

```python
# Get all users
all_users = session.query(Users).all()
for user in all_users:
    print(user)

# Get all posts
all_posts = session.query(Posts).all()
for post in all_posts:
    print(post)
```

### Filtering Data (`.filter_by()`, `.filter()`)

*   **`filter_by()`**: Uses keyword arguments for equality comparisons.
*   **`filter()`**: Uses SQL expressions (more flexible).

```python
# Find user by username
alice = session.query(Users).filter_by(username="alice_smith").first()
print(f"Found Alice: {alice}")

# Find posts by a specific user (using user_id)
alice_posts = session.query(Posts).filter_by(user_id=alice.id).all()
for post in alice_posts:
    print(post)

# Using filter() for more complex conditions
# Find users with 'example.com' in their email
example_users = session.query(Users).filter(Users.email.like('%@example.com%')).all()
for user in example_users:
    print(user)

# Find users created after a specific date
from datetime import datetime, timedelta
yesterday = datetime.now() - timedelta(days=1)
recent_users = session.query(Users).filter(Users.created_at > yesterday).all()
for user in recent_users:
    print(user)
```

### Retrieving Single Objects (`.first()`, `.one_or_none()`, `.get()`)

*   **`.first()`**: Returns the first result of the query, or `None` if no results.
*   **`.one_or_none()`**: Returns exactly one result, or `None` if no results. Raises an error if more than one result.
*   **`.get(primary_key)`**: Efficiently retrieves an object by its primary key.

```python
# Get user by primary key (ID)
user_by_id = session.get(Users, 1) # Assuming ID 1 exists
print(f"User by ID 1: {user_by_id}")

# Get a unique user
unique_user = session.query(Users).filter_by(email="bob@example.com").one_or_none()
if unique_user:
    print(f"Unique user: {unique_user}")
```

### Ordering Results (`.order_by()`)

```python
# Get all users ordered by username ascending
ordered_users = session.query(Users).order_by(Users.username).all()
for user in ordered_users:
    print(user)

# Get all posts ordered by creation date descending
recent_posts = session.query(Posts).order_by(Posts.created_at.desc()).all()
for post in recent_posts:
    print(post)
```

---

## 5. Update Operations

Updating records involves retrieving the object, modifying its attributes, and committing the changes.

```python
# Find the user to update
user_to_update = session.query(Users).filter_by(username="alice_smith").first()

if user_to_update:
    # Modify attributes
    user_to_update.email = "alice.new@example.com"
    user_to_update.bio = "Updated bio for Alice."
    
    session.commit() # Commit changes to the database
    print(f"Updated user: {user_to_update}")
else:
    print("User not found for update.")

# Update a post
post_to_update = session.query(Posts).filter_by(id=1).first() # Assuming Post ID 1 exists
if post_to_update:
    post_to_update.content = "This is an updated post content!"
    session.commit()
    print(f"Updated post: {post_to_update}")
```

---

## 6. Delete Operations

Deleting records involves retrieving the object and removing it from the session.

```python
# Find the user to delete
user_to_delete = session.query(Users).filter_by(username="charlie_chaplin").first()

if user_to_delete:
    session.delete(user_to_delete) # Mark object for deletion
    session.commit()               # Commit deletion to the database
    print(f"Deleted user: {user_to_delete}")
else:
    print("User not found for deletion.")

# Delete a post
post_to_delete = session.query(Posts).filter_by(id=2).first() # Assuming Post ID 2 exists
if post_to_delete:
    session.delete(post_to_delete)
    session.commit()
    print(f"Deleted post: {post_to_delete}")
```

---

## 7. Relationships

SQLAlchemy handles relationships between models, allowing you to access related objects directly.

### One-to-Many Relationship (User has many Posts)

```python
# Assuming a User has many Posts (defined by 'posts' relationship in Users model)
user = session.query(Users).filter_by(username="alice_smith").first()
if user:
    print(f"\nPosts by {user.username}:")
    for post in user.posts: # Access posts directly through the user object
        print(f"- {post.content}")
```

### Many-to-Many Relationship (Followers, Liked Posts)

SQLAlchemy uses association tables to manage many-to-many relationships.

```python
# Example: User following another user
user1 = session.query(Users).filter_by(username="alice_smith").first()
user2 = session.query(Users).filter_by(username="bob_builder").first()

if user1 and user2:
    user1.following.append(user2) # Alice follows Bob
    session.commit()
    print(f"{user1.username} is now following {user2.username}.")

    print(f"\n{user1.username} is following:")
    for followed_user in user1.following:
        print(f"- {followed_user.username}")

    print(f"\n{user2.username} is followed by:")
    for follower_user in user2.followers:
        print(f"- {follower_user.username}")

# Example: Liking a post
user = session.query(Users).filter_by(username="alice_smith").first()
post = session.query(Posts).filter_by(id=1).first() # Assuming Post ID 1 exists

if user and post:
    user.liked_posts.append(post) # User likes the post
    session.commit()
    print(f"{user.username} liked Post ID {post.id}.")

    print(f"\nPosts liked by {user.username}:")
    for liked_post in user.liked_posts:
        print(f"- {liked_post.content}")
```

---

## 8. Practical Assignments (from new data)

These assignments will help solidify your understanding of SQLAlchemy CRUD operations and relationships.

### Assignment 1: User Profile Management

**Objective**: Extend the existing models and implement functions to manage user profiles.

1.  **Add a `profile_picture_url` field to the `Users` model.**
    *   `ALTER TABLE` (SQL DDL equivalent) or add to model and run migration.
2.  **Implement a function to update a user's `bio` and `profile_picture_url`.**
3.  **Implement a function to find users who have not posted anything yet.**
    *   *Hint:* Use a `LEFT JOIN` and check for `NULL` posts.

### Assignment 2: Post Interaction and Analytics

**Objective**: Implement functions for post interactions and basic analytics.

1.  **Implement a function for a user to comment on a post.**
    *   *Hint:* You might need a `Comments` model with a foreign key to `Posts` and `Users`.
2.  **Implement a function to retrieve all comments for a given post.**
3.  **Implement a function to count the number of likes for each post.**
    *   *Hint:* Use a `JOIN` with the `likes` association table and `GROUP BY`.
4.  **Find the user with the most posts.**
    *   *Hint:* Use `GROUP BY` and `ORDER BY` with `COUNT()`.

---

## See Also

-   **[SQL and SQLAlchemy Cheat Sheet](../cheatsheets/SQL_and_SQLAlchemy_Cheat_Sheet.md)** - Basic SQLAlchemy concepts and SQL syntax.
-   **[SQL DDL Guide](../guides/SQL_DDL_Guide.md)** - For understanding `CREATE`, `ALTER`, `DROP` table commands.
-   **[SQL_Advanced_Queries_Guide.md](../guides/SQL_Advanced_Queries_Guide.md)** - For advanced querying techniques that can be applied with ORM.
-   **[OOP Cheat Sheet](../cheatsheets/OOP_Cheat_Sheet.md)** - For foundational object-oriented programming concepts used in ORM.
-   **[Interactive CLI with ORM Project Guide](../guides/Interactive_CLI_ORM_Project_Guide.md)** - A complete project example integrating ORM in a CLI.
