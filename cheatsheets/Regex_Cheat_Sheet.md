# Regular Expressions (Regex) - Complete Reference Guide

Regular Expressions, often shortened to Regex, are powerful tools for pattern matching within strings. They provide a concise and flexible way to identify and manipulate text based on specific patterns. This guide focuses on Python's `re` module.

## Quick Reference Card

| Pattern     | Matches                                  | Example (`re.search` or `re.findall`)     |
| :---------- | :--------------------------------------- | :---------------------------------------- |
| `.`         | Any character (except newline)           | `re.search(r"a.c", "abc")`                |
| `\d`        | Any digit [0-9]                          | `re.findall(r"\d+", "123 abc")`           |
| `\D`        | Any non-digit character                  | `re.findall(r"\D+", "123 abc")`           |
| `\w`        | Any word character [a-zA-Z0-9_]          | `re.findall(r"\w+", "hello_123")`         |
| `\W`        | Any non-word character                   | `re.findall(r"\W", "hello!")`             |
| `\s`        | Any whitespace character (space, tab, newline) | `re.findall(r"\s+", "a b")`             |
| `\S`        | Any non-whitespace character             | `re.findall(r"\S", "a b")`                |
| `^`         | Start of string/line                     | `re.search(r"^Hello", "Hello World")`     |
| `$`         | End of string/string                     | `re.search(r"World$", "Hello World")`     |
| `\b`        | Word boundary                            | `re.search(r"\bcat\b", "catapult")` (`None`) |
| `\B`        | Non-word boundary                        | `re.search(r"\Bcat\B", "catapult")`       |
| `*`         | 0 or more occurrences of the preceding   | `re.search(r"ab*", "a")`                 |
| `+`         | 1 or more occurrences of the preceding   | `re.search(r"ab+", "a")` (`None`)         |
| `?`         | 0 or 1 occurrence of the preceding       | `re.search(r"ab?", "ac")`                 |
| `{n}`       | Exactly `n` occurrences                  | `re.search(r"\d{3}", "12345")`            |
| `{n,}`      | `n` or more occurrences                  | `re.search(r"\d{2,}", "1")` (`None`)      |
| `{n,m}`     | Between `n` and `m` occurrences (inclusive) | `re.search(r"\d{2,4}", "12345")`          |
| `[]`        | Character set (match any one char inside)| `re.search(r"[aeiou]", "Python")`         |
| `[^]`       | Negated character set (match any one char NOT inside) | `re.search(r"[^0-9]", "123a")`      |
| `( )`       | Capturing group                          | `re.search(r"(\d+)", "ID: 123").group(1)` |
| `(?: )`     | Non-capturing group                      | `re.search(r"(?:\d+)", "ID: 123")`        |
| `(?P<name> )`| Named capturing group                    | `re.search(r"(?P<id>\d+)", "ID: 123").group("id")` |
| `|`         | OR (alternation)                         | `re.search(r"cat|dog", "my cat")`         |

--- 

## Table of Contents

- [1. Introduction to Regex](#1-introduction-to-regex)
- [2. Basic Pattern Matching](#2-basic-pattern-matching)
- [3. Metacharacters](#3-metacharacters)
- [4. Quantifiers](#4-quantifiers)
- [5. Character Sets](#5-character-sets)
- [6. Groups and Capturing](#6-groups-and-capturing)
- [7. Regex Methods](#7-regex-methods)
- [8. Practical Patterns](#8-practical-patterns)
- [9. Best Practices](#9-best-practices)

--- 

## 1. Introduction to Regex

Regular Expressions (Regex) are sequences of characters that define a search pattern. They are extremely powerful for tasks involving text manipulation, such as:
*   **Searching**: Finding specific patterns in text.
*   **Validation**: Checking if input strings conform to a certain format (e.g., email, phone numbers).
*   **Extraction**: Pulling out specific pieces of information from larger texts.
*   **Replacement**: Substituting parts of a string that match a pattern with new text.

In Python, the `re` module provides full support for regular expressions.

```python
import re # Import the regular expression module
```

## 2. Basic Pattern Matching

The most fundamental operations are `re.search()` and `re.findall()`.

### `re.search(pattern, string)`
Scans through string looking for the first location where the regular expression pattern produces a match, and returns a match object, or `None` if no match is found.

```python
import re

text = "I love Python programming. Python is awesome!"
pattern = "Python"

match = re.search(pattern, text)

if match:
    print(f"Found '{match.group()}'")     # Output: Found 'Python' (the matched substring)
    print(f"Starts at index: {match.start()}") # Output: Starts at index: 7
    print(f"Ends at index: {match.end()}")   # Output: Ends at index: 13 (exclusive)
    print(f"Span: {match.span()}")         # Output: Span: (7, 13) (start, end tuple)
else:
    print(f"Pattern '{pattern}' not found.")

# Example with no match
no_match = re.search("Java", text)
print(no_match) # Output: None
```

## 3. Metacharacters

Metacharacters are characters with a special meaning.

### Character Classes (Shorthand Metacharacters)

| Metacharacter | Description                          | Equivalent Character Set |
| :------------ | :----------------------------------- | :----------------------- |
| `\d`          | Matches any digit (0-9)              | `[0-9]`                  |
| `\D`          | Matches any non-digit character      | `[^0-9]`                 |
| `\w`          | Matches any word character (alphanumeric + underscore) | `[a-zA-Z0-9_]`           |
| `\W`          | Matches any non-word character       | `[^a-zA-Z0-9_]`          |
| `\s`          | Matches any whitespace character (space, tab, newline, etc.) | `[ \t\n\r\f\v]`          |
| `\S`          | Matches any non-whitespace character | `[^ \t\n\r\f\v]`         |
| `.`           | Matches any character except newline |                          |

```python
text = "The price is $12.99 and order ID is ABC_123."

# Find first digit
match_digit = re.search(r"\d", text)
print(f"First digit: {match_digit.group()}") # Output: First digit: 1

# Find first word character
match_word = re.search(r"\w", text)
print(f"First word character: {match_word.group()}") # Output: First word character: T

# Find first whitespace
match_space = re.search(r"\s", text)
print(f"First whitespace: '{match_space.group()}'") # Output: First whitespace: ' ' 

# Find any character (except newline)
match_any = re.search(r".", text)
print(f"Any character: '{match_any.group()}'") # Output: Any character: 'T'
```

### Anchors

Anchors do not match any character but assert a position.

| Metacharacter | Description                                          |
| :------------ | :--------------------------------------------------- |
| `^`           | Matches the beginning of the string (or line in `re.MULTILINE` mode). |
| `$`           | Matches the end of the string (or line in `re.MULTILINE` mode). |
| `\b`          | Matches an empty string at the beginning or end of a word (word boundary). |
| `\B`          | Matches an empty string NOT at the beginning or end of a word (non-word boundary). |

```python
text = "Hello World\nHello Python"

# ^ (start of string/line)
print(re.findall(r"^Hello", text))          # Output: ['Hello']
print(re.findall(r"^Hello", text, re.MULTILINE)) # Output: ['Hello', 'Hello']

# $ (end of string/line)
print(re.findall(r"World$", text))          # Output: ['World']
print(re.findall(r"Python$", text, re.MULTILINE)) # Output: ['Python']

# \b (word boundary)
text_boundary = "cat catches the cats"
print(re.findall(r"\bcat\b", text_boundary)) # Output: ['cat', 'cat']
print(re.findall(r"cat", text_boundary))     # Output: ['cat', 'cat', 'cat'] (matches in 'catches')
```

## 4. Quantifiers

Quantifiers specify how many occurrences of the preceding character, group, or character set must be present for a match.

| Quantifier | Description                                   |
| :--------- | :-------------------------------------------- |
| `*`        | Matches 0 or more occurrences (greedy)        |
| `+`        | Matches 1 or more occurrences (greedy)        |
| `?`        | Matches 0 or 1 occurrence (optional, greedy)  |
| `{n}`      | Matches exactly `n` occurrences               |
| `{n,}`     | Matches `n` or more occurrences               |
| `{n,m}`    | Matches between `n` and `m` occurrences (inclusive) |
| `*?`, `+?`, `??`, `{n,}?`, `{n,m}?` | Non-greedy versions of quantifiers |

```python
text = "123 abc 45 def 6"

# \d+ : One or more digits (greedy)
print(re.findall(r"\d+", text)) # Output: ['123', '45', '6']

# \w* : Zero or more word characters
print(re.findall(r"\w*", "hello world")) # Output: ['hello', '', 'world', '']

# \d{3} : Exactly three digits
phone_number = "My number is 123-456-7890"
print(re.search(r"\d{3}", phone_number).group()) # Output: 123

# \d{2,4} : Two to four digits
print(re.findall(r"\d{2,4}", "ID: 12, CODE: 12345, PIN: 9")) # Output: ['12', '1234', '9']
```

### Greedy vs. Non-Greedy (Lazy) Quantifiers

By default, quantifiers are greedy; they try to match the longest possible string. Adding `?` after a quantifier makes it non-greedy (or lazy), matching the shortest possible string.

```python
html = "<div>Content 1</div><div>Content 2</div>"

# Greedy: .* matches until the very last </div>
greedy_match = re.search(r"<div>.*</div>", html)
print(f"Greedy: {greedy_match.group()}")
# Output: Greedy: <div>Content 1</div><div>Content 2</div>

# Non-greedy: .*? matches until the first occurrence of </div>
non_greedy_match = re.search(r"<div>.*?</div>", html)
print(f"Non-Greedy: {non_greedy_match.group()}")
# Output: Non-Greedy: <div>Content 1</div>
```

## 5. Character Sets (`[]`)

Character sets allow you to match any *one* character from a specified set.

| Character Set | Description                               | Example        |
| :------------ | :---------------------------------------- | :----------------------- |
| `[abc]`       | Matches `a`, `b`, or `c`                  | `re.search(r"[aeiou]", "Python")` |
| `[a-z]`       | Matches any lowercase letter              | `re.findall(r"[a-z]+", "Hello")`   |
| `[A-Z]`       | Matches any uppercase letter              | `re.findall(r"[A-Z]+", "World")`   |
| `[0-9]`       | Matches any digit (same as `\d`)          | `re.findall(r"[0-9]+", "ID123")`   |
| `[a-zA-Z0-9]` | Matches any alphanumeric character        | `re.findall(r"[a-zA-Z0-9]+", "text_1")` |
| `[^abc]`      | Matches any character *except* `a`, `b`, or `c` (negation) | `re.findall(r"[^aeiou]", "Python")` |

```python
text = "apple, banana, cherry, date"

# Match 'at' preceded by 'b' or 'c' or 'r'
print(re.findall(r"[bcr]at", "bat cat hat rat")) # Output: ['bat', 'cat', 'rat']

# Find all vowels
print(re.findall(r"[aeiou]", text)) # Output: ['a', 'e', 'a', 'a', 'e', 'e']

# Find all non-digits
print(re.findall(r"[^0-9]", "Product ID: 12345")) # Output: ['P', 'r', 'o', 'd', 'u', 'c', 't', ' ', 'I', 'D', ': ', ' ']
```

## 6. Groups and Capturing (`()`)

Groups are used to treat multiple characters as a single unit. They also allow you to capture (extract) specific parts of a match.

### Basic Capturing Groups

Parentheses `()` create a capturing group, which can be referenced later.

```python
text = "Contact: John Doe <john.doe@example.com>"

# Capture name and email separately
pattern = r"Contact: ([A-Za-z ]+) <(\w+\.?\w*@\w+\.\w+)>"
match = re.search(pattern, text)

if match:
    print(f"Full match: {match.group(0)}") # Output: Full match: Contact: John Doe <john.doe@example.com>
    print(f"Name: {match.group(1)}")       # Output: Name: John Doe
    print(f"Email: {match.group(2)}")      # Output: Email: john.doe@example.com
```

### Named Capturing Groups

`(?P<name>pattern)` allows you to name a capturing group, making the extracted data easier to reference.

```python
text = "Order ID: 12345, Date: 2025-12-12"

pattern = r"Order ID: (?P<order_id>\d+), Date: (?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, text)

if match:
    print(f"Order ID: {match.group('order_id')}") # Output: Order ID: 12345
    print(f"Year: {match.group('year')}")         # Output: Year: 2025
    print(match.groupdict()) # Output: {'order_id': '12345', 'year': '2025', 'month': '12', 'day': '12'}
```

### Non-Capturing Groups

`(?:pattern)` matches a pattern but does not capture the matched text. Useful when you need to group for applying quantifiers or alternation but don't need to extract that specific part.

```python
text = "http://example.com https://secure.com"

# Match http or https, but only capture the domain
pattern = r"(?:http|https)://(\w+\.\w+)"
matches = re.findall(pattern, text)
print(matches) # Output: ['example.com', 'secure.com']
# If () was used instead of (?:), it would capture 'http'/'https' as well.
```

### Alternation (`|`)

The vertical bar `|` acts as an OR operator, allowing you to match one of several patterns.

```python
text = "I have a cat and a dog. Also a bird."

# Match 'cat' or 'dog' or 'bird'
pets = re.findall(r"cat|dog|bird", text)
print(pets) # Output: ['cat', 'dog', 'bird']

# Grouped alternation
# Matches "apple pie" or "banana split"
dessert_pattern = r"(apple pie|banana split)"
print(re.search(dessert_pattern, "I love apple pie!").group(1)) # Output: apple pie
```

## 7. Regex Methods

The `re` module provides several functions to work with compiled regular expressions or directly with string patterns.

### `re.findall(pattern, string, flags=0)`
Returns a list of all non-overlapping matches of `pattern` in `string`.

```python
text = "The quick brown fox jumps over the lazy dog."
words = re.findall(r"\b\w+\b", text) # Find all words
print(words) # Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

numbers_text = "Order 123 costs $45.99."
numbers = re.findall(r"\d+", numbers_text) # Find all sequences of digits
print(numbers) # Output: ['123', '45', '99']
```

### `re.sub(pattern, repl, string, count=0, flags=0)`
Replaces all (or `count` many) occurrences of the `pattern` in `string` with `repl`. `repl` can be a string or a function.

```python
# Replace all "cat" with "dog"
text = "I love cats, and cats love me."
new_text = re.sub(r"cat", "dog", text)
print(new_text) # Output: I love dogs, and dogs love me.

# Redact phone numbers
phone_data = "Contact at 555-123-4567 or 123-456-7890."
redacted_phones = re.sub(r"\d{3}-\d{3}-\d{4}", "[PHONE]", phone_data)
print(redacted_phones) # Output: Contact at [PHONE] or [PHONE].

# Rearrange date format using groups
date_text = "Date: 07/22/2025"
new_date_format = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\1-\2", date_text)
print(new_date_format) # Output: Date: 2025-07-22
```

### `re.split(pattern, string, maxsplit=0, flags=0)`
Splits `string` by the occurrences of `pattern`.

```python
text = "apple,banana;cherry,date"
items = re.split(r"[,;]", text) # Split by comma or semicolon
print(items) # Output: ['apple', 'banana', 'cherry', 'date']

text_multi_space = "One   Two \tThree\nFour"
words = re.split(r"\s+", text_multi_space) # Split by one or more whitespace
print(words) # Output: ['One', 'Two', 'Three', 'Four']
```

### `re.compile(pattern, flags=0)`
Compiles a regular expression pattern into a regex object. This can be used to perform matches more efficiently when the expression will be used many times.

```python
# Compile pattern once
email_pattern_compiled = re.compile(r"^[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,}$")

# Use the compiled pattern multiple times
text_email = "My email is test@example.com and his is user@domain.org"
matches = email_pattern_compiled.findall(text_email)
print(matches) # Output: ['test@example.com', 'user@domain.org']

# Can use search, sub, split methods on compiled objects too
match = email_pattern_compiled.search(text_email)
if match:
    print(f"First email: {match.group()}") # Output: First email: test@example.com
```

### `re.match(pattern, string, flags=0)`
Checks for a match only at the beginning of the string. Returns a match object if found, `None` otherwise. (Contrast with `re.search` which scans the entire string).

```python
text = "Python is awesome"

match_start = re.match(r"Python", text)
print(match_start.group()) # Output: Python

no_match_start = re.match(r"awesome", text)
print(no_match_start) # Output: None
```

## 8. Practical Patterns

### Email Validation

```python
def validate_email(email_address):
    # This pattern is more robust than simple \w+@\w+\.\w+
    pattern = r"^[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,}$"
    return bool(re.match(pattern, email_address)) # Use re.match for full string validation

print(validate_email("test@example.com")) # Output: True
print(validate_email("invalid-email"))    # Output: False
print(validate_email("user.name@sub.domain.co.uk")) # Output: True
```

### Phone Number Validation (US Format)

```python
def validate_us_phone(phone_number):
    # Matches (xxx) xxx-xxxx, xxx-xxx-xxxx, xxx.xxx.xxxx, xxx xxx xxxx
    pattern = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    return bool(re.match(pattern, phone_number))

print(validate_us_phone("(123) 456-7890")) # Output: True
print(validate_us_phone("123-456-7890"))   # Output: True
print(validate_us_phone("123.456.7890"))   # Output: True
print(validate_us_phone("123 456 7890"))   # Output: True
print(validate_us_phone("123-4567"))      # Output: False (not full format)
```

### URL Extraction

```python
text = "Visit https://www.example.com/page?id=123 or http://anothersite.org/index.html"

# More comprehensive URL pattern
url_pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[a-zA-Z0-9._~:/?#[\\]@!$&'()*+,;=%\-]*)?"
urls = re.findall(url_pattern, text)
print(urls)
# Output: ['https://www.example.com/page?id=123', 'http://anothersite.org/index.html']
```

### Password Strength Validation

```python
def validate_password_strength(password):
    # Minimum 8 characters, at least one uppercase, one lowercase, one digit, one special char
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r"\d", password):
        return "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."
    return "Password is strong."

print(validate_password_strength("MyP@ssw0rd")) # Output: Password is strong.
print(validate_password_strength("weakpass"))   # Output: Password must contain at least one uppercase letter.
```

### Data Cleaning (Removing extra spaces)

```python
text = "This   has   too    many      spaces."
# Replace one or more whitespace characters with a single space, then strip leading/trailing whitespace
cleaned_text = re.sub(r"\s+", " ", text).strip()
print(cleaned_text) # Output: This has too many spaces.
```

### Data Extraction (Hashtags and Mentions)

```python
text = "I love #Python and #coding with @gemini and @developer"
hashtags = re.findall(r"#(\w+)", text) # Captures the word after '#'
mentions = re.findall(r"@(\w+)", text) # Captures the word after '@'
print(f"Hashtags: {hashtags}") # Output: Hashtags: ['Python', 'coding']
print(f"Mentions: {mentions}") # Output: Mentions: ['gemini', 'developer']
```

## 9. Best Practices

### Use Raw Strings (`r"..."`)

Always use raw strings for regular expression patterns in Python. This prevents backslashes from being interpreted as escape sequences by Python, ensuring they are passed directly to the regex engine.

```python
# Bad Example: Python interprets '\b' as a backspace character
# import re
# print(re.search("word\b", "oneword")) # May lead to unexpected results

# Good Example: Raw string (r"...") passes '\b' directly to the regex engine as a word boundary
import re
print(re.search(r"\bword\b", "one word")) # Output: <re.Match object; span=(4, 8), match='word'>
```

### Compile Patterns for Reuse (`re.compile()`)

If you use a regex pattern multiple times in your code, compile it using `re.compile()` for better performance. This compiles the pattern into a regex object once, which can then be reused.

```python
import re

# Without compiling: The pattern is re-compiled each time
# for _ in range(1000):
#     re.search(r"some_complex_pattern", "target_text")

# With compiling: The pattern is compiled once, then reused
compiled_pattern = re.compile(r"some_complex_pattern")
# for _ in range(1000):
#     compiled_pattern.search("target_text")

# Compiled patterns can be used with all re module functions (search, findall, sub, etc.)
email_compiled = re.compile(r"^[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,}$")
match_email = email_compiled.search("info@example.com")
if match_email:
    print(f"Valid email found: {match_email.group()}")
```

### Use Flags for Modifiers

Use flags like `re.IGNORECASE` (or `re.I`) and `re.MULTILINE` (or `re.M`) to modify the matching behavior of your patterns.

```python
text_case = "Python is great. PYTHON is powerful."

# Case-sensitive (default)
matches_sensitive = re.findall(r"Python", text_case)
print(f"Case-sensitive: {matches_sensitive}") # Output: ['Python']

# Case-insensitive with flag
matches_insensitive = re.findall(r"python", text_case, re.IGNORECASE)
print(f"Case-insensitive: {matches_insensitive}") # Output: ['Python', 'PYTHON']

text_multi = "Line 1\nLine 2\nLine 3"

# Without MULTILINE: ^ and $ match string start/end
matches_start_string = re.findall(r"^Line", text_multi)
print(f"Matches start of string: {matches_start_string}") # Output: ['Line']

# With MULTILINE: ^ and $ match line start/end
matches_start_line = re.findall(r"^Line", text_multi, re.MULTILINE)
print(f"Matches start of line: {matches_start_line}") # Output: ['Line', 'Line', 'Line']
```

### Test Your Patterns

Thoroughly test your regex patterns with various inputs, including edge cases, to ensure they behave as expected.

```python
def test_regex_pattern(pattern, test_cases):
    """
    Tests a regex pattern against a list of test cases.
    Each test case is a tuple: (input_string, expected_boolean_result).
    """
    compiled_pattern = re.compile(pattern)
    print(f"\n--- Testing pattern: {pattern} ---")
    for input_string, expected in test_cases:
        match = bool(compiled_pattern.search(input_string))
        status = "PASS" if match == expected else "FAIL"
        print(f"  '{input_string}' -> Expected: {expected}, Got: {match} ({status})")

email_pattern_to_test = r"^[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,}$"
email_tests = [
    ("valid@example.com", True),
    ("user.name@sub.domain.co.uk", True),
    ("invalid-email", False),
    ("no@domain", False),
    ("user@.com", False)
]
test_regex_pattern(email_pattern_to_test, email_tests)
```

--- 

## See Also

-   **[Python Basics Cheat Sheet](../cheatsheets/Python_Basics_Cheat_Sheet.md)** - Essential Python string operations and text processing fundamentals.
-   **[Functional Programming Cheat Sheet](../cheatsheets/Functional_Programming_Cheat_Sheet.md)** - Concepts like `map` and `filter` that can be combined with regex for data transformation.
-   **[Error Handling Cheat Sheet](../cheatsheets/Error_Handling_Cheat_Sheet.md)** - Handling exceptions that might arise from malformed regex patterns or invalid input.
-   **[File Operations Cheat Sheet](../cheatsheets/File_Operations_Cheat_Sheet.md)** - Applying regex for searching and manipulating content within files.
-   **[Big O Notation Cheat Sheet](../cheatsheets/Big_O_Notation_Cheat_Sheet.md)** - Understanding the performance implications of complex regex patterns.
