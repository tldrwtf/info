# Pet Clinic ORM Project Guide

This guide details the design and implementation of a command-line interface (CLI) application for managing a pet clinic, utilizing Python and SQLAlchemy ORM. It showcases fundamental database operations (CRUD) and CLI interaction patterns.

---

## 1. Project Overview

The Pet Clinic ORM Project is a Python-based CLI application designed to manage owners, their pets, veterinarians, and appointments within a veterinary clinic setting. It leverages SQLAlchemy as an Object-Relational Mapper (ORM) to interact with a SQLite database, providing a robust and structured way to handle data persistence.

### Key Features
*   **User Authentication:** Owner registration and login.
*   **Owner Management:** View, update, and delete owner profiles.
*   **Pet Management:** Create, view, update, and delete pets associated with an owner.
*   **Appointment Scheduling:** Create, view, reschedule, and complete appointments with veterinarians.
*   **Interactive CLI:** Menu-driven interface for easy navigation.

---

## 2. Database Models (`models.py`)

The heart of the application is its database schema, defined using SQLAlchemy's declarative base. This section outlines the `Owners`, `Pets`, `Vets`, and `Appointments` models and their relationships.

```python
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Boolean, Text
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Mapped, mapped_column
from datetime import date

# Database setup
# engine = create_engine('sqlite:///pet_clinic.db')
Base = declarative_base() # Base class for declarative models
# Session = sessionmaker(bind=engine)
# session = Session()

class Owners(Base):
    """Owner model representing pet owners"""
    __tablename__ = 'owners'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String, nullable=False)

    # Relationship to pets (one-to-many)
    pets: Mapped[list["Pets"]] = relationship("Pets", back_populates="owner", cascade="all, delete-orphan")
    appointments: Mapped[list["Appointments"]] = relationship("Appointments", back_populates="owner", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Owner(id={self.id}, name='{self.name}', email='{self.email}')>"

    def display(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")


class Pets(Base):
    """Pet model representing pets in the clinic"""
    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    species: Mapped[str] = mapped_column(String)
    breed: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    owner_id: Mapped[int] = mapped_column(ForeignKey('owners.id')) # Foreign key to Owners

    # Relationships
    owner: Mapped["Owners"] = relationship("Owners", back_populates="pets")
    appointments: Mapped[list["Appointments"]] = relationship("Appointments", back_populates="pet", cascade="all, delete-orphan")


    def __repr__(self):
        return f"<Pet(id={self.id}, name='{self.name}', species='{self.species}', owner_id={self.owner_id})>"
    
    def display(self):
      print(f"Name: {self.name}")
      print(f"Species: {self.species}")
      print(f"Breed: {self.breed}")
      print(f"Age: {self.age}")


class Vets(Base):
    """Veterinarian model representing clinic veterinarians"""
    __tablename__ = 'vets'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    specialization: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    # Relationships
    appointments: Mapped[list["Appointments"]] = relationship("Appointments", back_populates="vet")

    def __repr__(self):
        return f"<Vet(id={self.id}, name='{self.name}', specialization='{self.specialization}')>"

    def display(self):
      print(f"Name: {self.name}")
      print(f"Specialization: {self.specialization}")


class Appointments(Base):
    """Appointment model representing pet appointments with veterinarians"""
    __tablename__ = 'appointments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pet_id: Mapped[int] = mapped_column(ForeignKey('pets.id'))
    vet_id: Mapped[int] = mapped_column(ForeignKey('vets.id'))
    owner_id: Mapped[int] = mapped_column(ForeignKey('owners.id'))
    appointment_date: Mapped[date] = mapped_column(Date, nullable=False)
    reason: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String, default='scheduled') # scheduled, completed, cancelled

    # Relationships
    pet: Mapped["Pets"] = relationship("Pets", back_populates="appointments")
    vet: Mapped["Vets"] = relationship("Vets", back_populates="appointments")
    owner: Mapped["Owners"] = relationship("Owners", back_populates="appointments")

    def __repr__(self):
        return f"<Appointment(id={self.id}, pet_id={self.pet_id}, vet_id={self.vet_id}, date={self.appointment_date}, status='{self.status}')>"

    def display(self):
      print(f"Pet: {self.pet.name}")
      print(f"Vet: {self.vet.name}")
      print(f"Date: {self.appointment_date}")
      print(f"Reason: {self.reason}")
      print(f"Status: {self.status}")

# Base.metadata.create_all(engine) # Call this once to create tables
```

---

## 3. Authentication and User Management (`bp_auth.py`)

This blueprint handles owner registration and login, centralizing user authentication logic.

```python
from models import Owners, session # Assuming session is created globally

def login():
    """Handles owner login."""
    print("\n----------- Login -------------")
    email = input("Email: ")
    password = input("Password: ")

    # Search for owner by email
    owner = session.query(Owners).filter_by(email=email).first()

    if owner and owner.password == password: # Simplified password check
        print("Successfully logged in!")
        print(f"Welcome back, {owner.name}!")
        return owner
    else:
        print("Invalid email or password.")
        return None

def register():
    """Handles new owner registration."""
    print("\n----------- Register -------------")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    password = input("Password: ")

    try:
        new_owner = Owners(name=name, email=email, phone=phone, password=password)
        session.add(new_owner)
        session.commit()
        print("Registration successful!")
        return new_owner
    except Exception as e:
        session.rollback()
        print(f"Registration failed: {e}")
        return None
```

---

## 4. Owner Operations (`bp_owner.py`)

This blueprint provides functionalities for an authenticated owner to manage their profile.

```python
from models import Owners, session # Assuming session is created globally

def view_owner(current_user):
    """Displays the current user's profile information."""
    print("\n--- Your Profile ---")
    current_user.display()

def update_owner(current_user):
    """Allows the current user to update their profile information."""
    print("\n--- Update Profile ---")
    print(f"Current Name: {current_user.name}")
    new_name = input(f"Enter new name (current: {current_user.name}): ")
    if new_name:
        current_user.name = new_name

    print(f"Current Email: {current_user.email}")
    new_email = input(f"Enter new email (current: {current_user.email}): ")
    if new_email:
        current_user.email = new_email

    print(f"Current Phone: {current_user.phone}")
    new_phone = input(f"Enter new phone (current: {current_user.phone}): ")
    if new_phone:
        current_user.phone = new_phone
    
    # Password update would require current password verification
    
    try:
        session.commit()
        print("Profile updated successfully!")
        return current_user # Return updated user
    except Exception as e:
        session.rollback()
        print(f"Error updating profile: {e}")
        return None

def delete_owner(current_user):
    """Allows the current user to delete their account."""
    print(f"\n--- Delete Account ({current_user.name}) ---")
    confirm = input("Are you sure you want to delete your account? (y/n): ").lower()
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

## 5. Pet Management (`bp_pets.py`)

This blueprint handles all operations related to an owner's pets.

```python
from models import Pets, session # Assuming session is created globally

def view_pets(current_user):
    """Displays all pets belonging to the current user."""
    if not current_user.pets:
        print("You have no pets registered.")
        return

    print(f"\n--- {current_user.name}'s Pets ---")
    for i, pet in enumerate(current_user.pets):
        print(f"[{i+1}]")
        pet.display()
        print("-" * 20)

def create_pet(current_user):
    """Allows the current user to register a new pet."""
    print("\n--- Register New Pet ---")
    name = input("Pet's Name: ")
    species = input("Species: ")
    breed = input("Breed: ")
    age = int(input("Age: "))

    try:
        new_pet = Pets(name=name, species=species, breed=breed, age=age, owner=current_user)
        session.add(new_pet)
        session.commit()
        print(f"Pet '{name}' registered successfully for {current_user.name}!")
        return new_pet
    except Exception as e:
        session.rollback()
        print(f"Error registering pet: {e}")
        return None

def update_pet(current_user):
    """Allows the current user to update information for one of their pets."""
    if not current_user.pets:
        print("You have no pets to update.")
        return
    
    view_pets(current_user)
    choice = int(input("Enter the number of the pet you want to update: ")) - 1

    if 0 <= choice < len(current_user.pets):
        pet_to_update = current_user.pets[choice]
        print(f"\n--- Update {pet_to_update.name}'s Info ---")
        
        new_name = input(f"Enter new name (current: {pet_to_update.name}): ")
        if new_name: pet_to_update.name = new_name
        
        new_species = input(f"Enter new species (current: {pet_to_update.species}): ")
        if new_species: pet_to_update.species = new_species

        new_breed = input(f"Enter new breed (current: {pet_to_update.breed}): ")
        if new_breed: pet_to_update.breed = new_breed

        new_age = input(f"Enter new age (current: {pet_to_update.age}): ")
        if new_age: pet_to_update.age = int(new_age)

        try:
            session.commit()
            print(f"{pet_to_update.name}'s info updated successfully!")
            return pet_to_update
        except Exception as e:
            session.rollback()
            print(f"Error updating pet info: {e}")
            return None
    else:
        print("Invalid pet selection.")
        return None

def delete_pet(current_user):
    """Allows the current user to delete one of their pets."""
    if not current_user.pets:
        print("You have no pets to delete.")
        return

    view_pets(current_user)
    choice = int(input("Enter the number of the pet you want to delete: ")) - 1

    if 0 <= choice < len(current_user.pets):
        pet_to_delete = current_user.pets[choice]
        confirm = input(f"Are you sure you want to delete {pet_to_delete.name}? (y/n): ").lower()
        if confirm == 'y':
            try:
                session.delete(pet_to_delete)
                session.commit()
                print(f"{pet_to_delete.name} deleted successfully.")
            except Exception as e:
                session.rollback()
                print(f"Error deleting pet: {e}")
        else:
            print("Pet deletion cancelled.")
    else:
        print("Invalid pet selection.")
```

---

## 6. Appointment Management (`bp_appointments.py`)

This blueprint handles scheduling, viewing, rescheduling, and completing appointments.

```python
from models import Owners, Pets, Vets, session, Appointments
from datetime import datetime

def create_appointment(current_user):
    """Allows an owner to create a new appointment for one of their pets."""
    print("\n--- Create New Appointment ---")
    if not current_user.pets:
        print("You have no pets to schedule an appointment for. Please add a pet first.")
        return

    # Display pets
    print("\nYour Pets:")
    for i, pet in enumerate(current_user.pets):
        print(f"[{i+1}] {pet.name} (Species: {pet.species})")
    pet_choice = int(input("Enter the number of the pet for this appointment: ")) - 1
    if not (0 <= pet_choice < len(current_user.pets)):
        print("Invalid pet selection.")
        return
    selected_pet = current_user.pets[pet_choice]

    # Display vets
    vets = session.query(Vets).all()
    if not vets:
        print("No veterinarians available.")
        return
    print("\nAvailable Veterinarians:")
    for i, vet in enumerate(vets):
        print(f"[{i+1}] {vet.name} (Specialization: {vet.specialization})")
    vet_choice = int(input("Enter the number of the vet for this appointment: ")) - 1
    if not (0 <= vet_choice < len(vets)):
        print("Invalid veterinarian selection.")
        return
    selected_vet = vets[vet_choice]

    appointment_date_str = input("Enter appointment date (YYYY-MM-DD): ")
    try:
        appointment_date = datetime.strptime(appointment_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    reason = input("Reason for appointment: ")

    try:
        new_appointment = Appointments(
            pet=selected_pet,
            vet=selected_vet,
            owner=current_user,
            appointment_date=appointment_date,
            reason=reason,
            status='scheduled'
        )
        session.add(new_appointment)
        session.commit()
        print("Appointment scheduled successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error scheduling appointment: {e}")

def view_appointments(current_user):
    """Displays all appointments for the current user's pets."""
    print("\n--- Your Appointments ---")
    owner_appointments = session.query(Appointments).filter_by(owner_id=current_user.id).all()
    if not owner_appointments:
        print("You have no appointments scheduled.")
        return
    
    for i, appt in enumerate(owner_appointments):
        print(f"[{i+1}]")
        appt.display()
        print("-" * 20)

def reschedule_appointment(current_user):
    """Allows an owner to reschedule one of their appointments."""
    view_appointments(current_user)
    if not current_user.appointments: # Re-check after potential view
        return

    choice = int(input("Enter the number of the appointment to reschedule: ")) - 1
    if not (0 <= choice < len(current_user.appointments)):
        print("Invalid appointment selection.")
        return
    
    appt_to_reschedule = current_user.appointments[choice]
    print(f"Current appointment date: {appt_to_reschedule.appointment_date}")
    new_date_str = input("Enter new date (YYYY-MM-DD): ")
    try:
        new_date = datetime.strptime(new_date_str, "%Y-%m-%d").date()
        appt_to_reschedule.appointment_date = new_date
        session.commit()
        print("Appointment rescheduled successfully!")
    except ValueError:
        print("Invalid date format.")
    except Exception as e:
        session.rollback()
        print(f"Error rescheduling: {e}")

def complete_appointment(current_user):
    """Allows an owner to mark one of their appointments as completed."""
    view_appointments(current_user)
    if not current_user.appointments: # Re-check after potential view
        return

    choice = int(input("Enter the number of the appointment to mark as complete: ")) - 1
    if not (0 <= choice < len(current_user.appointments)):
        print("Invalid appointment selection.")
        return
    
    appt_to_complete = current_user.appointments[choice]
    if appt_to_complete.status == 'completed':
        print("Appointment is already marked as completed.")
        return

    try:
        appt_to_complete.status = 'completed'
        session.commit()
        print("Appointment marked as completed!")
    except Exception as e:
        session.rollback()
        print(f"Error marking appointment complete: {e}")
```

---

## 7. Interactive CLI Frontend (`front_end.py`)

This file ties all the blueprints together, presenting a menu-driven interface to the user.

```python
from models import Owners, session # Assuming session is created globally
from bp_auth import register, login
from bp_owner import view_owner, update_owner, delete_owner
from bp_pets import view_pets, create_pet, update_pet, delete_pet
from bp_appointments import create_appointment, reschedule_appointment, view_appointments, complete_appointment
import sys

# Helper for confirmation, assuming it's imported or defined globally
def confirm_action(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']: return True
        elif response in ['n', 'no']: return False
        else: print("Please enter 'y' or 'n'.")


def welcome_menu():
    """Displays the welcome menu for login/registration."""
    while True:
        print("\n" + "="*30)
        print("   Welcome to Pet Clinic!   ")
        print("="*30)
        print("1. Login")
        print("2. Register")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user = login()
            if user: return user
        elif choice == '2':
            user = register()
            if user: return user
        elif choice == '0':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice.")

def owner_menu(current_user):
    """Displays the menu for an authenticated owner."""
    while True:
        print(f"\n--- Welcome, {current_user.name}! ---")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Manage Pets")
        print("4. Manage Appointments")
        print("0. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_owner(current_user)
        elif choice == '2':
            updated_user = update_owner(current_user)
            if updated_user: current_user = updated_user # Update current_user if changes were made
        elif choice == '3':
            pets_menu(current_user)
        elif choice == '4':
            appointments_menu(current_user)
        elif choice == '0':
            print("Logging out.")
            return # Exit owner menu
        else:
            print("Invalid choice.")

def pets_menu(current_user):
    """Displays the pet management menu."""
    while True:
        print(f"\n--- {current_user.name}'s Pet Management ---")
        print("1. View All Pets")
        print("2. Add New Pet")
        print("3. Update Pet Info")
        print("4. Delete Pet")
        print("0. Back to Owner Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_pets(current_user)
        elif choice == '2':
            create_pet(current_user)
        elif choice == '3':
            update_pet(current_user)
        elif choice == '4':
            delete_pet(current_user)
        elif choice == '0':
            return
        else:
            print("Invalid choice.")

def appointments_menu(current_user):
    """Displays the appointment management menu."""
    while True:
        print(f"\n--- {current_user.name}'s Appointment Management ---")
        print("1. View My Appointments")
        print("2. Schedule New Appointment")
        print("3. Reschedule Appointment")
        print("4. Complete Appointment")
        print("0. Back to Owner Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_appointments(current_user)
        elif choice == '2':
            create_appointment(current_user)
        elif choice == '3':
            reschedule_appointment(current_user)
        elif choice == '4':
            complete_appointment(current_user)
        elif choice == '0':
            return
        else:
            print("Invalid choice.")

def main():
    """Main function to run the Pet Clinic CLI application."""
    engine = create_engine('sqlite:///pet_clinic.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    global session # Make session globally available to blueprints
    session = Session()

    current_user = None
    try:
        while True:
            if not current_user:
                current_user = welcome_menu()
            else:
                owner_menu(current_user)
                current_user = None # Logout returns to welcome menu
    except KeyboardInterrupt:
        print("\nApplication interrupted. Exiting.")
    finally:
        session.close() # Ensure session is closed

if __name__ == '__main__':
    main()
```

---

## See Also

-   **[Python CLI Applications Guide](../guides/Python_CLI_Applications_Guide.md)** - For general CLI development concepts.
-   **[SQL and SQLAlchemy Cheat Sheet](../cheatsheets/SQL_and_SQLAlchemy_Cheat_Sheet.md)** - For core SQLAlchemy and SQL concepts.
-   **[OOP Cheat Sheet](../cheatsheets/OOP_Cheat_Sheet.md)** - For understanding the object-oriented design of the models.
-   **[Error Handling Cheat Sheet](../cheatsheets/Error_Handling_Cheat_Sheet.md)** - For strategies to make your CLI robust.
