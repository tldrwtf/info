# Python Standard Library Essentials Cheat Sheet

## Quick Reference Card

| Module | Purpose | Key Functions/Classes |
|--------|---------|----------------------|
| **collections** | Specialized data structures | Counter, defaultdict, deque, namedtuple |
| **datetime** | Date and time handling | date, time, datetime, timedelta |
| **os** | Operating system interface | getcwd, listdir, mkdir, remove |
| **sys** | System parameters | argv, exit, path, version |
| **json** | JSON encoding/decoding | dump, load, dumps, loads |
| **math** | Mathematical functions | sqrt, ceil, floor, pi, e |
| **random** | Random number generation | random, randint, choice, shuffle |
| **argparse** | Command-line arguments | ArgumentParser, add_argument |
| **pathlib** | Object-oriented paths | Path, exists, mkdir, glob |
| **itertools** | Iterator functions | chain, cycle, combinations, permutations |

## Table of Contents
1. [collections Module](#collections-module)
2. [datetime Module](#datetime-module)
3. [os and sys Modules](#os-and-sys-modules)
4. [json Module](#json-module)
5. [math and random Modules](#math-and-random-modules)
6. [argparse Module](#argparse-module)
7. [Other Useful Modules](#other-useful-modules)
8. [Best Practices](#best-practices)

---

## collections Module

### Counter

```python
from collections import Counter

# Count elements in a list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counter = Counter(numbers)
print(counter)  # Counter({4: 4, 3: 3, 2: 2, 1: 1})

# Count characters in string
text = 'hello world'
counter = Counter(text)
print(counter)  # Counter({'l': 3, 'o': 2, 'h': 1, ...})

# Most common elements
print(counter.most_common(3))  # [('l', 3), ('o', 2), ('h', 1)]

# Counter arithmetic
c1 = Counter(['a', 'b', 'c', 'a'])
c2 = Counter(['a', 'b', 'd'])
print(c1 + c2)  # Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
print(c1 - c2)  # Counter({'a': 1, 'c': 1})

# Word frequency
words = 'the quick brown fox jumps over the lazy dog'.split()
word_freq = Counter(words)
print(word_freq.most_common(3))  # [('the', 2), ('quick', 1), ('brown', 1)]
```

### defaultdict

```python
from collections import defaultdict

# Dictionary with default value
dd = defaultdict(int)  # Default value: 0
dd['a'] += 1  # No KeyError, starts at 0
print(dd['a'])  # 1
print(dd['b'])  # 0 (default)

# Group items
data = [('fruit', 'apple'), ('vegetable', 'carrot'), ('fruit', 'banana')]
grouped = defaultdict(list)
for category, item in data:
    grouped[category].append(item)
print(dict(grouped))
# {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']}

# Count occurrences
words = ['apple', 'banana', 'apple', 'cherry']
counts = defaultdict(int)
for word in words:
    counts[word] += 1
print(dict(counts))  # {'apple': 2, 'banana': 1, 'cherry': 1}

# Nested defaultdict
nested = defaultdict(lambda: defaultdict(int))
nested['user1']['score'] += 10
nested['user1']['score'] += 5
print(dict(nested))  # {'user1': {'score': 15}}
```

### deque (Double-ended Queue)

```python
from collections import deque

# Create deque
d = deque([1, 2, 3])

# Add to ends
d.append(4)       # Add to right: [1, 2, 3, 4]
d.appendleft(0)   # Add to left: [0, 1, 2, 3, 4]

# Remove from ends
d.pop()           # Remove from right: [0, 1, 2, 3]
d.popleft()       # Remove from left: [1, 2, 3]

# Rotate
d = deque([1, 2, 3, 4, 5])
d.rotate(2)       # [4, 5, 1, 2, 3]
d.rotate(-1)      # [5, 1, 2, 3, 4]

# Max length (circular buffer)
d = deque(maxlen=3)
d.extend([1, 2, 3])  # [1, 2, 3]
d.append(4)          # [2, 3, 4] (1 dropped)

# Use as queue (FIFO)
queue = deque()
queue.append('first')
queue.append('second')
print(queue.popleft())  # 'first'

# Use as stack (LIFO)
stack = deque()
stack.append('first')
stack.append('second')
print(stack.pop())  # 'second'
```

### namedtuple

```python
from collections import namedtuple

# Create named tuple type
Point = namedtuple('Point', ['x', 'y'])

# Create instance
p = Point(11, 22)
print(p.x, p.y)  # 11 22

# Access like tuple
print(p[0], p[1])  # 11 22

# Unpack
x, y = p

# Named tuples are immutable
# p.x = 33  # AttributeError

# Use for structured data
Person = namedtuple('Person', ['name', 'age', 'city'])
alice = Person('Alice', 30, 'NYC')
print(alice.name)  # Alice
print(alice.age)   # 30

# Convert to dict
print(alice._asdict())
# {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# Replace values (creates new tuple)
bob = alice._replace(name='Bob', age=25)
print(bob)  # Person(name='Bob', age=25, city='NYC')
```

### OrderedDict

```python
from collections import OrderedDict

# Maintains insertion order (Python 3.7+ dicts do this too)
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3

print(list(od.keys()))  # ['first', 'second', 'third']

# Move to end
od.move_to_end('first')
print(list(od.keys()))  # ['second', 'third', 'first']

# Move to beginning
od.move_to_end('first', last=False)
print(list(od.keys()))  # ['first', 'second', 'third']

# Pop last item
key, value = od.popitem()
print(key, value)  # 'third' 3
```

---

## datetime Module

### Date and Time Objects

```python
from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print(now)  # 2024-01-15 14:30:45.123456

# Current date
today = date.today()
print(today)  # 2024-01-15

# Create specific datetime
dt = datetime(2024, 12, 25, 10, 30, 0)
print(dt)  # 2024-12-25 10:30:00

# Create specific date
d = date(2024, 12, 25)
print(d)  # 2024-12-25

# Create specific time
t = time(14, 30, 0)
print(t)  # 14:30:00

# Access components
print(now.year)    # 2024
print(now.month)   # 1
print(now.day)     # 15
print(now.hour)    # 14
print(now.minute)  # 30
print(now.second)  # 45
```

### Formatting Dates

```python
from datetime import datetime

now = datetime.now()

# Format as string (strftime)
formatted = now.strftime('%Y-%m-%d')
print(formatted)  # '2024-01-15'

formatted = now.strftime('%B %d, %Y')
print(formatted)  # 'January 15, 2024'

formatted = now.strftime('%I:%M %p')
print(formatted)  # '02:30 PM'

# Common format codes:
# %Y - Year (4 digits)        %y - Year (2 digits)
# %m - Month (01-12)          %B - Month name
# %d - Day (01-31)            %A - Weekday name
# %H - Hour (00-23)           %I - Hour (01-12)
# %M - Minute                 %S - Second
# %p - AM/PM

# Parse string to datetime (strptime)
date_string = '2024-01-15'
dt = datetime.strptime(date_string, '%Y-%m-%d')
print(dt)  # 2024-01-15 00:00:00

date_string = 'January 15, 2024'
dt = datetime.strptime(date_string, '%B %d, %Y')
print(dt)  # 2024-01-15 00:00:00
```

### Time Deltas

```python
from datetime import datetime, timedelta

# Create timedelta
one_day = timedelta(days=1)
one_week = timedelta(weeks=1)
two_hours = timedelta(hours=2)

# Date arithmetic
today = datetime.now()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
next_week = today + timedelta(weeks=1)

print(f'Today: {today.date()}')
print(f'Tomorrow: {tomorrow.date()}')
print(f'Yesterday: {yesterday.date()}')

# Calculate difference
start = datetime(2024, 1, 1)
end = datetime(2024, 12, 31)
difference = end - start
print(f'Days: {difference.days}')  # 365
print(f'Total seconds: {difference.total_seconds()}')

# Due date calculation
task_created = datetime.now()
due_date = task_created + timedelta(days=7)
print(f'Due: {due_date.strftime("%Y-%m-%d")}')

# Check if date passed
deadline = datetime(2024, 1, 1)
if datetime.now() > deadline:
    print('Deadline passed')
```

### Working with Timestamps

```python
from datetime import datetime

# Get current timestamp
timestamp = datetime.now().timestamp()
print(timestamp)  # 1705329045.123456

# Convert timestamp to datetime
dt = datetime.fromtimestamp(timestamp)
print(dt)

# ISO format
iso_string = datetime.now().isoformat()
print(iso_string)  # '2024-01-15T14:30:45.123456'

# Parse ISO format
dt = datetime.fromisoformat(iso_string)
print(dt)
```

---

## os and sys Modules

### os Module - File System

```python
import os

# Current working directory
cwd = os.getcwd()
print(cwd)  # '/path/to/directory'

# Change directory
os.chdir('/tmp')

# List directory contents
files = os.listdir('.')
print(files)  # ['file1.txt', 'file2.txt', ...]

# Check if path exists
if os.path.exists('file.txt'):
    print('File exists')

# Check if file or directory
os.path.isfile('file.txt')  # True if file
os.path.isdir('folder')     # True if directory

# Create directory
os.mkdir('new_folder')
os.makedirs('path/to/nested/folder')  # Create nested directories

# Remove file or directory
os.remove('file.txt')      # Remove file
os.rmdir('folder')         # Remove empty directory
os.removedirs('path/to')   # Remove nested empty directories

# Rename
os.rename('old_name.txt', 'new_name.txt')

# Get file size
size = os.path.getsize('file.txt')
print(f'Size: {size} bytes')

# Join paths (OS-independent)
path = os.path.join('folder', 'subfolder', 'file.txt')
print(path)  # 'folder/subfolder/file.txt' (or '\' on Windows)

# Split path
directory, filename = os.path.split('/path/to/file.txt')
print(directory)  # '/path/to'
print(filename)   # 'file.txt'

# Get file extension
name, ext = os.path.splitext('file.txt')
print(name)  # 'file'
print(ext)   # '.txt'

# Absolute path
abs_path = os.path.abspath('file.txt')
print(abs_path)
```

### os Module - Environment

```python
import os

# Environment variables
home = os.environ.get('HOME')
path = os.environ.get('PATH')

# Set environment variable
os.environ['MY_VAR'] = 'value'

# Get all environment variables
for key, value in os.environ.items():
    print(f'{key} = {value}')

# Execute system command
os.system('ls -l')  # Unix
os.system('dir')    # Windows
```

### sys Module

```python
import sys

# Command-line arguments
print(sys.argv)  # ['script.py', 'arg1', 'arg2', ...]

# Python version
print(sys.version)
print(sys.version_info)

# Platform
print(sys.platform)  # 'linux', 'darwin', 'win32', etc.

# Exit program
sys.exit(0)  # Exit with status code

# Standard streams
sys.stdout.write('Hello\n')  # Standard output
sys.stderr.write('Error\n')  # Standard error

# Module search path
print(sys.path)  # List of directories Python searches for modules

# Maximum integer
print(sys.maxsize)

# Get object size
import sys
x = [1, 2, 3]
print(sys.getsizeof(x))  # Size in bytes
```

---

## json Module

### JSON Basics

```python
import json

# Python to JSON string
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'NYC',
    'hobbies': ['reading', 'coding']
}

json_string = json.dumps(data)
print(json_string)
# '{"name": "Alice", "age": 30, "city": "NYC", "hobbies": ["reading", "coding"]}'

# JSON string to Python
json_string = '{"name": "Bob", "age": 25}'
data = json.loads(json_string)
print(data['name'])  # 'Bob'

# Pretty print
json_string = json.dumps(data, indent=4)
print(json_string)
# {
#     "name": "Alice",
#     "age": 30,
#     ...
# }

# Sort keys
json_string = json.dumps(data, indent=4, sort_keys=True)
```

### JSON Files

```python
import json

# Write to file
data = {'users': ['Alice', 'Bob', 'Charlie']}
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# Read from file
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)

# Handle errors
try:
    with open('invalid.json', 'r') as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    print(f'Invalid JSON: {e}')
except FileNotFoundError:
    print('File not found')
```

---

## math and random Modules

### math Module

```python
import math

# Constants
print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045

# Rounding
print(math.ceil(4.2))   # 5 (round up)
print(math.floor(4.8))  # 4 (round down)
print(math.trunc(4.8))  # 4 (remove decimal)

# Powers and roots
print(math.sqrt(16))    # 4.0
print(math.pow(2, 3))   # 8.0
print(math.exp(2))      # e^2 = 7.389...

# Logarithms
print(math.log(10))      # Natural log
print(math.log10(100))   # 2.0 (base 10)
print(math.log2(8))      # 3.0 (base 2)

# Trigonometry (radians)
print(math.sin(math.pi / 2))  # 1.0
print(math.cos(0))             # 1.0
print(math.tan(math.pi / 4))   # 1.0

# Convert degrees/radians
print(math.degrees(math.pi))   # 180.0
print(math.radians(180))       # 3.14159...

# Factorial
print(math.factorial(5))  # 120

# Greatest common divisor
print(math.gcd(48, 18))  # 6

# Check special values
print(math.isnan(float('nan')))  # True
print(math.isinf(float('inf')))  # True
```

### random Module

```python
import random

# Random float between 0 and 1
print(random.random())  # 0.7234...

# Random integer
print(random.randint(1, 10))  # 1-10 inclusive

# Random float in range
print(random.uniform(1.0, 10.0))  # 5.432...

# Random choice from list
colors = ['red', 'green', 'blue']
print(random.choice(colors))

# Multiple random choices (with replacement)
print(random.choices(colors, k=3))
# ['red', 'blue', 'red']

# Random sample (without replacement)
numbers = list(range(1, 50))
lottery = random.sample(numbers, 6)
print(lottery)  # [23, 7, 42, 15, 33, 8]

# Shuffle list in place
cards = ['A', 'K', 'Q', 'J', '10']
random.shuffle(cards)
print(cards)  # ['Q', '10', 'A', 'K', 'J']

# Set seed for reproducibility
random.seed(42)
print(random.random())  # Always same value

# Random with weights
outcomes = ['win', 'lose', 'draw']
weights = [10, 5, 1]  # Win is 10x more likely than draw
result = random.choices(outcomes, weights=weights, k=1)[0]
```

---

## argparse Module

### Basic Command-Line Arguments

```python
import argparse

# Create parser
parser = argparse.ArgumentParser(description='Process some data')

# Add arguments
parser.add_argument('input', help='Input file path')
parser.add_argument('output', help='Output file path')
parser.add_argument('--verbose', '-v', action='store_true',
                    help='Verbose output')
parser.add_argument('--count', '-c', type=int, default=1,
                    help='Number of iterations')

# Parse arguments
args = parser.parse_args()

# Access arguments
print(f'Input: {args.input}')
print(f'Output: {args.output}')
if args.verbose:
    print('Verbose mode enabled')
print(f'Count: {args.count}')

# Usage:
# python script.py input.txt output.txt
# python script.py input.txt output.txt --verbose --count 5
```

### Advanced argparse

```python
import argparse

parser = argparse.ArgumentParser(
    prog='MyProgram',
    description='Program description',
    epilog='Thanks for using %(prog)s!'
)

# Positional argument
parser.add_argument('filename', help='File to process')

# Optional argument with short and long form
parser.add_argument('-o', '--output', help='Output file')

# Flag (boolean)
parser.add_argument('-v', '--verbose', action='store_true')

# Integer argument with default
parser.add_argument('-n', '--number', type=int, default=10)

# Choice from list
parser.add_argument('--format', choices=['json', 'xml', 'csv'],
                    default='json')

# Multiple values
parser.add_argument('--values', nargs='+', type=int,
                    help='One or more integers')

# Optional argument with required flag
parser.add_argument('--config', required=True,
                    help='Configuration file (required)')

args = parser.parse_args()
```

---

## Other Useful Modules

### string Module

```python
import string

# Constants
print(string.ascii_lowercase)  # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase)  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.digits)           # '0123456789'
print(string.punctuation)      # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# Template strings
from string import Template
template = Template('Hello, $name! You are $age years old.')
result = template.substitute(name='Alice', age=30)
print(result)  # 'Hello, Alice! You are 30 years old.'
```

### copy Module

```python
import copy

# Shallow copy
original = [1, 2, [3, 4]]
shallow = copy.copy(original)
shallow[2][0] = 99
print(original)  # [1, 2, [99, 4]] - Inner list affected!

# Deep copy
original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)
deep[2][0] = 99
print(original)  # [1, 2, [3, 4]] - Original unchanged
```

### re Module (Regex)

```python
import re

# Find pattern
text = 'My email is alice@example.com'
match = re.search(r'\w+@\w+\.\w+', text)
if match:
    print(match.group())  # 'alice@example.com'

# Find all matches
text = 'Emails: alice@example.com, bob@test.org'
emails = re.findall(r'\w+@\w+\.\w+', text)
print(emails)  # ['alice@example.com', 'bob@test.org']

# Replace
text = 'Phone: 123-456-7890'
clean = re.sub(r'\D', '', text)  # Remove non-digits
print(clean)  # '1234567890'

# Split
text = 'one,two;three four'
parts = re.split(r'[,;\s]+', text)
print(parts)  # ['one', 'two', 'three', 'four']
```

### time Module

```python
import time

# Current time (seconds since epoch)
now = time.time()
print(now)  # 1705329045.123

# Sleep
time.sleep(2)  # Pause for 2 seconds

# Measure execution time
start = time.time()
# ... code to measure ...
end = time.time()
print(f'Execution time: {end - start} seconds')

# Formatted time
print(time.ctime())  # 'Mon Jan 15 14:30:45 2024'
```

---

## Best Practices

### Choose the Right Data Structure

```python
from collections import Counter, defaultdict, deque

# Use Counter for counting
word_count = Counter(['apple', 'banana', 'apple'])

# Use defaultdict to avoid KeyError
groups = defaultdict(list)

# Use deque for queue operations
queue = deque()
queue.append(item)
queue.popleft()
```

### Use datetime for Date Operations

```python
from datetime import datetime, timedelta

# Don't manipulate dates manually
# Bad
days_to_add = 7
# ... complex date calculation ...

# Good
deadline = datetime.now() + timedelta(days=7)
```

### Use pathlib Instead of os.path

```python
from pathlib import Path

# Modern approach
path = Path('folder') / 'file.txt'
if path.exists():
    content = path.read_text()

# Old approach (still works)
import os
path = os.path.join('folder', 'file.txt')
if os.path.exists(path):
    with open(path) as f:
        content = f.read()
```

### Use json for Configuration

```python
import json

# Store configuration as JSON
config = {
    'database': {'host': 'localhost', 'port': 5432},
    'api_key': 'secret123'
}

with open('config.json', 'w') as f:
    json.dump(config, f, indent=4)
```

### Use argparse for CLI Tools

```python
import argparse

# Make scripts configurable
parser = argparse.ArgumentParser()
parser.add_argument('--config', default='config.json')
parser.add_argument('--verbose', action='store_true')
args = parser.parse_args()
```

---

## See Also

- **[File Operations Cheat Sheet](./File_Operations_Cheat_Sheet.md)** - pathlib and file I/O
- **[Data Structures Cheat Sheet](./Data_Structures_Cheat_Sheet.md)** - Built-in data structures
- [**Iterators and Generators Cheat Sheet](./Iterators_and_Generators_Cheat_Sheet.md)** - itertools module
- **[Regular Expressions Cheat Sheet](./Regular_Expressions_Cheat_Sheet.md)** - re module details

---

## Summary

The Python standard library provides powerful, ready-to-use modules:
- **collections** - Specialized data structures (Counter, deque, defaultdict)
- **datetime** - Comprehensive date and time handling
- **os/sys** - System and filesystem operations
- **json** - JSON encoding and decoding
- **math/random** - Mathematical and random operations
- **argparse** - Professional command-line interfaces
- **pathlib** - Modern, object-oriented file paths
- **itertools** - Advanced iterator operations

---
