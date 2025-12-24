# ==========================================
# CONTROL FLOW - PRACTICE SOLUTIONS
# ==========================================
"""
Python control flow exercises demonstrating conditionals, loops, and exception handling.

These solutions show best practices for:
- if/elif/else conditional chains
- while loops with break conditions
- try/except error handling
- Input validation and sanitization
- Accumulator patterns for data collection

Control flow determines the order in which code executes, allowing programs
to make decisions and repeat operations based on conditions.
"""

from datetime import datetime


# ==========================================
# TASK 1.1: Greeting
# ==========================================
def task_greeting() -> None:
    """
    Prompt for user's name and age, then print a personalized greeting.

    Demonstrates:
    - User input collection
    - Type conversion with error handling
    - Exception handling with try/except
    - f-string formatting

    The function wraps int() conversion in a try block because users might
    enter non-numeric values, which would raise a ValueError.

    Returns:
        None: Prints greeting or error message to console

    Example:
        >>> task_greeting()
        Enter your name: Alice
        Enter your age: 25
        Hello, Alice! You are 25 years old!

    Best Practice:
        Always validate user input, especially when converting types.
        Never trust that users will enter expected formats.
    """
    print("\n--- Task 1.1: Greeting ---")

    # Get name as string (no conversion needed)
    name = input("Enter your name: ")

    try:
        # Attempt to convert age input to integer
        # This will raise ValueError if user enters non-numeric text
        age = int(input("Enter your age: "))
        print(f"Hello, {name}! You are {age} years old!")
    except ValueError:
        # Catch ValueError and provide helpful error message
        # In production, you might loop and ask again instead
        print("Invalid age entered.")


# ==========================================
# TASK 1.2: Century Age Calculator
# ==========================================
def task_century_calculator() -> None:
    """
    Calculate what year the user will turn 100 years old.

    Demonstrates:
    - Using datetime module to get current year
    - Arithmetic with dates and ages
    - Exception handling for invalid input
    - Mathematical problem decomposition

    Algorithm:
        1. Get current year from system
        2. Calculate years remaining to reach 100
        3. Add remaining years to current year

    Returns:
        None: Prints the target year or error message

    Example:
        >>> task_century_calculator()
        Enter your age: 25
        You will turn 100 in the year 2099.

    Note:
        This assumes the user will live to 100. In production,
        you might handle negative ages or ages over 100 differently.
    """
    print("\n--- Task 1.2: Century Calculator ---")

    try:
        # Get user's current age
        age = int(input("Enter your age: "))

        # Get current year using datetime module
        # datetime.now() returns current date/time, .year extracts just the year
        current_year = datetime.now().year

        # Calculate how many more years until age 100
        years_to_go = 100 - age

        # Add those years to current year to get target year
        century_year = current_year + years_to_go

        print(f"You will turn 100 in the year {century_year}.")

    except ValueError:
        # Handle non-numeric input
        print("Please enter a valid number.")


# ==========================================
# TASK 1.3: Simple Conditional
# ==========================================
def task_weather_check() -> None:
    """
    Ask if it's raining and provide appropriate advice.

    Demonstrates:
    - Simple if/else conditional (binary choice)
    - String manipulation (.lower(), .strip())
    - Handling variations in user input

    The .lower() method converts input to lowercase so "Yes", "YES", and "yes"
    are all treated the same. The .strip() removes leading/trailing whitespace.

    Returns:
        None: Prints weather-appropriate advice

    Example:
        >>> task_weather_check()
        Is it raining? (yes/no): yes
        Take an umbrella

    Best Practice:
        When accepting yes/no input, normalize the string (lowercase, strip)
        to handle user input variations. Consider accepting 'y', 'n', '1', '0' too.
    """
    print("\n--- Task 1.3: Weather Check ---")

    # Get user input and normalize it (lowercase and remove extra spaces)
    # This makes the comparison more forgiving of input variations
    answer = input("Is it raining? (yes/no): ").lower().strip()

    # Simple binary conditional - only two possible paths
    if answer == 'yes':
        print("Take an umbrella")
    else:
        # 'else' catches everything that isn't 'yes' (including 'no', typos, etc.)
        print("Enjoy the sun")


# ==========================================
# TASK 1.4: Voting Eligibility
# ==========================================
def task_voting_check() -> None:
    """
    Determine if user is old enough to vote (18+ in most jurisdictions).

    Demonstrates:
    - Comparison operators (>=)
    - Threshold-based decision making
    - Input validation with exception handling

    The >= operator checks "greater than or equal to", which is appropriate
    for age thresholds (18 years old can vote, 17 cannot).

    Returns:
        None: Prints voting eligibility status

    Example:
        >>> task_voting_check()
        Enter your age: 21
        Can vote

    Note:
        Voting age varies by country. This uses 18 as the threshold,
        which is common in many countries including the US, UK, and Canada.
    """
    print("\n--- Task 1.4: Voting Check ---")

    try:
        # Get user's age as integer
        age = int(input("Enter your age: "))

        # Compare age against voting threshold
        # >= means "greater than or equal to"
        if age >= 18:
            print("Can vote")
        else:
            # Anyone under 18 cannot vote
            print("Cannot vote")

    except ValueError:
        # Handle non-numeric input
        print("Invalid input.")


# ==========================================
# TASK 1.5: Grade Converter
# ==========================================
def task_grade_converter() -> None:
    """
    Convert numerical score (0-100) to letter grade (A-F).

    Demonstrates:
    - if/elif/else chains for multiple conditions
    - Range checking with compound conditions (<=, <)
    - Order matters in conditional chains

    Grading scale:
        A: 90-100
        B: 80-89
        C: 70-79
        D: 60-69
        F: 0-59

    The order of conditions is important! We check highest grades first.
    Once a condition is True, Python skips the remaining elif/else blocks.

    Returns:
        None: Prints letter grade or error message

    Example:
        >>> task_grade_converter()
        Enter score (0-100): 85
        Grade: B

    Best Practice:
        Always validate range for scores. Consider using constants for
        grade thresholds to make the code more maintainable:
        GRADE_A_THRESHOLD = 90, etc.
    """
    print("\n--- Task 1.5: Grade Converter ---")

    try:
        # Get numerical score from user
        score = int(input("Enter score (0-100): "))

        # Check conditions from highest to lowest grade
        # Order matters! If we checked F first, everything would be F
        if 90 <= score <= 100:
            # Compound condition: score must be between 90 and 100 (inclusive)
            print("Grade: A")
        elif 80 <= score < 90:
            # 'elif' means "else if" - only checked if previous condition was False
            print("Grade: B")
        elif 70 <= score < 80:
            print("Grade: C")
        elif 60 <= score < 70:
            print("Grade: D")
        elif 0 <= score < 60:
            # Lowest passing grade
            print("Grade: F")
        else:
            # Catches negative numbers or scores > 100
            print("Invalid score range.")

    except ValueError:
        # Catches non-numeric input like "eighty-five"
        print("Please enter a number.")


# ==========================================
# TASK 1.6 & 2.3: Password Loop with Exception Handling
# ==========================================
def task_password_loop() -> None:
    """
    Implement a password prompt that loops until correct password is entered.

    Demonstrates:
    - Infinite while loops (while True)
    - Loop control with 'break' statement
    - Authentication pattern (simplified)

    This pattern is common in login systems: keep prompting until successful
    authentication. The 'break' statement exits the loop immediately.

    Returns:
        None: Prints access status and exits after correct password

    Example:
        >>> task_password_loop()
        Enter password (type 'secret' to exit): wrong
        Access Denied. Try again.
        Enter password (type 'secret' to exit): secret
        Access Granted!

    Security Note:
        This is a teaching example only! Real password systems should:
        1. Hash passwords (never store plain text)
        2. Limit login attempts to prevent brute force
        3. Use secure input methods (e.g., getpass module)
        4. Implement account lockout after failed attempts
    """
    print("\n--- Task 2.3: Password Loop ---")

    # Infinite loop - will run until 'break' is executed
    while True:
        # Prompt user for password
        password = input("Enter password (type 'secret' to exit): ")

        # Check if password matches (case-sensitive comparison)
        if password == "secret":
            print("Access Granted!")
            break  # Exit the loop immediately
        # If password doesn't match, print denial and loop continues
        print("Access Denied. Try again.")


# ==========================================
# TASK 2.4: Temperature Monitor
# ==========================================
def task_temp_monitor() -> None:
    """
    Collect temperature readings and calculate statistics.

    Demonstrates:
    - Accumulator pattern (building a list over time)
    - Loop with sentinel value ('done' to exit)
    - Data validation in loops
    - Aggregate functions (sum, min, max, len)
    - Formatted output with f-strings

    This pattern is common in data collection: gather values until user signals
    they're done, then compute statistics on the collected data.

    Returns:
        None: Prints statistics about collected temperature readings

    Example:
        >>> task_temp_monitor()
        Enter temp (or 'done'): 72.5
        Enter temp (or 'done'): 68.0
        Enter temp (or 'done'): 71.3
        Enter temp (or 'done'): done
        Count: 3
        Total: 211.8
        Avg: 70.60
        Min: 68.0
        Max: 72.5

    Best Practice:
        Using an accumulator (list) to collect data, then processing it after
        collection is complete, is more flexible than computing statistics
        incrementally. It allows for more complex analysis later.
    """
    print("\n--- Task 2.4: Temperature Monitor ---")

    # Initialize empty list to accumulate temperature readings
    # This is the "accumulator pattern" - start empty, add items over time
    readings = []

    # Loop until user types 'done'
    while True:
        # Get input from user
        val = input("Enter temp (or 'done'): ")

        # Check for sentinel value (exit condition)
        # .lower() allows 'Done', 'DONE', 'done' to all work
        if val.lower() == 'done':
            break  # Exit loop when user is finished

        # Try to convert input to float (handles both integers and decimals)
        try:
            readings.append(float(val))  # Add valid reading to list
        except ValueError:
            # If conversion fails (non-numeric input), show error but continue looping
            print("Invalid number.")

    # Process collected data (only if user entered at least one reading)
    if readings:
        # Built-in functions make statistics easy:
        # len() counts items, sum() adds them, min()/max() find extremes
        print(f"Count: {len(readings)}")
        print(f"Total: {sum(readings)}")

        # Calculate average - sum divided by count
        # :.2f formats to 2 decimal places
        print(f"Avg: {sum(readings)/len(readings):.2f}")

        print(f"Min: {min(readings)}")
        print(f"Max: {max(readings)}")
    else:
        # Handle case where user entered no valid readings
        print("No readings entered.")


# Script entry point
if __name__ == "__main__":
    """
    Test individual functions by uncommenting the ones you want to run.
    The __name__ == "__main__" pattern allows this file to be both:
    - Executed directly (functions run)
    - Imported as a module (functions available, but not auto-executed)
    """
    # Uncomment lines to run specific tasks
    # task_greeting()
    # task_century_calculator()
    # task_weather_check()
    # task_voting_check()
    # task_grade_converter()
    # task_password_loop()
    task_temp_monitor()
