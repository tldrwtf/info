# SQL Data Definition Language (DDL) Guide

Data Definition Language (DDL) is a subset of SQL used to define and manage the structure of your database. Unlike DML (Data Manipulation Language) which deals with data (INSERT, UPDATE, DELETE), DDL deals with schemas (CREATE, ALTER, DROP).

## 1. Creating a Database

In SQLite, creating a database is often as simple as connecting to a file that doesn't exist yet.

```bash
# From command line
sqlite3 my_database.db
```

## 2. The CREATE Statement

The `CREATE TABLE` statement is used to define a new table, its columns, and data types.

### Basic Syntax
```sql
CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    ...
);
```

### Example: Students Table
```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob DATE,
    grade_level INTEGER
);
```

### Common Data Types (SQLite)
*   `INTEGER`: Whole numbers.
*   `TEXT`: Strings of text.
*   `REAL`: Floating point numbers.
*   `BLOB`: Binary data.
*   `NULL`: Missing value.

### Common Constraints
*   `PRIMARY KEY`: Uniquely identifies each record.
*   `NOT NULL`: Ensures the column cannot have a NULL value.
*   `UNIQUE`: Ensures all values in a column are different.
*   `DEFAULT value`: Sets a default value if none is specified.
*   `FOREIGN KEY`: Links to another table.

## 3. Relationships & Foreign Keys

To link tables together, we use Foreign Keys. This enforces referential integrity.

### Example: Pet Clinic Schema

**Owners Table:**
```sql
CREATE TABLE owners (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
```

**Pets Table (One-to-Many):**
Each pet belongs to one owner.
```sql
CREATE TABLE pets (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT,
    age INTEGER,
    owner_id INTEGER,
    FOREIGN KEY (owner_id) REFERENCES owners(id)
);
```

## 4. The ALTER Statement

The `ALTER TABLE` statement is used to modify an existing table structure.

### Adding a Column
```sql
ALTER TABLE students ADD COLUMN email TEXT;
```

### Renaming a Table
```sql
ALTER TABLE students RENAME TO learners;
```

*Note: SQLite has limited support for `ALTER TABLE` compared to PostgreSQL or MySQL. You often cannot drop a column or change constraints without recreating the table.*

## 5. The DROP Statement

The `DROP TABLE` statement deletes a table and all of its data permanently.

```sql
DROP TABLE IF EXISTS students;
```

## 6. Practice Assignments

### Assignment 1: Basic Table Setup
**Goal:** Create a database for a school system.
1.  Create a `assignment.db` file.
2.  Create a `students` table with fields: `id`, `first_name`, `last_name`, `dob`, `grade_level`.
3.  Insert 2 test students to verify the schema.

```sql
-- Solution
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    dob TEXT,
    grade_level INTEGER
);

INSERT INTO students (first_name, last_name, grade_level) VALUES ('Alice', 'Wonder', 10);
INSERT INTO students (first_name, last_name, grade_level) VALUES ('Bob', 'Builder', 11);
```

### Assignment 2: Pet Clinic Schema
**Goal:** Create a related schema for a Vet Clinic.
1.  Create an `owners` table (`id`, `first_name`, `last_name`, `email`).
2.  Create a `pets` table (`id`, `owner_id`, `species`, `age`).
3.  Ensure `owner_id` is a Foreign Key referencing `owners(id)`.

```sql
-- Solution
CREATE TABLE owners (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT
);

CREATE TABLE pets (
    id INTEGER PRIMARY KEY,
    owner_id INTEGER,
    species TEXT,
    age INTEGER,
    FOREIGN KEY(owner_id) REFERENCES owners(id)
);
```

### Assignment 3: Schema Modification
**Goal:** Update the Pet Clinic schema.
1.  Add a `phone_number` column to the `owners` table.
2.  Rename the `pets` table to `animals` (just for practice, then rename it back if you want).

```sql
-- Solution
ALTER TABLE owners ADD COLUMN phone_number TEXT;
ALTER TABLE pets RENAME TO animals;
```

---

## See Also
- **[SQL and SQLAlchemy Cheat Sheet](../cheatsheets/SQL_and_SQLAlchemy_Cheat_Sheet.md)**
- **[SQL Advanced Queries Guide](SQL_Advanced_Queries_Guide.md)**
