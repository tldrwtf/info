# ==========================================
# INTRO TO PYTHON - CLASS CODE EXTENSIONS
# ==========================================
"""
Introductory Python exercises demonstrating variables, user input,
type conversion, string formatting, and basic control flow.

These examples showcase fundamental Python concepts that form the foundation
for more advanced programming patterns.
"""

# --- Practice 1: Variables & Output ---
def practice_1_variables() -> None:
    """
    Demonstrate variable assignment, reassignment, and f-string formatting.

    This function introduces core concepts:
    - Variable naming conventions (lowercase with underscores)
    - Dynamic typing (variables can be reassigned different values)
    - f-strings for string interpolation (Python 3.6+)
    - Boolean type for true/false values

    Returns:
        None: Prints output directly to console

    Example:
        >>> practice_1_variables()
        --- Practice 1 ---
        There once was a man named John,
        he was 35 years old.
        ...
    """
    print("\n--- Practice 1 ---")

    # Variable assignment - Python uses dynamic typing
    character_name = "John"
    character_age = "35"  # Stored as string initially (could be int, but showing flexibility)
    is_male = True  # Boolean type for binary values

    # f-strings (formatted string literals) allow embedding expressions inside {}
    print(f"There once was a man named {character_name},")
    print(f"he was {character_age} years old.")

    # Variables can be reassigned to new values at any time
    character_name = "Mike"
    print(f"He really liked the name {character_name},")
    print(f"but didn't like being {character_age}.")


# --- Practice 2: Input & Math ---
def practice_2_math() -> None:
    """
    Demonstrate user input, type conversion, and basic arithmetic.

    Key concepts:
    - input() always returns a string, requiring type conversion for math
    - float() converts strings to decimal numbers (handles both integers and decimals)
    - Type conversion is explicit in Python (no automatic coercion)

    Returns:
        None: Prints result to console

    Raises:
        ValueError: If user input cannot be converted to float

    Example:
        >>> practice_2_math()
        Enter a number: 5.5
        Enter another number: 2.3
        Result: 7.8

    Note:
        This is a basic example. Production code should include error handling
        for invalid input (non-numeric strings).
    """
    print("\n--- Practice 2 ---")

    # input() function reads user input as a string
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")

    # Convert strings to floats for mathematical operations
    # float() is preferred over int() because it handles both integers and decimals
    # Without conversion, num1 + num2 would concatenate strings instead of adding numbers
    result = float(num1) + float(num2)

    print(f"Result: {result}")


# --- Practice 3: Mad Libs (String Logic) ---
def practice_3_madlibs() -> None:
    """
    Create a Mad Libs game using string interpolation and user input.

    Mad Libs is a word game where players provide words that are inserted
    into a story template, often creating humorous results.

    Concepts demonstrated:
    - Multiple input() calls to gather data
    - Variable naming that describes content (semantic naming)
    - String formatting with f-strings
    - No type conversion needed (strings used as-is)

    Returns:
        None: Prints the completed story to console

    Example:
        >>> practice_3_madlibs()
        Enter a color: red
        Enter a plural noun: flowers
        Enter a celebrity: Taylor Swift
        Roses are red
        flowers are blue
        I love Taylor Swift
    """
    print("\n--- Practice 3 (Mad Libs) ---")

    # Collect user inputs - descriptive variable names make code self-documenting
    color = input("Enter a color: ")
    plural_noun = input("Enter a plural noun: ")
    celebrity = input("Enter a celebrity: ")

    # Build the story using f-strings to interpolate variables
    print(f"Roses are {color}")
    print(f"{plural_noun} are blue")
    print(f"I love {celebrity}")


# --- Assignment 1 (Lists & Functions): Calculator ---
def calculator_logic() -> None:
    """
    Implement a basic command-line calculator with four operations.

    This function combines several concepts:
    - User input with type conversion
    - Conditional logic (if/elif/else)
    - Basic arithmetic operations
    - Input validation

    Supported operations:
        + : Addition
        - : Subtraction
        / : Division
        * : Multiplication

    Returns:
        None: Prints calculation result to console

    Raises:
        ValueError: If numeric inputs cannot be converted to float
        ZeroDivisionError: If division by zero is attempted (not currently handled)

    Example:
        >>> calculator_logic()
        Enter first number: 10
        Enter operator (+, -, /, *): +
        Enter second number: 5
        15.0

    Best Practices:
        - In production code, this should:
          1. Handle ZeroDivisionError for division
          2. Use try-except blocks for input validation
          3. Return values instead of printing directly (better for testing)
          4. Consider using a dictionary to map operators to functions
    """
    print("\n--- Calculator ---")

    # Get numeric inputs - float() allows decimal numbers
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, /, *): ")
    num2 = float(input("Enter second number: "))

    # Use if/elif chain to determine which operation to perform
    # Each condition is checked in order until one matches
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        # Note: This will raise ZeroDivisionError if num2 is 0
        # Better practice: if num2 == 0: print("Cannot divide by zero")
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    else:
        # Fallback for invalid operators
        print("Invalid Operator")


# Script entry point - only runs when file is executed directly (not imported)
if __name__ == "__main__":
    """
    The __name__ == "__main__" idiom is a Python convention that allows
    a script to be both:
    1. Executable as a standalone program
    2. Importable as a module without running the code

    When Python runs a file directly, it sets __name__ to "__main__"
    When the file is imported, __name__ is set to the module name
    """
    # Uncomment the function you want to test:
    # practice_1_variables()
    # practice_2_math()
    # practice_3_madlibs()
    calculator_logic()
