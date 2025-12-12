# Interactive CLI ORM Project Guide (Social Media App)

This guide walks through the architecture of a text-based "Finstagram" (Fake Instagram) application. It demonstrates how to build a complex CLI application using Python, SQLAlchemy ORM, and a modular "Blueprint-like" structure for feature separation.

## Project Structure

This project mimics a web application structure but runs in the terminal.

```
project/
├── models.py           # Database definitions (SQLAlchemy)
├── front_end.py        # Main CLI loop and menus
├── bp_auth.py          # Authentication logic
├── bp_users.py         # User profile management
├── bp_posts.py         # Post creation and management
└── bp_social.py        # Likes and Follows logic
```

---

## 1. Database Modeling (`models.py`)

We use SQLAlchemy to define our data structure. Key features include **Self-Referential Many-to-Many Relationships** (Following) and **Association Tables** (Likes).

```python
from sqlalchemy import create_engine, Integer, String, Float, ForeignKey, DateTime, Table, Column
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///socials.db')
Session = sessionmaker(bind=engine)
session = Session()

# Association Table for User-to-User Following
following = Table(
  'following',
  Base.metadata,
  Column('follower_id', Integer, ForeignKey('users.id')),
  Column('followed_id', Integer, ForeignKey('users.id'))
)

# Association Table for Likes
likes = Table(
  "likes",
  Base.metadata,
  Column('users_id', Integer, ForeignKey('users.id')),
  Column('posts_id', Integer, ForeignKey('posts.id'))
)

class Users(Base):
  __tablename__ = 'users'

  id: Mapped[int] = mapped_column(primary_key=True)
  username: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
  email: Mapped[str] = mapped_column(String(360), nullable=False, unique=True)
  password: Mapped[str] = mapped_column(String(100), nullable=False)
  bio: Mapped[str] = mapped_column(String(40), nullable=False)
  created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), nullable=False)

  # Relationships
  user_posts: Mapped[list['Posts']] = relationship('Posts', back_populates='user')
  liked_posts: Mapped[list['Posts']] = relationship('Posts', secondary=likes, back_populates='liked_by')
  
  # Self-Referential Relationship (Following)
  following: Mapped[list['Users']] = relationship(
    'Users',
    secondary="following",
    primaryjoin="Users.id==following.c.follower_id",
    secondaryjoin="Users.id==following.c.followed_id",
    backref='followed_by'
  )

class Posts(Base):
  __tablename__ = "posts"

  id: Mapped[int] = mapped_column(primary_key=True)
  img: Mapped[str] = mapped_column(String(500), nullable=False) # URL to image
  caption: Mapped[str] = mapped_column(String(500))
  location: Mapped[float] = mapped_column(Float, nullable=True)
  user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))

  user: Mapped['Users'] = relationship('Users', back_populates='user_posts')
  liked_by: Mapped[list['Users']] = relationship('Users', secondary=likes, back_populates='liked_posts')

Base.metadata.create_all(bind=engine)
```

---

## 2. Authentication Module (`bp_auth.py`)

Handles user registration and login. Note the use of `**user_data` to unpack dictionary keys directly into the model constructor.

```python
from models import Users, session

def register_user(user_data):
  """
  Creates a User object from dictionary data.
  user_data = {username, bio, email, password}
  """
  try:
    new_user = Users(**user_data)
    session.add(new_user)
    session.commit()
    return new_user
  except Exception as e:
    print(f"Error: {e}")
    return None

def login(user_credentials):
  """
  Finds user by email and checks password.
  """
  try:
    user = session.query(Users).where(Users.email == user_credentials['email']).first()
    if user and user.password == user_credentials['password']:
      return user
    return None
  except Exception as e:
    print(f"Error: {e}")
    return None
```

---

## 3. Social Features (`bp_social.py`)

This module demonstrates how to manage relationships.

### Liking a Post
```python
def like_post(current_user):
  # 1. List all posts
  all_posts = session.query(Posts).all()
  for post in all_posts:
      print(f"{post.id}: {post.caption}")
  
  # 2. Get selection
  choice = int(input("Post ID to like: "))
  post_to_like = session.get(Posts, choice)
  
  # 3. Add relationship
  if post_to_like and post_to_like not in current_user.liked_posts:
    current_user.liked_posts.append(post_to_like)
    session.commit()
    print("Liked!")
```

### Unliking a Post
```python
def unlike_post(current_user):
    # Logic is similar, but uses .remove()
    # if post_to_unlike in current_user.liked_posts:
    #   current_user.liked_posts.remove(post_to_unlike)
```

---

## 4. Main Application Loop (`front_end.py`)

The entry point of the application. It maintains the `current_user` state and routes the user to different sub-menus.

```python
from bp_auth import register_user, login
from bp_users import show_profile, update_profile
from bp_posts import create_post, show_my_posts
from bp_social import like_post

def main():
  # Phase 1: Authentication Loop
  current_user = None
  while not current_user:
    choice = input("1. Login, 2. Register, q. Quit: ")
    if choice == '1':
       # ... collect credentials ...
       current_user = login(creds)
    elif choice == '2':
       # ... collect info ...
       current_user = register_user(data)
    elif choice == 'q':
       return

  # Phase 2: Main App Loop
  while True:
    print(f"Welcome {current_user.username}")
    print("1. Profile\n2. Posts\n3. Social")
    choice = input("Select: ")
    
    if choice == '1':
      # Call User Menu Logic
      pass
    elif choice == '2':
      # Call Posts Menu Logic
      pass
    elif choice == '3':
      like_post(current_user)
```

## Key Takeaways
1.  **Session Management**: The `session` object is imported from `models.py` and shared across all modules. This ensures everyone is talking to the same database transaction.
2.  **State Passing**: The `current_user` object is retrieved once during login and passed into every function that needs context (e.g., `create_post(current_user)`).
3.  **Modular Design**: "Blueprints" (bp_*) separate logic by domain (User logic vs Post logic), preventing a massive 1000-line main file.

---

## See Also
- **[SQLAlchemy Relationships Guide](SQLAlchemy_Relationships_Guide.md)**
- **[Pet Clinic Project Guide](Pet_Clinic_ORM_Project_Guide.md)** (Another ORM example)

```