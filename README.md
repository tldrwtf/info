# Python Learning - Complete Cheat Sheet Collection by [tldrwtf](https://github.com/tldrwtf)
If you found any of this information useful, leaving a star on this repository would be highly appreciated! 

---

## Available Cheat Sheets

### 1. [Python Basics](./Python_Basics_Cheat_Sheet.md)

**Foundation of Python programming**

- Variables & Data Types
- Control Flow (if/elif/else)
- Loops (for/while)
- Functions (def, parameters, return)
- Built-in Functions
- Best Practices

**Best for:** Complete beginners, quick syntax reference

---

### 2. [Data Structures](./Data_Structures_Cheat_Sheet.md)

**Working with Python's core data structures**

- Lists (arrays)
- Dictionaries (hash maps)
- Sets
- Tuples
- Linked Lists (custom implementation)
- Stacks & Queues

**Best for:** Understanding when to use each data structure, time complexity considerations

---

### 3. [Object-Oriented Programming](./OOP_Cheat_Sheet.md)

**Master OOP concepts and design patterns**

- Classes & Objects
- Attributes & Methods
- Constructors (`__init__`)
- Inheritance
- Polymorphism
- Abstraction & Abstract Classes
- Encapsulation (public, protected, private)
- Special/Magic Methods
- SOLID Principles

**Best for:** Building scalable applications, understanding design patterns

---

### 4. [Functional Programming](./Functional_Programming_Cheat_Sheet.md)

**Functional programming paradigms in Python**

- Lambda Functions
- Map, Filter, Reduce
- List Comprehensions
- Dictionary Comprehensions
- Set Comprehensions
- Generator Expressions
- Function Composition

**Best for:** Writing concise, readable code; data transformations

---

### 5. [APIs & HTTP Requests](./APIs_and_Requests_Cheat_Sheet.md)

**Making HTTP requests and consuming APIs**

- HTTP Methods (GET, POST, PUT, PATCH, DELETE)
- Requests Library
- Headers & Query Parameters
- Request/Response Handling
- Authentication (API Key, Bearer Token, OAuth 2.0)
- Error Handling
- Best Practices (sessions, retries, caching)

**Best for:** Working with web APIs, external data sources

---

### 6. [Regular Expressions (Regex)](./Regex_Cheat_Sheet.md)

**Pattern matching and text processing**

- Metacharacters (`\d`, `\w`, `\s`, `.`)
- Quantifiers (`+`, `*`, `?`, `{n,m}`)
- Character Sets (`[a-z]`, `[^0-9]`)
- Groups & Capturing
- Regex Methods (search, findall, sub, split)
- Practical Patterns (email, phone, URL)

**Best for:** Data validation, text parsing, find & replace

---

### 7. [SQL & SQLAlchemy](./SQL_and_SQLAlchemy_Cheat_Sheet.md)

**Database management and ORM**

- SQL Basics (SELECT, INSERT, UPDATE, DELETE)
- DDL (CREATE, ALTER, DROP)
- SQL Queries (JOIN, GROUP BY, ORDER BY)
- SQLAlchemy Setup & Models
- CRUD Operations
- Relationships (One-to-Many, Many-to-Many)
- Advanced Queries

**Best for:** Database operations, data persistence

---

### 8. [SQLAlchemy Relationships](./SQLAlchemy_Relationships_Guide.md)

**Advanced ORM relationship patterns**

- One-to-Many Relationships
- Many-to-One Relationships
- One-to-One Relationships
- Many-to-Many Relationships
- Association Objects
- Self-Referential Relationships
- Lazy Loading Strategies
- Cascade Operations

**Best for:** Complex database relationships, data modeling, advanced SQLAlchemy

---

### 9. [Flask REST API Development](./Flask_REST_API_Development_Guide.md)

**Building RESTful APIs with Flask**

- Flask Application Factory Pattern
- Blueprints & Route Organization
- Database Configuration
- SQLAlchemy Models
- Marshmallow Schemas
- CRUD Operations
- Error Handling
- Testing APIs

**Best for:** Building web APIs, full-stack development, microservices

---

### 10. [API Authentication](./API_Authentication_Guide.md)

**Securing APIs with various authentication methods**

- API Keys
- Bearer Tokens
- Basic Authentication
- OAuth 2.0 (Spotify, GitHub examples)
- JWT (JSON Web Tokens)
- Session-Based Authentication
- Security Best Practices

**Best for:** API security, user authentication, OAuth integrations

---

### 11. [Python CLI Applications](./Python_CLI_Applications_Guide.md)

**Building command-line interface applications**

- User Input & Validation
- Command-Line Arguments (argparse)
- Interactive Menus
- CLI with Database (ORM)
- Formatting Output (tabulate, rich, colorama)
- Error Handling
- Complete CLI Examples

**Best for:** CLI tools, automation scripts, interactive applications

---

### 12. [Big O Notation & Time Complexity](./Big_O_Notation_Cheat_Sheet.md)

**Algorithm analysis and optimization**

- What is Big O?
- Common Complexities (O(1), O(log n), O(n), O(n²), etc.)
- Analyzing Algorithms
- Space Complexity
- Data Structure Complexities
- Sorting Algorithm Comparisons
- Optimization Tips

**Best for:** Technical interviews, algorithm optimization

---

### 13. [File Operations](./File_Operations_Cheat_Sheet.md)

**Reading, writing, and managing files**

- File Modes (read, write, append, binary)
- Reading Files (line by line, chunks)
- Writing Files (text, binary)
- CSV Operations (csv module, DictReader/Writer)
- JSON Operations (json.dump, json.load)
- Path Operations (pathlib module)
- File System Operations (os module)
- Best Practices (context managers, encoding)

**Best for:** File I/O, data processing, working with CSV/JSON

---

### 14. [Error Handling & Exceptions](./Error_Handling_Cheat_Sheet.md)

**Exception handling and debugging techniques**

- Try/Except/Else/Finally
- Common Built-in Exceptions
- Raising Exceptions
- Custom Exceptions
- Exception Chaining
- Context Managers (with statement)
- Error Handling Best Practices

**Best for:** Writing robust code, handling errors gracefully

---

### 15. [Decorators](./Decorators_Cheat_Sheet.md)

**Function and class decorators**

- Function Decorators
- Decorators with Arguments
- Class Decorators
- Built-in Decorators (@property, @staticmethod, @classmethod)
- functools Decorators (@wraps, @lru_cache, @singledispatch)
- Practical Examples (timer, debug, rate limiter)
- Best Practices

**Best for:** Code reusability, aspect-oriented programming, metaprogramming

---

### 16. [Iterators & Generators](./Iterators_and_Generators_Cheat_Sheet.md)

**Efficient iteration and lazy evaluation**

- Iterator Protocol (__iter__, __next__)
- Creating Custom Iterators
- Generator Functions (yield keyword)
- Generator Expressions
- Yield From (delegation)
- itertools Module
- Practical Examples (large files, pipelines)
- Best Practices

**Best for:** Memory-efficient data processing, working with large datasets

---

### 17. [Testing & Debugging](./Testing_and_Debugging_Cheat_Sheet.md)

**Writing tests and debugging code**

- unittest Module
- pytest Framework
- Assertions and Test Structure
- Mocking and Patching
- Test Fixtures
- Test Coverage
- Debugging with pdb
- Debugging Techniques

**Best for:** Test-driven development, ensuring code quality

---

### 18. [Standard Library Essentials](./Standard_Library_Essentials_Cheat_Sheet.md)

**Essential Python standard library modules**

- collections (Counter, defaultdict, deque, namedtuple)
- datetime (date, time, timedelta)
- os and sys Modules
- json Module
- math and random Modules
- argparse (command-line arguments)
- Other Useful Modules (string, copy, time)

**Best for:** Using built-in tools, avoiding external dependencies

---

### 19. [Linked Lists and Custom Data Structures](./Linked_Lists_and_Custom_Data_Structures_Guide.md)

**Building data structures from scratch**

- Node Implementation
- LinkedList Class with Operations
- Stack Implementation (LIFO)
- Queue Implementation (FIFO)
- Time Complexity Analysis
- Practical Applications (music playlists, browser history)
- Optimization Techniques
- When to Use Each Structure

**Best for:** Understanding data structures, technical interviews, custom implementations

---

### 20. [OAuth2 and Token Management](./OAuth2_and_Token_Management_Guide.md)

**Implementing OAuth2 authentication flows**

- Client Credentials Flow
- Base64 Encoding for Credentials
- Token Acquisition and Storage
- Bearer Token Usage
- Token Lifecycle Management
- Error Handling
- Security Best Practices
- Complete Implementation Examples

**Best for:** API authentication, third-party integrations, secure token management

---

### 21. [SQLAlchemy Advanced Patterns](./SQLAlchemy_Advanced_Patterns_Guide.md)

**Advanced ORM patterns and production best practices**

- Session Management Patterns
- Query Optimization (avoiding N+1 queries)
- Complex Relationships
- Association Objects vs Association Tables
- Self-Referential Relationships
- Lazy Loading Strategies
- Cascade Operations
- Transaction Handling
- Production Patterns

**Best for:** Production applications, performance optimization, complex data models

---

### 22. [Flask Advanced Features](./Flask_Advanced_Features_Guide.md)

**Advanced Flask patterns for production applications**

- Rate Limiting with Flask-Limiter
- Caching with Flask-Caching
- Pagination Patterns
- Advanced Blueprint Architecture
- Request Validation with Marshmallow
- Error Handling Middleware
- Application Factory Pattern
- JWT Authentication
- CORS Configuration
- Production Best Practices

**Best for:** Production Flask applications, API optimization, scalable architecture

---

## Learning Paths

### Beginner Path

1. **Python Basics** - Start here for fundamentals
2. **Data Structures** - Learn core data structures
3. **File Operations** - Read and write files
4. **Error Handling** - Handle errors gracefully
5. **Functional Programming** - Write cleaner code
6. **Regex** - Text processing basics

### Intermediate Path

1. **OOP** - Object-oriented design
2. **Decorators** - Advanced function concepts
3. **Iterators & Generators** - Memory-efficient code
4. **APIs & Requests** - Work with external data
5. **SQL & SQLAlchemy** - Database operations
6. **Big O Notation** - Algorithm analysis

### Advanced Path

1. **Testing & Debugging** - Write robust, testable code
2. **Standard Library Essentials** - Master built-in modules
3. **Linked Lists and Custom Data Structures** - Build data structures from scratch
4. **SQLAlchemy Advanced Patterns** - Production ORM patterns
5. **OAuth2 and Token Management** - Advanced authentication
6. **Flask Advanced Features** - Production Flask patterns

### Full Stack Web Development Path

1. **Python Basics** - Foundation
2. **OOP** - Object-oriented programming
3. **SQL & SQLAlchemy** - Database basics
4. **SQLAlchemy Relationships** - Advanced relationships
5. **SQLAlchemy Advanced Patterns** - Production patterns and optimization
6. **Flask REST API Development** - Build APIs
7. **Flask Advanced Features** - Rate limiting, caching, pagination
8. **API Authentication** - Secure APIs
9. **OAuth2 and Token Management** - OAuth2 flows and token lifecycle
10. **APIs & Requests** - Consume APIs
11. **Testing & Debugging** - Test your applications

### CLI Development Path

1. **Python Basics** - Foundation
2. **Data Structures** - Core structures
3. **Linked Lists and Custom Data Structures** - Custom implementations
4. **File Operations** - File I/O
5. **SQL & SQLAlchemy** - Database operations
6. **SQLAlchemy Advanced Patterns** - Session management and optimization
7. **Python CLI Applications** - Build interactive CLIs
8. **Error Handling** - Robust error handling
9. **Testing & Debugging** - Test your tools

### Data Structures & Algorithms Path

1. **Python Basics** - Foundation
2. **Data Structures** - Built-in structures
3. **Linked Lists and Custom Data Structures** - Custom implementations
4. **Big O Notation** - Time and space complexity
5. **Functional Programming** - Efficient data transformations
6. **Iterators & Generators** - Memory-efficient patterns

---

## Quick Reference

### Find by Topic

**Working with Data:**

- Lists/Arrays → Data Structures
- Linked Lists → Linked Lists and Custom Data Structures
- Stacks & Queues → Linked Lists and Custom Data Structures
- Dictionaries/Hash Maps → Data Structures, Standard Library Essentials
- Database Operations → SQL & SQLAlchemy, SQLAlchemy Relationships, SQLAlchemy Advanced Patterns
- API Calls → APIs & Requests, API Authentication, OAuth2 and Token Management
- File I/O → File Operations
- CSV/JSON → File Operations
- Data Processing → Iterators & Generators

**Code Organization:**

- Functions → Python Basics, Decorators
- Classes → OOP
- Design Patterns → OOP
- Code Reuse → Decorators
- Error Handling → Error Handling & Exceptions

**Development Tools:**

- Testing → Testing & Debugging
- Debugging → Testing & Debugging
- Mocking → Testing & Debugging
- Standard Library → Standard Library Essentials
- CLI Tools → Python CLI Applications

**Text Processing:**

- String Manipulation → Python Basics
- Pattern Matching → Regex
- Validation → Regex
- File Reading → File Operations

**Performance:**

- Algorithm Analysis → Big O Notation
- Optimization → Big O Notation, Functional Programming, Iterators & Generators, SQLAlchemy Advanced Patterns
- Memory Efficiency → Iterators & Generators, Linked Lists and Custom Data Structures
- Caching → Decorators, Flask Advanced Features
- Query Optimization → SQLAlchemy Advanced Patterns
- Rate Limiting → Flask Advanced Features

**Python Features:**

- Decorators → Decorators
- Generators → Iterators & Generators
- Context Managers → Error Handling & Exceptions, File Operations
- Exceptions → Error Handling & Exceptions

**Web Development:**

- REST APIs → Flask REST API Development, APIs & Requests
- Authentication → API Authentication, OAuth2 and Token Management
- OAuth2 → OAuth2 and Token Management
- JWT Tokens → OAuth2 and Token Management, Flask Advanced Features
- Database Models → SQL & SQLAlchemy, SQLAlchemy Relationships
- API Security → API Authentication, OAuth2 and Token Management
- Flask Blueprints → Flask REST API Development, Flask Advanced Features
- Rate Limiting → Flask Advanced Features
- Caching → Flask Advanced Features
- Pagination → Flask Advanced Features

**Application Development:**

- CLI Applications → Python CLI Applications
- Command-Line Arguments → Python CLI Applications, Standard Library Essentials
- Interactive Menus → Python CLI Applications
- User Input Validation → Python CLI Applications, Regex

**Database & ORM:**

- Basic CRUD → SQL & SQLAlchemy
- Relationships → SQLAlchemy Relationships
- One-to-Many → SQLAlchemy Relationships
- Many-to-Many → SQLAlchemy Relationships
- Association Tables → SQLAlchemy Relationships, SQLAlchemy Advanced Patterns
- Lazy Loading → SQLAlchemy Relationships, SQLAlchemy Advanced Patterns
- Session Management → SQLAlchemy Advanced Patterns
- Query Optimization → SQLAlchemy Advanced Patterns
- Transactions → SQLAlchemy Advanced Patterns
- Cascade Operations → SQLAlchemy Advanced Patterns

**Data Structures:**

- Node Implementation → Linked Lists and Custom Data Structures
- LinkedList → Linked Lists and Custom Data Structures
- Stack (LIFO) → Linked Lists and Custom Data Structures
- Queue (FIFO) → Linked Lists and Custom Data Structures
- Time Complexity → Big O Notation, Linked Lists and Custom Data Structures
- Custom Implementations → Linked Lists and Custom Data Structures

---
