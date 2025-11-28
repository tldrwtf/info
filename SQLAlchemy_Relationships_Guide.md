# SQLAlchemy Relationships Guide

## Quick Reference Card

| Relationship Type | Pattern | Use Case | Example |
|-------------------|---------|----------|---------|
| One-to-Many | `db.relationship()` on parent | User has many posts | User → Posts |
| Many-to-One | `db.ForeignKey()` on child | Many posts belong to user | Posts → User |
| One-to-One | `uselist=False` | User has one profile | User ↔ Profile |
| Many-to-Many | Association table | Students take many courses | Students ↔ Courses |
| Self-Referential | Points to same table | Employee has manager | Employee → Employee |

**Common Parameters:**
- `backref`: Creates reverse relationship
- `lazy`: How to load related data ('select', 'joined', 'dynamic')
- `cascade`: What happens on delete ('all, delete-orphan')

## Table of Contents
1. [Understanding Relationships](#understanding-relationships)
2. [One-to-Many Relationships](#one-to-many-relationships)
3. [Many-to-One Relationships](#many-to-one-relationships)
4. [One-to-One Relationships](#one-to-one-relationships)
5. [Many-to-Many Relationships](#many-to-many-relationships)
6. [Association Objects](#association-objects)
7. [Self-Referential Relationships](#self-referential-relationships)
8. [Lazy Loading Strategies](#lazy-loading-strategies)
9. [Cascade Operations](#cascade-operations)
10. [Best Practices](#best-practices)

---

## Understanding Relationships

### Why Relationships Matter
```python
# Without relationships - Manual joins needed
user_id = 1
user = db.session.query(User).filter(User.id == user_id).first()
posts = db.session.query(Post).filter(Post.user_id == user_id).all()

# With relationships - Automatic
user = User.query.get(1)
posts = user.posts  # Automatically fetched!
```

### Key Concepts
```python
# 1. Foreign Key - Links tables together
user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

# 2. Relationship - Provides convenient access
posts = db.relationship('Post', backref='author')

# 3. Backref - Creates reverse relationship automatically
# Instead of defining relationship on both sides, backref does it for you
```

---

## One-to-Many Relationships

### Basic Pattern
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Parent table - One user has many posts"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Relationship to posts
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    """Child table - Many posts belong to one user"""
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # Foreign key to users table
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
```

### Using One-to-Many
```python
# Create user
user = User(username='alice', email='alice@example.com')
db.session.add(user)
db.session.commit()

# Create posts for user
post1 = Post(title='First Post', content='Hello world!', author=user)
post2 = Post(title='Second Post', content='Another post', author=user)

db.session.add_all([post1, post2])
db.session.commit()

# Access user's posts
user = User.query.filter_by(username='alice').first()
for post in user.posts:
    print(post.title)  # "First Post", "Second Post"

# Access post's author
post = Post.query.first()
print(post.author.username)  # "alice"
```

### With Cascade Delete
```python
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)

    # When user is deleted, delete all their posts
    posts = db.relationship(
        'Post',
        backref='author',
        lazy=True,
        cascade='all, delete-orphan'
    )

# Delete user and all their posts
user = User.query.get(1)
db.session.delete(user)  # This deletes user AND all their posts
db.session.commit()
```

---

## Many-to-One Relationships

### Pattern (Reverse of One-to-Many)
```python
class Department(db.Model):
    """One department has many employees"""
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    employees = db.relationship('Employee', backref='department')

class Employee(db.Model):
    """Many employees belong to one department"""
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    department_id = db.Column(
        db.Integer,
        db.ForeignKey('departments.id'),
        nullable=False
    )
```

### Usage
```python
# Create department
engineering = Department(name='Engineering')
db.session.add(engineering)
db.session.commit()

# Add employees to department
emp1 = Employee(name='Alice', department=engineering)
emp2 = Employee(name='Bob', department=engineering)

db.session.add_all([emp1, emp2])
db.session.commit()

# Access employees of department
dept = Department.query.filter_by(name='Engineering').first()
for employee in dept.employees:
    print(employee.name)

# Access department of employee
employee = Employee.query.filter_by(name='Alice').first()
print(employee.department.name)  # "Engineering"
```

---

## One-to-One Relationships

### Pattern
```python
class User(db.Model):
    """One user has one profile"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)

    # uselist=False makes it one-to-one
    profile = db.relationship('Profile', backref='user', uselist=False)

class Profile(db.Model):
    """One profile belongs to one user"""
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text)
    website = db.Column(db.String(200))

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False,
        unique=True  # Enforces one-to-one
    )
```

### Usage
```python
# Create user and profile
user = User(username='alice')
profile = Profile(bio='Software Developer', website='https://alice.dev', user=user)

db.session.add_all([user, profile])
db.session.commit()

# Access profile from user
user = User.query.filter_by(username='alice').first()
print(user.profile.bio)  # "Software Developer"

# Access user from profile
profile = Profile.query.first()
print(profile.user.username)  # "alice"
```

---

## Many-to-Many Relationships

### Association Table Pattern
```python
# Association table (no model class needed for simple many-to-many)
student_course = db.Table('student_course',
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True)
)

class Student(db.Model):
    """Many students take many courses"""
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Many-to-many relationship
    courses = db.relationship(
        'Course',
        secondary=student_course,
        backref=db.backref('students', lazy='dynamic')
    )

class Course(db.Model):
    """Many courses have many students"""
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer)
```

### Usage
```python
# Create students and courses
alice = Student(name='Alice')
bob = Student(name='Bob')

python = Course(name='Python 101', credits=3)
sql = Course(name='SQL Fundamentals', credits=3)

# Add courses to students
alice.courses.append(python)
alice.courses.append(sql)
bob.courses.append(python)

db.session.add_all([alice, bob, python, sql])
db.session.commit()

# Get all courses for a student
student = Student.query.filter_by(name='Alice').first()
for course in student.courses:
    print(course.name)  # "Python 101", "SQL Fundamentals"

# Get all students in a course
course = Course.query.filter_by(name='Python 101').first()
for student in course.students:
    print(student.name)  # "Alice", "Bob"

# Remove student from course
alice.courses.remove(python)
db.session.commit()
```

---

## Association Objects

### When to Use Association Objects
```python
# Use association object when junction table needs extra data
# Example: Track enrollment date and grade

class Enrollment(db.Model):
    """Association object with additional data"""
    __tablename__ = 'enrollments'

    student_id = db.Column(
        db.Integer,
        db.ForeignKey('students.id'),
        primary_key=True
    )
    course_id = db.Column(
        db.Integer,
        db.ForeignKey('courses.id'),
        primary_key=True
    )

    # Additional fields
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)
    grade = db.Column(db.String(2))

    # Relationships
    student = db.relationship('Student', backref='enrollments')
    course = db.relationship('Course', backref='enrollments')

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
```

### Using Association Objects
```python
# Enroll student in course
alice = Student(name='Alice')
python = Course(name='Python 101')

enrollment = Enrollment(student=alice, course=python, grade='A')
db.session.add_all([alice, python, enrollment])
db.session.commit()

# Query enrollments
student = Student.query.filter_by(name='Alice').first()
for enrollment in student.enrollments:
    print(f"{enrollment.course.name}: {enrollment.grade}")
    print(f"Enrolled on: {enrollment.enrollment_date}")
```

### Advanced: Hybrid Association
```python
class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Access courses through enrollment
    def get_courses(self):
        return [e.course for e in self.enrollments]

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def get_students(self):
        return [e.student for e in self.enrollments]

# Usage
student = Student.query.first()
courses = student.get_courses()
```

### Real-World Example: Pet Clinic System

This complete example demonstrates a veterinary clinic database with multiple relationship types working together.

```python
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Boolean, Text
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Mapped, mapped_column
from datetime import date

# Database setup
Base = declarative_base()
engine = create_engine('sqlite:///pet_clinic.db')
Session = sessionmaker(bind=engine)
session = Session()


class Owners(Base):
    """Owner model representing pet owners"""
    __tablename__ = 'owners'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    # One-to-many relationship: One owner has many pets
    pets: Mapped[list["Pets"]] = relationship("Pets", back_populates="owner")

    def display(self):
        print("--------- My Info ---------------")
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone:", self.phone)


class Pets(Base):
    """Pet model representing pets in the clinic"""
    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    species: Mapped[str] = mapped_column(String(50), nullable=False)
    breed: Mapped[str] = mapped_column(String(100), nullable=True)
    age: Mapped[int] = mapped_column(Integer, nullable=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('owners.id'), nullable=False)

    # Relationships
    owner: Mapped["Owners"] = relationship("Owners", back_populates="pets")
    appointments: Mapped[list["Appointments"]] = relationship("Appointments", back_populates="pet")

    def display(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Species:", self.species)
        print("Age:", self.age)


class Vets(Base):
    """Veterinarian model representing clinic veterinarians"""
    __tablename__ = 'vets'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    specialization: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    appointments: Mapped[list["Appointments"]] = relationship("Appointments", back_populates="vet")

    def display(self):
        print("Name:", self.name)
        print("Specialization:", self.specialization)
        print("Email:", self.email)


class Appointments(Base):
    """Appointment model - acts as association table with additional fields"""
    __tablename__ = 'appointments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey('pets.id'), nullable=False)
    veterinarian_id: Mapped[int] = mapped_column(Integer, ForeignKey('vets.id'), nullable=False)
    appointment_date: Mapped[date] = mapped_column(Date, nullable=False)
    notes: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="Scheduled", nullable=False)

    # Relationships
    pet: Mapped["Pets"] = relationship("Pets", back_populates="appointments")
    vet: Mapped["Vets"] = relationship("Vets", back_populates="appointments")

    def display(self):
        print("Id:", self.id)
        print("Appointment_date:", self.appointment_date)
        print("Vet:", self.vet.name)
        print("Notes:", self.notes)
        print("Status:", self.status)


Base.metadata.create_all(engine)
```

**Using the Pet Clinic System:**

```python
# Create an owner
owner = Owners(
    name="John Smith",
    phone="555-0123",
    email="john@example.com",
    password="password123"
)

# Create pets for the owner
dog = Pets(
    name="Buddy",
    species="Dog",
    breed="Golden Retriever",
    age=3,
    owner=owner
)

cat = Pets(
    name="Whiskers",
    species="Cat",
    breed="Siamese",
    age=2,
    owner=owner
)

# Create a vet
vet = Vets(
    name="Dr. Sarah Johnson",
    specialization="Small Animals",
    email="dr.sarah@petclinic.com"
)

# Create appointments (many-to-many through association object)
appt1 = Appointments(
    pet=dog,
    vet=vet,
    appointment_date=date(2025, 12, 15),
    notes="Annual checkup",
    status="Scheduled"
)

appt2 = Appointments(
    pet=cat,
    vet=vet,
    appointment_date=date(2025, 12, 16),
    notes="Vaccination",
    status="Scheduled"
)

# Save to database
session.add_all([owner, dog, cat, vet, appt1, appt2])
session.commit()

# Query examples:
# Get all pets for an owner
owner_pets = owner.pets
for pet in owner_pets:
    print(f"{owner.name} owns {pet.name} the {pet.species}")

# Get all appointments for a pet
pet_appointments = dog.appointments
for appt in pet_appointments:
    print(f"{dog.name} has appointment with {appt.vet.name} on {appt.appointment_date}")

# Get all patients for a vet
vet_patients = [appt.pet for appt in vet.appointments]
for pet in vet_patients:
    print(f"Dr. {vet.name} will see {pet.name} (owned by {pet.owner.name})")
```

**Why This Example is Valuable:**

- **Multiple relationship types:** One-to-Many (Owner→Pets, Vet→Appointments) and Many-to-Many (Pets↔Vets through Appointments)
- **Modern SQLAlchemy:** Uses `Mapped` type hints and `mapped_column()` (SQLAlchemy 2.0 style)
- **Association object:** Appointments table connects Pets and Vets while storing additional data (date, notes, status)
- **Real-world scenario:** Students can relate to a pet clinic system
- **Complete relationships:** Shows how to traverse relationships in multiple directions
- **Practical methods:** Includes `display()` methods for user-friendly output

---

## Self-Referential Relationships

### Employee-Manager Pattern
```python
class Employee(db.Model):
    """Employee can have a manager (another employee)"""
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100))

    # Self-referential foreign key
    manager_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    # Relationship to manager
    manager = db.relationship(
        'Employee',
        remote_side=[id],  # Specifies the remote side
        backref='subordinates'
    )
```

### Usage
```python
# Create manager
ceo = Employee(name='Alice', position='CEO')

# Create subordinates
manager1 = Employee(name='Bob', position='Manager', manager=ceo)
manager2 = Employee(name='Charlie', position='Manager', manager=ceo)

# Create employees under manager
emp1 = Employee(name='David', position='Developer', manager=manager1)
emp2 = Employee(name='Eve', position='Designer', manager=manager1)

db.session.add_all([ceo, manager1, manager2, emp1, emp2])
db.session.commit()

# Get employee's manager
employee = Employee.query.filter_by(name='David').first()
print(employee.manager.name)  # "Bob"

# Get manager's subordinates
manager = Employee.query.filter_by(name='Bob').first()
for subordinate in manager.subordinates:
    print(subordinate.name)  # "David", "Eve"
```

### Tree Structure (Comments/Replies)
```python
class Comment(db.Model):
    """Comments can have replies (nested comments)"""
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Self-referential for replies
    parent_id = db.Column(db.Integer, db.ForeignKey('comments.id'))

    replies = db.relationship(
        'Comment',
        backref=db.backref('parent', remote_side=[id]),
        lazy='dynamic'
    )

# Usage
main_comment = Comment(text='Great article!')
reply1 = Comment(text='Thanks!', parent=main_comment)
reply2 = Comment(text='Agreed!', parent=main_comment)
nested_reply = Comment(text='Me too!', parent=reply1)

# Get all replies to a comment
for reply in main_comment.replies:
    print(reply.text)
```

### Real-World Example: Social Media Following System

This example demonstrates a many-to-many self-referential relationship where users can follow other users.

```python
from sqlalchemy import create_engine, Integer, String, Float, ForeignKey, DateTime, Table, Column
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///social_media.db')
Session = sessionmaker(bind=engine)
session = Session()

# Many-to-many self-referential association table
user_follows = Table(
    'user_follows',
    Base.metadata,
    Column('follower_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('following_id', Integer, ForeignKey('users.id'), primary_key=True)
)

class Users(Base):
    """User model with self-referential many-to-many following"""
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    bio: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    # Self-referential many-to-many: Users follow other users
    following: Mapped[list["Users"]] = relationship(
        "Users",
        secondary=user_follows,
        primaryjoin=(user_follows.c.follower_id == id),
        secondaryjoin=(user_follows.c.following_id == id),
        backref="followers"
    )

    posts: Mapped[list["Posts"]] = relationship("Posts", back_populates="author")

    def display(self):
        print(f"@{self.username}")
        print(f"Bio: {self.bio}")
        print(f"Following: {len(self.following)}")
        print(f"Followers: {len(self.followers)}")


class Posts(Base):
    """Posts belong to users"""
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)

    author: Mapped["Users"] = relationship("Users", back_populates="posts")


Base.metadata.create_all(engine)
```

**Using the Social Media System:**

```python
# Create users
alice = Users(username="alice", email="alice@example.com", bio="Python developer")
bob = Users(username="bob", email="bob@example.com", bio="Data scientist")
charlie = Users(username="charlie", email="charlie@example.com", bio="Web developer")

# Alice follows Bob and Charlie
alice.following.append(bob)
alice.following.append(charlie)

# Bob follows Charlie
bob.following.append(charlie)

# Charlie follows Alice (creating a follow-back relationship)
charlie.following.append(alice)

# Add to database
session.add_all([alice, bob, charlie])
session.commit()

# Query examples:
# Who does Alice follow?
print(f"{alice.username} follows:")
for user in alice.following:
    print(f"  - @{user.username}")

# Who follows Alice?
print(f"\n{alice.username}'s followers:")
for user in alice.followers:
    print(f"  - @{user.username}")

# Check if Alice follows Bob
if bob in alice.following:
    print(f"\n@{alice.username} follows @{bob.username}")

# Unfollow example
alice.following.remove(bob)
session.commit()
print(f"\n@{alice.username} unfollowed @{bob.username}")

# Get mutual follows (users who follow each other)
mutual_follows = set(alice.following) & set(alice.followers)
print(f"\nMutual follows for @{alice.username}:")
for user in mutual_follows:
    print(f"  - @{user.username}")
```

**Why This Example is Valuable:**

- **Many-to-many self-referential:** Shows how a table can have a many-to-many relationship with itself
- **Social media pattern:** Students understand following/followers concept from real platforms
- **Bidirectional access:** Can access both `following` and `followers` lists
- **Complex primaryjoin/secondaryjoin:** Demonstrates how to properly configure self-referential M2M
- **Practical operations:** Shows follow, unfollow, mutual follows, follower count
- **Association table:** Simple junction table without extra fields (vs association object)

---

## Lazy Loading Strategies

### Understanding Lazy Loading
```python
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))

    # Different lazy loading strategies
    posts_select = db.relationship('Post', lazy='select')      # Default
    posts_joined = db.relationship('Post', lazy='joined')      # JOIN
    posts_subquery = db.relationship('Post', lazy='subquery')  # Subquery
    posts_dynamic = db.relationship('Post', lazy='dynamic')    # Query object
```

### Lazy Options Explained
```python
# 1. 'select' (default) - Load when accessed
posts = db.relationship('Post', lazy='select')
user = User.query.get(1)
print(user.posts)  # Triggers separate query to load posts

# 2. 'joined' - Use JOIN to load in one query
posts = db.relationship('Post', lazy='joined')
user = User.query.get(1)  # Loads user and posts in one query

# 3. 'subquery' - Load with a subquery
posts = db.relationship('Post', lazy='subquery')
users = User.query.all()  # Loads all users and their posts efficiently

# 4. 'dynamic' - Return query object (not list)
posts = db.relationship('Post', lazy='dynamic')
user = User.query.get(1)
recent_posts = user.posts.filter(Post.created_at > '2024-01-01').all()
```

### Choosing the Right Strategy
```python
# Use 'select' when:
# - You don't always need related data
# - Small number of relationships

# Use 'joined' when:
# - You always need related data
# - Avoid N+1 query problem

# Use 'dynamic' when:
# - Large number of related items
# - Need to filter/sort related items
# - Need pagination on relationships

# Example: Blog with many comments
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))

    # Dynamic for large number of comments
    comments = db.relationship('Comment', lazy='dynamic')

# Can now filter/paginate comments
post = Post.query.get(1)
recent_comments = post.comments.filter(
    Comment.created_at > datetime.now() - timedelta(days=7)
).order_by(Comment.created_at.desc()).limit(10).all()
```

---

## Cascade Operations

### Cascade Options
```python
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))

    # Cascade options
    posts = db.relationship(
        'Post',
        cascade='all, delete-orphan',  # Most common
        backref='author'
    )
```

### Cascade Types
```python
# 'save-update' - Default, propagate add/update
# 'delete' - Delete children when parent deleted
# 'delete-orphan' - Delete children when removed from relationship
# 'merge' - Propagate merge operations
# 'all' - Shortcut for all cascades except delete-orphan

# Example 1: Delete cascade
class User(db.Model):
    posts = db.relationship('Post', cascade='delete')

user = User.query.get(1)
db.session.delete(user)  # Deletes user and all posts
db.session.commit()

# Example 2: Delete-orphan
class User(db.Model):
    posts = db.relationship('Post', cascade='all, delete-orphan')

user = User.query.get(1)
post = user.posts[0]
user.posts.remove(post)  # Post is deleted from database
db.session.commit()
```

### Practical Example: Blog Platform
```python
class Blog(db.Model):
    """Blog with posts and comments"""
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    posts = db.relationship(
        'Post',
        cascade='all, delete-orphan',
        backref='blog'
    )

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    comments = db.relationship(
        'Comment',
        cascade='all, delete-orphan',
        backref='post'
    )

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

# Delete blog deletes all posts and comments
blog = Blog.query.get(1)
db.session.delete(blog)  # Cascade deletes posts and comments
db.session.commit()
```

---

## Best Practices

### 1. Always Use backref or back_populates
```python
# Good - Using backref
class User(db.Model):
    posts = db.relationship('Post', backref='author')

# Good - Using back_populates (more explicit)
class User(db.Model):
    posts = db.relationship('Post', back_populates='author')

class Post(db.Model):
    author = db.relationship('User', back_populates='posts')

# Bad - No reverse relationship
class User(db.Model):
    posts = db.relationship('Post')  # Can't access user from post
```

### 2. Use Indexes on Foreign Keys
```python
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)

    # Index foreign key for better performance
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False,
        index=True  # Add index
    )
```

### 3. Choose Appropriate Lazy Loading
```python
# Don't do this - N+1 query problem
users = User.query.all()
for user in users:
    print(user.posts)  # Separate query for each user!

# Do this - Use joined loading
users = User.query.options(db.joinedload('posts')).all()
for user in users:
    print(user.posts)  # All loaded in one query
```

### 4. Use Cascade Wisely
```python
# Be careful with cascade='all, delete'
# Make sure you want to delete related data

# Good for dependent data (comments belong to post)
class Post(db.Model):
    comments = db.relationship(
        'Comment',
        cascade='all, delete-orphan'
    )

# Bad for independent data (user and their addresses)
# Maybe you want to keep address history
class User(db.Model):
    addresses = db.relationship(
        'Address',
        cascade='save-update'  # Don't cascade delete
    )
```

### 5. Naming Conventions
```python
# Use plural for one-to-many
class User(db.Model):
    posts = db.relationship('Post')  # Plural - many posts

# Use singular for many-to-one
class Post(db.Model):
    author = db.relationship('User')  # Singular - one author

# Use meaningful backref names
class User(db.Model):
    posts = db.relationship('Post', backref='author')  # Not 'user'
```

---

## Complete Example: Library System

```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Many-to-many association table
book_author = db.Table('book_author',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), primary_key=True)
)

class User(db.Model):
    """Library user"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # One-to-many: User has many loans
    loans = db.relationship(
        'Loan',
        backref='user',
        lazy='dynamic',
        cascade='all, delete-orphan'
    )

class Author(db.Model):
    """Book author"""
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Many-to-many: Authors write many books
    books = db.relationship(
        'Book',
        secondary=book_author,
        backref=db.backref('authors', lazy='dynamic')
    )

class Book(db.Model):
    """Library book"""
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    isbn = db.Column(db.String(13), unique=True)

    # One-to-many: Book has many loans
    loans = db.relationship(
        'Loan',
        backref='book',
        lazy='dynamic'
    )

class Loan(db.Model):
    """Book loan record (association object)"""
    __tablename__ = 'loans'

    id = db.Column(db.Integer, primary_key=True)
    loan_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime)
    returned = db.Column(db.Boolean, default=False)

    # Foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)

# Usage examples
def example_usage():
    # Create author and books
    author = Author(name='George Orwell')
    book1 = Book(title='1984', isbn='1234567890123')
    book2 = Book(title='Animal Farm', isbn='9876543210987')

    author.books.extend([book1, book2])

    # Create user
    user = User(name='Alice', email='alice@example.com')

    # Create loan
    loan = Loan(user=user, book=book1)

    db.session.add_all([author, book1, book2, user, loan])
    db.session.commit()

    # Query examples
    # Get all books by an author
    author = Author.query.filter_by(name='George Orwell').first()
    for book in author.books:
        print(book.title)

    # Get all active loans for a user
    user = User.query.filter_by(name='Alice').first()
    active_loans = user.loans.filter_by(returned=False).all()

    # Get all users who borrowed a specific book
    book = Book.query.filter_by(title='1984').first()
    for loan in book.loans:
        print(loan.user.name)
```

---

## See Also

- **[SQL and SQLAlchemy Cheat Sheet](./SQL_and_SQLAlchemy_Cheat_Sheet.md)** - Basic SQL operations
- **[Flask REST API Development Guide](./Flask_REST_API_Development_Guide.md)** - Using relationships in APIs
- **[OOP Cheat Sheet](./OOP_Cheat_Sheet.md)** - Class relationships
- **[Data Structures Cheat Sheet](./Data_Structures_Cheat_Sheet.md)** - Data modeling concepts

---
