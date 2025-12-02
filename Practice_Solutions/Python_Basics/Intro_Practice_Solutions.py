# ==========================================
# INTRO TO PYTHON - CLASS CODE EXTENSIONS
# ==========================================

# --- Practice 1: Variables & Output ---
def practice_1_variables():
    print("\n--- Practice 1 ---")
    character_name = "John"
    character_age = "35" # Stored as string initially
    is_male = True
    
    print(f"There once was a man named {character_name},")
    print(f"he was {character_age} years old.")
    
    character_name = "Mike"
    print(f"He really liked the name {character_name},")
    print(f"but didn't like being {character_age}.")

# --- Practice 2: Input & Math ---
def practice_2_math():
    print("\n--- Practice 2 ---")
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    
    # Convert to float for decimal support
    result = float(num1) + float(num2)
    print(f"Result: {result}")

# --- Practice 3: Mad Libs (String Logic) ---
def practice_3_madlibs():
    print("\n--- Practice 3 (Mad Libs) ---")
    color = input("Enter a color: ")
    plural_noun = input("Enter a plural noun: ")
    celebrity = input("Enter a celebrity: ")
    
    print(f"Roses are {color}")
    print(f"{plural_noun} are blue")
    print(f"I love {celebrity}")

# --- Assignment 1 (Lists & Functions): Calculator ---
def calculator_logic():
    print("\n--- Calculator ---")
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, /, *): ")
    num2 = float(input("Enter second number: "))
    
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print("Invalid Operator")

if __name__ == "__main__":
    # practice_1_variables()
    # practice_2_math()
    # practice_3_madlibs()
    calculator_logic()
