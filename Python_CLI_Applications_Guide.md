# Python CLI Applications Guide

## Quick Reference Card

| Component | Library | Purpose | Example |
|-----------|---------|---------|---------|
| Simple input | `input()` | Get user input | `name = input("Name: ")` |
| Command args | `sys.argv` | Access CLI arguments | `python script.py arg1 arg2` |
| Argument parsing | `argparse` | Parse complex args | `parser.add_argument('--name')` |
| Menu system | Custom loop | Interactive menu | `while True: show_menu()` |
| Colored output | `colorama` | Add colors to text | `print(Fore.RED + "Error!")` |
| Tables | `tabulate` | Display data in tables | `tabulate(data, headers)` |
| Progress bars | `tqdm` | Show progress | `for item in tqdm(items):` |
| Rich UI | `rich` | Beautiful CLI output | `console.print("[bold]Text")` |

**Common Patterns:** Menu loop, CRUD operations, Input validation, Error handling, Session management

## Table of Contents
1. [CLI Basics](#cli-basics)
2. [User Input and Validation](#user-input-and-validation)
3. [Command-Line Arguments](#command-line-arguments)
4. [Interactive Menus](#interactive-menus)
5. [CLI with Database (ORM)](#cli-with-database-orm)
6. [Formatting Output](#formatting-output)
7. [Error Handling](#error-handling)
8. [Complete CLI Application Example](#complete-cli-application-example)
9. [Advanced Features](#advanced-features)
10. [Best Practices](#best-practices)

---

## CLI Basics

### Simple CLI Program
```python
def main():
    """Basic CLI program"""
    print("Welcome to My CLI App!")

    name = input("Enter your name: ")
    age = input("Enter your age: ")

    print(f"Hello, {name}! You are {age} years old.")

if __name__ == '__main__':
    main()
```

### CLI with Loop
```python
def main():
    """CLI with continuous loop"""
    print("Welcome! Type 'quit' to exit.")

    while True:
        command = input("> ").strip().lower()

        if command == 'quit':
            print("Goodbye!")
            break
        elif command == 'help':
            print("Available commands: help, quit, greet")
        elif command == 'greet':
            name = input("Enter your name: ")
            print(f"Hello, {name}!")
        else:
            print("Unknown command. Type 'help' for options.")

if __name__ == '__main__':
    main()
```

---

## User Input and Validation

### Getting Input
```python
# Basic input
name = input("Enter your name: ")

# Input with type conversion
age = int(input("Enter your age: "))

# Input with default value
def get_input(prompt, default=""):
    """Get input with default value"""
    value = input(f"{prompt} [{default}]: ").strip()
    return value if value else default

name = get_input("Enter your name", "Guest")
```

### Input Validation
```python
def get_valid_integer(prompt, min_val=None, max_val=None):
    """Get valid integer input with range"""
    while True:
        try:
            value = int(input(prompt))

            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue

            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue

            return value

        except ValueError:
            print("Please enter a valid number")

# Usage
age = get_valid_integer("Enter your age: ", min_val=0, max_val=120)
```

### Email Validation
```python
import re

def get_valid_email(prompt="Enter email: "):
    """Get valid email address"""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    while True:
        email = input(prompt).strip()

        if re.match(email_pattern, email):
            return email
        else:
            print("Invalid email format. Please try again.")

email = get_valid_email()
```

### Yes/No Confirmation
```python
def confirm(prompt="Are you sure? (y/n): "):
    """Get yes/no confirmation"""
    while True:
        response = input(prompt).strip().lower()

        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'")

# Usage
if confirm("Delete this record? (y/n): "):
    delete_record()
```

---

## Command-Line Arguments

### Using sys.argv
```python
import sys

def main():
    """Access command-line arguments"""
    # sys.argv[0] is the script name
    # sys.argv[1:] are the arguments

    if len(sys.argv) < 2:
        print("Usage: python script.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    print(f"Hello, {name}!")

if __name__ == '__main__':
    main()

# Run: python script.py Alice
# Output: Hello, Alice!
```

### Using argparse
```python
import argparse

def main():
    """CLI with argparse"""
    parser = argparse.ArgumentParser(
        description='Simple CLI application'
    )

    # Positional argument
    parser.add_argument('name', help='Your name')

    # Optional argument
    parser.add_argument(
        '--age',
        type=int,
        help='Your age',
        default=25
    )

    # Flag
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    print(f"Hello, {args.name}!")

    if args.verbose:
        print(f"Age: {args.age}")

if __name__ == '__main__':
    main()

# Run: python script.py Alice --age 30 --verbose
```

### Advanced argparse
```python
import argparse

def create_user(args):
    """Create user command"""
    print(f"Creating user: {args.username}")

def delete_user(args):
    """Delete user command"""
    print(f"Deleting user: {args.username}")

def main():
    """CLI with subcommands"""
    parser = argparse.ArgumentParser(description='User Management CLI')

    # Create subparsers
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Create command
    create_parser = subparsers.add_parser('create', help='Create a user')
    create_parser.add_argument('username', help='Username')
    create_parser.add_argument('--email', required=True, help='Email address')
    create_parser.set_defaults(func=create_user)

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a user')
    delete_parser.add_argument('username', help='Username')
    delete_parser.set_defaults(func=delete_user)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

# Run: python script.py create alice --email alice@example.com
# Run: python script.py delete alice
```

---

## Interactive Menus

### Simple Menu
```python
def show_menu():
    """Display menu options"""
    print("\n=== Main Menu ===")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("0. Exit")

def main():
    """Interactive menu application"""
    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            print("You selected Option 1")
        elif choice == '2':
            print("You selected Option 2")
        elif choice == '3':
            print("You selected Option 3")
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
```

### Menu with Functions
```python
def option_1():
    """Handle option 1"""
    print("Executing Option 1...")

def option_2():
    """Handle option 2"""
    print("Executing Option 2...")

def option_3():
    """Handle option 3"""
    print("Executing Option 3...")

def main():
    """Menu with function mapping"""
    menu_options = {
        '1': ('Option 1', option_1),
        '2': ('Option 2', option_2),
        '3': ('Option 3', option_3),
        '0': ('Exit', None)
    }

    while True:
        print("\n=== Main Menu ===")
        for key, (label, _) in menu_options.items():
            print(f"{key}. {label}")

        choice = input("\nEnter your choice: ").strip()

        if choice in menu_options:
            label, func = menu_options[choice]

            if func is None:  # Exit
                print("Goodbye!")
                break

            func()
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
```

---

## CLI with Database (ORM)

### Setup
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    """User model"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)

# Database setup
engine = create_engine('sqlite:///cli_app.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
```

### CRUD Operations
```python
def create_user(session):
    """Create a new user"""
    username = input("Enter username: ").strip()
    email = input("Enter email: ").strip()

    try:
        user = User(username=username, email=email)
        session.add(user)
        session.commit()
        print(f"User '{username}' created successfully!")

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

def list_users(session):
    """List all users"""
    users = session.query(User).all()

    if not users:
        print("No users found.")
        return

    print("\n=== Users ===")
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

def find_user(session):
    """Find user by username"""
    username = input("Enter username to search: ").strip()

    user = session.query(User).filter_by(username=username).first()

    if user:
        print(f"\nFound: ID: {user.id}, Username: {user.username}, Email: {user.email}")
    else:
        print(f"User '{username}' not found.")

def update_user(session):
    """Update user information"""
    username = input("Enter username to update: ").strip()

    user = session.query(User).filter_by(username=username).first()

    if not user:
        print(f"User '{username}' not found.")
        return

    print(f"\nCurrent email: {user.email}")
    new_email = input("Enter new email (or press Enter to keep current): ").strip()

    if new_email:
        user.email = new_email
        session.commit()
        print("User updated successfully!")

def delete_user(session):
    """Delete a user"""
    username = input("Enter username to delete: ").strip()

    user = session.query(User).filter_by(username=username).first()

    if not user:
        print(f"User '{username}' not found.")
        return

    if confirm(f"Delete user '{username}'? (y/n): "):
        session.delete(user)
        session.commit()
        print("User deleted successfully!")
```

### Complete CLI with ORM
```python
def show_menu():
    """Display main menu"""
    print("\n=== User Management System ===")
    print("1. Create User")
    print("2. List Users")
    print("3. Find User")
    print("4. Update User")
    print("5. Delete User")
    print("0. Exit")

def main():
    """Main application"""
    session = Session()

    menu_options = {
        '1': create_user,
        '2': list_users,
        '3': find_user,
        '4': update_user,
        '5': delete_user
    }

    print("Welcome to User Management System!")

    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == '0':
            print("Goodbye!")
            session.close()
            break
        elif choice in menu_options:
            menu_options[choice](session)
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
```

---

## Formatting Output

### Using tabulate
```python
from tabulate import tabulate

def list_users_formatted(session):
    """List users with tabulate"""
    users = session.query(User).all()

    if not users:
        print("No users found.")
        return

    # Prepare data for table
    table_data = [
        [user.id, user.username, user.email]
        for user in users
    ]

    headers = ["ID", "Username", "Email"]

    print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))

# Install: pip install tabulate
```

### Using rich
```python
from rich.console import Console
from rich.table import Table

console = Console()

def list_users_rich(session):
    """List users with rich"""
    users = session.query(User).all()

    if not users:
        console.print("[yellow]No users found.[/yellow]")
        return

    table = Table(title="Users")
    table.add_column("ID", style="cyan")
    table.add_column("Username", style="magenta")
    table.add_column("Email", style="green")

    for user in users:
        table.add_row(str(user.id), user.username, user.email)

    console.print(table)

# Install: pip install rich
```

### Colored Output with colorama
```python
from colorama import init, Fore, Style

init()  # Initialize colorama

def print_success(message):
    """Print success message in green"""
    print(Fore.GREEN + message + Style.RESET_ALL)

def print_error(message):
    """Print error message in red"""
    print(Fore.RED + message + Style.RESET_ALL)

def print_warning(message):
    """Print warning message in yellow"""
    print(Fore.YELLOW + message + Style.RESET_ALL)

def print_info(message):
    """Print info message in blue"""
    print(Fore.BLUE + message + Style.RESET_ALL)

# Usage
print_success("User created successfully!")
print_error("Error: User not found.")
print_warning("Warning: This action cannot be undone.")
print_info("Loading data...")

# Install: pip install colorama
```

---

## Error Handling

### Try-Except in CLI
```python
def safe_create_user(session):
    """Create user with error handling"""
    try:
        username = input("Enter username: ").strip()
        email = input("Enter email: ").strip()

        # Validation
        if not username or not email:
            raise ValueError("Username and email are required")

        if '@' not in email:
            raise ValueError("Invalid email format")

        # Create user
        user = User(username=username, email=email)
        session.add(user)
        session.commit()

        print_success(f"User '{username}' created successfully!")

    except ValueError as e:
        print_error(f"Validation error: {e}")
    except Exception as e:
        session.rollback()
        print_error(f"Database error: {e}")
```

### Custom Exception Handling
```python
class CLIError(Exception):
    """Base CLI exception"""
    pass

class ValidationError(CLIError):
    """Validation error"""
    pass

class DatabaseError(CLIError):
    """Database error"""
    pass

def validate_username(username):
    """Validate username"""
    if len(username) < 3:
        raise ValidationError("Username must be at least 3 characters")

    if not username.isalnum():
        raise ValidationError("Username must be alphanumeric")

def create_user_with_validation(session):
    """Create user with custom exceptions"""
    try:
        username = input("Enter username: ").strip()
        validate_username(username)

        email = input("Enter email: ").strip()

        user = User(username=username, email=email)
        session.add(user)
        session.commit()

        print_success("User created successfully!")

    except ValidationError as e:
        print_error(f"Validation error: {e}")
    except DatabaseError as e:
        print_error(f"Database error: {e}")
    except Exception as e:
        session.rollback()
        print_error(f"Unexpected error: {e}")
```

---

## Complete CLI Application Example

```python
#!/usr/bin/env python3
"""
Complete CLI Application with Database
User Management System
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from colorama import init, Fore, Style

# Initialize colorama
init()

# Database setup
Base = declarative_base()

class User(Base):
    """User model"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)

# Create engine and session
engine = create_engine('sqlite:///users.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Helper functions
def print_success(msg):
    print(Fore.GREEN + msg + Style.RESET_ALL)

def print_error(msg):
    print(Fore.RED + msg + Style.RESET_ALL)

def print_info(msg):
    print(Fore.CYAN + msg + Style.RESET_ALL)

def confirm(prompt):
    """Get yes/no confirmation"""
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        print("Please enter 'y' or 'n'")

# CRUD Operations
def create_user(session):
    """Create new user"""
    print_info("\n--- Create User ---")
    username = input("Username: ").strip()
    email = input("Email: ").strip()

    if not username or not email:
        print_error("Username and email are required!")
        return

    try:
        user = User(username=username, email=email)
        session.add(user)
        session.commit()
        print_success(f"User '{username}' created successfully!")
    except Exception as e:
        session.rollback()
        print_error(f"Error: {e}")

def list_users(session):
    """List all users"""
    users = session.query(User).all()

    if not users:
        print_info("No users found.")
        return

    print_info("\n--- All Users ---")
    print(f"{'ID':<5} {'Username':<20} {'Email':<30}")
    print("-" * 55)
    for user in users:
        print(f"{user.id:<5} {user.username:<20} {user.email:<30}")

def find_user(session):
    """Find user by username"""
    username = input("\nEnter username: ").strip()

    user = session.query(User).filter_by(username=username).first()

    if user:
        print_info(f"\nFound: {user.id} | {user.username} | {user.email}")
    else:
        print_error(f"User '{username}' not found.")

def update_user(session):
    """Update user"""
    username = input("\nEnter username to update: ").strip()

    user = session.query(User).filter_by(username=username).first()

    if not user:
        print_error(f"User '{username}' not found.")
        return

    print_info(f"Current email: {user.email}")
    new_email = input("New email (or Enter to skip): ").strip()

    if new_email:
        user.email = new_email
        session.commit()
        print_success("User updated!")
    else:
        print_info("No changes made.")

def delete_user(session):
    """Delete user"""
    username = input("\nEnter username to delete: ").strip()

    user = session.query(User).filter_by(username=username).first()

    if not user:
        print_error(f"User '{username}' not found.")
        return

    if confirm(f"Delete '{username}'? (y/n): "):
        session.delete(user)
        session.commit()
        print_success("User deleted!")
    else:
        print_info("Cancelled.")

def show_menu():
    """Display menu"""
    print("\n" + "=" * 40)
    print(Fore.YELLOW + "    User Management System" + Style.RESET_ALL)
    print("=" * 40)
    print("1. Create User")
    print("2. List All Users")
    print("3. Find User")
    print("4. Update User")
    print("5. Delete User")
    print("0. Exit")
    print("=" * 40)

def main():
    """Main application loop"""
    session = Session()

    menu_options = {
        '1': create_user,
        '2': list_users,
        '3': find_user,
        '4': update_user,
        '5': delete_user
    }

    print_success("\nWelcome to User Management System!")

    while True:
        show_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == '0':
            print_success("\nGoodbye!")
            session.close()
            sys.exit(0)
        elif choice in menu_options:
            menu_options[choice](session)
        else:
            print_error("Invalid choice!")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye!")
        sys.exit(0)
```

---

## Advanced Features

### Progress Bars with tqdm
```python
from tqdm import tqdm
import time

def process_users(session):
    """Process users with progress bar"""
    users = session.query(User).all()

    print("Processing users...")
    for user in tqdm(users, desc="Processing"):
        # Simulate processing
        time.sleep(0.1)
        # Do something with user

# Install: pip install tqdm
```

### Logging
```python
import logging

# Configure logging
logging.basicConfig(
    filename='cli_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_user_with_logging(session):
    """Create user with logging"""
    try:
        username = input("Username: ").strip()
        email = input("Email: ").strip()

        user = User(username=username, email=email)
        session.add(user)
        session.commit()

        logging.info(f"User created: {username}")
        print_success("User created!")

    except Exception as e:
        logging.error(f"Error creating user: {e}")
        session.rollback()
        print_error(f"Error: {e}")
```

---

## Best Practices

### 1. Input Validation
```python
# Always validate user input
def get_valid_input(prompt, validator=None):
    """Get input with validation"""
    while True:
        value = input(prompt).strip()

        if validator:
            is_valid, message = validator(value)
            if not is_valid:
                print_error(message)
                continue

        return value
```

### 2. Error Handling
```python
# Wrap operations in try-except
try:
    operation()
except SpecificError as e:
    handle_specific_error(e)
except Exception as e:
    handle_general_error(e)
```

### 3. Clear User Feedback
```python
# Use colors and clear messages
print_success("Operation successful!")
print_error("Operation failed!")
print_info("Loading...")
```

### 4. Confirm Destructive Actions
```python
# Always confirm before deleting
if confirm("Delete this? (y/n): "):
    delete_item()
```

### 5. Session Management
```python
# Always close database sessions
session = Session()
try:
    # Do work
    pass
finally:
    session.close()
```

---

## See Also

- **[SQL and SQLAlchemy Cheat Sheet](./SQL_and_SQLAlchemy_Cheat_Sheet.md)** - Database operations
- **[Error Handling Cheat Sheet](./Error_Handling_Cheat_Sheet.md)** - Exception handling
- **[Python Basics Cheat Sheet](./Python_Basics_Cheat_Sheet.md)** - Input/output basics
- **[File Operations Cheat Sheet](./File_Operations_Cheat_Sheet.md)** - File I/O

---