# Pet Clinic ORM Project: Architecture Guide

This guide breaks down the architecture of a complete Python CLI application built with **SQLAlchemy**. It demonstrates how to structure a medium-sized application using patterns similar to Flask (Blueprints/Controllers) but adapted for a Command Line Interface.

---

## 1. Project Structure

The project uses a modular design, separating the Database Models, Business Logic (Controllers), and User Interface (CLI).

```
Pet-Clinic-ORM-Project/
├── models.py           # Database Schema (The "M" in MVC)
├── front_end.py        # Main Entry Point & Menus (The "V" in MVC)
├── bp_auth.py          # Authentication Logic
├── bp_owner.py         # Owner Management Logic
├── bp_pets.py          # Pet Management Logic
├── bp_appointments.py  # Appointment Logic
└── requirements.txt    # Dependencies
```

### Why this structure?
Instead of putting all code in one file, we split it by **Domain** (Pets, Owners, Appointments). This is similar to the **Blueprint** pattern in Flask.

---

## 2. Database Models (`models.py`)

The data layer uses SQLAlchemy 2.0 style declarative models.

### Key Features
*   **Centralized Setup:** The engine and session are initialized here and imported elsewhere.
*   **Type Hinting:** Uses `Mapped[]` and `mapped_column()` for modern type safety.
*   **Relationships:** Defines the web of connections between Owners, Pets, and Vets.

```python
# models.py snippet
class Pets(Base):
    __tablename__ = 'pets'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # ... fields ...
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('owners.id'))
    
    # Relationships
    owner: Mapped["Owners"] = relationship("Owners", back_populates="pets")
    appointments: Mapped[list["Appointments"]] = relationship("Appointments", back_populates="pet")
```

---

## 3. Business Logic (The "Blueprints")

Each `bp_*.py` file acts as a controller for a specific domain.

### Authentication (`bp_auth.py`)
Handles user identity.
*   **Login:** Queries the `Owners` table by email and matches password.
*   **Register:** Creates a new `Owners` record.

```python
def login():
    email = input("Email: ")
    password = input("Password: ")
    # Query exact match
    user = session.query(Owners).where(Owners.email == email).first()
    if user and user.password == password:
        return user
    return None
```

### Pet Management (`bp_pets.py`)
Handles CRUD for Pets, scoped to the *current logged-in user*.

*   **View Pets:** Uses the relationship `current_user.pets` to avoid manual queries.
*   **Create Pet:** Links the new pet to `current_user.id`.

```python
def view_pets(current_user):
    # Leveraging the relationship!
    for pet in current_user.pets:
        pet.display()
```

### Complex Logic: Appointments (`bp_appointments.py`)
This is where the application gets interesting. Creating an appointment requires:
1.  Selecting a Pet (from the user's list).
2.  Selecting a Vet (from the database).
3.  Parsing a Date string into a Python `datetime` object.

```python
# Date Conversion Pattern
from datetime import datetime
date_format = "%Y-%m-%d"

date_string = input("Enter date (YYYY-MM-DD): ")
date_object = datetime.strptime(date_string, date_format)
```

---

## 4. User Interface (`front_end.py`)

The main entry point handles the "State" of the application (User Session) and navigation.

### The Session Loop
The app runs in an infinite loop, presenting menus based on whether a user is logged in.

```python
def main():
    print("Welcome to Pet Clinic")
    
    # Phase 1: Authentication Loop
    current_user = welcome_menu() 

    # Phase 2: Main Application Loop
    while current_user:
        choice = input("1. Pets, 2. Appointments, 3. Profile, 4. Logout")
        
        if choice == '1':
            pets_menu(current_user)
        elif choice == '2':
            appointments_menu(current_user)
        # ...
```

---

## 5. Key Takeaways for Students

1.  **Session Management:** Notice how `current_user` is passed to every function (`view_pets(current_user)`). This mimics how web frameworks handle sessions (e.g., `flask_login.current_user`).
2.  **Input Handling:** Every input needs validation (though simple here). Date parsing is a common point of failure.
3.  **Relationships in Action:** We rarely write `SELECT * FROM pets WHERE owner_id = X`. Instead, we use `user.pets`.
4.  **Separation of Concerns:** `front_end.py` handles *menus*, while `bp_pets.py` handles *database logic*. This makes the code testable and organized.

---

## See Also
- **[SQLAlchemy Relationships Guide](SQLAlchemy_Relationships_Guide.md)** - Deep dive into the relationship definitions used here.
- **[Python CLI Applications Guide](Python_CLI_Applications_Guide.md)** - General patterns for building CLI tools.
