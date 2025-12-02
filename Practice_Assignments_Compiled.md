# Compiled Practice Assignments

## Table of Contents

1. [Intro to Python & Control Flow](#1-intro-to-python--control-flow)
2. [Loops & Logic](#2-loops--logic)
3. [Functions & Lists](#3-functions--lists)
4. [Dictionaries & Sets](#4-dictionaries--sets)
5. [Object-Oriented Programming (OOP)](#5-object-oriented-programming-oop)
6. [Regular Expressions (Regex)](#6-regular-expressions-regex)
7. [Functional Programming](#7-functional-programming)
8. [APIs & HTTP Requests](#8-apis--http-requests)
9. [SQL & Database Design](#9-sql--database-design)
10. [Flask & ORM (Intermediate/Advanced)](#10-flask--orm-intermediateadvanced)

---

## 1. Intro to Python & Control Flow

**Solution:** [Python_Basics/Control_Flow_Solutions.py](./Practice_Solutions/Python_Basics/Control_Flow_Solutions.py)

### Task 1.1: Greeting

- **Goal:** Write a script that asks for a user's name and age, then prints a greeting message like: `"Hello, [Name]! You are [Age] years old!"`

### Task 1.2: Century Age Calculator

- **Goal:** Calculate the year a person will turn 100.
- **Logic:** `century_year = current_year + (100 - current_age)`

### Task 1.3: Simple Conditional

- **Goal:** Write an if-else statement.
- **Prompt:** Ask for user input (e.g., "Is it raining?"). If yes, print "Take an umbrella". If no, print "Enjoy the sun".

### Task 1.4: Comparison Operators Practice

- **Goal:** Check voting eligibility.
- **Logic:** If `age >= 18`, print "Can vote". Else, print "Cannot vote".

### Task 1.5: Complex Decisions (Grades)

- **Goal:** Convert numerical scores to letter grades.
- **Logic:**
  - 90-100: A
  - 80-89: B
  - 70-79: C
  - 60-69: D
  - < 60: F

### Task 1.6: Exception Handling

- **Goal:** Write a program that asks for an integer (age).
- **Requirement:** Use `try/except` to handle cases where the user types text instead of a number.

---

## 2. Loops & Logic

**Solution:** [Python_Basics/Control_Flow_Solutions.py](./Practice_Solutions/Python_Basics/Control_Flow_Solutions.py)

### Task 2.1: Basic While Loop

- **Goal:** Create a loop that counts from 1 to 5 and prints each number.

### Task 2.2: Countdown

- **Goal:** Create a loop that counts down from 5 to 1, then prints "Blast Off!".

### Task 2.3: Password Checker

- **Goal:** Create a `while` loop that repeatedly asks the user for a password until they type "secret".

### Task 2.4: Temperature Monitor

- **Goal:** Create a script that accepts temperature readings from the user until they type 'done'.
- **Output:** Print the count of readings, the total, the average, the minimum, and the maximum.

---

## 3. Functions & Lists

**Solution:** [Data_Structures/Lists_Dicts_Solutions.py](./Practice_Solutions/Data_Structures/Lists_Dicts_Solutions.py)

### Task 3.1: Basic Functions

- **Define:** `greet(name)` -> prints "Hello [name]"
- **Define:** `rectangle_area(length, width)` -> returns area.
- **Define:** `add(num1, num2)` -> returns sum.

### Task 3.2: Temperature Converter

- **Define:** `celcius_to_farenheit(celcius)` -> returns converted temp.

### Task 3.3: List Statistics

- **Goal:** Write a function `list_statistics(numbers)` that takes a list of numbers and returns a dictionary containing:
  - `max`: Maximum value
  - `min`: Minimum value
  - `avg`: Average value
  - `sum`: Sum of values

### Task 3.4: List Operations

- Create a list of fruits.
- Add "strawberry" to the end.
- Remove "orange" by value.
- Remove the item at index 1.
- Check if "apple" is in the list.

---

## 4. Dictionaries & Sets

**Solution:** [Data_Structures/Lists_Dicts_Solutions.py](./Practice_Solutions/Data_Structures/Lists_Dicts_Solutions.py)

### Task 4.1: Student Scores

- **Data:** A dictionary of student names and scores.
- **Subtasks:**
    1. Loop through and print all names.
    2. Loop through and print all scores.
    3. Print "Name: Score" pairs.
    4. Use `.get()` to safely check for a missing student.

### Task 4.2: Inventory System

- **Structure:** Nested dictionary (Categories -> Items -> Details).
- **Subtasks:**
    1. Access and print specific item prices.
    2. Update stock levels.
    3. Add new items and categories.
    4. Calculate the total value of inventory.

### Task 4.3: Cleaning Usernames

- **Goal:** Write a function `clean_usernames(raw_list)` that takes a list of strings (some with whitespace/casing issues) and returns a clean list (lowercase, stripped).

### Task 4.4: Set Operations

- **Scenario:** You have two lists of hobbies (e.g., `wilson_hobbies` and `friend_hobbies`).
- **Subtasks:**
    1. Find common interests (Intersection).
    2. Find all unique hobbies combined (Union).
    3. Find hobbies unique to one person (Difference).

---

## 5. Object-Oriented Programming (OOP)

**Solution:** [OOP/OOP_Solutions.py](./Practice_Solutions/OOP/OOP_Solutions.py)

### Task 5.1: Student Class

- **Attributes:** `name`, `age`, `grades` (list).
- **Methods:**
  - `add_grade(grade)`
  - `grade_avg()`: Returns average.
  - `info()`: Prints student details.

### Task 5.2: User Class (Encapsulation)

- **Attributes:** `username` (public), `_password` (protected/private).
- **Methods:**
  - `set_password(new_pass)`: Validates length/characters before setting.
  - `get_password()`: Returns the password (or a masked version).

### Task 5.3: RPG Battle System (Inheritance/Polymorphism)

- **Base Class:** `Character` (name, health, attack_power).
- **Subclasses:**
  - `Warrior` (High health, standard attack).
  - `Mage` (Lower health, high attack, `special_attack` method).
  - `EvilWizard` (Boss character, `regenerate` method).
- **Goal:** Simulate a battle loop where characters attack each other until one falls.

---

## 6. Regular Expressions (Regex)

**Solution:** [Regex/Regex_Solutions.py](./Practice_Solutions/Regex/Regex_Solutions.py)

### Task 6.1: Basic Patterns

- Find the first word in a text (`\w`).
- Find a phone number (`\d{3}-\d{4}`).
- Find all 5-digit IDs (`\d{5}`).

### Task 6.2: Data Cleaning

- **Input:** Raw customer feedback with varying spacing and sensitive data.
- **Subtasks:**
    1. Remove phone numbers (Replace with "[REDACTED]").
    2. Fix multiple spaces (Replace `\s+` with `" "`).

---

## 7. Functional Programming

**Solution:** [Functional/Functional_Solutions.py](./Practice_Solutions/Functional/Functional_Solutions.py)

### Task 7.1: Sorting (Lambda)

- **Input:** List of product dictionaries (`{'name': 'A', 'price': 10}`).
- **Goal:** Sort by price (descending) using `sorted()` and a `lambda` key.

### Task 7.2: Map

- **Input:** List of employee dictionaries.
- **Goal:** Use `map()` to create a new list where every employee gets a 7% raise.

### Task 7.3: Filter

- **Input:** List of books (`{'title': 'A', 'rating': 4.5}`).
- **Goal:** Use `filter()` to find books with a rating >= 4.0.

### Task 7.4: List Comprehensions

- **Goal:** Write a one-liner that takes a list of numbers, keeps only the evens, and doubles them.

---

## 8. APIs & HTTP Requests

**Solution:** [APIs/API_Solutions.py](./Practice_Solutions/APIs/API_Solutions.py)

### Task 8.1: Basic Fetch

- **Goal:** Use `requests` to fetch a random dog image from `https://dog.ceo/api/breeds/image/random` and print the URL.

### Task 8.2: PokeAPI Wrapper

- **Goal:** Write a function `get_pokemon_data(name)` that:
    1. Fetches data from `https://pokeapi.co/api/v2/pokemon/{name}`.
    2. Parses JSON to extract Name, ID, HP, and Type.
    3. Returns a dictionary (or `None` on error).

### Task 8.3: Spotify Token (Auth)

- **Goal:** Implement the Client Credentials Flow to get a Spotify Access Token.
- **Steps:**
    1. Base64 encode `client_id:client_secret`.
    2. POST to `https://accounts.spotify.com/api/token`.
    3. Extract `access_token` from the response.

---

## 9. SQL & Database Design

**Solution:** [SQL/SQL_Solutions.sql](./Practice_Solutions/SQL/SQL_Solutions.sql)

### Task 9.1: DDL (Creating Tables)

- Write SQL to create a `Students` table (id, name, email) and a `Courses` table (id, title, instructor).

### Task 9.2: Basic Queries

- Write SQL to select all students named "Alice".
- Write SQL to update a course title.
- Write SQL to delete a specific record.

---

## 10. Flask & ORM (Intermediate/Advanced)

**Solution:**

- [Mechanic Shop Solution](./Practice_Solutions/Mechanic_Shop_Solutions.py)
- [Inventory/Order Solution](./Practice_Solutions/Inventory_Order_Solutions.py)
- [ORM Clinic Logic](./Practice_Solutions/ORM_Clinic/ORM_Clinic_Implementation.py)

### Task 10.1: Mechanic Shop API

- **Context:** Mechanics, Customers, Tickets.
- **Subtasks:**
    1. **Customer Search:** Endpoint to find customer by email (`GET /search?email=...`).
    2. **Analytics:** Endpoint to find the mechanic with the most completed tickets.
    3. **Pagination:** Paginate the `GET /tickets` endpoint.

### Task 10.2: Library/Inventory Logic

- **Goal:** Implement "Item Definition" vs "Item Instance" pattern.
- **Endpoints:**
  - `POST /catalog`: Create a generic book title.
  - `POST /catalog/{id}/add`: Add a physical copy of that book.

### Task 10.3: Order Processing

- **Goal:** Implement a checkout flow.
- **Flow:** Create Order (Pending) -> Add Items -> Checkout (Complete).

### Task 10.4: Pet Clinic Appointments

- **Goal:** Create a CLI or API function to schedule an appointment.
- **Logic:** Select Pet -> Select Vet -> Choose Date -> Commit to DB.
