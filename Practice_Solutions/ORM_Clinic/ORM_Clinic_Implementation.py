# ==========================================
# ORM CLINIC PROJECT - LOGIC IMPLEMENTATION
# ==========================================
# This file implements the logic described in the 'ORM-Clinic-Project-Assignment'
# comments found in bp_auth.py, bp_pets.py, etc.
# ==========================================

# --- MOCK DATABASE & MODELS ---
# Simulating the SQLAlchemy models and session for logic demonstration
class MockSession:
    def __init__(self):
        self.data = []
    def add(self, obj): self.data.append(obj)
    def commit(self): print(">> Database Committed")
    def query(self, model): return MockQuery(self.data, model)
    def delete(self, obj):
        if obj in self.data: self.data.remove(obj)

class MockQuery:
    def __init__(self, data, model):
        self.data = [d for d in data if isinstance(d, model)]
    def filter_by(self, **kwargs):
        key, val = list(kwargs.items())[0]
        self.data = [d for d in self.data if getattr(d, key) == val]
        return self
    def first(self): return self.data[0] if self.data else None
    def all(self): return self.data

class Owner:
    def __init__(self, name, email, password):
        self.name = name; self.email = email; self.password = password; self.pets = []

class Pet:
    def __init__(self, name, species, breed, age, owner_id):
        self.name = name; self.species = species; self.breed = breed; self.age = age; self.owner_id = owner_id

session = MockSession()

# --- AUTHENTICATION LOGIC (bp_auth.py) ---

def login():
    print("\n--- LOGIN ---")
    email = input("Email: ")
    password = input("Password: ")
    
    # check database for owner with the given email
    user = session.query(Owner).filter_by(email=email).first()
    
    if user and user.password == password:
        print(f"Welcome back, {user.name}!")
        return user
    else:
        print("Invalid credentials.")
        return None

def register():
    print("\n--- REGISTER ---")
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    
    # Check if exists
    if session.query(Owner).filter_by(email=email).first():
        print("Email already registered.")
        return None
        
    new_owner = Owner(name, email, password)
    session.add(new_owner)
    session.commit()
    print("Registration successful!")
    return new_owner

# --- PET MANAGEMENT LOGIC (bp_pets.py) ---

def create_pet(current_user):
    print("\n--- ADD PET ---")
    name = input("Pet Name: ")
    species = input("Species: ")
    breed = input("Breed: ")
    age = input("Age: ")
    
    new_pet = Pet(name, species, breed, age, owner_id=current_user.email) # Using email as ID mock
    # current_user.pets.append(new_pet) # In real ORM this happens via relation
    session.add(new_pet)
    session.commit()
    print(f"{name} added!")

def update_pet(current_user):
    print("\n--- UPDATE PET ---")
    pet_name = input("Enter name of pet to update: ")
    
    # Logic: Find pet in DB belonging to user
    # Mocking the query:
    pet = next((p for p in session.data if isinstance(p, Pet) and p.name == pet_name), None)
    
    if pet:
        new_age = input(f"Enter new age for {pet.name}: ")
        pet.age = new_age
        session.commit()
        print("Pet updated.")
    else:
        print("Pet not found.")

# --- MAIN MOCK LOOP ---
if __name__ == "__main__":
    # Seed
    session.add(Owner("Alice", "alice@test.com", "123456"))
    
    # Test Flow
    user = login() # Try alice@test.com / 123456
    if user:
        create_pet(user)
        update_pet(user)
