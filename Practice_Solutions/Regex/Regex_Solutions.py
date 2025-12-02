import re

# ==========================================
# ASSIGNMENT 1: Basic Patterns
# ==========================================

text_sample = "Order #54321: Contact 555-0199 for assistance. Backup: 555-0100."

def regex_assignment_1():
    print("\n--- Regex Assignment 1 ---")
    
    # Task 1: Find the first word
    # \w+ matches one or more word characters
    first_word = re.search(r"\w+", text_sample)
    if first_word:
        print(f"First Word: {first_word.group()}")

    # Task 2: Find phone number (555-XXXX)
    # \d{3} matches 3 digits, - matches literal dash, \d{4} matches 4 digits
    phone = re.search(r"\d{3}-\d{4}", text_sample)
    if phone:
        print(f"Phone Found: {phone.group()}")

    # Task 3: Find all numbers
    all_nums = re.findall(r"\d+", text_sample)
    print(f"All Numbers: {all_nums}")

    # Task 4: Find 5-digit Order ID
    order_id = re.search(r"\b\d{5}\b", text_sample)
    if order_id:
        print(f"Order ID: {order_id.group()}")

# ==========================================
# ASSIGNMENT 2: Data Cleaning
# ==========================================

feedback_data = """
User:    Alice   
Phone: 555-1234
Message: Great   service!
"""

def regex_assignment_2():
    print("\n--- Regex Assignment 2 ---")
    
    # Task 1: Redact Phone Numbers
    # Replace pattern with "[REDACTED]"
    # Pattern: \d{3}-\d{4} (simple US format)
    redacted = re.sub(r"\d{3}-\d{4}", "[REDACTED]", feedback_data)
    print("Redacted Data:")
    print(redacted)

    # Task 2: Clean Extra Spaces
    # \s+ matches one or more whitespace characters
    # We replace multiple spaces with a single space, but be careful with newlines
    # Ideally, we might want to just clean distinct lines
    cleaned = re.sub(r"[ ]{2,}", " ", redacted) # Replace 2+ spaces with 1
    print("\nCleaned Spacing:")
    print(cleaned.strip())

if __name__ == "__main__":
    regex_assignment_1()
    regex_assignment_2()
