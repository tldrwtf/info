# Python File Operations Cheat Sheet

## Quick Reference Card

| Operation | Syntax | Example |
|-----------|--------|---------|
| Open file | `open(filename, mode)` | `open('data.txt', 'r')` |
| Read entire file | `file.read()` | `content = f.read()` |
| Read lines | `file.readlines()` | `lines = f.readlines()` |
| Write to file | `file.write(text)` | `f.write('Hello\n')` |
| Context manager | `with open() as f:` | `with open('file.txt') as f:` |
| Check if exists | `Path.exists()` | `Path('file.txt').exists()` |
| Read CSV | `csv.reader(file)` | `reader = csv.reader(f)` |
| Read JSON | `json.load(file)` | `data = json.load(f)` |
| Write JSON | `json.dump(data, file)` | `json.dump(data, f)` |
| Create directory | `Path.mkdir()` | `Path('folder').mkdir()` |

## Table of Contents
1. [Basic File Operations](#basic-file-operations)
2. [File Modes](#file-modes)
3. [Reading Files](#reading-files)
4. [Writing Files](#writing-files)
5. [Working with CSV Files](#working-with-csv-files)
6. [Working with JSON Files](#working-with-json-files)
7. [Path Operations (pathlib)](#path-operations-pathlib)
8. [File System Operations](#file-system-operations)
9. [Best Practices](#best-practices)

---

## Basic File Operations

### Opening and Closing Files

```python
# Manual open/close (not recommended)
file = open('example.txt', 'r')
content = file.read()
file.close()

# Context manager (recommended)
with open('example.txt', 'r') as file:
    content = file.read()
# File automatically closed after block
```

### Why Use Context Managers?

```python
# Automatically handles:
# - Closing files even if an exception occurs
# - Cleaner code
# - No need to remember to close files

with open('data.txt', 'r') as f:
    data = f.read()
    # File is automatically closed after this block
```

---

## File Modes

| Mode | Description | Creates if Missing | Overwrites |
|------|-------------|-------------------|------------|
| `'r'` | Read (default) | No | N/A |
| `'w'` | Write | Yes | Yes |
| `'a'` | Append | Yes | No |
| `'x'` | Exclusive create | Yes | Error if exists |
| `'r+'` | Read and write | No | No |
| `'w+'` | Write and read | Yes | Yes |
| `'a+'` | Append and read | Yes | No |
| `'rb'` | Read binary | No | N/A |
| `'wb'` | Write binary | Yes | Yes |

```python
# Read mode (file must exist)
with open('input.txt', 'r') as f:
    content = f.read()

# Write mode (overwrites existing file)
with open('output.txt', 'w') as f:
    f.write('New content')

# Append mode (adds to end of file)
with open('log.txt', 'a') as f:
    f.write('New log entry\n')

# Exclusive create (fails if file exists)
try:
    with open('unique.txt', 'x') as f:
        f.write('This file is new')
except FileExistsError:
    print('File already exists')

# Binary mode (for images, PDFs, etc.)
with open('image.png', 'rb') as f:
    binary_data = f.read()
```

---

## Reading Files

### Read Entire File

```python
# Read as single string
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)

# Read with specific encoding
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

### Read Line by Line

```python
# Method 1: Using readline() (one line at a time)
with open('file.txt', 'r') as f:
    line = f.readline()  # Read first line
    while line:
        print(line.strip())  # Remove newline
        line = f.readline()

# Method 2: Using readlines() (all lines as list)
with open('file.txt', 'r') as f:
    lines = f.readlines()  # Returns list of lines
    for line in lines:
        print(line.strip())

# Method 3: Iterate over file object (memory efficient)
with open('file.txt', 'r') as f:
    for line in f:  # Best for large files
        print(line.strip())
```

### Read Specific Number of Characters

```python
with open('file.txt', 'r') as f:
    # Read first 100 characters
    chunk = f.read(100)
    print(chunk)

    # Read next 100 characters
    next_chunk = f.read(100)
```

### Read File in Chunks (Large Files)

```python
def read_in_chunks(file_path, chunk_size=1024):
    """Read file in chunks to save memory"""
    with open(file_path, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Usage
for chunk in read_in_chunks('large_file.txt'):
    process(chunk)
```

---

## Writing Files

### Write Strings

```python
# Write (overwrites file)
with open('output.txt', 'w') as f:
    f.write('Line 1\n')
    f.write('Line 2\n')

# Write multiple lines
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('output.txt', 'w') as f:
    f.writelines(lines)

# Append to file
with open('output.txt', 'a') as f:
    f.write('Additional line\n')
```

### Write with Print Function

```python
# Print to file instead of console
with open('output.txt', 'w') as f:
    print('Hello, World!', file=f)
    print('Second line', file=f)
```

### Write Binary Data

```python
# Write binary data (images, etc.)
with open('output.bin', 'wb') as f:
    f.write(b'\x00\x01\x02\x03')

# Copy binary file
with open('source.png', 'rb') as source:
    with open('destination.png', 'wb') as dest:
        dest.write(source.read())
```

---

## Working with CSV Files

### Reading CSV Files

```python
import csv

# Basic CSV reading
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # row is a list

# Skip header row
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        print(row)

# Read as dictionary (header as keys)
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])  # Access by column name

# Custom delimiter
with open('data.tsv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(row)
```

### Writing CSV Files

```python
import csv

# Basic CSV writing
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'NYC'],
    ['Bob', 25, 'LA']
]

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)  # Write all rows

# Write row by row
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City'])  # Header
    writer.writerow(['Alice', 30, 'NYC'])
    writer.writerow(['Bob', 25, 'LA'])

# Write as dictionary
data = [
    {'name': 'Alice', 'age': 30, 'city': 'NYC'},
    {'name': 'Bob', 'age': 25, 'city': 'LA'}
]

with open('output.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # Write header
    writer.writerows(data)  # Write all rows
```

### CSV Practical Example

```python
import csv

# Read CSV and process data
def process_sales_data(input_file, output_file):
    """Calculate total sales and write summary"""
    sales_by_region = {}

    # Read data
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            region = row['region']
            amount = float(row['amount'])
            sales_by_region[region] = sales_by_region.get(region, 0) + amount

    # Write summary
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Region', 'Total Sales'])
        for region, total in sales_by_region.items():
            writer.writerow([region, total])

# Usage
process_sales_data('sales.csv', 'summary.csv')
```

---

## Working with JSON Files

### Reading JSON Files

```python
import json

# Read JSON file
with open('data.json', 'r') as f:
    data = json.load(f)  # Returns dict or list
    print(data)

# Handle JSON errors
try:
    with open('data.json', 'r') as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    print(f'Invalid JSON: {e}')

# Read JSON with encoding
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
```

### Writing JSON Files

```python
import json

# Write JSON (compact)
data = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
with open('output.json', 'w') as f:
    json.dump(data, f)

# Write JSON (pretty-printed)
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)

# Write JSON with sorted keys
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)

# Write list of objects
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25}
]
with open('users.json', 'w') as f:
    json.dump(data, f, indent=4)
```

### Converting Between JSON Strings and Python Objects

```python
import json

# Python to JSON string
data = {'name': 'Alice', 'age': 30}
json_string = json.dumps(data)
print(json_string)  # '{"name": "Alice", "age": 30}'

# JSON string to Python
json_string = '{"name": "Alice", "age": 30}'
data = json.loads(json_string)
print(data['name'])  # 'Alice'

# Pretty-print JSON string
json_string = json.dumps(data, indent=4, sort_keys=True)
print(json_string)
```

### JSON Practical Example

```python
import json

# Save configuration
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'name': 'mydb'
    },
    'api': {
        'url': 'https://api.example.com',
        'key': 'secret123'
    }
}

with open('config.json', 'w') as f:
    json.dump(config, f, indent=4)

# Load configuration
with open('config.json', 'r') as f:
    config = json.load(f)
    db_host = config['database']['host']
    api_url = config['api']['url']
```

---

## Path Operations (pathlib)

### Creating Path Objects

```python
from pathlib import Path

# Create path objects
p = Path('folder/file.txt')
p = Path('folder') / 'subfolder' / 'file.txt'  # Join paths
p = Path.home()  # User home directory
p = Path.cwd()  # Current working directory
```

### Checking Path Properties

```python
from pathlib import Path

p = Path('folder/file.txt')

# Check existence
p.exists()  # True if exists
p.is_file()  # True if is a file
p.is_dir()  # True if is a directory

# Get path components
p.name  # 'file.txt'
p.stem  # 'file' (without extension)
p.suffix  # '.txt'
p.parent  # Path('folder')
p.absolute()  # Absolute path

# Example
path = Path('documents/report.pdf')
print(f'Name: {path.name}')  # 'report.pdf'
print(f'Extension: {path.suffix}')  # '.pdf'
print(f'Directory: {path.parent}')  # 'documents'
```

### Reading and Writing with pathlib

```python
from pathlib import Path

# Read file
p = Path('data.txt')
content = p.read_text()  # Read as string
binary_content = p.read_bytes()  # Read as bytes

# Write file
p = Path('output.txt')
p.write_text('Hello, World!')  # Write string
p.write_bytes(b'\x00\x01')  # Write bytes
```

### Listing Directory Contents

```python
from pathlib import Path

# List all files and directories
p = Path('.')
for item in p.iterdir():
    print(item)

# List only files
for item in p.iterdir():
    if item.is_file():
        print(item)

# List with glob pattern
for txt_file in p.glob('*.txt'):
    print(txt_file)

# Recursive glob
for py_file in p.rglob('*.py'):  # Find all .py files recursively
    print(py_file)
```

### Creating and Deleting Directories

```python
from pathlib import Path

# Create directory
p = Path('new_folder')
p.mkdir()  # Create directory
p.mkdir(exist_ok=True)  # Don't error if exists
p.mkdir(parents=True)  # Create parent directories too

# Create nested directories
p = Path('parent/child/grandchild')
p.mkdir(parents=True, exist_ok=True)

# Delete file
p = Path('file.txt')
if p.exists():
    p.unlink()  # Delete file

# Delete directory
p = Path('folder')
if p.exists() and p.is_dir():
    p.rmdir()  # Delete empty directory
```

### Path Practical Example

```python
from pathlib import Path

def organize_files_by_extension(directory):
    """Organize files in directory by extension"""
    dir_path = Path(directory)

    for file_path in dir_path.iterdir():
        if file_path.is_file():
            # Get extension without dot
            extension = file_path.suffix[1:] if file_path.suffix else 'no_extension'

            # Create folder for extension
            ext_folder = dir_path / extension
            ext_folder.mkdir(exist_ok=True)

            # Move file
            new_path = ext_folder / file_path.name
            file_path.rename(new_path)
            print(f'Moved {file_path.name} to {extension}/')

# Usage
organize_files_by_extension('downloads')
```

---

## File System Operations

### Using os Module

```python
import os

# Current working directory
cwd = os.getcwd()
print(cwd)

# Change directory
os.chdir('/path/to/directory')

# List directory contents
contents = os.listdir('.')  # Returns list of names
for item in contents:
    print(item)

# Check if path exists
os.path.exists('file.txt')
os.path.isfile('file.txt')
os.path.isdir('folder')

# Get file size
size = os.path.getsize('file.txt')  # Size in bytes

# Join paths (OS-independent)
path = os.path.join('folder', 'subfolder', 'file.txt')
```

### File and Directory Operations

```python
import os
import shutil

# Rename/move file
os.rename('old_name.txt', 'new_name.txt')

# Copy file
shutil.copy('source.txt', 'destination.txt')
shutil.copy2('source.txt', 'dest.txt')  # Preserves metadata

# Copy entire directory
shutil.copytree('source_folder', 'destination_folder')

# Move file or directory
shutil.move('source.txt', 'destination_folder/')

# Delete file
os.remove('file.txt')

# Delete empty directory
os.rmdir('empty_folder')

# Delete directory and contents
shutil.rmtree('folder')  # Careful! Deletes everything
```

### Walking Directory Trees

```python
import os

# Walk directory tree
for root, dirs, files in os.walk('start_directory'):
    print(f'Current directory: {root}')
    print(f'Subdirectories: {dirs}')
    print(f'Files: {files}')

    for file in files:
        full_path = os.path.join(root, file)
        print(full_path)

# Find all Python files
def find_python_files(directory):
    """Find all .py files recursively"""
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

# Usage
py_files = find_python_files('.')
for file in py_files:
    print(file)
```

---

## Best Practices

### Always Use Context Managers

```python
# Bad: Manual file handling
f = open('file.txt', 'r')
content = f.read()
f.close()  # Easy to forget

# Good: Context manager
with open('file.txt', 'r') as f:
    content = f.read()
# Automatically closed
```

### Specify Encoding

```python
# Always specify encoding for text files
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Content with special chars: ñ, é, 中文')
```

### Handle Errors Gracefully

```python
from pathlib import Path

# Check if file exists before reading
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('Permission denied')
except Exception as e:
    print(f'Error: {e}')

# Or use pathlib
p = Path('data.txt')
if p.exists():
    content = p.read_text()
else:
    print('File does not exist')
```

### Use Appropriate File Modes

```python
# Read-only when you don't need to write
with open('input.txt', 'r') as f:
    data = f.read()

# Use append to add to existing files
with open('log.txt', 'a') as f:
    f.write('New log entry\n')

# Use 'x' mode to prevent overwriting
try:
    with open('important.txt', 'x') as f:
        f.write('Data')
except FileExistsError:
    print('File already exists, not overwriting')
```

### Process Large Files Efficiently

```python
# Bad: Load entire file into memory
with open('huge_file.txt', 'r') as f:
    content = f.read()  # May cause memory issues

# Good: Process line by line
with open('huge_file.txt', 'r') as f:
    for line in f:
        process_line(line)

# Good: Process in chunks
with open('huge_file.txt', 'r') as f:
    while True:
        chunk = f.read(8192)  # Read 8KB at a time
        if not chunk:
            break
        process_chunk(chunk)
```

### Use pathlib for Path Operations

```python
from pathlib import Path

# Modern approach
p = Path('folder') / 'file.txt'
if p.exists():
    content = p.read_text()

# Easier than os.path
# Old way
import os
path = os.path.join('folder', 'file.txt')
if os.path.exists(path):
    with open(path, 'r') as f:
        content = f.read()
```

### Secure File Operations

```python
import os
from pathlib import Path

# Use temporary files for sensitive data
import tempfile

with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
    tmp.write('Sensitive data')
    tmp_path = tmp.name

# Process temporary file
# ...

# Clean up
os.unlink(tmp_path)

# Set file permissions (Unix)
os.chmod('file.txt', 0o600)  # Owner read/write only
```

### Organize Related File Operations

```python
from pathlib import Path
import json

class DataManager:
    """Manage data file operations"""

    def __init__(self, data_dir):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)

    def save_json(self, filename, data):
        """Save data as JSON"""
        file_path = self.data_dir / filename
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def load_json(self, filename):
        """Load data from JSON"""
        file_path = self.data_dir / filename
        if not file_path.exists():
            return None
        with open(file_path, 'r') as f:
            return json.load(f)

    def list_files(self, pattern='*.json'):
        """List all JSON files"""
        return list(self.data_dir.glob(pattern))

# Usage
manager = DataManager('data')
manager.save_json('users.json', {'users': ['Alice', 'Bob']})
data = manager.load_json('users.json')
files = manager.list_files()
```

---

## See Also

- **[Error Handling Cheat Sheet](Error_Handling_Cheat_Sheet.md)** - Exception handling for file operations
- **[Python Basics Cheat Sheet](Python_Basics_Cheat_Sheet.md)** - Python fundamentals
- **[Standard Library Essentials Cheat Sheet](Standard_Library_Essentials_Cheat_Sheet.md)** - More useful modules

---
