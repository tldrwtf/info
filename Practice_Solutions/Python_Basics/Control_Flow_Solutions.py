# ==========================================
# TASK 1.1: Greeting
# ==========================================
def task_greeting():
    print("\n--- Task 1.1: Greeting ---")
    name = input("Enter your name: ")
    try:
        age = int(input("Enter your age: "))
        print(f"Hello, {name}! You are {age} years old!")
    except ValueError:
        print("Invalid age entered.")

# ==========================================
# TASK 1.2: Century Age Calculator
# ==========================================
from datetime import datetime

def task_century_calculator():
    print("\n--- Task 1.2: Century Calculator ---")
    try:
        age = int(input("Enter your age: "))
        current_year = datetime.now().year
        years_to_go = 100 - age
        century_year = current_year + years_to_go
        print(f"You will turn 100 in the year {century_year}.")
    except ValueError:
        print("Please enter a valid number.")

# ==========================================
# TASK 1.3: Simple Conditional
# ==========================================
def task_weather_check():
    print("\n--- Task 1.3: Weather Check ---")
    answer = input("Is it raining? (yes/no): ").lower().strip()
    if answer == 'yes':
        print("Take an umbrella")
    else:
        print("Enjoy the sun")

# ==========================================
# TASK 1.4: Voting Eligibility
# ==========================================
def task_voting_check():
    print("\n--- Task 1.4: Voting Check ---")
    try:
        age = int(input("Enter your age: "))
        if age >= 18:
            print("Can vote")
        else:
            print("Cannot vote")
    except ValueError:
        print("Invalid input.")

# ==========================================
# TASK 1.5: Grade Converter
# ==========================================
def task_grade_converter():
    print("\n--- Task 1.5: Grade Converter ---")
    try:
        score = int(input("Enter score (0-100): "))
        if 90 <= score <= 100:
            print("Grade: A")
        elif 80 <= score < 90:
            print("Grade: B")
        elif 70 <= score < 80:
            print("Grade: C")
        elif 60 <= score < 70:
            print("Grade: D")
        elif 0 <= score < 60:
            print("Grade: F")
        else:
            print("Invalid score range.")
    except ValueError:
        print("Please enter a number.")

# ==========================================
# TASK 1.6 & 2.3: Password Loop with Exception Handling
# ==========================================
def task_password_loop():
    print("\n--- Task 2.3: Password Loop ---")
    while True:
        password = input("Enter password (type 'secret' to exit): ")
        if password == "secret":
            print("Access Granted!")
            break
        print("Access Denied. Try again.")

# ==========================================
# TASK 2.4: Temp Monitor
# ==========================================
def task_temp_monitor():
    print("\n--- Task 2.4: Temperature Monitor ---")
    readings = []
    while True:
        val = input("Enter temp (or 'done'): ")
        if val.lower() == 'done':
            break
        try:
            readings.append(float(val))
        except ValueError:
            print("Invalid number.")
    
    if readings:
        print(f"Count: {len(readings)}")
        print(f"Total: {sum(readings)}")
        print(f"Avg: {sum(readings)/len(readings):.2f}")
        print(f"Min: {min(readings)}")
        print(f"Max: {max(readings)}")
    else:
        print("No readings entered.")

if __name__ == "__main__":
    # Uncomment lines to run specific tasks
    # task_greeting()
    # task_century_calculator()
    # task_weather_check()
    # task_voting_check()
    # task_grade_converter()
    # task_password_loop()
    task_temp_monitor()
