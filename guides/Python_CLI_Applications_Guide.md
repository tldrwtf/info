# Python CLI Applications Guide

This guide provides a comprehensive overview of building Command-Line Interface (CLI) applications in Python. It covers fundamental concepts from basic input/output to advanced features like argument parsing, database integration, API interaction, and rich output formatting.

## Quick Reference Card

| Component          | Library   | Purpose                             | Example                                      |
| :----------------- | :-------- | :---------------------------------- | :------------------------------------------- |
| Simple input       | `input()` | Get user input                      | `name = input("Name: ")`                     |
| Command args       | `sys.argv`| Access CLI arguments                | `python script.py arg1 arg2`                 |
| Argument parsing   | `argparse`| Parse complex arguments             | `parser.add_argument('--name')`              |
| Interactive menus  | Custom loop| Build menu-driven applications      | `while True: show_menu()`                    |
| Colored output     | `colorama`| Add colors to console text          | `print(Fore.RED + "Error!")`                 |
| Tables             | `tabulate`| Display data in tabular format      | `tabulate(data, headers)`                    |
| Progress bars      | `tqdm`    | Show progress for long operations   | `for item in tqdm(items):`                   |
| Rich UI            | `rich`    | Create beautiful and interactive CLI output | `console.print("[bold]Text")`                |
| HTTP Requests      | `requests`| Interact with Web APIs              | `requests.get('https://api.example.com')`    |

**Common Patterns:** Menu loop, CRUD operations, Input validation, Error handling, Session management

---

## Table of Contents
1. [CLI Basics](#1-cli-basics)
2. [User Input and Validation](#2-user-input-and-validation)
3. [Command-Line Arguments](#3-command-line-arguments)
4. [Interactive Menus](#4-interactive-menus)
5. [CLI with Database (ORM)](#5-cli-with-database-orm)
6. [CLI with External APIs](#6-cli-with-external-apis)
7. [Formatting Output](#7-formatting-output)
8. [Error Handling](#8-error-handling)
9. [Complete CLI Application Example](#9-complete-cli-application-example)
10. [Advanced Features](#10-advanced-features)
11. [Best Practices](#11-best-practices)

---

## 1. CLI Basics

A Command-Line Interface (CLI) application allows users to interact with a program by typing commands in a terminal.

### Simple CLI Program
This example demonstrates a basic CLI that prompts the user for input and displays a greeting.

```python
def main():
    """Basic CLI program that gets user input and prints a greeting."""
    print("Welcome to My Basic CLI App!")

    name = input("Enter your name: ")
    age = input("Enter your age: ")

    print(f"Hello, {name}! You are {age} years old.")

if __name__ == '__main__':
    main()
```

### CLI with a Continuous Loop
Many CLI applications run in a loop, allowing the user to enter multiple commands until they choose to exit.

```python
def main():
    """A CLI with a continuous command loop."""
    print("Welcome! Type 'quit' to exit.")

    while True:
        command = input("> ").strip().lower() # Get user command, clean it

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

## 2. User Input and Validation

Effective CLI applications need to robustly handle user input, including validating its format and range.

### Getting Input
```python
# Basic input: input() always returns a string
name = input("Enter your name: ")

# Input with type conversion: Use int(), float() etc.
age = int(input("Enter your age: "))

# Input with default value if user enters nothing
def get_input_with_default(prompt, default=""):
    """Gets user input, returning a default value if input is empty."""
    value = input(f"{prompt} [{default}]: ").strip()
    return value if value else default

user_name = get_input_with_default("Enter your name", "Guest")
print(f"Hello, {user_name}!")
```

### Input Validation
Functions can be created to repeatedly ask for input until valid data is provided.

```python
def get_valid_integer(prompt, min_val=None, max_val=None):
    """Prompts for an integer until a valid one within optional bounds is entered."""
    while True:
        try:
            value = int(input(prompt))

            if min_val is not None and value < min_val:
                print(f"Error: Value must be at least {min_val}.")
                continue

            if max_val is not None and value > max_val:
                print(f"Error: Value must be at most {max_val}.")
                continue

            return value

        except ValueError:
            print("Error: Please enter a valid whole number.")

# Usage examples
user_age = get_valid_integer("Enter your age: ", min_val=0, max_val=120)
choice = get_valid_integer("Enter your choice (1-3): ", min_val=1, max_val=3)
```

### Email Validation
Using regular expressions (`re` module) for complex pattern validation.

```python
import re

def get_valid_email(prompt="Enter email: "):
    """Prompts for an email address until a valid format is entered."""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    while True:
        email = input(prompt).strip()

        if re.match(email_pattern, email):
            return email
        else:
            print("Invalid email format. Please try again.")

# user_email = get_valid_email()
```

### Yes/No Confirmation
```python
def confirm_action(prompt="Are you sure? (y/n): "):
    """Gets a yes/no confirmation from the user."""
    while True:
        response = input(prompt).strip().lower()

        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# if confirm_action("Delete this item? "): 
#     print("Item deleted.")
# else:
#     print("Action cancelled.")
```

---

## 3. Command-Line Arguments

For non-interactive or script-like CLIs, arguments passed directly when running the script are essential.

### Using `sys.argv`
The `sys.argv` list contains all command-line arguments, where `sys.argv[0]` is the script name.

```python
import sys

def main():
    """Processes command-line arguments using sys.argv."""
    if len(sys.argv) < 2:
        print("Usage: python my_script.py <name>")
        sys.exit(1) # Exit with an error code

    name_arg = sys.argv[1]
    print(f"Hello, {name_arg} from sys.argv!")

if __name__ == '__main__':
    # To run: python your_script_name.py Alice
    main()
```

### Using `argparse` (Recommended for Complex CLIs)
The `argparse` module makes it easy to write user-friendly command-line interfaces. It handles parsing arguments, generating help messages, and reporting errors.

```python
import argparse

def main():
    """Parses command-line arguments using argparse."""
    parser = argparse.ArgumentParser(
        description='A simple greeting CLI application.'
    )

    # Positional argument (required, order matters)
    parser.add_argument('name', type=str, help='The name of the person to greet.')

    # Optional argument with type and default value
    parser.add_argument(
        '--age',
        type=int,
        default=25,
        help='The age of the person (optional, defaults to 25).'
    )

    # Optional flag (boolean switch)
    parser.add_argument(
        '--verbose',
        action='store_true', # Stores True if flag is present
        help='Enable verbose output.'
    )

    args = parser.parse_args() # Parse the arguments

    print(f"Hello, {args.name}!")
    if args.verbose:
        print(f"Verbose mode enabled. Age: {args.age}.")

if __name__ == '__main__':
    # To run:
    # python your_script_name.py Alice
    # python your_script_name.py Bob --age 30 --verbose
    main()
```

### Subcommands with `argparse`
For CLIs with distinct functionalities (e.g., `git commit`, `git push`), `argparse` supports subcommands.

```python
import argparse

def create_user_command(args):
    """Handler for the 'create' subcommand."""
    print(f"Creating user: {args.username} with email: {args.email}")

def delete_user_command(args):
    """Handler for the 'delete' subcommand."""
    print(f"Deleting user: {args.username}")

def main():
    """CLI application with 'create' and 'delete' subcommands."""
    parser = argparse.ArgumentParser(description='User Management CLI.')

    # Create subparsers to define different commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # 'create' subcommand
    create_parser = subparsers.add_parser('create', help='Create a new user.')
    create_parser.add_argument('username', type=str, help='Username for the new user.')
    create_parser.add_argument('--email', type=str, required=True, help='Email address of the new user.')
    create_parser.set_defaults(func=create_user_command) # Link to handler function

    # 'delete' subcommand
    delete_parser = subparsers.add_parser('delete', help='Delete an existing user.')
    delete_parser.add_argument('username', type=str, help='Username of the user to delete.')
    delete_parser.set_defaults(func=delete_user_command) # Link to handler function

    args = parser.parse_args()

    # Call the function associated with the chosen subcommand
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help() # If no subcommand is given

if __name__ == '__main__':
    # To run:
    # python your_script_name.py create john_doe --email john@example.com
    # python your_script_name.py delete jane_smith
    main()
```

---

## 4. Interactive Menus

Menu-driven CLI applications are common for guiding users through various options.

### Simple Menu Loop
```python
def show_main_menu():
    """Displays the main menu options."""
    print("\n=== Main Menu ===")
    print("1. View Data")
    print("2. Process File")
    print("0. Exit")

def handle_view_data():
    print("Displaying data...")

def handle_process_file():
    print("Processing file...")

def main():
    """Main loop for a menu-driven CLI application."""
    while True:
        show_main_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            handle_view_data()
        elif choice == '2':
            handle_process_file()
        elif choice == '0':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
```

### Menu with Function Mapping
Mapping menu choices to functions improves readability and maintainability.

```python
def do_action_a():
    print("Action A performed.")

def do_action_b():
    print("Action B performed.")

def do_action_c():
    print("Action C performed.")

def display_menu_options():
    """Displays menu options with their descriptions."""
    print("\n--- Choose an action ---")
    menu_actions = {
        '1': ("Perform Action A", do_action_a),
        '2': ("Perform Action B", do_action_b),
        '3': ("Perform Action C", do_action_c),
        '0': ("Exit", None) # None indicates exit
    }
    for key, (description, _) in menu_actions.items():
        print(f"{key}. {description}")
    return menu_actions

def main():
    """Interactive menu using a function mapping."""
    actions = display_menu_options() # Get menu options and their handlers

    while True:
        choice = input("\nEnter your choice: ").strip()
        
        if choice in actions:
            description, func = actions[choice]
            if func:
                func() # Execute the chosen function
            else:
                print("Exiting. Farewell!")
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
```

---

## 5. CLI with Database (ORM)

Integrating a database into a CLI application allows for persistent storage and retrieval of data. This section demonstrates using SQLAlchemy, a popular Python ORM.

### Setup (SQLAlchemy ORM)
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the base class for declarative models
Base = declarative_base()

class User(Base):
    """SQLAlchemy model for a User."""
    __tablename__ = 'users' # Table name in the database

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

# Setup database connection
engine = create_engine('sqlite:///cli_app.db') # Connect to a SQLite database file
Base.metadata.create_all(engine) # Create tables defined by Base's metadata
Session = sessionmaker(bind=engine) # Create a session class
```

### CRUD Operations (Create, Read, Update, Delete)
```python
# Assuming Session and User model are defined as above

def create_user_db(session):
    """Creates a new user record in the database."""
    username = input("Enter new username: ").strip()
    email = input("Enter new email: ").strip()

    try:
        new_user = User(username=username, email=email)
        session.add(new_user) # Add the new user object to the session
        session.commit() # Commit the transaction to save to DB
        print(f"User '{username}' created successfully!")
    except Exception as e:
        session.rollback() # Rollback in case of error
        print(f"Error creating user: {e}")

def list_users_db(session):
    """Lists all users from the database."""
    users = session.query(User).all() # Retrieve all users

    if not users:
        print("No users found in the database.")
        return

    print("\n--- Current Users ---")
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

def find_user_db(session):
    """Finds and displays a user by username."""
    username = input("Enter username to find: ").strip()
    user = session.query(User).filter_by(username=username).first() # Query by username

    if user:
        print(f"\nFound User: ID: {user.id}, Username: {user.username}, Email: {user.email}")
    else:
        print(f"User '{username}' not found.")

def update_user_db(session):
    """Updates an existing user's email."""
    username = input("Enter username to update: ").strip()
    user = session.query(User).filter_by(username=username).first()

    if not user:
        print(f"User '{username}' not found.")
        return

    print(f"Current email for '{username}': {user.email}")
    new_email = input("Enter new email (or leave blank to keep current): ").strip()

    if new_email:
        user.email = new_email
        session.commit()
        print(f"User '{username}' updated successfully!")
    else:
        print("No changes made to user.")

def delete_user_db(session):
    """Deletes a user from the database."""
    username = input("Enter username to delete: ").strip()
    user = session.query(User).filter_by(username=username).first()

    if not user:
        print(f"User '{username}' not found.")
        return

    if confirm_action(f"Are you sure you want to delete user '{username}'? (y/n): "):
        session.delete(user) # Mark user for deletion
        session.commit()     # Commit the deletion
        print(f"User '{username}' deleted successfully!")
    else:
        print("User deletion cancelled.")
```

---

## 6. CLI with External APIs

CLI applications can interact with external web APIs to fetch or send data, enriching their functionality. This section demonstrates using the `requests` library to interact with a public API.

### Fetching Pokemon Data (PokeAPI Example)

This example shows how to fetch data for a Pokemon (by name or ID), parse the JSON response, and extract relevant statistics.

```python
import requests

def get_pokemon_data(pokemon_identifier):
    """
    Fetches Pokemon data from the PokeAPI and returns key game-relevant information.

    Args:
        pokemon_identifier (str or int): The name (str) or ID (int) of the Pokemon.
                                       E.g., "pikachu", "charizard", 25.

    Returns:
        dict: A dictionary containing the Pokemon's name, ID, HP, Attack, sprite URL,
              and primary type. Returns None if the Pokemon is not found or an error occurs.
    """
    # Construct the API endpoint URL
    url = f"https://pokeapi.co/api/v2/pokemon/{str(pokemon_identifier).lower()}"
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx) 
        
        data = response.json() # Parse JSON response into a Python dictionary
        
        # Extract desired information from the nested JSON structure
        pokemon_info = {
            "name": data['name'].title(), # Capitalize first letter
            "id": data['id'],
            # Stats array: HP is usually first, Attack is second
            "hp": next((s['base_stat'] for s in data['stats'] if s['stat']['name'] == 'hp'), None),
            "attack": next((s['base_stat'] for s in data['stats'] if s['stat']['name'] == 'attack'), None),
            "sprite_url": data['sprites']['front_default'],
            "type": data['types'][0]['type']['name'].title() # Primary type
        }
        return pokemon_info

    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 404:
            print(f"Pokemon '{pokemon_identifier}' not found.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred while fetching Pokemon data: {e}")
        
    return None

# Example usage:
# pikachu_data = get_pokemon_data("pikachu")
# if pikachu_data:
#     print(f"{pikachu_data['name']} (ID: {pikachu_data['id']}) - Type: {pikachu_data['type']}")
#     print(f"HP: {pikachu_data['hp']}, Attack: {pikachu_data['attack']}")
```

### Building a Simple Pokemon CLI Game

This example combines API interaction with OOP principles to create an interactive Pokemon game where a player can manage a team of Pokemon.

```python
class Pokemon:
    """Represents a simple Pokemon object with basic stats."""
    def __init__(self, name, pokemon_id, hp, attack, sprite_url, pokemon_type):
        self.name = name
        self.pokemon_id = pokemon_id
        self.hp = hp
        self.attack = attack
        self.sprite_url = sprite_url
        self.pokemon_type = pokemon_type

    def display_info(self):
        """Prints the Pokemon's information."""
        print(f"Name: {self.name}")
        print(f"ID: {self.pokemon_id}")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack}")
        print(f"Type: {self.pokemon_type}")
        print(f"Sprite: {self.sprite_url}")

class Player:
    """Represents a player with a collection of Pokemon."""
    def __init__(self, name):
        self.name = name
        self.pokemon_collection = [] # Player's team

    def add_pokemon(self, pokemon):
        """Adds a Pokemon object to the player's collection."""
        if len(self.pokemon_collection) < 6: # Limit team size
            self.pokemon_collection.append(pokemon)
            print(f"{pokemon.name} added to your collection!")
        else:
            print("Your Pokemon collection is full! (Max 6 Pokemon)")

    def remove_pokemon(self, index):
        """Removes a Pokemon from the collection by index."""
        if 0 <= index < len(self.pokemon_collection):
            removed_pokemon = self.pokemon_collection.pop(index)
            print(f"{removed_pokemon.name} was removed from your collection.")
        else:
            print("Invalid index. No Pokemon removed.")

    def show_collection(self):
        """Displays all Pokemon in the player's collection."""
        if not self.pokemon_collection:
            print(f"{self.name}'s collection is empty.")
            return

        print(f"\n--- {self.name}'s Pokemon Collection ---")
        for i, pokemon in enumerate(self.pokemon_collection):
            print(f"--- Slot {i+1} ---")
            pokemon.display_info()
            print("-" * 20)

def choose_starter_pokemon(player):
    """Allows the player to choose a starter Pokemon."""
    starters = ["bulbasaur", "charmander", "squirtle"]
    print("\nChoose your starter Pokemon:")
    for i, name in enumerate(starters):
        print(f"{i+1}. {name.title()}")

    choice = get_valid_integer("Enter the number of your choice: ", min_val=1, max_val=len(starters))
    chosen_starter_name = starters[choice - 1]

    starter_data = get_pokemon_data(chosen_starter_name)
    if starter_data:
        starter_pokemon = Pokemon(
            name=starter_data['name'],
            pokemon_id=starter_data['id'],
            hp=starter_data['hp'],
            attack=starter_data['attack'],
            sprite_url=starter_data['sprite_url'],
            pokemon_type=starter_data['type']
        )
        player.add_pokemon(starter_pokemon)
        print(f"\nCongratulations! You chose {starter_pokemon.name} as your starter!")
    else:
        print("Could not get starter Pokemon data. Please try again.")

def main_game_loop():
    """Main game loop for the Pokemon CLI game."""
    player_name = input("Enter your name, trainer: ")
    player = Player(player_name)

    choose_starter_pokemon(player)

    while True:
        print("\n--- Pokemon Game Menu ---")
        print("1. Show My Pokemon Collection")
        print("2. Catch a New Pokemon")
        print("3. Release a Pokemon")
        print("0. Exit Game")

        choice = get_valid_integer("Enter your choice: ", min_val=0, max_val=3)

        if choice == 1:
            player.show_collection()
        elif choice == 2:
            pokemon_name_or_id = input("Enter Pokemon name or ID to catch: ")
            new_pokemon_data = get_pokemon_data(pokemon_name_or_id)
            if new_pokemon_data:
                new_pokemon = Pokemon(
                    name=new_pokemon_data['name'],
                    pokemon_id=new_pokemon_data['id'],
                    hp=new_pokemon_data['hp'],
                    attack=new_pokemon_data['attack'],
                    sprite_url=new_pokemon_data['sprite_url'],
                    pokemon_type=new_pokemon_data['type']
                )
                player.add_pokemon(new_pokemon)
        elif choice == 3:
            if player.pokemon_collection:
                player.show_collection()
                release_index = get_valid_integer("Enter the slot number of the Pokemon to release (e.g., 1 for first): ", min_val=1, max_val=len(player.pokemon_collection))
                player.remove_pokemon(release_index - 1) # Adjust for 0-based indexing
            else:
                print("Your collection is empty. Nothing to release.")
        elif choice == 0:
            print(f"Thanks for playing, {player.name}! See you next time!")
            break

if __name__ == '__main__':
    # Ensure get_valid_integer is available (copied from above)
    def get_valid_integer(prompt, min_val=None, max_val=None):
        while True:
            try:
                value = int(input(prompt))
                if min_val is not None and value < min_val:
                    print(f"Error: Value must be at least {min_val}.")
                    continue
                if max_val is not None and value > max_val:
                    print(f"Error: Value must be at most {max_val}.")
                    continue
                return value
            except ValueError:
                print("Error: Please enter a valid whole number.")
    
    main_game_loop()
```

---

## 7. Formatting Output

Clear and well-structured output is crucial for a good CLI user experience.

### Using `tabulate` for Tables
The `tabulate` library allows you to print data in a well-formatted tabular form.

```python
from tabulate import tabulate

# Assuming 'Session' and 'User' model are defined from previous DB section
# def list_users_formatted(session):
#     """Lists users in a formatted table using tabulate."""
#     users = session.query(User).all()
#     if not users:
#         print("No users found.")
#         return
#     table_data = [[user.id, user.username, user.email] for user in users]
#     headers = ["ID", "Username", "Email"]
#     print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))

# Install: pip install tabulate
```

### Using `rich` for Beautiful CLI Output
The `rich` library provides rich text, tables, progress bars, markdown, syntax highlighting, and more to the terminal.

```python
from rich.console import Console
from rich.table import Table

console = Console() # Rich console object

# Assuming 'Session' and 'User' model are defined
# def list_users_rich(session):
#     """Lists users with rich, including styled output."""
#     users = session.query(User).all()
#     if not users:
#         console.print("[yellow]No users found.[/yellow]")
#         return
#     table = Table(title="Database Users")
#     table.add_column("ID", style="cyan", no_wrap=True)
#     table.add_column("Username", style="magenta")
#     table.add_column("Email", style="green")
#     for user in users:
#         table.add_row(str(user.id), user.username, user.email)
#     console.print(table)

# Install: pip install rich
```

### Colored Output with `colorama`
The `colorama` library (especially on Windows) helps make ANSI escape codes work for colored terminal output.

```python
from colorama import init, Fore, Style

init()  # Initialize colorama for cross-platform compatibility

def print_success(message):
    """Prints a success message in green."""
    print(Fore.GREEN + message + Style.RESET_ALL)

def print_error(message):
    """Prints an error message in red."""
    print(Fore.RED + message + Style.RESET_ALL)

def print_warning(message):
    """Prints a warning message in yellow."""
    print(Fore.YELLOW + message + Style.RESET_ALL)

def print_info(message):
    """Prints an informational message in blue."""
    print(Fore.BLUE + message + Style.RESET_ALL)

# Usage examples
# print_success("Operation completed successfully!")
# print_error("Error: Something went wrong.")
# print_warning("Warning: Proceed with caution.")
# print_info("Fetching data...")

# Install: pip install colorama
```

---

## 8. Error Handling

Robust CLI applications must gracefully handle errors, providing informative feedback to the user.

### Basic Try-Except in CLI
```python
# Assuming Session and User model are defined
# def safe_create_user(session):
#     """Attempts to create a user with basic error handling."""
#     try:
#         username = input("Enter username: ").strip()
#         email = input("Enter email: ").strip()
#         
#         # Simple validation
#         if not username:
#             raise ValueError("Username cannot be empty.")
#         if "@" not in email:
#             raise ValueError("Email must contain '@'.")

#         user = User(username=username, email=email)
#         session.add(user)
#         session.commit()
#         print_success(f"User '{username}' created successfully!")

#     except ValueError as ve:
#         print_error(f"Validation Error: {ve}")
#     except Exception as e: # Catch broader exceptions
#         session.rollback() # Important for database transactions
#         print_error(f"An unexpected error occurred: {e}")
```

### Custom Exception Handling
Defining custom exception classes can make error handling more specific and clearer.

```python
class CLIAppError(Exception):
    """Base exception for CLI Application errors."""
    pass

class InvalidInputError(CLIAppError):
    """Raised when user input is invalid."""
    pass

class DatabaseOperationError(CLIAppError):
    """Raised when a database operation fails."""
    pass

# Example validation function using custom exception
def validate_username(username):
    if not username or len(username) < 3:
        raise InvalidInputError("Username must be at least 3 characters long.")
    if not username.isalnum():
        raise InvalidInputError("Username must be alphanumeric.")
    return True

# Example usage in a function
# def create_user_with_custom_exceptions(session):
#     try:
#         username = input("Enter username: ").strip()
#         validate_username(username) # This might raise InvalidInputError
        
#         email = get_valid_email() # Re-using previously defined email validation
        
#         # Simulate DB error
#         if username == "faildb":
#             raise DatabaseOperationError("Simulated database error.")

#         user = User(username=username, email=email)
#         session.add(user)
#         session.commit()
#         print_success(f"User '{username}' created successfully!")

#     except InvalidInputError as iie:
#         print_error(f"Input Error: {iie}")
#     except DatabaseOperationError as doe:
#         session.rollback()
#         print_error(f"Database Error: {doe}")
#     except Exception as e:
#         session.rollback()
#         print_error(f"An unexpected error occurred: {e}")
```

---

## 9. Complete CLI Application Example

This section presents a fully functional user management CLI application, demonstrating the integration of various concepts discussed.

```python
#!/usr/bin/env python3
"""
Complete CLI Application with Database Integration.
Manages users (Create, Read, Update, Delete) using SQLAlchemy and provides styled output.
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from colorama import init, Fore, Style # For colored terminal output
import re # For email validation

# Initialize colorama for cross-platform colored output
init()

# --- Database Setup (SQLAlchemy) ---
Base = declarative_base() # Base class for declarative models

class User(Base):
    """SQLAlchemy model representing a user in the database."""
    __tablename__ = 'users' # Table name in the database

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

# Configure and create the database engine
engine = create_engine('sqlite:///cli_users.db', echo=False) # 'echo=True' for SQL logging
Base.metadata.create_all(engine) # Create tables
Session = sessionmaker(bind=engine) # Session factory

# --- Helper Functions for Output ---
def print_success(msg):
    print(Fore.GREEN + msg + Style.RESET_ALL)

def print_error(msg):
    print(Fore.RED + msg + Style.RESET_ALL)

def print_info(msg):
    print(Fore.CYAN + msg + Style.RESET_ALL)

def confirm_action(prompt):
    """Gets a yes/no confirmation from the user."""
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']: return True
        elif response in ['n', 'no']: return False
        else: print_error("Please enter 'y' or 'n'.")

# --- CRUD Operations ---
def create_user_cli(session):
    """CLI function to create a new user."""
    print_info("\n--- Create New User ---")
    username = input("Enter username: ").strip()
    email = get_valid_email_cli("Enter email: ") # Re-use validation

    if not username:
        print_error("Username cannot be empty.")
        return

    try:
        if session.query(User).filter_by(username=username).first():
            print_error(f"Username '{username}' already exists.")
            return
        if session.query(User).filter_by(email=email).first():
            print_error(f"Email '{email}' already registered.")
            return

        new_user = User(username=username, email=email)
        session.add(new_user)
        session.commit()
        print_success(f"User '{username}' created successfully!")
    except Exception as e:
        session.rollback()
        print_error(f"Database error: {e}")

def list_all_users_cli(session):
    """CLI function to list all users."""
    users = session.query(User).all()
    if not users:
        print_info("No users found.")
        return

    print_info("\n--- All Registered Users ---")
    print(f"{'ID':<5} {'Username':<20} {'Email':<30}")
    print("-" * 55)
    for user in users:
        print(f"{user.id:<5} {user.username:<20} {user.email:<30}")

def find_user_cli(session):
    """CLI function to find a user by username."""
    username = input("Enter username to search: ").strip()
    user = session.query(User).filter_by(username=username).first()

    if user:
        print_info(f"\nFound: ID: {user.id} | Username: {user.username} | Email: {user.email}")
    else:
        print_error(f"User '{username}' not found.")

def update_user_cli(session):
    """CLI function to update a user's email."""
    username = input("\nEnter username to update: ").strip()
    user = session.query(User).filter_by(username=username).first()

    if not user:
        print_error(f"User '{username}' not found.")
        return

    print_info(f"Current email: {user.email}")
    new_email = get_valid_email_cli("Enter new email (or press Enter to keep current): ", allow_empty=True)

    if new_email and new_email != user.email:
        user.email = new_email
        session.commit()
        print_success(f"User '{username}' email updated successfully!")
    else:
        print_info("No changes made to user email.")

def delete_user_cli(session):
    """CLI function to delete a user."""
    username = input("\nEnter username to delete: ").strip()
    user = session.query(User).filter_by(username=username).first()

    if not user:
        print_error(f"User '{username}' not found.")
        return

    if confirm_action(f"Are you sure you want to delete user '{username}'? (y/n): "):
        session.delete(user)
        session.commit()
        print_success(f"User '{username}' deleted successfully!")
    else:
        print_info("User deletion cancelled.")

# --- Menu and Main Loop ---
def show_main_menu():
    """Displays the main menu of the User Management System."""
    print("\n" + "=" * 40)
    print(Fore.YELLOW + "    User Management System" + Style.RESET_ALL)
    print("=" * 40)
    print("1. Create User")
    print("2. List All Users")
    print("3. Find User")
    print("4. Update User Email")
    print("5. Delete User")
    print("0. Exit")
    print("=" * 40)

def get_valid_email_cli(prompt="Enter email: ", allow_empty=False):
    """Helper for email validation in CLI context."""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    while True:
        email = input(prompt).strip()
        if allow_empty and not email:
            return ""
        if re.match(email_pattern, email):
            return email
        print_error("Invalid email format. Please try again.")

def main_cli_app():
    """Main function to run the complete CLI application."""
    session = Session() # Create a new session for each run

    menu_actions = {
        '1': create_user_cli,
        '2': list_all_users_cli,
        '3': find_user_cli,
        '4': update_user_cli,
        '5': delete_user_cli
    }

    print_success("\nWelcome to the User Management System CLI!")

    try:
        while True:
            show_main_menu()
            choice = input("\nEnter your choice: ").strip()

            if choice == '0':
                print_success("\nExiting application. Goodbye!")
                break
            elif choice in menu_actions:
                menu_actions[choice](session)
            else:
                print_error("Invalid choice. Please select a valid option.")
    except KeyboardInterrupt:
        print_info("\n\nApplication interrupted. Exiting gracefully.")
    finally:
        session.close() # Ensure session is closed

if __name__ == '__main__':
    main_cli_app()
```

---

## Advanced Features

### Progress Bars with `tqdm`
For long-running operations, `tqdm` provides smart progress bars.

```python
from tqdm import tqdm
import time

def simulate_long_process(items):
    """Simulates a long process with a tqdm progress bar."""
    print("Starting long process...")
    for item in tqdm(items, desc="Processing Items", unit="item"):
        time.sleep(0.05) # Simulate work
    print("Process complete!")

# Example usage:
# my_items_to_process = list(range(100))
# simulate_long_process(my_items_to_process)

# Install: pip install tqdm
```

### Logging
Python's built-in `logging` module is essential for tracking events, debugging, and understanding application behavior.

```python
import logging

# Configure basic logging
logging.basicConfig(
    filename='cli_app.log', # Log to a file
    level=logging.INFO,     # Log INFO level and above
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def example_function_with_logging(data_id):
    """An example function demonstrating logging."""
    logging.info(f"Function started for data_id: {data_id}")
    try:
        # Simulate an operation
        if data_id % 2 != 0:
            raise ValueError("Data ID must be even.")
        logging.debug(f"Processed even data_id: {data_id}")
        print(f"Processing data_id: {data_id}")
    except ValueError as e:
        logging.error(f"Validation error for data_id {data_id}: {e}")
        print(f"Error for {data_id}: {e}")
    except Exception as e:
        logging.critical(f"Critical error for data_id {data_id}: {e}")
        print(f"Critical error for {data_id}.")

# example_function_with_logging(10)
# example_function_with_logging(7)
```

---

## Best Practices

### 1. Input Validation
Always validate user input to prevent errors and ensure data integrity. This includes type checks, range checks, and format checks.

### 2. Clear User Feedback
Provide clear, concise, and actionable feedback to the user. Use colors, tables, and progress indicators to enhance the user experience.

### 3. Handle Errors Gracefully
Implement robust `try-except` blocks to catch potential errors, inform the user, and prevent the application from crashing. Rollback database transactions on error.

### 4. Confirm Destructive Actions
For operations that modify or delete data, always ask for user confirmation.

### 5. Modularize Your Code
Break down your CLI application into smaller, manageable functions and modules (e.g., separate logic for input, output, database, API calls).

### 6. Use Environment Variables for Secrets
Never hardcode sensitive information like API keys or database credentials directly in your code. Use environment variables.

### 7. Session Management (for Database/APIs)
When interacting with databases or stateful APIs, manage sessions properly, ensuring they are opened and closed correctly.

---

## See Also

-   **[SQL and SQLAlchemy Cheat Sheet](../cheatsheets/SQL_and_SQLAlchemy_Cheat_Sheet.md)** - For database setup and ORM details.
-   **[APIs & HTTP Requests Cheat Sheet](../cheatsheets/APIs_and_Requests_Cheat_Sheet.md)** - For making HTTP requests to external APIs.
-   **[Error Handling Cheat Sheet](../cheatsheets/Error_Handling_Cheat_Sheet.md)** - In-depth guide on Python error handling.
-   **[Python Basics Cheat Sheet](../cheatsheets/Python_Basics_Cheat_Sheet.md)** - Fundamentals of Python programming.
