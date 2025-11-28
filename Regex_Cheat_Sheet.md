# Regular Expressions (Regex) - Complete Reference Guide

## Quick Reference Card

| Pattern | Matches | Example |
|---------|---------|---------|
| `.` | Any character (except newline) | `a.c` matches "abc", "a2c" |
| `\d` | Digit [0-9] | `\d{3}` matches "123" |
| `\w` | Word character [a-zA-Z0-9_] | `\w+` matches "hello_123" |
| `\s` | Whitespace | `\s+` matches spaces/tabs |
| `^` | Start of string | `^Hello` matches start |
| `$` | End of string | `world$` matches end |
| `*` | 0 or more | `ab*` matches "a", "ab", "abb" |
| `+` | 1 or more | `ab+` matches "ab", "abb" |
| `?` | 0 or 1 | `ab?` matches "a", "ab" |
| `{n}` | Exactly n times | `\d{3}` matches "123" |
| `[abc]` | Any of a, b, or c | `[aeiou]` matches vowels |
| `[^abc]` | Not a, b, or c | `[^0-9]` matches non-digits |
| `(abc)` | Capture group | `(\d+)` captures digits |
| `a|b` | a or b | `cat|dog` matches either |

**Common Methods:** `re.search()`, `re.match()`, `re.findall()`, `re.sub()`, `re.split()`

## Table of Contents

- [Regex Basics](#regex-basics)
- [Metacharacters](#metacharacters)
- [Quantifiers](#quantifiers)
- [Character Sets](#character-sets)
- [Groups and Capturing](#groups-and-capturing)
- [Regex Methods](#regex-methods)
- [Practical Patterns](#practical-patterns)
- [Best Practices](#best-practices)

---

## Regex Basics

### What is Regex?

```python
# Regular Expression - Pattern matching for strings
# Used for:
# - Searching text
# - Validating input (email, phone, etc.)
# - Extracting data
# - Find and replace operations

import re  # Python's regex module
```

### Basic Pattern Matching

```python
import re

text = "I love Python programming"

# Search for a pattern
match = re.search("Python", text)
if match:
    print("Found:", match.group())  # "Python"
    print("Position:", match.start())  # 7
    print("Span:", match.span())  # (7, 13)

# Check if pattern exists
if re.search("Java", text):
    print("Found Java")
else:
    print("Java not found")
```

---

## Metacharacters

### Basic Metacharacters

```python
import re

text = "Contact us at info@company.com or call 555-0123"

# \d - Any digit (0-9)
digits = re.search(r"\d", text)
print(digits.group())  # "5" (first digit)

all_digits = re.findall(r"\d", text)
print(all_digits)  # ['5', '5', '5', '0', '1', '2', '3']

# \w - Any word character (letter, digit, underscore)
word = re.search(r"\w", text)
print(word.group())  # "C"

# \s - Any whitespace (space, tab, newline)
space = re.search(r"\s", text)
print(space.group())  # " "

# . - Any character except newline
any_char = re.search(r".", text)
print(any_char.group())  # "C"
```

### Negated Metacharacters

```python
import re

# \D - NOT a digit
# \W - NOT a word character
# \S - NOT whitespace

text = "User123 has 5 items"

# Find non-digits
non_digits = re.findall(r"\D", text)
# ['U', 's', 'e', 'r', ' ', 'h', 'a', 's', ' ', ' ', 'i', 't', 'e', 'm', 's']

# Find non-word characters
non_word = re.findall(r"\W", text)
# [' ', ' ', ' ']
```

### Anchors

```python
import re

# ^ - Start of string
# $ - End of string

text = "Hello World"

# Starts with "Hello"
if re.search(r"^Hello", text):
    print("Starts with Hello")  # Matches

# Ends with "World"
if re.search(r"World$", text):
    print("Ends with World")  # Matches

# Exact match
if re.search(r"^Hello World$", text):
    print("Exact match")  # Matches

# Word boundaries
text2 = "The cat catches the mouse"

# \b - Word boundary
words = re.findall(r"\bcat\b", text2)  # Matches "cat" but not "catches"
# ['cat']
```

---

## Quantifiers

### Basic Quantifiers

```python
import re

# + - One or more
# * - Zero or more
# ? - Zero or one (optional)
# {n} - Exactly n times
# {n,} - n or more times
# {n,m} - Between n and m times

text = "Contact us at info@company.com or call 555-0123"

# \d+ - One or more digits
numbers = re.findall(r"\d+", text)
print(numbers)  # ['555', '0123']

# \w+ - One or more word characters (whole words)
words = re.findall(r"\w+", text)
# ['Contact', 'us', 'at', 'info', 'company', 'com', 'or', 'call', '555', '0123']

# \d* - Zero or more digits
text2 = "abc 123 def"
results = re.findall(r"\d*", text2)
# ['', '', '', '', '123', '', '', '', '', '']

# \d? - Zero or one digit
results = re.findall(r"\d?", text2)
```

### Specific Repetition

```python
import re

# Phone number: xxx-xxxx
phone = "Call 555-1234"
match = re.search(r"\d{3}-\d{4}", phone)
print(match.group())  # "555-1234"

# ZIP code: 5 or 9 digits
text = "ZIP: 12345-6789"
zip_code = re.search(r"\d{5}(-\d{4})?", text)
print(zip_code.group())  # "12345-6789"

# Social Security: xxx-xx-xxxx
ssn = "SSN: 123-45-6789"
match = re.search(r"\d{3}-\d{2}-\d{4}", ssn)
print(match.group())  # "123-45-6789"
```

### Greedy vs Non-Greedy

```python
import re

html = "<div>Content</div><div>More</div>"

# Greedy (default) - matches as much as possible
greedy = re.search(r"<div>.*</div>", html)
print(greedy.group())  # "<div>Content</div><div>More</div>"

# Non-greedy - matches as little as possible
non_greedy = re.search(r"<div>.*?</div>", html)
print(non_greedy.group())  # "<div>Content</div>"
```

---

## Character Sets

### Basic Character Sets

```python
import re

# [abc] - Match any one character: a, b, or c
text = "bat cat hat rat"
matches = re.findall(r"[bcr]at", text)
print(matches)  # ['bat', 'cat', 'rat']

# [a-z] - Match any lowercase letter
lowercase = re.findall(r"[a-z]+", "Hello World 123")
print(lowercase)  # ['ello', 'orld']

# [A-Z] - Match any uppercase letter
uppercase = re.findall(r"[A-Z]+", "Hello World 123")
print(uppercase)  # ['H', 'W']

# [a-zA-Z] - Match any letter
letters = re.findall(r"[a-zA-Z]+", "Hello World 123")
print(letters)  # ['Hello', 'World']

# [0-9] - Match any digit (same as \d)
digits = re.findall(r"[0-9]+", "Hello World 123")
print(digits)  # ['123']
```

### Negated Character Sets

```python
import re

# [^abc] - Match anything EXCEPT a, b, or c

text = "bat cat hat mat"
not_bat_cat = re.findall(r"[^bc]at", text)
print(not_bat_cat)  # ['hat', 'mat']

# [^0-9] - Match anything that's NOT a digit
text2 = "User123"
non_digits = re.findall(r"[^0-9]+", text2)
print(non_digits)  # ['User']
```

### Special Character Sets

```python
import re

# Phone numbers with various formats
phone_data = "Call 555-123-4567 or (999)-888-7777"

# Match digits, hyphens, parentheses
phone_chars = re.findall(r"[0-9()-]+", phone_data)
print(phone_chars)  # ['555-123-4567', '(999)-888-7777']

# Email pattern
email = "contact@example.com"
# [A-z0-9._+-] for username, [A-z0-9.-] for domain
pattern = r"[A-z0-9._+-]+@[A-z0-9.-]+\.[A-z]{2,}"
match = re.search(pattern, email)
print(match.group())  # "contact@example.com"
```

---

## Groups and Capturing

### Basic Groups

```python
import re

# () - Create a capturing group

text = "Contact: John Doe <john@example.com>"

# Capture name and email separately
pattern = r"Contact: ([A-z ]+) <(\w+@\w+\.\w+)>"
match = re.search(pattern, text)

if match:
    print(match.group(0))  # Full match: "Contact: John Doe <john@example.com>"
    print(match.group(1))  # First group: "John Doe"
    print(match.group(2))  # Second group: "john@example.com"
```

### Named Groups

```python
import re

text = "Contact: John Doe <john@example.com>"

# (?P<name>pattern) - Named group
pattern = r"Contact: (?P<name>[A-z ]+) <(?P<email>\w+@\w+\.\w+)>"
match = re.search(pattern, text)

if match:
    print(match.group("name"))   # "John Doe"
    print(match.group("email"))  # "john@example.com"
    print(match.groupdict())     # {'name': 'John Doe', 'email': 'john@example.com'}
```

### Groups with Alternation

```python
import re

# | - OR operator

text = "I have a cat and a dog"

# Match cat or dog
pets = re.findall(r"cat|dog", text)
print(pets)  # ['cat', 'dog']

# Group with alternation
pattern = r"I have a (cat|dog|bird)"
match = re.search(pattern, text)
print(match.group(1))  # "cat"

# File extensions
files = "script.py config.json data.csv readme.md"
code_files = re.findall(r"\w+\.(py|js|java)", files)
print(code_files)  # ['py']
```

### Non-Capturing Groups

```python
import re

# (?:pattern) - Non-capturing group (doesn't create a group reference)

text = "http://example.com https://secure.com"

# Capture domain only, not protocol
pattern = r"(?:http|https)://(\w+\.\w+)"
matches = re.findall(pattern, text)
print(matches)  # ['example.com', 'secure.com']

# With capturing group, would return: [('http', 'example.com'), ...]
```

---

## Regex Methods

### re.search()

```python
import re

# Finds FIRST match in string

text = "I love Python programming. Python is awesome"

match = re.search("Python", text)
if match:
    print(match.group())  # "Python"
    print(match.start())  # 7
    print(match.end())    # 13

# Returns None if no match
result = re.search("Java", text)
print(result)  # None
```

### re.findall()

```python
import re

# Returns list of ALL matches

text = "Contact us at info@company.com or sales@company.com"

# Find all email addresses
emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)  # ['info@company.com', 'sales@company.com']

# Find all digits
text2 = "Order 123 costs $45.99"
numbers = re.findall(r"\d+", text2)
print(numbers)  # ['123', '45', '99']
```

### re.finditer()

```python
import re

# Returns iterator of match objects

text = "Python is great. Python is powerful."

for match in re.finditer("Python", text):
    print(f"Found '{match.group()}' at position {match.start()}")

# Output:
# Found 'Python' at position 0
# Found 'Python' at position 17
```

### re.sub()

```python
import re

# Replace matches with new text
# Syntax: re.sub(pattern, replacement, text)

# Replace all cats with dogs
text = "I love cats and cats love me"
new_text = re.sub("cats", "dogs", text)
print(new_text)  # "I love dogs and dogs love me"

# Replace first 6 digits with ******
phone = "Call me at: 887-889-1245"
protected = re.sub(r"\d{3}-\d{3}", "***-***", phone)
print(protected)  # "Call me at: ***-***-1245"

# Remove all digits
text2 = "User123 has 5 items"
no_digits = re.sub(r"\d", "", text2)
print(no_digits)  # "User has  items"

# Replace with groups
date = "07/22/2026"
new_format = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\1-\2", date)
print(new_format)  # "2026-07-22"
```

### re.split()

```python
import re

# Split string by pattern

# Split by spaces
text = "Hello    World   Python"
words = re.split(r"\s+", text)
print(words)  # ['Hello', 'World', 'Python']

# Split by comma or semicolon
data = "apple,banana;cherry,date"
items = re.split(r"[,;]", data)
print(items)  # ['apple', 'banana', 'cherry', 'date']

# Split by multiple delimiters
text2 = "one-two_three.four"
parts = re.split(r"[-_.]", text2)
print(parts)  # ['one', 'two', 'three', 'four']
```

### re.compile()

```python
import re

# Compile pattern for reuse (more efficient)

# Without compile (repeated compilation)
text1 = "Find numbers: 123"
text2 = "More numbers: 456"
nums1 = re.findall(r"\d+", text1)
nums2 = re.findall(r"\d+", text2)

# With compile (compile once, use many times)
number_pattern = re.compile(r"\d+")
nums1 = number_pattern.findall(text1)
nums2 = number_pattern.findall(text2)

# Use all methods with compiled pattern
email_pattern = re.compile(r"\w+@\w+\.\w+")
email_pattern.search("Email: test@example.com")
email_pattern.findall("a@b.com and c@d.com")
email_pattern.sub("[REDACTED]", "Email: test@example.com")
```

---

## Practical Patterns

### Email Validation

```python
import re

# Simple email pattern
email_pattern = r"\w+@\w+\.\w+"

# More comprehensive
email_pattern = r"[A-z0-9._+-]+@[A-z0-9.-]+\.[A-z]{2,}"

def validate_email(email):
    pattern = r"[A-z0-9._+-]+@[A-z0-9.-]+\.[A-z]{2,}"
    return bool(re.search(pattern, email))

print(validate_email("john@example.com"))  # True
print(validate_email("invalid.email"))     # False
```

### Phone Number Validation

```python
import re

# US phone: (xxx) xxx-xxxx or xxx-xxx-xxxx
phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"

def validate_phone(phone):
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    return bool(re.search(pattern, phone))

print(validate_phone("(555) 123-4567"))  # True
print(validate_phone("555-123-4567"))    # True
print(validate_phone("5551234567"))      # True
print(validate_phone("123-4567"))        # False
```

### URL Extraction

```python
import re

text = "Visit https://example.com or http://test.org for more info"

# Simple URL pattern
url_pattern = r"https?://\w+\.\w+"

urls = re.findall(url_pattern, text)
print(urls)  # ['https://example.com', 'http://test.org']

# More comprehensive
url_pattern = r"https?://[A-z0-9.-]+\.[A-z]{2,}(/[A-z0-9._~:/?#[\]@!$&'()*+,;=-]*)?"
```

### Password Validation

```python
import re

def validate_password(password):
    """
    Password must:
    - Be at least 8 characters
    - Contain uppercase and lowercase
    - Contain at least one digit
    - Contain at least one special character
    """
    if len(password) < 8:
        return False

    # Check for uppercase
    if not re.search(r"[A-Z]", password):
        return False

    # Check for lowercase
    if not re.search(r"[a-z]", password):
        return False

    # Check for digit
    if not re.search(r"\d", password):
        return False

    # Check for special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True

print(validate_password("Weak"))           # False
print(validate_password("Strong123!"))     # True
```

### Extract Data from Text

```python
import re

# Extract dates
text = "Meeting on 2024-01-15 and 2024-02-20"
dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)
print(dates)  # ['2024-01-15', '2024-02-20']

# Extract prices
text = "Items cost $19.99 and $5.50"
prices = re.findall(r"\$\d+\.\d{2}", text)
print(prices)  # ['$19.99', '$5.50']

# Extract hashtags
text = "Love #Python and #Coding #Developer"
hashtags = re.findall(r"#\w+", text)
print(hashtags)  # ['#Python', '#Coding', '#Developer']

# Extract mentions
text = "Thanks @john and @jane for the help"
mentions = re.findall(r"@\w+", text)
print(mentions)  # ['@john', '@@jane']
```

### Data Cleaning

```python
import re

# Remove extra whitespace
text = "Too    many     spaces"
cleaned = re.sub(r"\s+", " ", text)
print(cleaned)  # "Too many spaces"

# Remove phone numbers for privacy
text = "Call me at 555-0123 or email"
redacted = re.sub(r"\d{3}-\d{4}", "[PHONE REMOVED]", text)
print(redacted)  # "Call me at [PHONE REMOVED] or email"

# Remove HTML tags
html = "<p>Hello <b>World</b></p>"
clean = re.sub(r"<[^>]+>", "", html)
print(clean)  # "Hello World"

# Extract numbers from mixed text
text = "Price: $25.99 (was $30.00)"
numbers = re.findall(r"\d+\.?\d*", text)
print(numbers)  # ['25.99', '30.00']
```

---

## Best Practices

### Raw Strings

```python
import re

# Always use raw strings (r"") for regex patterns
# This prevents Python from interpreting backslashes

# Bad - Python interprets \d as escape sequence
pattern = "\d+"  # Actually "\d+" after Python processes it

# Good - Raw string, Python doesn't interpret backslashes
pattern = r"\d+"

# Example where it matters
# \b is backspace in regular string, word boundary in regex
text = "The cat"
re.search(r"\bcat\b", text)  # Works - word boundary
# re.search("\bcat\b", text)  # Doesn't work - backspace character
```

### Testing Patterns

```python
import re

def test_pattern(pattern, test_cases):
    """Test regex pattern against multiple inputs"""
    for text, expected in test_cases:
        result = bool(re.search(pattern, text))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} '{text}': {result}")

# Example: Email pattern
email_pattern = r"[A-z0-9._+-]+@[A-z0-9.-]+\.[A-z]{2,}"

test_cases = [
    ("john@example.com", True),
    ("invalid.email", False),
    ("test@test.co.uk", True),
    ("@example.com", False)
]

test_pattern(email_pattern, test_cases)
```

### Case-Insensitive Matching

```python
import re

text = "Python is awesome. PYTHON is powerful."

# Case-sensitive (default)
matches = re.findall(r"Python", text)
print(matches)  # ['Python']

# Case-insensitive with flag
matches = re.findall(r"python", text, re.IGNORECASE)
print(matches)  # ['Python', 'PYTHON']

# Or use re.I (short form)
matches = re.findall(r"python", text, re.I)
```

### Multiline Mode

```python
import re

text = """Line 1: Start here
Line 2: Middle content
Line 3: End here"""

# Without multiline - ^ and $ match string start/end
matches = re.findall(r"^Line", text)
print(matches)  # ['Line'] - only first line

# With multiline - ^ and $ match line start/end
matches = re.findall(r"^Line", text, re.MULTILINE)
print(matches)  # ['Line', 'Line', 'Line'] - all lines

# Or use re.M (short form)
matches = re.findall(r"^Line", text, re.M)
```

---

## Quick Reference Card

### Common Metacharacters

| Pattern | Matches                            |
| ------- | ---------------------------------- |
| `.`     | Any character except newline       |
| `\d`    | Digit (0-9)                        |
| `\D`    | Non-digit                          |
| `\w`    | Word character (a-z, A-Z, 0-9, \_) |
| `\W`    | Non-word character                 |
| `\s`    | Whitespace                         |
| `\S`    | Non-whitespace                     |
| `^`     | Start of string/line               |
| `$`     | End of string/line                 |
| `\b`    | Word boundary                      |

### Quantifiers

| Pattern | Matches               |
| ------- | --------------------- |
| `*`     | 0 or more             |
| `+`     | 1 or more             |
| `?`     | 0 or 1 (optional)     |
| `{n}`   | Exactly n times       |
| `{n,}`  | n or more times       |
| `{n,m}` | Between n and m times |

### Character Sets

| Pattern  | Matches              |
| -------- | -------------------- |
| `[abc]`  | a, b, or c           |
| `[a-z]`  | Any lowercase letter |
| `[A-Z]`  | Any uppercase letter |
| `[0-9]`  | Any digit            |
| `[^abc]` | NOT a, b, or c       |

### Methods

```python
import re

re.search(pattern, text)      # Find first match
re.findall(pattern, text)     # Find all matches (list)
re.finditer(pattern, text)    # Find all matches (iterator)
re.sub(pattern, repl, text)   # Replace matches
re.split(pattern, text)       # Split by pattern
re.compile(pattern)           # Compile for reuse
```

### Quick Patterns

```python
# Email
r"[A-z0-9._+-]+@[A-z0-9.-]+\.[A-z]{2,}"

# Phone (US)
r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"

# URL
r"https?://[A-z0-9.-]+\.[A-z]{2,}"

# Date (YYYY-MM-DD)
r"\d{4}-\d{2}-\d{2}"

# Time (HH:MM)
r"\d{2}:\d{2}"

# Hex color
r"#[0-9A-Fa-f]{6}"

# IP Address
r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
```

---

## See Also

- **[Python Basics Cheat Sheet](./Python_Basics_Cheat_Sheet.md)** - String operations
- **[File Operations Cheat Sheet](./File_Operations_Cheat_Sheet.md)** - Text file processing
- **[Standard Library Essentials Cheat Sheet](./Standard_Library_Essentials_Cheat_Sheet.md)** - re module details
- **[Error Handling Cheat Sheet](./Error_Handling_Cheat_Sheet.md)** - Handling regex errors

---