# Regex Cheat Sheet (Python)

Regular Expressions (Regex) are a powerful tool for pattern matching and text manipulation. In Python, the `re` module provides full support for Perl-like regular expressions.

## Quick Reference

| Pattern | Description | Example | Matches |
| :--- | :--- | :--- | :--- |
| `.` | Any character (except newline) | `a.b` | "aab", "axb", "a@b" |
| `\d` | Digit (0-9) | `User\d` | "User1", "User9" |
| `\D` | Non-digit | `\D` | "A", "@", " " |
| `\w` | Word char (a-z, A-Z, 0-9, _) | `\w+` | "Hello_123" |
| `\W` | Non-word char | `\W` | " ", "!", "@" |
| `\s` | Whitespace (space, tab, newline) | `Hello\sWorld` | "Hello World" |
| `\S` | Non-whitespace | `\S+` | "Hello" |
| `^` | Start of string | `^Hello` | "Hello..." |
| `$` | End of string | `World$` | "...World" |
| `*` | 0 or more repetitions | `ab*` | "a", "ab", "abbb" |
| `+` | 1 or more repetitions | `ab+` | "ab", "abbb" |
| `?` | 0 or 1 repetition | `colou?r` | "color", "colour" |
| `{n}` | Exactly n repetitions | `\d{3}` | "123" |
| `{n,}` | n or more repetitions | `\d{2,}` | "12", "12345" |
| `{n,m}` | Between n and m repetitions | `\d{2,4}` | "12", "123", "1234" |
| `[]` | Character set (any one char) | `[aeiou]` | "a", "e" |
| `[^]` | Negated set (not these chars) | `[^0-9]` | Any non-digit |
| `|` | OR operator | `cat|dog` | "cat", "dog" |
| `()` | Grouping | `(ab)+` | "ab", "abab" |

---

## 1. The `re` Module

To use regex in Python, import the module:

```python
import re
```

### Common Functions

#### `re.search(pattern, text)`
Scans through `text` looking for the **first location** where the regex `pattern` produces a match. Returns a `Match` object or `None`.

```python
text = "The order ID is 12345 and the customer ID is 67890."
match = re.search(r"\d{5}", text)

if match:
    print(match.group()) # Output: 12345
    print(match.start()) # Output: 16
    print(match.end())   # Output: 21
    print(match.span())  # Output: (16, 21)
else:
    print("No match found")
```

#### `re.findall(pattern, text)`
Return **all non-overlapping matches** of pattern in string, as a list of strings.

```python
text = "The order ID is 12345 and the customer ID is 67890."
all_ids = re.findall(r"\d{5}", text)
print(all_ids) # Output: ['12345', '67890']
```

#### `re.sub(pattern, replacement, text)`
Return the string obtained by **replacing** the leftmost non-overlapping occurrences of `pattern` in `text` by the `replacement`.

```python
text = "Please call 555-0123 or 555-0199."
# Protect phone numbers
cleaned = re.sub(r"\d{3}-\d{4}", "[REDACTED]", text)
print(cleaned) # Output: Please call [REDACTED] or [REDACTED].

# Clean up extra spaces
messy_text = "This    is   a   messy    sentence."
clean_text = re.sub(r"\s+", " ", messy_text)
print(clean_text) # Output: This is a messy sentence.
```

#### `re.compile(pattern)`
Compile a regular expression pattern into a regex object, which can be used for matching using its `match()`, `search()` and other methods. Efficient if you use the same pattern multiple times.

```python
# Create a reusable pattern object
email_pattern = re.compile(r"[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,}")

text1 = "Contact: john@example.com"
text2 = "Support: support@site.org"

match1 = email_pattern.search(text1)
match2 = email_pattern.search(text2)

print(match1.group()) # john@example.com
print(match2.group()) # support@site.org
```

---

## 2. Character Sets & Ranges

Character sets `[]` match any single character inside the brackets.

*   `[abc]`: Matches 'a', 'b', or 'c'.
*   `[a-z]`: Matches any lowercase letter.
*   `[A-Z]`: Matches any uppercase letter.
*   `[0-9]`: Matches any digit (same as `\d`).
*   `[a-zA-Z0-9]`: Matches any alphanumeric character.
*   `[^abc]`: Matches anything **EXCEPT** 'a', 'b', or 'c' (Negation).

```python
text = "Product codes: A123, B456, c789"
# Match uppercase letter followed by 3 digits
codes = re.findall(r"[A-Z]\d{3}", text)
print(codes) # Output: ['A123', 'B456']
```

---

## 3. Quantifiers

Quantifiers specify how many times the preceding element should be repeated.

*   `*`: Zero or more times. `ab*` matches "a", "ab", "abb".
*   `+`: One or more times. `ab+` matches "ab", "abb".
*   `?`: Zero or one time. `colou?r` matches "color", "colour".
*   `{n}`: Exactly `n` times. `\d{3}` matches "123".
*   `{n,}`: `n` or more times. `\d{2,}` matches "12", "123", "1234"...
*   `{n,m}`: Between `n` and `m` times. `\d{2,4}` matches "12", "123", "1234".

```python
text = "IDs: 12, 123, 1234, 12345"
# Match IDs with 2 to 4 digits
short_ids = re.findall(r"\b\d{2,4}\b", text) # \b is word boundary
print(short_ids) # Output: ['12', '123', '1234']
```

---

## 4. Groups and Capturing

Parentheses `()` create groups.

### Capturing Groups
You can extract specific parts of a match using groups.

```python
text = "Date: 2023-12-25"
match = re.search(r"Date: (\d{4})-(\d{2})-(\d{2})", text)

if match:
    print("Full Match:", match.group(0)) # Date: 2023-12-25
    print("Year:", match.group(1))       # 2023
    print("Month:", match.group(2))      # 12
    print("Day:", match.group(3))        # 25
```

### Named Groups
Give groups a name for easier access: `(?P<name>...)`

```python
text = "Contact: john@example.com"
pattern = r"Contact: (?P<username>[\w.]+)@(?P<domain>[\w.]+)"
match = re.search(pattern, text)

if match:
    print(match.group("username")) # john
    print(match.group("domain"))   # example.com
```

### Backreferences in Substitutions
Use `\1`, `\2` or `\g<name>` to reference captured groups in a replacement string.

```python
date = "12/25/2023"
# Convert MM/DD/YYYY to YYYY-MM-DD
new_date = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\1-\2", date)
print(new_date) # Output: 2023-12-25

# Using named groups
new_date_named = re.sub(r"(?P<m>\d{2})/(?P<d>\d{2})/(?P<y>\d{4})", r"\g<y>-\g<m>-\g<d>", date)
print(new_date_named) # Output: 2023-12-25
```

---

## 5. Common Patterns (Cookbook)

### Email Address
```regex
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

### Phone Number (North America)
Matches formats like 123-456-7890, (123) 456-7890
```regex
\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}
```

### Date (YYYY-MM-DD)
```regex
\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])
```

### URL (Simple)
```regex
https?://(?:www\.)?[\w-]+\.[\w./]+
```

### Strong Password
(At least 8 chars, 1 uppercase, 1 lowercase, 1 number, 1 special char)
```regex
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$
```

---

## See Also

- [Python `re` module documentation](https://docs.python.org/3/library/re.html)
- [Regex101](https://regex101.com/) - Online regex tester and debugger