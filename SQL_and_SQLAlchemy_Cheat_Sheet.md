# SQL & SQLAlchemy ORM - Complete Reference Guide

## Table of Contents
- [SQL Basics](#sql-basics)
- [DDL - Data Definition](#ddl---data-definition)
- [DML - Data Manipulation](#dml---data-manipulation)
- [SQL Queries](#sql-queries)
- [SQLAlchemy Setup](#sqlalchemy-setup)
- [SQLAlchemy Models](#sqlalchemy-models)
- [SQLAlchemy CRUD](#sqlalchemy-crud)
- [Relationships](#relationships)
- [Advanced Queries](#advanced-queries)

---

## SQL Basics

### What is SQL?
```sql
-- SQL - Structured Query Language
-- Used to manage and query relational databases

-- CRUD Operations:
-- Create (INSERT)
-- Read (SELECT)
-- Update (UPDATE)
-- Delete (DELETE)
```

### Database Concepts
```sql
-- Database: Collection of tables
-- Table: Collection of rows (records)
-- Row: Single record with multiple columns
-- Column: Single field/attribute

-- Example:
-- Database: school
--   Table: students
--     Columns: id, name, age, grade
--     Row: (1, 'Wilson', 20, 'A')
```

---

## DDL - Data Definition

### Create Table
```sql
-- CREATE TABLE - Define new table structure

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER,
    grade TEXT,
    enrolled_date DATE DEFAULT CURRENT_DATE
);

-- With constraints
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    CHECK (age >= 18)
);
```

### Alter Table
```sql
-- ALTER TABLE - Modify existing table

-- Add column
ALTER TABLE students
ADD COLUMN phone TEXT;

-- Drop column
ALTER TABLE students
DROP COLUMN phone;

-- Rename column
ALTER TABLE students
RENAME COLUMN grade TO gpa;

-- Rename table
ALTER TABLE students
RENAME TO enrollments;
```

### Drop Table
```sql
-- DROP TABLE - Delete entire table

DROP TABLE students;

-- Drop if exists (safer)
DROP TABLE IF EXISTS students;
```

### Data Types
```sql
-- Common SQLite data types:

INTEGER  -- Whole numbers: 1, 42, -100
REAL     -- Decimal numbers: 3.14, 99.99
TEXT     -- Strings: 'Hello', 'Wilson@email.com'
BLOB     -- Binary data: images, files
BOOLEAN  -- True/False (stored as 0/1)
DATE     -- Dates: '2024-01-15'
DATETIME -- Date and time: '2024-01-15 14:30:00'
```

### Constraints
```sql
-- Constraints - Rules for data integrity

CREATE TABLE products (
    id INTEGER PRIMARY KEY,           -- Unique identifier
    name TEXT NOT NULL,               -- Cannot be NULL
    price REAL NOT NULL CHECK (price > 0),  -- Must be positive
    sku TEXT UNIQUE,                  -- Must be unique
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)  -- Must exist in categories
);
```

---

## DML - Data Manipulation

### INSERT - Add Data
```sql
-- Insert single row
INSERT INTO students (first_name, last_name, email, age)
VALUES ('Wilson', 'Johnson', 'Wilson@email.com', 20);

-- Insert multiple rows
INSERT INTO students (first_name, last_name, email, age)
VALUES
    ('Bob', 'Smith', 'bob@email.com', 22),
    ('Charlie', 'Brown', 'charlie@email.com', 21),
    ('Diana', 'Prince', 'diana@email.com', 23);

-- Insert with all columns
INSERT INTO students
VALUES (1, 'Eve', 'Wilson', 'eve@email.com', 19, 'A', '2024-01-15');
```

### SELECT - Retrieve Data
```sql
-- Select all columns
SELECT * FROM students;

-- Select specific columns
SELECT first_name, last_name, email FROM students;

-- Select with alias
SELECT first_name AS "First Name",
       last_name AS "Last Name"
FROM students;

-- Select distinct values
SELECT DISTINCT grade FROM students;

-- Select with calculation
SELECT first_name, age, age + 1 AS "Next Year Age"
FROM students;
```

### UPDATE - Modify Data
```sql
-- Update single row
UPDATE students
SET grade = 'A+'
WHERE id = 1;

-- Update multiple columns
UPDATE students
SET grade = 'B', age = 21
WHERE first_name = 'Wilson';

-- Update all rows (careful!)
UPDATE students
SET is_active = 1;

-- Update with calculation
UPDATE products
SET price = price * 1.1  -- 10% increase
WHERE category = 'Electronics';
```

### DELETE - Remove Data
```sql
-- Delete specific rows
DELETE FROM students
WHERE id = 1;

-- Delete with condition
DELETE FROM students
WHERE age < 18;

-- Delete all rows (careful!)
DELETE FROM students;

-- Better: use TRUNCATE (if supported)
TRUNCATE TABLE students;
```

---

## SQL Queries

### WHERE Clause
```sql
-- Filter results with conditions

-- Equal
SELECT * FROM students WHERE grade = 'A';

-- Not equal
SELECT * FROM students WHERE grade != 'F';

-- Comparison
SELECT * FROM students WHERE age >= 21;

-- Multiple conditions (AND)
SELECT * FROM students
WHERE grade = 'A' AND age >= 20;

-- Multiple conditions (OR)
SELECT * FROM students
WHERE grade = 'A' OR grade = 'B';

-- IN operator
SELECT * FROM students
WHERE grade IN ('A', 'B', 'C');

-- BETWEEN
SELECT * FROM students
WHERE age BETWEEN 18 AND 22;

-- LIKE (pattern matching)
SELECT * FROM students
WHERE email LIKE '%@gmail.com';

-- IS NULL
SELECT * FROM students
WHERE phone IS NULL;
```

### ORDER BY
```sql
-- Sort results

-- Ascending (default)
SELECT * FROM students
ORDER BY last_name;

-- Descending
SELECT * FROM students
ORDER BY age DESC;

-- Multiple columns
SELECT * FROM students
ORDER BY grade ASC, age DESC;
```

### LIMIT and OFFSET
```sql
-- Limit number of results
SELECT * FROM students
LIMIT 10;

-- Pagination
SELECT * FROM students
LIMIT 10 OFFSET 20;  -- Skip first 20, get next 10

-- Top 5 oldest students
SELECT * FROM students
ORDER BY age DESC
LIMIT 5;
```

### Aggregate Functions
```sql
-- COUNT - Count rows
SELECT COUNT(*) FROM students;
SELECT COUNT(*) FROM students WHERE grade = 'A';

-- SUM - Sum values
SELECT SUM(price) FROM products;

-- AVG - Average
SELECT AVG(age) FROM students;

-- MIN/MAX
SELECT MIN(age), MAX(age) FROM students;

-- Multiple aggregates
SELECT
    COUNT(*) as total_students,
    AVG(age) as average_age,
    MIN(age) as youngest,
    MAX(age) as oldest
FROM students;
```

### GROUP BY
```sql
-- Group and aggregate

-- Count students per grade
SELECT grade, COUNT(*) as student_count
FROM students
GROUP BY grade;

-- Average age per grade
SELECT grade, AVG(age) as avg_age
FROM students
GROUP BY grade;

-- HAVING - Filter groups (like WHERE for groups)
SELECT grade, COUNT(*) as count
FROM students
GROUP BY grade
HAVING COUNT(*) > 5;
```

### JOINs
```sql
-- INNER JOIN - Rows with matches in both tables
SELECT students.name, courses.course_name
FROM students
INNER JOIN enrollments ON students.id = enrollments.student_id
INNER JOIN courses ON enrollments.course_id = courses.id;

-- LEFT JOIN - All from left, matches from right
SELECT students.name, courses.course_name
FROM students
LEFT JOIN enrollments ON students.id = enrollments.student_id;

-- Self JOIN - Join table to itself
SELECT e1.name, e2.name as manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.id;
```

---

## SQLAlchemy Setup

### Installation
```bash
pip install sqlalchemy
```

### Basic Setup
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Create engine (connect to database)
engine = create_engine('sqlite:///my_database.db', echo=True)
# echo=True shows SQL queries in console

# Create base class for models
Base = declarative_base()

# Create session factory
Session = sessionmaker(bind=engine)
session = Session()
```

### Database Engines
```python
# SQLite (file-based)
engine = create_engine('sqlite:///database.db')

# SQLite (in-memory)
engine = create_engine('sqlite:///:memory:')

# PostgreSQL
engine = create_engine('postgresql://user:password@localhost/dbname')

# MySQL
engine = create_engine('mysql://user:password@localhost/dbname')
```

---

## SQLAlchemy Models

### Basic Model
```python
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  # Table name in database

    # Define columns
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(300), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(120), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
```

### Create Tables
```python
from sqlalchemy import create_engine

engine = create_engine('sqlite:///my_db.db')

# Create all tables defined in Base
Base.metadata.create_all(engine)
```

### Model with Validation
```python
from sqlalchemy import Column, Integer, String, event
from sqlalchemy.orm import validates

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(300))
    age: Mapped[int] = mapped_column(Integer)

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("Invalid email address")
        return email.lower()

    @validates('age')
    def validate_age(self, key, age):
        if age < 0 or age > 150:
            raise ValueError("Invalid age")
        return age
```

---

## SQLAlchemy CRUD

### Create (Insert)
```python
from models import User, session

# Create single user
new_user = User(
    username='Wilson',
    email='Wilson@example.com',
    password='hashed_password'
)

# Add to session
session.add(new_user)

# Commit to database
session.commit()

# Access ID after commit
print(new_user.id)  # Auto-generated ID

# Create multiple users
users = [
    User(username='bob', email='bob@example.com', password='pass123'),
    User(username='charlie', email='charlie@example.com', password='pass456')
]

session.add_all(users)
session.commit()
```

### Read (Query)
```python
from models import User, session

# Get all users
all_users = session.query(User).all()

# Get first user
first_user = session.query(User).first()

# Get by ID
user = session.get(User, 1)  # User with id=1

# Query with filter
Wilson = session.query(User).filter(User.username == 'Wilson').first()

# Multiple filters (AND)
user = session.query(User).filter(
    User.username == 'Wilson',
    User.is_active == True
).first()

# OR condition
from sqlalchemy import or_
users = session.query(User).filter(
    or_(User.username == 'Wilson', User.username == 'bob')
).all()

# LIKE query
gmail_users = session.query(User).filter(
    User.email.like('%@gmail.com')
).all()

# IN query
users = session.query(User).filter(
    User.username.in_(['Wilson', 'bob', 'charlie'])
).all()

# Order by
users = session.query(User).order_by(User.username).all()
users = session.query(User).order_by(User.created_at.desc()).all()

# Limit
users = session.query(User).limit(10).all()

# Count
count = session.query(User).count()
```

### Update
```python
from models import User, session

# Method 1: Query, modify, commit
user = session.query(User).filter(User.username == 'Wilson').first()
if user:
    user.email = 'newemail@example.com'
    user.is_active = False
    session.commit()

# Method 2: Update query (more efficient)
session.query(User).filter(User.username == 'Wilson').update({
    'email': 'newemail@example.com',
    'is_active': False
})
session.commit()

# Update multiple records
session.query(User).filter(User.is_active == False).update({
    'is_active': True
})
session.commit()
```

### Delete
```python
from models import User, session

# Method 1: Get object, delete
user = session.query(User).filter(User.username == 'Wilson').first()
if user:
    session.delete(user)
    session.commit()

# Method 2: Delete query
session.query(User).filter(User.username == 'bob').delete()
session.commit()

# Delete multiple
session.query(User).filter(User.is_active == False).delete()
session.commit()
```

---

## Relationships

### One-to-Many
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Owner(Base):
    __tablename__ = 'owners'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    # Relationship: one owner has many pets
    pets: Mapped[list["Pet"]] = relationship("Pet", back_populates="owner")

class Pet(Base):
    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    species: Mapped[str] = mapped_column(String(50))

    # Foreign key to owner
    owner_id: Mapped[int] = mapped_column(ForeignKey('owners.id'))

    # Relationship: many pets belong to one owner
    owner: Mapped["Owner"] = relationship("Owner", back_populates="pets")

# Usage
owner = Owner(name="Wilson")
pet1 = Pet(name="Buddy", species="Dog")
pet2 = Pet(name="Whiskers", species="Cat")

owner.pets.append(pet1)
owner.pets.append(pet2)

session.add(owner)
session.commit()

# Access relationship
print(owner.pets)  # [Pet(Buddy), Pet(Whiskers)]
print(pet1.owner)  # Owner(Wilson)
```

### Many-to-Many
```python
from sqlalchemy import Table, Column, Integer, ForeignKey

# Association table
student_course = Table(
    'student_course',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    # Many-to-many relationship
    courses: Mapped[list["Course"]] = relationship(
        "Course",
        secondary=student_course,
        back_populates="students"
    )

class Course(Base):
    __tablename__ = 'courses'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    # Many-to-many relationship
    students: Mapped[list["Student"]] = relationship(
        "Student",
        secondary=student_course,
        back_populates="courses"
    )

# Usage
student = Student(name="Wilson")
course1 = Course(name="Python 101")
course2 = Course(name="Web Development")

student.courses.append(course1)
student.courses.append(course2)

session.add(student)
session.commit()

# Access relationship
print(student.courses)  # [Course(Python 101), Course(Web Development)]
print(course1.students)  # [Student(Wilson)]
```

### Association Object (Advanced Many-to-Many)
```python
from datetime import datetime

class Enrollment(Base):
    """Association object with extra data"""
    __tablename__ = 'enrollments'

    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey('students.id'))
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'))

    # Extra fields
    enrolled_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    grade: Mapped[str] = mapped_column(String(2), nullable=True)

    # Relationships
    student: Mapped["Student"] = relationship("Student", back_populates="enrollments")
    course: Mapped["Course"] = relationship("Course", back_populates="enrollments")

class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    enrollments: Mapped[list["Enrollment"]] = relationship(
        "Enrollment",
        back_populates="student"
    )

class Course(Base):
    __tablename__ = 'courses'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    enrollments: Mapped[list["Enrollment"]] = relationship(
        "Enrollment",
        back_populates="course"
    )

# Usage
student = Student(name="Wilson")
course = Course(name="Python 101")
enrollment = Enrollment(student=student, course=course, grade="A")

session.add(enrollment)
session.commit()
```

---

## Advanced Queries

### Filtering with Relationships
```python
# Get all pets owned by Wilson
pets = session.query(Pet).join(Owner).filter(Owner.name == 'Wilson').all()

# Get all students enrolled in Python 101
students = session.query(Student).join(
    student_course
).join(Course).filter(Course.name == 'Python 101').all()

# Count pets per owner
from sqlalchemy import func

results = session.query(
    Owner.name,
    func.count(Pet.id).label('pet_count')
).join(Pet).group_by(Owner.name).all()
```

### Aggregations
```python
from sqlalchemy import func

# Count
user_count = session.query(func.count(User.id)).scalar()

# Average
avg_age = session.query(func.avg(User.age)).scalar()

# Min/Max
min_age = session.query(func.min(User.age)).scalar()
max_age = session.query(func.max(User.age)).scalar()

# Group by
results = session.query(
    User.grade,
    func.count(User.id)
).group_by(User.grade).all()
```

### Subqueries
```python
# Subquery for average age
avg_age_subquery = session.query(func.avg(User.age)).scalar_subquery()

# Find users older than average
older_users = session.query(User).filter(User.age > avg_age_subquery).all()
```

---

## Best Practices

### Session Management
```python
# Use context manager for automatic cleanup
from contextlib import contextmanager

@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

# Usage
with get_session() as session:
    user = User(username='Wilson', email='Wilson@example.com')
    session.add(user)
# Auto-commits and closes
```

### Error Handling
```python
from sqlalchemy.exc import IntegrityError

try:
    new_user = User(username='Wilson', email='Wilson@example.com')
    session.add(new_user)
    session.commit()
except IntegrityError as e:
    session.rollback()
    print("User already exists or constraint violated")
except Exception as e:
    session.rollback()
    print(f"Error: {e}")
finally:
    session.close()
```

### Query Performance
```python
# Eager loading (prevent N+1 queries)
from sqlalchemy.orm import joinedload

# Load owner with pets in single query
owners = session.query(Owner).options(joinedload(Owner.pets)).all()

# Select only needed columns
users = session.query(User.username, User.email).all()

# Use pagination
page = 1
per_page = 20
users = session.query(User).limit(per_page).offset((page - 1) * per_page).all()
```

---

## Quick Reference

### SQL Commands
| Command | Purpose | Example |
|---------|---------|---------|
| CREATE TABLE | Define new table | `CREATE TABLE users (...)` |
| INSERT | Add rows | `INSERT INTO users VALUES (...)` |
| SELECT | Query data | `SELECT * FROM users` |
| UPDATE | Modify rows | `UPDATE users SET ...` |
| DELETE | Remove rows | `DELETE FROM users WHERE ...` |
| DROP TABLE | Delete table | `DROP TABLE users` |

### SQLAlchemy CRUD
```python
# Create
user = User(username='Wilson')
session.add(user)
session.commit()

# Read
users = session.query(User).all()
user = session.query(User).filter(User.username == 'Wilson').first()

# Update
user.email = 'new@email.com'
session.commit()

# Delete
session.delete(user)
session.commit()
```

### Common Queries
```python
# Filter
session.query(User).filter(User.age > 18).all()

# Order
session.query(User).order_by(User.name.desc()).all()

# Limit
session.query(User).limit(10).all()

# Count
session.query(User).count()

# Join
session.query(User).join(Post).all()
```

---

## See Also

- **[OOP Cheat Sheet](./OOP_Cheat_Sheet.md)** - Classes for SQLAlchemy models
- **[Error Handling Cheat Sheet](./Error_Handling_Cheat_Sheet.md)** - Database error handling
- **[File Operations Cheat Sheet](./File_Operations_Cheat_Sheet.md)** - Database configuration files
- **[Testing and Debugging Cheat Sheet](./Testing_and_Debugging_Cheat_Sheet.md)** - Testing database operations

---
