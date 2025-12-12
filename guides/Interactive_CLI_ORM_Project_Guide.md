# Interactive CLI with ORM Project Guide

This guide details the design and implementation of an interactive Command-Line Interface (CLI) application that leverages Python and SQLAlchemy ORM to manage users, posts, and social interactions within a simulated social media platform.

---

## 1. Project Overview

The Interactive CLI with ORM project demonstrates how to build a fully functional text-based application that interacts with a database. It covers user authentication, content creation (posts), and social features like following other users and liking posts. The project uses SQLAlchemy for object-relational mapping, simplifying database interactions.

### Key Features
*   **User Management:** Register, login, view, update, and delete user profiles.
*   **Post Management:** Create, view, update, and delete text-based posts.
*   **Social Interactions:** Follow/unfollow other users, like/unlike posts, view liked posts.
*   **Persistent Data:** All data is stored in a SQLite database via SQLAlchemy ORM.
*   **Interactive Menu:** A menu-driven interface guides user interactions.

---

## 2. Database Models (`models.py`)

The application's data structure is defined by SQLAlchemy models, representing `Users` and `Posts` tables, and their relationships.

```python
from sqlalchemy import create_engine, Integer, String, Float, ForeignKey, DateTime, Table, Column
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship
from datetime import datetime

# Database setup
engine = create_engine('sqlite:///social_app.db')
Base = declarative_base() # Base class for declarative models
Session = sessionmaker(bind=engine)
session = Session()

# Association table for many-to-many User-User relationship (Follows)
followers_association_table = Table(
    'followers_association', Base.metadata,
    Column('follower_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('followed_id', Integer, ForeignKey('users.id'), primary_key=True)
)

# Association table for many-to-many User-Post relationship (Likes)
likes_association_table = Table(
    'likes_association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True)
)

class Users(Base):
    """SQLAlchemy model for a User."""
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False) # Hashed in real app
    bio: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    posts: Mapped[list["Posts"]] = relationship("Posts", back_populates="user", cascade="all, delete-orphan")

    # Self-referential Many-to-Many for followers
    following: Mapped[list["Users"]] = relationship(
        "Users", secondary=followers_association_table,
        primaryjoin=id==followers_association_table.c.follower_id,
        secondaryjoin=id==followers_association_table.c.followed_id,
        back_populates="followers"
    )
    followers: Mapped[list["Users"]] = relationship(
        "Users", secondary=followers_association_table,
        primaryjoin=id==followers_association_table.c.followed_id,
        secondaryjoin=id==followers_association_table.c.follower_id,
        back_populates="following"
    )

    liked_posts: Mapped[list["Posts"]] = relationship(
        "Posts", secondary=likes_association_table, back_populates="liked_by_users"
    )

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"


class Posts(Base):
    """SQLAlchemy model for a Post."""
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    user: Mapped["Users"] = relationship("Users", back_populates="posts")
    liked_by_users: Mapped[list["Users"]] = relationship(
        "Users", secondary=likes_association_table, back_populates="liked_posts"
    )

    def __repr__(self):
        return f"<Post(id={self.id}, user_id={self.user_id}, content='{self.content[:20]}...')>"

# Base.metadata.create_all(engine) # Creates all tables in the database
```

---

## 3. Authentication (`bp_auth.py`)

This blueprint handles user registration and login, allowing users to access the application.

```python
from models import Users, session # Assuming session is created globally

def register_user(user_data):
    """
    Registers a new user. Expects user_data dictionary with username, email, password, and bio.
    """
    try:
        new_user = Users(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password'], # In real app, hash this!
            bio=user_data.get('bio', '')
        )
        session.add(new_user)
        session.commit()
        print(f"User '{new_user.username}' registered successfully!")
        return new_user
    except Exception as e:
        session.rollback()
        print(f"Registration failed: {e}")
        return None

def login(user_credentials):
    """
    Logs in a user. Expects user_credentials dictionary with username and password.
    """
    username = user_credentials.get('username')
    password = user_credentials.get('password')

    user = session.query(Users).filter_by(username=username).first()

    if user and user.password == password: # Simplified password check
        print(f"Welcome back, {user.username}!")
        return user
    else:
        print("Invalid username or password.")
        return None
```

---

## 4. User Management (`bp_users.py`)

This blueprint provides functionalities for users to manage their own profiles, including viewing, updating, and deleting.

```python
from models import Users, session

def show_profile(current_user):
    """Displays the current user's profile information."""
    print("\n--- Your Profile ---")
    print(f"Username: {current_user.username}")
    print(f"Email: {current_user.email}")
    print(f"Bio: {current_user.bio}")
    print(f"Joined: {current_user.created_at.strftime('%Y-%m-%d')}")
    print(f"Following: {len(current_user.following)}")
    print(f"Followers: {len(current_user.followers)}")

def update_profile(current_user):
    """Allows the current user to update their profile information."""
    print("\n--- Update Profile ---")
    new_username = input(f"New Username (current: {current_user.username}, leave blank to keep): ").strip()
    if new_username:
        current_user.username = new_username

    new_email = input(f"New Email (current: {current_user.email}, leave blank to keep): ").strip()
    if new_email:
        current_user.email = new_email
    
    new_bio = input(f"New Bio (current: {current_user.bio if current_user.bio else 'None'}, leave blank to keep): ").strip()
    if new_bio:
        current_user.bio = new_bio

    try:
        session.commit()
        print("Profile updated successfully!")
        return current_user
    except Exception as e:
        session.rollback()
        print(f"Error updating profile: {e}")
        return None

def delete_user(current_user):
    """Deletes the current user's account."""
    confirm = input(f"Are you sure you want to delete your account '{current_user.username}'? (y/n): ").lower()
    if confirm == 'y':
        try:
            session.delete(current_user)
            session.commit()
            print("Account deleted successfully. Goodbye!")
            return True # Indicate successful deletion
        except Exception as e:
            session.rollback()
            print(f"Error deleting account: {e}")
            return False
    else:
        print("Account deletion cancelled.")
        return False
```

---

## 5. Post Management (`bp_posts.py`)

This blueprint provides functions for users to create, view, update, and delete their posts.

```python
from models import Posts, session
from datetime import datetime

def show_my_posts(current_user):
    """Displays all posts made by the current user."""
    if not current_user.posts:
        print("You haven't made any posts yet.")
        return

    print(f"\n--- {current_user.username}'s Posts ---")
    for i, post in enumerate(current_user.posts):
        print(f"[{i+1}] Post ID: {post.id} (Created: {post.created_at.strftime('%Y-%m-%d %H:%M')})")
        print(f"  Content: {post.content}")
        print("-" * 30)

def create_post(current_user):
    """Allows the current user to create a new post."""
    print("\n--- Create New Post ---")
    content = input("Enter your post content: ").strip()

    if not content:
        print("Post content cannot be empty.")
        return

    try:
        new_post = Posts(user_id=current_user.id, content=content, created_at=datetime.now())
        session.add(new_post)
        session.commit()
        print("Post created successfully!")
        return new_post
    except Exception as e:
        session.rollback()
        print(f"Error creating post: {e}")
        return None

def update_post(current_user):
    """Allows the current user to update one of their existing posts."""
    if not current_user.posts:
        print("You have no posts to update.")
        return
    
    show_my_posts(current_user)
    post_choice = int(input("Enter the number of the post you want to update: ")) - 1

    if 0 <= post_choice < len(current_user.posts):
        post_to_update = current_user.posts[post_choice]
        print(f"\n--- Update Post (ID: {post_to_update.id}) ---")
        new_content = input(f"New content (current: {post_to_update.content}, leave blank to keep): ").strip()
        
        if new_content:
            post_to_update.content = new_content
            try:
                session.commit()
                print("Post updated successfully!")
            except Exception as e:
                session.rollback()
                print(f"Error updating post: {e}")
        else:
            print("No changes made to post.")
    else:
        print("Invalid post selection.")

def delete_post(current_user):
    """Allows the current user to delete one of their posts."""
    if not current_user.posts:
        print("You have no posts to delete.")
        return

    show_my_posts(current_user)
    post_choice = int(input("Enter the number of the post you want to delete: ")) - 1

    if 0 <= post_choice < len(current_user.posts):
        post_to_delete = current_user.posts[post_choice]
        confirm = input(f"Are you sure you want to delete this post (ID: {post_to_delete.id})? (y/n): ").lower()
        if confirm == 'y':
            try:
                session.delete(post_to_delete)
                session.commit()
                print("Post deleted successfully.")
            except Exception as e:
                session.rollback()
                print(f"Error deleting post: {e}")
        else:
            print("Post deletion cancelled.")
    else:
        print("Invalid post selection.")
```

---

## 6. Social Features (`bp_social.py`)

This blueprint enables social interactions such as liking posts and viewing liked content.

```python
from models import Users, Posts, session

def like_post(current_user):
    """Allows the current user to like a post."""
    post_id = int(input("Enter the ID of the post you want to like: "))
    post = session.query(Posts).filter_by(id=post_id).first()

    if not post:
        print("Post not found.")
        return

    if post in current_user.liked_posts:
        print("You have already liked this post.")
        return
    
    try:
        current_user.liked_posts.append(post)
        session.commit()
        print(f"You liked post ID: {post.id}!")
    except Exception as e:
        session.rollback()
        print(f"Error liking post: {e}")

def unlike_post(current_user):
    """Allows the current user to unlike a post."""
    post_id = int(input("Enter the ID of the post you want to unlike: "))
    post = session.query(Posts).filter_by(id=post_id).first()

    if not post:
        print("Post not found.")
        return

    if post not in current_user.liked_posts:
        print("You have not liked this post.")
        return
    
    try:
        current_user.liked_posts.remove(post)
        session.commit()
        print(f"You unliked post ID: {post.id}.")
    except Exception as e:
        session.rollback()
        print(f"Error unliking post: {e}")

def view_liked_posts(current_user):
    """Displays all posts liked by the current user."""
    if not current_user.liked_posts:
        print("You haven't liked any posts yet.")
        return

    print(f"\n--- Posts Liked by {current_user.username} ---")
    for post in current_user.liked_posts:
        print(f"Post ID: {post.id} by {post.user.username} (Created: {post.created_at.strftime('%Y-%m-%d %H:%M')})")
        print(f"  Content: {post.content}")
        print("-" * 30)
```

---

## 7. CLI Frontend (`front_end.py`)

This file integrates all the functionalities, providing an interactive menu-driven experience for the user.

```python
from bp_auth import register_user, login
from bp_users import show_profile, update_profile, delete_user
from bp_posts import show_my_posts, create_post, update_post, delete_post
from bp_social import like_post, unlike_post, view_liked_posts
from models import session, Base, engine # Import for global session and setup
import sys # For sys.exit

def welcome_menu():
    """Displays the welcome menu for login/registration."""
    while True:
        print("\n" + "="*30)
        print("   Welcome to Social App!   ")
        print("="*30)
        print("1. Login")
        print("2. Register")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            user = login({'username': username, 'password': password})
            if user: return user
        elif choice == '2':
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")
            bio = input("Bio (optional): ")
            user = register_user({'username': username, 'email': email, 'password': password, 'bio': bio})
            if user: return user
        elif choice == '0':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice.")

def user_menu(current_user):
    """Displays the main menu for an authenticated user."""
    while True:
        print(f"\n--- Welcome, {current_user.username}! ---")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Delete Account")
        print("4. Manage Posts")
        print("5. Social Features")
        print("0. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_profile(current_user)
        elif choice == '2':
            updated_user = update_profile(current_user)
            if updated_user: current_user = updated_user
        elif choice == '3':
            if delete_user(current_user): return None # Account deleted, logout
        elif choice == '4':
            posts_menu(current_user)
        elif choice == '5':
            social_menu(current_user)
        elif choice == '0':
            print("Logging out.")
            return None # Logout
        else:
            print("Invalid choice.")

def posts_menu(current_user):
    """Displays the post management menu."""
    while True:
        print(f"\n--- {current_user.username}'s Posts ---")
        print("1. View My Posts")
        print("2. Create New Post")
        print("3. Update My Post")
        print("4. Delete My Post")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_my_posts(current_user)
        elif choice == '2':
            create_post(current_user)
        elif choice == '3':
            update_post(current_user)
        elif choice == '4':
            delete_post(current_user)
        elif choice == '0':
            return
        else:
            print("Invalid choice.")

def social_menu(current_user):
    """Displays the social features menu."""
    while True:
        print(f"\n--- {current_user.username}'s Social ---")
        print("1. Like a Post")
        print("2. Unlike a Post")
        print("3. View Liked Posts")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            like_post(current_user)
        elif choice == '2':
            unlike_post(current_user)
        elif choice == '3':
            view_liked_posts(current_user)
        elif choice == '0':
            return
        else:
            print("Invalid choice.")

def main_cli_app():
    """Main function to run the Interactive Social App CLI application."""
    Base.metadata.create_all(engine) # Ensure tables are created

    current_user = None
    try:
        while True:
            if not current_user:
                current_user = welcome_menu() # Handles login/registration/exit
            else:
                current_user = user_menu(current_user) # Handles user actions/logout
    except KeyboardInterrupt:
        print("\nApplication interrupted. Exiting.")
    finally:
        session.close() # Ensure session is closed

if __name__ == '__main__':
    main_cli_app()
```

---

## See Also

-   **[Python CLI Applications Guide](../guides/Python_CLI_Applications_Guide.md)** - For general CLI development concepts.
-   **[SQL and SQLAlchemy Cheat Sheet](../cheatsheets/SQL_and_SQLAlchemy_Cheat_Sheet.md)** - For core SQLAlchemy and SQL concepts.
-   **[OOP Cheat Sheet](../cheatsheets/OOP_Cheat_Sheet.md)** - For understanding the object-oriented design of the models.
-   **[Error Handling Cheat Sheet](../cheatsheets/Error_Handling_Cheat_Sheet.md)** - For strategies to make your CLI robust.
