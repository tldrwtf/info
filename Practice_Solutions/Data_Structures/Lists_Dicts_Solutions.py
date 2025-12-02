# ==========================================
# TASK 3.1: Basic Functions
# ==========================================
def greet(name):
    print(f"Hello {name}")

def rectangle_area(length, width):
    return length * width

def add(num1, num2):
    return num1 + num2

# ==========================================
# TASK 3.2: Converter
# ==========================================
def celcius_to_farenheit(c):
    return (c * 9/5) + 32

# ==========================================
# TASK 3.3: List Statistics
# ==========================================
def list_statistics(numbers):
    if not numbers:
        return None
    return {
        "max": max(numbers),
        "min": min(numbers),
        "avg": sum(numbers) / len(numbers),
        "sum": sum(numbers)
    }

# ==========================================
# TASK 4.1: Student Dictionary
# ==========================================
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

def process_students():
    print("\n--- Names ---")
    for name in students:
        print(name)
    
    print("\n--- Scores ---")
    for score in students.values():
        print(score)
        
    print("\n--- Pairs ---")
    for name, score in students.items():
        print(f"{name}: {score}")
        
    print("\n--- Safe Check ---")
    print(f"David's score: {students.get('David', 'Not Found')}")

# ==========================================
# TASK 4.2: Inventory System (Nested Dicts)
# ==========================================
inventory = {
    "Electronics": {
        "Laptop": {"price": 1000, "stock": 5},
        "Mouse": {"price": 20, "stock": 50}
    },
    "Furniture": {
        "Chair": {"price": 100, "stock": 10}
    }
}

def manage_inventory():
    # 1. Access price
    print(f"Laptop Price: {inventory['Electronics']['Laptop']['price']}")
    
    # 2. Update stock
    inventory['Electronics']['Laptop']['stock'] -= 1
    
    # 3. Add Item
    inventory['Electronics']['Keyboard'] = {"price": 50, "stock": 20}
    
    # 4. Total Value
    total = 0
    for category in inventory.values():
        for item in category.values():
            total += item['price'] * item['stock']
    print(f"Total Inventory Value: ${total}")

# ==========================================
# TASK 4.3: Clean Usernames
# ==========================================
def clean_usernames(raw_list):
    """
    Takes raw strings, strips whitespace, converts to lowercase.
    """
    cleaned = []
    for name in raw_list:
        cleaned.append(name.strip().lower())
    return cleaned

# ==========================================
# TASK 4.4: Set Operations
# ==========================================
def set_hobbies():
    wilson = {"coding", "gaming", "reading"}
    friend = {"gaming", "hiking", "cooking"}

    print(f"Common: {wilson.intersection(friend)}")
    print(f"All Unique: {wilson.union(friend)}")
    print(f"Wilson Only: {wilson.difference(friend)}")

if __name__ == "__main__":
    print(list_statistics([10, 20, 30, 40]))
    process_students()
    manage_inventory()
    print(clean_usernames(["  Bob  ", "ALICE", "  charlie  "]))
    set_hobbies()
