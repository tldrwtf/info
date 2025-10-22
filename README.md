Python Cheat Sheet -

### Variables \& Data Types

```python
# Variable assignment
name = "Allan"
age = 28
price = 3.14
is_active = True

# Type checking
type(variable)  # Returns the type
isinstance(value, int)  # Check if value is int
isinstance(value, (int, float))  # Check multiple types

# Type conversion (casting)
age_string = str(age)
price_int = int(price)  # 3
number_from_string = int("42")
```


### Input \& Output

```python
# Getting user input
username = input("Enter your name: ")
age = int(input("Enter age: "))  # Convert to integer

# Printing
print("Hello")
print(f"Hello, {name}!")  # f-string formatting
print(f"Average: {total/count:.2f}")  # 2 decimal places

# String concatenation
print("Hello, " + name + "!")  # Less preferred
```


## Control Flow

### Conditional Statements

```python
# Basic if-elif-else
if condition:
    # code
elif another_condition:
    # code
else:
    # code

# Comparison operators: ==, !=, <, >, <=, >=
if x % 2 == 1:
    print("odd")
else:
    print("even")

# Logical operators: and, or, not
if age >= 18 and has_license:
    print("Can drive")

# Grade evaluation example
score = int(input("Enter your test score: "))

if score >= 90 and score <= 100:
    print("Grade: A - Excellent!")
elif score >= 80 and score < 90:
    print("Grade: B - Good Job!")
elif score >= 70 and score < 80:
    print("Grade: C - Satisfactory")
elif score >= 60 and score < 70:
    print("Grade: D - Needs improvement")
elif score >= 1 and score < 60:
    print("Grade: F - Please see teacher")
else:
    print("Invalid score")
```


### Truthy \& Falsy Values

```python
# Falsy: 0, "", [], {}, (), None, False
grocery_list = []
if grocery_list:
    print("Time to shop")
else:
    print("Nothing to buy")

# Truthy: Any non-zero number, non-empty string, non-empty collection
```


## Loops

### While Loops

```python
# Basic while loop
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

# Countdown example
number = 10
while number >= 1:
    print(number)
    number = number - 1
print("Blast Off!")

# Infinite loop with break
while True:
    answer = input("Type 'exit' to stop: ")
    if answer == "exit":
        break
    print("Still loading...")

# Continue - skip iteration
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)  # Skips printing 3
```


### For Loops

```python
# Loop through range
for i in range(5):  # 0 to 4
    print(i)

for i in range(1, 6):  # 1 to 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (step of 2)
    print(i)

# Loop through list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Loop through string
for letter in "ABC":
    print(f"Character: {letter}")

# Enumerate - get index and value
for index, fruit in enumerate(fruits):
    print(f"At index {index}: {fruit}")
```


## Lists

### List Basics

```python
# Creating lists
movies = ["Inception", "The Matrix", "Interstellar"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Alice", 25, True, 3.14]
empty = []

# Accessing elements
movies[^0]        # First element
movies[-1]       # Last element
movies[1:3]      # Slicing [start:stop]
movies[:2]       # First 2 elements
movies[2:]       # From index 2 to end
movies[::-1]     # Reverse list
```


### List Methods - Time Complexity

```python
# Adding elements
mylist.append(item)        # O(1) - add to end
mylist.insert(2, item)     # O(n) - insert at position
mylist.extend([1, 2, 3])   # O(k) - add multiple items

# Removing elements
mylist.pop()               # O(1) - remove last
mylist.pop(1)              # O(n) - remove by index
mylist.remove(item)        # O(n) - remove by value
del mylist[^3]              # O(n) - delete by index
mylist.clear()             # O(1) - empty list

# Other operations
len(mylist)                # O(1) - length
mylist.count(item)         # O(n) - count occurrences
mylist.index(item)         # O(n) - find index
mylist.reverse()           # O(n) - reverse in-place
mylist.sort()              # O(n log n) - sort in-place
sorted(mylist)             # O(n log n) - return sorted copy

# Membership check
if item in mylist:         # O(n) - linear search
    print("Found")
```


## Dictionaries

### Dictionary Basics

```python
# Creating dictionaries
student = {"name": "Maya", "age": 22, "major": "CS"}
empty_dict = {}

# Accessing values - O(1)
student["name"]                    # Direct access
student.get("age")                 # Safe access
student.get("grade", "N/A")        # With default value

# Adding/Modifying - O(1)
student["age"] = 28
student["gpa"] = 3.8

# Removing - O(1)
del student["major"]
removed = student.pop("age")

# Membership check - O(1) constant time
if "name" in student:
    print(f"Name: {student['name']}")
```


### Looping Through Dictionaries

```python
menu = {"burger": 14.50, "salad": 27.0, "fries": 2.50}

# Loop keys (default)
for item in menu:
    print(item)

# Loop values
for price in menu.values():
    print(price)

# Loop key-value pairs
for food, price in menu.items():
    print(f"{food}: ${price}")

# Get all keys/values
keys = list(menu.keys())
values = list(menu.values())
```


### Nested Dictionaries

```python
contact = {
    "Billy": {
        "phone": "12345678",
        "email": "billy@billy.com",
        "address": {"street": "1123 fun street", "city": "Python City"}
    }
}

# Accessing nested data
contact["Billy"]["phone"]
contact["Billy"]["address"]["city"]

# Library example
library = {
    "book1": {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    }
}
```


## Functions

### Function Basics

```python
# Basic function
def greet(name):
    print(f"Hello, {name}!")

# Function with return
def add(num1, num2):
    return num1 + num2

# Multiple return values
def divide_with_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# Using returned values
result = add(5, 8)
q, r = divide_with_remainder(10, 3)

# Rectangle area calculation
def rectangle_area(length, width):
    area = length * width
    print(f"The area is {area}")
    return area
```


### Parameters \& Arguments

```python
# Default parameters
def introduce(name, title="Mr./Mrs"):
    print(f"Hello, {title} {name}!")

introduce("Bob")              # Uses default
introduce("Sally", "Mrs.")    # Override default

# Format phone number with defaults
def format_phone_number(number, country_code="+1"):
    return f"{country_code}-{number}"

# Temperature conversion
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Compound interest calculator
def calculate_compound_interest(principal, rate=0.05, compounding_period=1, years=1):
    # A = P(1 + r/n)^nt
    amount = principal * (1 + rate/compounding_period) ** (compounding_period * years)
    return amount

# List statistics
def list_statistics(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum
```


## String Methods

### Common String Operations

```python
text = "  HeLlo WOrLd!  "

# Case conversion (out-of-place - returns new string)
text.lower()      # "  hello world!  "
text.upper()      # "  HELLO WORLD!  "
text.title()      # "  Hello World!  "

# Whitespace
text.strip()      # "HeLlo WOrLd!" - remove leading/trailing
text.strip("!@#$%^&*() ")   # Remove specific characters

# Testing
"12345".isdigit()          # True - all digits
"AllanAhmed".isalpha()     # True - all letters
"allan123".isalnum()       # True - letters/numbers

# Searching
sentence = "Python-is-fun-and-Python-is-powerful"
sentence.count("Python")   # 2 - count occurrences
sentence.find("power")     # 26 - starting index (-1 if not found)

# Splitting and joining
words = sentence.split("-")         # Split into list
joined = " ".join(words)            # Join list with space

# Membership
if "-" in sentence:
    print("Has hyphens")
```


## Sets \& Tuples

### Sets (Unique, Unordered)

```python
# Creating sets
unique_numbers = {1, 2, 3, 4, 5}
empty_set = set()  # {} creates empty dict

# Remove duplicates
alist = [1, 1, 2, 2, 3, 3]
unique = set(alist)  # {1, 2, 3}
back_to_list = list(unique)

# Adding/Removing
fruits = {"apple", "orange"}
fruits.add("banana")
fruits.update(["grapes", "pears"])
fruits.discard("apple")  # No error if not found
fruits.remove("orange")  # Raises error if not found

# Set operations
set1 = {1, 2, 3, 4}
set2 = {2, 4, 6, 8}
set1.union(set2)          # {1, 2, 3, 4, 6, 8}
set1.intersection(set2)   # {2, 4}
set1.difference(set2)     # {1, 3}
set1 - set2               # Same as difference

# Real-world example
allan_hobbies = {"coding", "gaming", "reading"}
peter_hobbies = {"gaming", "hiking", "reading"}
common_interests = allan_hobbies.intersection(peter_hobbies)
# {'gaming', 'reading'}
```


### Tuples (Immutable)

```python
# Creating tuples
coordinates = (3, 4)
singleton = (1,)  # Comma required for single item
empty_tuple = ()

# Accessing (like lists)
first, second = coordinates  # Unpacking

# Immutable - cannot modify
# coordinates[^0] = 5  # TypeError

# Zip - combine lists
foods = ["Pizza", "steak", "nachos"]
prices = [20, 63.5, 12]
zipped = list(zip(foods, prices))
# [("Pizza", 20), ("steak", 63.5), ("nachos", 12)]

for food, price in zip(foods, prices):
    print(f"{food}: ${price}")
```


## Regular Expressions (Regex)

### Regex Basics

```python
import re

# re.search() - finds FIRST match, returns match object
text = "My phone is 555-1234"
match = re.search(r"\d+", text)  # Finds "555"
if match:
    print(match.group())  # Unpack with .group()

# re.findall() - finds ALL occurrences, returns list
numbers = re.findall(r"\d+", "I have 5 cats and 3 dogs")
print(numbers)  # ['5', '3']

# re.match() - checks if text STARTS with pattern
result = re.match(r"Hello", "Hello world")  # Match object
result = re.match(r"Hello", "world Hello")  # None

# re.sub() - find and replace (powerful .replace())
text = "I love cats. cats are great."
new_text = re.sub(r"cats", "dogs", text)
```


### Metacharacters

```python
import re

# \d - any digit (0-9)
re.findall(r"\d", "abc123xyz")  # ['1', '2', '3']

# \w - word character (letters, digits, underscores)
re.findall(r"\w+", "hello_world123")  # ['hello_world123']

# \s - whitespace (spaces, tabs, newlines)
re.findall(r"\s", "hello world")  # [' ']

# . - wildcard (any character except newline)
re.findall(r".", "abc")  # ['a', 'b', 'c']

# \b - word boundary
re.findall(r"\bcat\b", "cat cats scatter")  # ['cat']
```


### Quantifiers

```python
# + means "one or more"
re.findall(r"\d+", "I have 123 apples and 45 oranges")
# ['123', '45']

# * means "zero or more"
re.findall(r"\d*", "abc123")  # ['', '', '', '123', '']

# ? means "zero or one"
re.findall(r"colou?r", "color colour")  # ['color', 'colour']

# {n} means "exactly n times"
re.findall(r"\d{3}", "123 45 6789")  # ['123', '678']

# {n,m} means "between n and m times"
re.findall(r"\d{2,4}", "1 12 123 1234 12345")
# ['12', '123', '1234', '1234']

# Find phone numbers
re.findall(r"\d{3}-\d{4}", "Call me at 555-1234")  # ['555-1234']
```


### Character Sets

```python
# [] allows custom character matching
re.findall(r"[aeiou]", "hello")  # ['e', 'o'] - vowels

# Ranges
re.findall(r"[a-z]+", "Hello123World")  # ['ello', 'orld']
re.findall(r"[0-9]", "abc123")  # ['1', '2', '3']
re.findall(r"[A-Z]", "Hello World")  # ['H', 'W']

# Partial ranges
re.findall(r"[0-5]", "0123456789")  # ['0', '1', '2', '3', '4', '5']

# Email pattern example
pattern = r"[a-zA-Z0-9._+-]+@[a-zA-Z_]+\.[a-z]{2,3}"
emails = re.findall(pattern, "Contact: john@email.com or sally@test.org")
```


### Groups and Substitution

```python
# Groups () - capture patterns
text = "John Smith, 555-1234"
match = re.search(r"(\w+) (\w+), (\d{3}-\d{4})", text)
if match:
    first = match.group(1)  # "John"
    last = match.group(2)   # "Smith"
    phone = match.group(3)  # "555-1234"

# Named groups
pattern = r"(?P<first>\w+) (?P<last>\w+)"
match = re.search(pattern, "John Smith")
print(match.group('first'))  # "John"

# Rearranging with sub
date = "12/25/2024"
new_format = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\1-\2", date)
print(new_format)  # "2024-12-25"

# Replace phone numbers for privacy
feedback = "Call me at 555-0123 for details"
cleaned = re.sub(r"\d{3}-\d{4}", "[PHONE REMOVED]", feedback)
```


### Compile (Store Patterns)

```python
# Compile for reuse and efficiency
email_pattern = re.compile(r"[a-zA-Z0-9._+-]+@[a-zA-Z_]+\.[a-z]{2,3}")

# Use compiled pattern
text1 = "Email: john@test.com"
text2 = "Contact: sarah@company.org"

emails1 = email_pattern.findall(text1)
emails2 = email_pattern.findall(text2)

# Multiple space cleanup
space_pattern = re.compile(r"\s{2,}")
cleaned = space_pattern.sub(" ", "Too    many     spaces")
```


## APIs \& HTTP Requests

### API Basics

```python
import requests

# GET request - retrieve data from server
def send_request():
    '''Making a request to the JSONPlaceholder API'''
    
    # Step 1: Define URL and endpoint
    url = "https://jsonplaceholder.typicode.com"
    endpoint = "/posts"
    
    # Step 2: Make the request
    response = requests.get(url + endpoint)
    
    # Step 3: Check status code
    print(response.status_code)  # 200 = success
    
    # Step 4: Parse JSON data
    data = response.json()
    print(data)

send_request()
```


### HTTP Methods (CRUD Operations)

```python
import requests

# POST - Create data in database
def create_new_post():
    '''Endpoint to send a POST request to the JSONPlaceholder API'''
    
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Create request body (data to send)
    new_post = {
        "title": "My new post",
        "body": "This is the content",
        "userId": 1
    }
    
    # Sending a POST request
    response = requests.post(url, json=new_post)
    
    if response.status_code == 201:  # 201 = Created
        print("Post created successfully!")
        print(response.json())

# GET - Read/retrieve data from database
def get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()
    return posts

# PUT - Update existing data in database
def update_post(post_id, updated_data):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.put(url, json=updated_data)
    return response.json()

# DELETE - Remove data from database
def delete_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.delete(url)
    return response.status_code  # 204 = No Content (success)
```


### Query Parameters

```python
import requests

def query_params():
    '''Testing using query parameters, sending info through the url'''
    
    # Query parameters come after '?'
    # Organized in key=value pairs
    # Often used for filtering, sorting, sending quick data
    
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Method 1: Add to URL directly
    response = requests.get(url + "?userId=1")
    
    # Method 2: Use params dictionary (preferred)
    params = {
        "userId": 1,
        "title": "some title"
    }
    response = requests.get(url, params=params)
    
    print(response.json())
```


### Headers

```python
import requests

def send_with_headers():
    # Headers store additional information about our request
    # Examples: date format, credentials, authorization tokens
    
    url = "https://jsonplaceholder.typicode.com/posts"
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "My-App/1.0",
        # "Authorization": "Bearer <token>"  # For authenticated requests
    }
    
    response = requests.get(url, headers=headers)
    return response.json()
```


### HTTP Status Codes

```python
# 2xx - Success
# 200 OK - Request was successful
# 201 Created - Successful creation
# 204 No Content - Request successful, no data returned

# 3xx - Redirection
# 301 Moved Permanently - Continuous redirection

# 4xx - Client Error (Your mistake)
# 400 Bad Request - Malformed or missing data
# 401 Unauthorized - You don't have proper credentials
# 404 Not Found - The resource does not exist
# 429 Too Many Requests - Exceeded max requests

# 5xx - Server Error (Their problem)
# 500 Internal Server Error - Something broke on their end
# 503 Service Unavailable - Temporarily down for maintenance
# 504 Gateway Timeout - Server took too long to respond
```


### Real-World API Example

```python
import requests

def get_random_dog():
    """
    Fetches a random dog image from Dog CEO API
    """
    # 1. Make a GET request to the API
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    
    # 2. Get the JSON response
    data = response.json()
    
    # 3. Print the image URL
    print(f"Random dog image: {data['message']}")
    return data['message']

# Test your function
get_random_dog()
```


### Virtual Environment Setup

```python
# Creating Virtual Environment
# Windows:
# python -m venv venv

# Mac:
# python3 -m venv venv

# Activating Virtual Environment
# Windows:
# venv\Scripts\activate

# Mac:
# source venv/bin/activate

# Confirm active by seeing (venv) next to user in terminal

# Installing packages
# pip install requests

# Check installs
# pip list  # Lists out all installed packages
```


## Functional Programming

### Lambda Functions

```python
# Basic lambda syntax
# lambda parameters: expression

# Regular function
def calculate_tax(price):
    return price * 0.07

# Lambda equivalent
calculate_tax = lambda price: price * 0.07
print(calculate_tax(15))  # 1.05

# Lambda for sorting
products = [
    {'name': 'laptop', 'price': 999.99},
    {'name': 'mouse', 'price': 64.99},
    {'name': 'keyboard', 'price': 129.99}
]

# Sort by price (descending)
sorted_products = sorted(products, key=lambda p: p["price"], reverse=True)

# Sort by multiple criteria
by_category_name = sorted(products, key=lambda p: (p['category'], p['name']))

# Lambda with conditionals (ternary operator)
check_even = lambda x: "even" if x % 2 == 0 else "odd"
print(check_even(4))  # "even"

# Lambda with two parameters
multiply = lambda x, y: x * y
print(multiply(5, 3))  # 15
```


### Map Function

```python
# Map applies a function to each item in a list
numbers = [1, 2, 3, 4, 5]

# Traditional approach
def double_nums(alist):
    output = []
    for num in alist:
        output.append(num * 2)
    return output

# Using map with lambda
doubled = list(map(lambda num: num * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Map with complex data
users = [
    {'name': 'PETER COTTONTAIL', 'email': 'PCOTTON@EMAIL.COM'},
    {'name': 'TONY STARK', 'email': 'TONYS@EMAIL.COM'}
]

# Normalize data
def normalize_user(user):
    return {
        'name': user['name'].title(),
        'email': user['email'].lower(),
        'username': user['name'].split()[^0].lower()
    }

normalized_users = list(map(normalize_user, users))
```


### Filter Function

```python
# Filter creates a new list based on a condition
numbers = [1, 2, 3, 4, 5]

# Traditional approach
def only_evens(nums):
    output = []
    for num in nums:
        if num % 2 == 0:
            output.append(num)
    return output

# Using filter with lambda
evens = list(filter(lambda num: num % 2 == 0, numbers))
print(evens)  # [2, 4]

# Filter with user-defined function
def is_even(num):
    return num % 2 == 0

evens = list(filter(is_even, numbers))

# Real-world example
books = [
    {'title': 'Python Programming', 'rating': 4.5, 'available': True},
    {'title': 'Web Development', 'rating': 3.8, 'available': False},
    {'title': 'Data Science', 'rating': 4.9, 'available': True}
]

# Find available books with rating >= 4.0
quality_books = list(filter(lambda book: book['available'] and book['rating'] >= 4.0, books))

# Filter valid transactions
transactions = [
    {'amount': 100, 'valid': True},
    {'amount': -50, 'valid': False},
    {'amount': 75, 'valid': True}
]
valid_trans = list(filter(lambda t: t['valid'], transactions))
```


### List Comprehensions

```python
# Syntax: [expression for item in list if condition]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Double all numbers
doubled = [num * 2 for num in numbers]

# Get only evens
evens = [num for num in numbers if num % 2 == 0]

# Double only evens (combining map + filter)
doubled_evens = [num * 2 for num in numbers if num % 2 == 0]

# Real-world data processing
employees = [
    {'name': 'Alice', 'job': 'Developer', 'salary': 75000},
    {'name': 'Bob', 'job': 'Designer', 'salary': 65000},
    {'name': 'Charlie', 'job': 'Developer', 'salary': 80000}
]

# High-earning developers
high_devs = [emp['name'] for emp in employees 
             if emp['job'] == 'Developer' and emp['salary'] > 70000]
# ['Alice', 'Charlie']

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Efficiency comparison:
# List Comprehensions (fastest)
# User Defined Functions (good for complex logic)
# Map and Filter (good for functional programming style)
```


## Object-Oriented Programming

### Class Basics

```python
class Student:
    # Constructor
    def __init__(self, name, age, grades):
        self.name = name      # Instance attribute
        self.age = age
        self.grades = grades
    
    # Instance method
    def info(self):
        print(f"My name is {self.name} and I am {self.age}")
    
    def grade_avg(self):
        '''Returns the average of a student's grades'''
        return sum(self.grades) / len(self.grades)
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def remove_last_grade(self):
        if self.grades:
            self.grades.pop()
    
    def clear_grades(self):
        self.grades.clear()

# Creating objects
allan = Student("Allan", 99, [45, 90])
allan.info()
print(allan.grade_avg())
allan.add_grade(85)
```


### Encapsulation

```python
class User:
    def __init__(self, username, email, password):
        # Public attribute
        self.username = username
        # Protected attributes (convention with _)
        self._email = email
        self._password = password
    
    # Getter methods
    def get_email(self):
        return self._email
    
    def get_password(self):
        return self._password
    
    # Setter methods with validation
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email
            return "Email updated"
        else:
            return "Invalid email"
    
    def set_password(self, new_password):
        if len(new_password) >= 8 and "!" in new_password:
            self._password = new_password
            return "Password changed"
        else:
            return "Invalid password - must be 8+ chars with !"

# Usage
user = User("alice", "alice@email.com", "pass!123")
print(user.get_email())
user.set_email("newemail@test.com")
```


### Inheritance \& Polymorphism

```python
# Parent Class
class Character:
    def __init__(self, name, health, attack_power=10):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name}")
    
    def display_stats(self):
        print(f"{self.name} - Health: {self.health}, Attack: {self.attack_power}")

# Child class (Inheritance)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)
    
    # Polymorphism - Override parent method
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} slashes with sword!")
    
    def special_attack(self, opponent):
        opponent.health -= self.attack_power * 2
        print(f"{self.name} uses POWER STRIKE!")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=30)
    
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} casts a spell!")

class EvilWizard(Character):
    def __init__(self):
        super().__init__("Evil Wizard", health=200, attack_power=25)
    
    def regenerate(self):
        self.health += 10
        print(f"{self.name} regenerates! Health: {self.health}")

# Usage - Abstraction (simple interface, complex implementation hidden)
warrior = Warrior("Conan")
mage = Mage("Gandalf")
boss = EvilWizard()

warrior.attack(mage)  # Different behavior for each class
warrior.special_attack(mage)
boss.regenerate()
```


### Class Variables \& Instance Variables

```python
class Car:
    # Class variable - shared by all instances
    wheels = 4
    
    def __init__(self, make, model, year, fuel=100):
        # Instance variables - unique to each object
        self.make = make
        self.model = model
        self.year = year
        self.fuel = fuel
    
    def start_engine(self):
        print(f"{self.make} {self.model} engine started!")
    
    def drive(self, miles):
        fuel_used = miles * 0.05
        if self.fuel >= fuel_used:
            self.fuel -= fuel_used
            print(f"Drove {miles} miles. Fuel remaining: {self.fuel:.2f}")
        else:
            print("Not enough fuel!")
    
    def refuel(self):
        self.fuel = 100
        print("Tank refilled!")

# Child class with inheritance
class Toyota(Car):
    def __init__(self, model, year, color, fuel=100):
        super().__init__("Toyota", model, year, fuel)
        self.color = color

# Usage
my_car = Toyota("Camry", 2020, "Blue")
my_car.start_engine()
my_car.drive(50)
```


## Advanced Data Structures

### Stacks (LIFO - Last In, First Out)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None  # Top of stack
        self.tail = None  # Bottom of stack
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    def push(self, item):
        '''Adding an item to the top of the stack (head)'''
        new_node = Node(item)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node  # Add to the head (top of the stack)
        
        self.size += 1
    
    def pop(self):
        '''Remove that last thing that was added to stack, and return it (head)'''
        if self.is_empty():
            return None
        
        item = self.head.data
        self.head = self.head.next
        
        # If stack becomes empty, reset tail
        if self.head is None:
            self.tail = None
        
        self.size -= 1
        return item
    
    def peek(self):
        '''View top item in the stack without removing it'''
        if self.is_empty():
            return None
        return self.head.data

# Using Python list as stack (simpler)
stack = []
stack.append(1)    # Push - O(1)
stack.append(2)
stack.append(3)
top = stack.pop()  # Pop - O(1)
peek = stack[-1]   # Peek - O(1)
```


### Queues (FIFO - First In, First Out)

```python
from collections import deque

# Using deque for efficient queue operations
queue = deque()

# Enqueue (add to end) - O(1)
queue.append("first")
queue.append("second")
queue.append("third")

print(f"Queue: {queue}")

# Dequeue (remove from front) - O(1)
front_item = queue.popleft()  # IMPORTANT: O(1) time
print(f"Dequeued: {front_item}")
print(f"Queue after: {queue}")

# Peek front
if queue:
    front = queue[^0]  # O(1)

# Note: Regular list pop(0) is O(n) - DON'T USE for queues
# Python builtin stack is just a python list
# append() adds to the end of the list (aka top of the stack) - O(1)
# pop() removes the last thing added from the list - O(1)
# list[-1] is equivalent to peek (Look at the last item) - O(1)

# Why can't lists behave like a queue?
# append() adds to the end of the list (aka end of the queue) - O(1)
# pop(0) removes the first item but happens slowly - O(n) BIG PROBLEM
# list[^0] is equivalent to peek (Looking at the first item) - O(1)

# Always use deque for queue operations!
```


## Linked Lists

### Node \& LinkedList Implementation

```python
class Node:
    def __init__(self, data):
        # data is the information we want to store in the node
        self.data = data
        # next is a pointer (or reference) to the next node in the list
        # Initially it's None because when we create a node it doesn't point to anything
        self.next = None

class LinkedList:
    def __init__(self):
        # head is the first node in the list
        # If the list is empty, head will be none
        self.head = None
        
        # tail is the last node in the list
        # If the list is empty, tail will be none
        # tail is used to make adding new nodes faster
        self.tail = None
    
    # Check if the linked list is empty
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        '''Add node to end - O(1) with tail'''
        # Step 1: Create a new node with the data
        new_node = Node(data)
        
        # Step 2: If the list is empty, the new node becomes both head and tail
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        
        # Step 3: If the list already has nodes
        # Link the current tail to the new node
        self.tail.next = new_node
        
        # Step 4: Move the tail pointer to point to the new node (the new end of the list)
        self.tail = new_node
    
    def traverse(self):
        '''Visit all nodes - O(n)'''
        # CASE 1: If the list is empty, let the user know
        if self.is_empty():
            print("List is empty")
            return
        
        # CASE 2: Start from the head and keep following the 'next' until there's no more nodes
        # Step 1: Create a 'current' marker pointing to the same node as the head
        current = self.head
        
        # Step 2: Display data of that node and move to the next node
        while current:
            print(current.data)
            current = current.next
    
    def insert_at_position(self, position, data):
        '''Insert at specific position - O(n)'''
        # Create the node with the data
        new_node = Node(data)
        
        # Case 1: Insert at the very beginning of the list (before the head)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            
            # If the list was empty, update the tail too
            if self.tail is None:
                self.tail = new_node
            return
        
        # Case 2: Insert somewhere else in the list
        current = self.head
        counter = 1
        
        # Move to the current just before the desired position
        while counter < position - 1 and current:
            current = current.next
            counter += 1
        
        # Insert the new node into the chain
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_position(self, position):
        '''Delete at specific position - O(n)'''
        # Case 1: If list is empty
        if self.is_empty():
            print("List is empty")
            return
        
        # Case 2: Deleting the head (first node)
        if position == 1:
            self.head = self.head.next
            
            # If the list becomes empty, reset the tail as well
            if self.head is None:
                self.tail = None
            return
        
        # Case 3: Deleting at any other position
        current = self.head
        counter = 1
        
        # Move to the node just before the one we want to delete
        while counter < position - 1 and current:
            current = current.next
            counter += 1
        
        if current and current.next:
            node_to_delete = current.next
            # Skip over the deleted node
            current.next = node_to_delete.next
            
            # If deleting the last node, update the tail
            if current.next is None:
                self.tail = current
    
    def get_at_position(self, position):
        """Get node at position - O(n)"""
        current = self.head
        counter = 1
        while counter < position and current:
            current = current.next
            counter += 1
        # If position is out of range
        return current.data if current else None

# Create a new linked list
songs = LinkedList()

# Append items
songs.append("Song 1")
songs.append("Song 2")
songs.append("Song 3")

# Print list contents
songs.traverse()
```


### Real-World Example: Music Playlist

```python
from linked_list import Node, LinkedList

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class MusicPlaylist:
    def __init__(self, name):
        self.name = name
        self.songs = LinkedList()
        self.current_position = -1
    
    def add_song(self, title, artist, duration):
        song = Song(title, artist, duration)
        self.songs.append(song)
    
    def display(self):
        '''Show all the songs and artists in my playlist'''
        print(f"============= {self.name} =============")
        current = self.songs.head
        counter = 1
        while current:
            print(f"{counter}.) {current.data.title} - {current.data.artist}")
            current = current.next
            counter += 1
    
    def play_song_at_position(self, position):
        song = self.songs.get_at_position(position)
        self.current_position = position
        if song:
            print(f"Now playing: {song.title} by {song.artist}")
        else:
            print("Song not found")
    
    def next_song(self):
        if self.current_position != -1:
            self.current_position += 1
            self.play_song_at_position(self.current_position)
    
    def previous_song(self):
        if self.current_position > 1:
            self.current_position -= 1
            self.play_song_at_position(self.current_position)
    
    def remove_current_song(self):
        if self.current_position != -1:
            self.songs.delete_at_position(self.current_position)
            self.display()

# Usage
playlist = MusicPlaylist("My Favorites")
playlist.add_song("Bohemian Rhapsody", "Queen", "5:55")
playlist.add_song("Stairway to Heaven", "Led Zeppelin", "8:02")
playlist.display()
playlist.play_song_at_position(1)
playlist.next_song()
```


## Time Complexity (Big O)

### Common Time Complexities

```python
# O(1) - Constant (most efficient)
x = 10
y = x + 1
dict_value = my_dict["key"]
mylist[^5]  # Access by index

# O(log n) - Logarithmic
# Binary search - faster than linear search

# O(n) - Linear
for item in alist:
    print(item)

# For every piece of input there is a corresponding operation

# O(n log n) - Linear Logarithmic
sorted_list = sorted(mylist)
mylist.sort()
# Try to avoid sorting if at all possible

# O(n²) - Quadratic (stem from nested linear operations)
# O(n) inside O(n)
for num1 in nums:
    for num2 in nums:
        if num1 + num2 == target:
            return (num1, num2)

# Even though I have two stacked O(n) operations
# The overall time complexity is still O(n)
# Because we don't multiply different operations
```


### Data Structure Operations

```python
# Lists
mylist[i]           # O(1) - access by index
mylist.append(x)    # O(1) - add to end
mylist.insert(i, x) # O(n) - insert at position
mylist.pop()        # O(1) - remove last
mylist.pop(i)       # O(n) - remove by index
x in mylist         # O(n) - membership check
mylist.count(x)     # O(n) - count occurrences
mylist.index(x)     # O(n) - find index

# Dictionaries (Hash Tables)
mydict[key]         # O(1) - access
mydict[key] = val   # O(1) - add/modify
del mydict[key]     # O(1) - remove
key in mydict       # O(1) - membership check
mydict.get(key)     # O(1) - safe access

# Sets
myset.add(x)        # O(1) - add element
x in myset          # O(1) - membership check
myset.remove(x)     # O(1) - remove element
```


## Error Handling

### Try-Except Blocks

```python
# Basic try-except
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a valid number")

print("Program continues...")

# Multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Try-except-else
try:
    age = int(input("Age: "))
except ValueError:
    return None
else:
    return f"User age: {age}"

# Exception with variable
try:
    print(mylist[^6])
except IndexError as e:
    print(f"Error: {e}")
```


## Built-in Functions

### Commonly Used

```python
# Numeric
sum(numbers)           # Sum of list
max(numbers)           # Maximum value
min(numbers)           # Minimum value
abs(-5)                # Absolute value
round(56.789, 2)       # Round to 2 decimals

# Length
len(mylist)            # Length of list/string/dict

# Range
range(5)               # 0, 1, 2, 3, 4
range(1, 6)            # 1, 2, 3, 4, 5
range(0, 10, 2)        # 0, 2, 4, 6, 8

# Type conversion
int("42")              # String to int
float("3.14")          # String to float
str(123)               # Number to string
list(range(5))         # Range to list

# Sorting
sorted(mylist)         # Return sorted copy (out-of-place)
mylist.sort()          # Sort in-place

# Type checking
isinstance(value, int)
type(variable)
```


***

## COMPREHENSIVE PRACTICE CHALLENGES

### Challenge 1: Weather API Data Analyzer

**Difficulty: Beginner-Intermediate**

```python
"""
Build a weather data fetcher and analyzer using the OpenWeatherMap API:

Requirements:
1. Create get_weather(city) function that fetches data from API
2. Parse JSON response and extract: temperature, humidity, description
3. Handle HTTP errors (404 for invalid city, 401 for bad API key)
4. Store weather data in a dictionary with city as key
5. calculate_average_temp(cities_list) - fetch multiple cities, return average
6. find_hottest_city(cities_list) - return city with highest temp
7. Use query parameters to specify units (metric/imperial)
8. Add headers for API key authentication

Bonus:
- Cache API responses using a dictionary (don't refetch same city)
- Use regex to validate city names (letters and spaces only)
- Create a Weather class with get_forecast() method
- Handle 429 (too many requests) with retry logic

Concepts: APIs, JSON, dictionaries, error handling, functions, classes
"""
```

**Concepts tested:** API integration, HTTP requests, JSON parsing, error handling, dictionaries, functions

### Challenge 2: Data Cleaning with Regex \& APIs

**Difficulty: Intermediate**

```python
"""
Build a user registration system that validates and cleans data:

Create UserValidator class:
1. validate_email(email) - use regex pattern
2. validate_phone(phone) - accepts formats: 555-1234, (555) 123-4567
3. validate_password(password) - min 8 chars, 1 uppercase, 1 number, 1 special
4. clean_username(username) - remove extra spaces, special chars
5. normalize_data(user_dict) - cleans all fields at once

Create UserAPI class:
1. register_user(user_data) - POST request to fake API
2. get_user(user_id) - GET request
3. update_user(user_id, data) - PUT request
4. delete_user(user_id) - DELETE request

Integration:
- Validate all data before sending to API
- Use regex to clean phone numbers to standard format
- Use re.sub() to remove HTML tags from user input
- Log all failed validations to a dictionary

Test data:
dirty_users = [
    {'email': 'bad_email', 'phone': '5551234', 'password': 'weak'},
    {'email': 'good@test.com', 'phone': '(555) 123-4567', 'password': 'Strong123!'}
]
"""
```

**Concepts tested:** Regex patterns, validation, APIs, OOP, error handling, data cleaning

### Challenge 3: E-commerce Product Manager (Functional + OOP + APIs)

**Difficulty: Advanced**

```python
"""
Build complete e-commerce system combining multiple concepts:

Product class:
- Attributes: id, name, category, price, stock, supplier_id
- Methods: restock(), sell(), apply_discount()
- Validation: price > 0, stock >= 0

Inventory class:
- products = {} (dictionary storage)
- filter_products(**criteria) - use lambda/filter
- sort_products(by="price", descending=False) - lambda/sorted
- low_stock_alert(threshold=10) - list comprehension
- total_value() - map + sum
- category_report() - dictionary comprehension

ProductAPI class:
- fetch_products() - GET from API
- create_product(data) - POST to API
- update_stock(product_id, quantity) - PUT
- delete_product(product_id) - DELETE
- search_products(query) - GET with query parameters

Tasks:
1. Fetch products from JSONPlaceholder or fake API
2. Use map() to apply 7% tax to all prices
3. Use filter() to find products with stock < threshold
4. Use regex to validate product names (alphanumeric + spaces)
5. Sort products by multiple criteria using lambda
6. Generate sales report with total revenue

Advanced features:
- Cache API responses for 5 minutes
- Implement retry logic for failed API calls
- Use functional programming to process bulk operations
- Create decorator for logging all API calls
"""
```

**Concepts tested:** OOP, APIs, functional programming, lambda, map, filter, dictionaries, regex, error handling

### Challenge 4: Music Streaming Service (Complete System)

**Difficulty: Expert**

```python
"""
Build a complete music streaming service combining all concepts:

Base classes:
- MediaItem(title, artist, duration, plays_count)
- Playlist(name, owner) using LinkedList

Child classes:
- Song(MediaItem) + album, genre
- Podcast(MediaItem) + episode_number
- Implement polymorphism for play() method

User class:
- playlists (Stack for recently viewed)
- listening_history (Queue with deque)
- play(media) - increments play_count
- get_recommendations() - based on history

StreamingAPI class:
- fetch_songs(genre) - GET with query params
- create_playlist(user_id, data) - POST
- add_to_playlist(playlist_id, song_id) - PUT
- get_trending() - GET top songs
- search(query, filters) - GET with multiple params

Analytics:
- Use map() to extract all genres from library
- Use filter() to find songs with plays > 1000
- Use regex to parse duration strings ("3:45" to seconds)
- List comprehension for fast queries
- Lambda for custom sorting

Features:
1. Fetch songs from MusicBrainz API or iTunes API
2. Parse JSON and create Song objects
3. Implement shuffle() using random + linked list
4. Queue system for up-next songs
5. Stack for navigation history
6. Regex to validate song titles (remove special chars)
7. API integration with error handling
8. Functional programming for data transformations

Data structures:
- LinkedList for playlists (insert, delete, traverse)
- Stack for recently played
- Queue for play queue
- Dictionary for O(1) user/media lookup
- Set for tracking unique genres

Time complexity requirements:
- add to playlist: O(1)
- play next song: O(1)
- search by title: O(n)
- get user stats: O(1)
"""
```

**Concepts tested:** Complete integration - APIs, OOP (inheritance/polymorphism), linked lists, stacks, queues, functional programming, regex, dictionaries, error handling, JSON parsing

### Challenge 5: Social Media CLI App (Comprehensive)

**Difficulty: Expert**

```python
"""
Create a complete social media application:

User class (Encapsulation):
- _username, _email, _password (protected)
- friends (list), posts (list)
- Getters/setters with validation (regex for email)
- add_friend(), create_post(), display_posts()

Post class:
- content, timestamp, likes (int), comments (list)
- like(), add_comment(), edit() methods

SocialMediaAPI:
- register(user_data) - POST
- login(credentials) - POST, returns token
- get_posts(user_id, limit) - GET with query params
- create_post(token, content) - POST with auth headers
- like_post(post_id) - PUT
- add_comment(post_id, text) - POST
- get_friends(user_id) - GET
- send_friend_request(user_id) - POST

Features:
1. Regex validation for:
   - Email: pattern with @ and domain
   - Username: alphanumeric, 3-20 chars
   - Password: min 8 chars, uppercase, number, special char
   
2. API integration:
   - Use requests library
   - Handle authentication tokens in headers
   - Query parameters for filtering/pagination
   - Error handling for all status codes
   
3. Functional programming:
   - Use map() to process multiple posts
   - Use filter() to find posts by hashtag
   - Lambda for sorting by likes/timestamp
   - List comprehension for fast queries

4. Data structures:
   - Dictionary for user cache (O(1) lookup)
   - Set for unique hashtags
   - Stack for navigation history
   - Queue for notifications

5. Advanced features:
   - Search posts using regex patterns
   - Extract hashtags from content with regex
   - Clean user input (remove extra spaces, HTML tags)
   - Implement pagination for API requests
   - Cache API responses to reduce calls

CLI Menu:
1. Register/Login
2. Create Post
3. View Feed
4. Add Friend
5. Search Users (regex)
6. View Profile
7. Logout
"""
```

**Concepts tested:** Complete Python mastery - OOP (all 4 pillars), APIs, regex, functional programming, data structures, error handling, validation, JSON, authentication

***

## Quick Reference Tips

**Naming Conventions:**

- Variables/functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Protected attributes: `_leading_underscore`

**Common Patterns:**

```python
# Swap variables
a, b = b, a

# Multiple assignment
x = y = z = 0

# Conditional expression (ternary)
result = "even" if x % 2 == 0 else "odd"

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in numbers if x % 2 == 0]

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}

# Combining map + filter (functional approach)
result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))

# Equivalent list comprehension (more Pythonic)
result = [x * 2 for x in numbers if x % 2 == 0]
```

**Time Complexity Quick Reference:**

- List access: O(1)
- List append: O(1)
- List insert: O(n)
- Dict access: O(1)
- Dict add/remove: O(1)
- Set membership: O(1)
- List membership: O(n)
- Sorting: O(n log n)

**API Best Practices:**

- Always use virtual environments
- Handle all HTTP status codes
- Use query parameters for filtering
- Store credentials securely (never hardcode)
- Implement retry logic for failed requests
- Cache responses when appropriate
- Validate all data before sending

