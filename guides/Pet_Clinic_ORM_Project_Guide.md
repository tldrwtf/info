# Pet Clinic ORM Project Guide

This guide details the implementation of a Veterinary Clinic management system using SQLAlchemy. It demonstrates how to handle **One-to-Many** relationships (Owners -> Pets) and **Complex Many-to-Many** relationships with extra data (Appointments between Pets and Vets).

## Project Overview

The system manages:
1.  **Owners**: Clients who own pets.
2.  **Pets**: Animals that belong to owners.
3.  **Vets**: Doctors who treat pets.
4.  **Appointments**: Scheduled visits connecting a Pet and a Vet at a specific time.

## 1. Data Models (`models.py`)

### Owner Model
Standard user model.
```python
class Owners(Base):
    __tablename__ = 'owners'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    # Relationship: One Owner has Many Pets
    pets: Mapped[list["Pets"]] = relationship("Pets", back_populates="owner")
```

### Pet Model
Belongs to an Owner.
```python
class Pets(Base):
    __tablename__ = 'pets'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('owners.id'))
    
    # Relationship: Many Pets belong to One Owner
    owner: Mapped["Owners"] = relationship("Owners", back_populates="pets")
    # Relationship: One Pet has Many Appointments
    appointments: Mapped[list["Appointments"]] = relationship("Appointments", back_populates="pet")
```

### Appointment Model (The Junction)
This acts as an Association Table between Pets and Vets but includes extra data: `appointment_date`, `notes`, and `status`.

```python
class Appointments(Base):
    __tablename__ = 'appointments'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey('pets.id'))
    veterinarian_id: Mapped[int] = mapped_column(Integer, ForeignKey('vets.id'))
    
    # Extra Data
    appointment_date: Mapped[date] = mapped_column(Date)
    notes: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20), default="Scheduled")
    
    # Relationships
    pet: Mapped["Pets"] = relationship("Pets", back_populates="appointments")
    vet: Mapped["Vets"] = relationship("Vets", back_populates="appointments")
```

---

## 2. Appointment Logic (`bp_appointments.py`)

Handling dates in CLI apps requires converting strings (input) to Python `date` objects (database).

### Creating an Appointment
```python
from datetime import datetime

date_format = "%Y-%m-%d"

def create_appointment(current_user):
    # 1. Select a Pet
    for pet in current_user.pets:
        print(pet.name)
    pet_name = input("Enter Pet Name: ")
    # Filter by name AND owner to prevent selecting someone else's pet
    pet = session.query(Pets).where(
        Pets.name.ilike(pet_name), 
        Pets.owner_id == current_user.id
    ).first()

    # 2. Select a Vet
    # ... (Display vets logic) ...
    vet = session.query(Vets).where(Vets.name.ilike(vet_name)).first()

    # 3. Get Date
    date_str = input("Date (YYYY-MM-DD): ")
    date_obj = datetime.strptime(date_str, date_format)

    # 4. Create Record
    new_apt = Appointments(
        pet_id=pet.id,
        veterinarian_id=vet.id,
        appointment_date=date_obj,
        notes="Annual Checkup"
    )
    session.add(new_apt)
    session.commit()
```

### Rescheduling (Updating)
```python
def reschedule_appointment(current_user):
    # ... Select appointment by ID ...
    appointment = session.get(Appointments, choice)
    
    # Security Check: Does this appointment belong to a pet owned by current_user?
    if appointment.pet.owner_id == current_user.id:
        new_date_str = input("New Date: ")
        appointment.appointment_date = datetime.strptime(new_date_str, date_format)
        session.commit()
```

---

## 3. CRUD Operations

### Create (Registering Owner)
```python
new_owner = Owners(name="John", email="john@example.com", ...)
session.add(new_owner)
session.commit()
```

### Read (Viewing Pets)
SQLAlchemy makes this easy via relationship attributes.
```python
def view_pets(current_user):
    # No need to write a complex SQL query manually
    for pet in current_user.pets:
        print(f"{pet.name} ({pet.species})")
```

### Delete (Removing a Pet)
```python
pet = session.query(Pets).filter_by(name="Buddy").first()
session.delete(pet)
session.commit()
# Note: If Cascade Delete is not set up in models, this might fail 
# if the pet has existing appointments.
```

---

## 4. Key Takeaways
1.  **Date Handling**: Always parse user input (`strptime`) before storing in a `Date` or `DateTime` column.
2.  **Security in CLI**: Even in a local CLI, ensure users can only modify *their own* data by checking `current_user.id` against the resource's owner ID.
3.  **Relationships**: Using `back_populates` allows us to navigate `owner.pets` or `pet.owner` seamlessly.

---

## See Also
- **[Interactive CLI Project Guide](Interactive_CLI_ORM_Project_Guide.md)**
- **[SQLAlchemy CRUD Guide](SQLAlchemy_CRUD_Guide.md)**