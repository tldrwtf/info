# SQL Data Definition Language (DDL) Guide

This guide focuses on SQL's Data Definition Language (DDL), which is used to define and manage database structures. DDL commands are essential for creating, modifying, and deleting database objects like tables, databases, and schemas.

---

## 1. Introduction to Data Definition Language (DDL)

DDL is a subset of SQL (Structured Query Language) used for creating and modifying the structure of database objects. Unlike DML (Data Manipulation Language) which deals with data within the tables, DDL deals with the schema itself.

### Key DDL Commands
*   `CREATE`: Used to create database objects (e.g., `CREATE TABLE`, `CREATE DATABASE`).
*   `ALTER`: Used to modify the structure of existing database objects (e.g., `ALTER TABLE`).
*   `DROP`: Used to delete database objects (e.g., `DROP TABLE`, `DROP DATABASE`).
*   `TRUNCATE`: Used to remove all records from a table, including all spaces allocated for the records, but not the table structure itself.
*   `RENAME`: Used to rename a database object.

---

## 2. `CREATE` Statements

### `CREATE DATABASE`

Used to create a new SQL database.

```sql
CREATE DATABASE database_name;
```

### `CREATE TABLE`

Used to create a new table in a database. You must specify the table name and define each column's name, data type, and constraints.

#### Basic `CREATE TABLE` Syntax

```sql
CREATE TABLE table_name (
    column1_name DATATYPE CONSTRAINTS,
    column2_name DATATYPE CONSTRAINTS,
    column3_name DATATYPE CONSTRAINTS,
    ...
);
```

#### Common SQL Data Types

| Type       | Description                                  |
| :--------- | :------------------------------------------- |
| `INT`      | Whole numbers                                |
| `VARCHAR(size)`| Variable-length string, `size` is max length |
| `TEXT`     | Variable-length string, long text            |
| `BOOLEAN`  | True/False (often stored as 0/1 in some DBs) |
| `DATE`     | Date in 'YYYY-MM-DD' format                  |
| `DATETIME` | Date and time in 'YYYY-MM-DD HH:MM:SS' format|
| `REAL`/`FLOAT`/`DOUBLE` | Floating-point numbers          |

#### Common SQL Constraints

| Constraint  | Description                                  |
| :---------- | :------------------------------------------- |
| `PRIMARY KEY`| Uniquely identifies each row (cannot be NULL) |
| `FOREIGN KEY`| Links two tables together                     |
| `NOT NULL`  | Ensures a column cannot have a NULL value    |
| `UNIQUE`    | Ensures all values in a column are different |
| `DEFAULT value`| Sets a default value for a column if no value is specified |
| `AUTOINCREMENT`| Automatically generates a unique number for new records (e.g., `AUTO_INCREMENT` in MySQL, `AUTOINCREMENT` in SQLite, `IDENTITY(1,1)` in SQL Server) |

#### `CREATE TABLE` Examples

**Example 1: `Students` Table**

```sql
CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    enrollment_date DATE DEFAULT CURRENT_DATE
);
```

**Example 2: `PetClinic` Database Schema (from new data)**

```sql
-- Create Owners Table
CREATE TABLE Owners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    password VARCHAR(255) NOT NULL -- In real app, store hashed passwords
);

-- Create Pets Table
CREATE TABLE Pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    species VARCHAR(100),
    breed VARCHAR(100),
    age INTEGER,
    owner_id INTEGER NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES Owners(id) ON DELETE CASCADE
);

-- Create Vets Table
CREATE TABLE Vets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    specialization VARCHAR(255),
    email VARCHAR(255) UNIQUE NOT NULL
);

-- Create Appointments Table
CREATE TABLE Appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pet_id INTEGER NOT NULL,
    vet_id INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    appointment_date DATE NOT NULL,
    reason TEXT,
    status VARCHAR(50) DEFAULT 'scheduled', -- e.g., 'scheduled', 'completed', 'cancelled'
    FOREIGN KEY (pet_id) REFERENCES Pets(id) ON DELETE CASCADE,
    FOREIGN KEY (vet_id) REFERENCES Vets(id) ON DELETE RESTRICT, -- Prevent deleting vet with active appts
    FOREIGN KEY (owner_id) REFERENCES Owners(id) ON DELETE CASCADE
);
```

---

## 3. `ALTER` Statements

Used to add, delete, or modify columns in an existing table.

### Adding a Column

```sql
ALTER TABLE table_name
ADD COLUMN new_column_name DATATYPE CONSTRAINTS;

-- Example: Add a 'status' column to the Students table
ALTER TABLE Students
ADD COLUMN status VARCHAR(50) DEFAULT 'active';
```

### Dropping a Column

```sql
ALTER TABLE table_name
DROP COLUMN column_name;

-- Example: Drop the 'phone' column from the Owners table
ALTER TABLE Owners
DROP COLUMN phone;
```

### Modifying a Column (Data Type, Constraints)

Syntax varies significantly across different SQL databases (MySQL, PostgreSQL, SQLite, SQL Server).

```sql
-- Example (PostgreSQL/SQL Server): Change data type of 'email'
ALTER TABLE Students
ALTER COLUMN email TYPE VARCHAR(150);

-- Example (MySQL): Change data type of 'email'
ALTER TABLE Students
MODIFY COLUMN email VARCHAR(150);

-- Example (SQLite - more complex, usually involves recreating table)
-- SQLite often requires recreating the table, copying data, dropping old, renaming new.
```

---

## 4. `DROP` Statements

Used to delete existing database objects. Be very careful with `DROP` commands as they permanently remove data and schema.

### `DROP DATABASE`

Deletes an entire database.

```sql
DROP DATABASE database_name;

-- Example: Delete the 'pet_clinic' database
-- (Specific syntax may vary per DB system)
```

### `DROP TABLE`

Deletes an entire table, including all its data, indexes, constraints, and triggers.

```sql
DROP TABLE table_name;

-- Example: Delete the 'Appointments' table
DROP TABLE Appointments;
```

---

## 5. `TRUNCATE` Statement

Removes all rows from a table. Unlike `DROP TABLE`, `TRUNCATE TABLE` keeps the table structure (schema, columns, constraints, indexes) intact. It is usually faster than `DELETE FROM table_name` because it doesn't log individual row deletions.

```sql
TRUNCATE TABLE table_name;

-- Example: Remove all appointments
TRUNCATE TABLE Appointments;
```

---

## See Also

-   **[SQL and SQLAlchemy Cheat Sheet](../cheatsheets/SQL_and_SQLAlchemy_Cheat_Sheet.md)** - General SQL concepts and Python ORM basics.
-   **[Database_and_ORM_Guide.md](../guides/Database_and_ORM_Guide.md)** - (If created) for broader database topics.
-   **[Interactive CLI with ORM Project Guide](../guides/Interactive_CLI_ORM_Project_Guide.md)** - Practical application of ORM in a CLI.
-   **[Pet Clinic ORM Project Guide](../guides/Pet_Clinic_ORM_Project_Guide.md)** - A complete project example using DDL concepts.