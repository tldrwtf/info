# Object-Oriented Programming (OOP) - Complete Reference Guide

## Table of Contents
- [Classes & Objects](#classes--objects)
- [Attributes & Methods](#attributes--methods)
- [Constructors & Initialization](#constructors--initialization)
- [Inheritance](#inheritance)
- [Polymorphism](#polymorphism)
- [Abstraction](#abstraction)
- [Encapsulation](#encapsulation)
- [Special Methods](#special-methods)

---

## Classes & Objects

### Basic Class Definition
```python
# Define a class
class Dog:
    pass

# Create an object (instance)
my_dog = Dog()
```

### Class with Attributes
```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

# Create instances
buddy = Dog("Buddy", 3)
charlie = Dog("Charlie", 5)

# Access attributes
print(buddy.name)      # "Buddy"
print(buddy.species)   # "Canis familiaris"
print(charlie.age)     # 5
```

### What is `self`?
```python
# self refers to the instance itself
class Person:
    def __init__(self, name):
        self.name = name  # self.name is instance attribute

    def greet(self):
        # self allows access to instance attributes
        return f"Hello, my name is {self.name}"

Wilson = Person("Wilson")
Wilson.greet()  # "Hello, my name is Wilson"
# Python automatically passes Wilson as self
```

---

## Attributes & Methods

### Instance Attributes
```python
class Person:
    def __init__(self, name, age):
        self.name = name    # Instance attribute
        self.age = age      # Instance attribute

Wilson = Person("Wilson", 30)
bob = Person("Bob", 25)

Wilson.name  # "Wilson"
bob.name    # "Bob" - different value
```

### Class Attributes
```python
class Employee:
    # Class attribute - shared by all instances
    company = "TechCorp"
    num_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.num_employees += 1  # Access class attribute

emp1 = Employee("Wilson")
emp2 = Employee("Bob")

print(Employee.num_employees)  # 2
print(emp1.company)            # "TechCorp"
print(emp2.company)            # "TechCorp" - same value
```

### Instance Methods
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Instance method - operates on instance
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return f"{self.owner}'s balance: ${self.balance}"

account = BankAccount("Wilson", 100)
account.deposit(50)        # 150
account.withdraw(30)       # 120
account.get_balance()      # "Wilson's balance: $120"
```

### Class Methods
```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    # Class method - operates on class, not instance
    @classmethod
    def get_population(cls):
        return f"Total population: {cls.population}"

    # Alternative constructor using class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)

Wilson = Person("Wilson")
bob = Person("Bob")

Person.get_population()  # "Total population: 2"
```

### Static Methods
```python
class MathOperations:
    # Static method - doesn't access instance or class
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Call without creating instance
result = MathOperations.add(5, 3)      # 8
result = MathOperations.multiply(4, 2) # 8
```

---

## Constructors & Initialization

### The `__init__` Method
```python
class User:
    def __init__(self, username, email):
        """Constructor - called when creating new instance"""
        self.username = username
        self.email = email
        self.active = True  # Default value
        print(f"User {username} created")

user = User("Wilson", "Wilson@email.com")
# Output: User Wilson created
```

### Default Values
```python
class Product:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

laptop = Product("Laptop", 999.99)       # quantity defaults to 0
mouse = Product("Mouse", 29.99, 100)     # quantity is 100
```

### Validation in Constructor
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.balance = balance

# Valid
account = BankAccount("Wilson", 100)

# Raises ValueError
# account = BankAccount("Bob", -50)
```

---

## Inheritance

### Basic Inheritance
```python
# Parent class (Base class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

# Child class (Derived class)
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.name         # "Buddy" (inherited from Animal)
dog.speak()      # "Woof!" (overridden in Dog)
cat.speak()      # "Meow!" (overridden in Cat)
```

### Extending Parent Constructor
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "Canine")
        # Add child-specific attributes
        self.breed = breed

    def info(self):
        return f"{self.name} is a {self.breed} ({self.species})"

dog = Dog("Buddy", "Golden Retriever")
dog.info()  # "Buddy is a Golden Retriever (Canine)"
```

### Multiple Inheritance
```python
class Flyer:
    def fly(self):
        return "Flying..."

class Swimmer:
    def swim(self):
        return "Swimming..."

# Inherit from multiple classes
class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

duck = Duck()
duck.fly()    # "Flying..." (from Flyer)
duck.swim()   # "Swimming..." (from Swimmer)
duck.quack()  # "Quack!" (from Duck)
```

### Method Resolution Order (MRO)
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
d.method()  # "B" (follows MRO: D -> B -> C -> A)

# View MRO
D.__mro__  # Shows the order: D, B, C, A, object
```

---

## Polymorphism

### Method Overriding
```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Polymorphism - same method name, different behavior
shapes = [Rectangle(5, 4), Circle(3), Rectangle(2, 6)]

for shape in shapes:
    print(shape.area())  # Calls appropriate area() method
```

### Duck Typing
```python
# "If it walks like a duck and quacks like a duck, it's a duck"

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

# Function doesn't care about type, only that object has speak()
def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()
duck = Duck()

animal_sound(dog)   # "Woof!"
animal_sound(cat)   # "Meow!"
animal_sound(duck)  # "Quack!"
```

### Operator Overloading
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Overload == operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2  # Uses __add__
print(p3)     # Point(4, 6) - Uses __str__

p1 == Point(1, 2)  # True - Uses __eq__
```

---

## Abstraction

### Abstract Base Classes
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class"""

    @abstractmethod
    def area(self):
        """Must be implemented by child classes"""
        pass

    @abstractmethod
    def perimeter(self):
        """Must be implemented by child classes"""
        pass

# Cannot instantiate abstract class
# shape = Shape()  # TypeError!

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Must implement all abstract methods
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 4)
rect.area()       # 20
rect.perimeter()  # 18
```

### Interface Pattern
```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Interface for payment processing"""

    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via credit card"

    def refund(self, amount):
        return f"Refunding ${amount} to credit card"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

    def refund(self, amount):
        return f"Refunding ${amount} to PayPal"

# Both implement same interface
def checkout(processor, amount):
    return processor.process_payment(amount)

cc = CreditCardProcessor()
pp = PayPalProcessor()

checkout(cc, 100)  # "Processing $100 via credit card"
checkout(pp, 100)  # "Processing $100 via PayPal"
```

---

## Encapsulation

### Public, Protected, and Private
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner              # Public
        self._account_id = "12345"      # Protected (convention)
        self.__balance = balance        # Private (name mangling)

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount("Wilson", 1000)

# Public - accessible
account.owner  # "Wilson"

# Protected - accessible but shouldn't use
account._account_id  # "12345" (but shouldn't access directly)

# Private - not directly accessible
# account.__balance  # AttributeError!
account.get_balance()  # 1000 (use public method)
```

### Property Decorators
```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter
    @property
    def age(self):
        return self._age

    # Setter
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    # Read-only property (no setter)
    @property
    def name(self):
        return self._name

person = Person("Wilson", 30)

# Use like regular attribute, but with validation
person.age = 31  # Uses setter
print(person.age)  # Uses getter: 31

# person.age = -5  # Raises ValueError
# person.name = "Bob"  # AttributeError (no setter)
```

### Getters and Setters (Classic Style)
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    def get_fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature(25)
temp.get_celsius()     # 25
temp.get_fahrenheit()  # 77.0
temp.set_celsius(30)
```

---

## Special Methods (Magic Methods)

### String Representation
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # For print() and str()
    def __str__(self):
        return f"{self.title} by {self.author}"

    # For developers/debugging
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

book = Book("1984", "George Orwell")

print(book)      # "1984 by George Orwell" (uses __str__)
str(book)        # "1984 by George Orwell"
repr(book)       # "Book('1984', 'George Orwell')"
```

### Comparison Operators
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        """== operator"""
        return self.age == other.age

    def __lt__(self, other):
        """< operator"""
        return self.age < other.age

    def __le__(self, other):
        """<= operator"""
        return self.age <= other.age

    def __gt__(self, other):
        """> operator"""
        return self.age > other.age

Wilson = Person("Wilson", 30)
bob = Person("Bob", 25)

Wilson == bob  # False
Wilson > bob   # True
Wilson < bob   # False
```

### Arithmetic Operators
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 1)

v3 = v1 + v2  # Vector(3, 4)
v4 = v1 - v2  # Vector(1, 2)
v5 = v1 * 2   # Vector(4, 6)
```

### Container Methods
```python
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        """len() function"""
        return len(self.songs)

    def __getitem__(self, index):
        """[] operator"""
        return self.songs[index]

    def __contains__(self, song):
        """'in' operator"""
        return song in self.songs

playlist = Playlist()
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")

len(playlist)              # 3
playlist[0]                # "Song A"
"Song B" in playlist       # True
"Song D" in playlist       # False

# Can iterate because of __getitem__
for song in playlist:
    print(song)
```

### Context Manager
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Called when entering 'with' block"""
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        if self.file:
            self.file.close()

# Use with 'with' statement
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")
# File automatically closed
```

---

## OOP Design Principles

### SOLID Principles Overview

```python
# S - Single Responsibility Principle
# A class should have one reason to change

# Bad
class User:
    def save_to_database(self):
        pass
    def send_email(self):
        pass

# Good - separate responsibilities
class User:
    pass

class UserRepository:
    def save(self, user):
        pass

class EmailService:
    def send(self, to, message):
        pass


# O - Open/Closed Principle
# Open for extension, closed for modification

class Discount:
    def calculate(self, price):
        return price

class StudentDiscount(Discount):
    def calculate(self, price):
        return price * 0.9  # 10% off

class SeniorDiscount(Discount):
    def calculate(self, price):
        return price * 0.85  # 15% off


# L - Liskov Substitution Principle
# Subtypes must be substitutable for base types

class Bird:
    def move(self):
        return "Flying"

class Penguin(Bird):
    def move(self):
        return "Swimming"  # Still valid movement


# I - Interface Segregation Principle
# Many specific interfaces better than one general

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass

class BasicPrinter(Printer):
    def print(self):
        pass

class MultifunctionDevice(Printer, Scanner):
    def print(self):
        pass
    def scan(self):
        pass


# D - Dependency Inversion Principle
# Depend on abstractions, not concretions

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print("Saving to MySQL")

class UserService:
    def __init__(self, database: Database):
        self.db = database  # Depends on abstraction

    def create_user(self, user_data):
        self.db.save(user_data)
```

---

## Quick Reference Card

| Concept | Syntax | Purpose |
|---------|--------|---------|
| Define class | `class MyClass:` | Create new class |
| Constructor | `def __init__(self):` | Initialize instance |
| Instance attribute | `self.attr = value` | Unique to instance |
| Class attribute | `MyClass.attr = value` | Shared by all |
| Instance method | `def method(self):` | Operate on instance |
| Class method | `@classmethod` | Operate on class |
| Static method | `@staticmethod` | Independent utility |
| Inheritance | `class Child(Parent):` | Extend parent class |
| Call parent | `super().__init__()` | Access parent |
| Property | `@property` | Getter method |
| Setter | `@attr.setter` | Setter method |
| String repr | `def __str__(self):` | String conversion |
| Equality | `def __eq__(self, other):` | == operator |

---

## See Also

- **[Python Basics Cheat Sheet](./Python_Basics_Cheat_Sheet.md)** - Python fundamentals
- **[Decorators Cheat Sheet](./Decorators_Cheat_Sheet.md)** - @property, @staticmethod, @classmethod decorators
- **[Error Handling Cheat Sheet](./Error_Handling_Cheat_Sheet.md)** - Custom exceptions and error handling
- **[Testing and Debugging Cheat Sheet](./Testing_and_Debugging_Cheat_Sheet.md)** - Testing OOP code

---
