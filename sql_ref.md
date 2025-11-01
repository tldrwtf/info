# COMPLETE SQL REFERENCE GUIDE

## SQL Fundamentals - DDL, DML, DQL

### DDL (Data Definition Language) - Defining the Structure

DDL commands are used to create and modify the structure of your database and tables.

```sql
-- CREATE DATABASE: Create a new database
CREATE DATABASE company_db;

-- USE: Select a database to work with
USE company_db;

-- CREATE TABLE: Define a new table with columns and data types
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT, -- Unique ID for each employee
    first_name VARCHAR(50) NOT NULL,    -- Employee's first name, cannot be null
    last_name VARCHAR(50) NOT NULL,     -- Employee's last name, cannot be null
    email VARCHAR(100) UNIQUE,          -- Email, must be unique
    hire_date DATE,                     -- Date the employee was hired
    salary DECIMAL(10, 2)               -- Salary with 2 decimal places
);

-- ALTER TABLE: Modify an existing table
-- Add a new column
ALTER TABLE employees ADD COLUMN department VARCHAR(50);

-- Modify a column's data type
ALTER TABLE employees MODIFY COLUMN salary DECIMAL(12, 2);

-- Add a constraint
ALTER TABLE employees ADD CONSTRAINT fk_department
FOREIGN KEY (department_id) REFERENCES departments(id);

-- DROP TABLE: Delete a table and all its data (use with caution!)
DROP TABLE employees;

-- TRUNCATE TABLE: Deletes all data from a table, but keeps the structure
TRUNCATE TABLE employees;
```


### DML (Data Manipulation Language) - Working with Data

DML commands are used to insert, update, and delete data within your tables.

```sql
-- INSERT INTO: Add new rows of data to a table
INSERT INTO employees (first_name, last_name, email, hire_date, salary)
VALUES ('John', 'Doe', 'john.doe@email.com', '2025-01-15', 60000.00);

-- Insert multiple rows at once
INSERT INTO employees (first_name, last_name, email, hire_date, salary)
VALUES
    ('Jane', 'Smith', 'jane.smith@email.com', '2025-03-22', 75000.00),
    ('Peter', 'Jones', 'peter.jones@email.com', '2024-11-10', 55000.00);

-- UPDATE: Modify existing data in a table
-- Always use a WHERE clause with UPDATE!
UPDATE employees
SET salary = 65000.00, department = 'Sales'
WHERE id = 1;

-- Give everyone a 10% raise
UPDATE employees
SET salary = salary * 1.10;

-- DELETE: Remove rows from a table
-- Always use a WHERE clause with DELETE!
DELETE FROM employees
WHERE id = 3;

-- Delete all employees in the 'HR' department
DELETE FROM employees
WHERE department = 'HR';
```


### DQL (Data Query Language) - Retrieving Data

The `SELECT` statement is used to query the database and retrieve data.

```sql
-- SELECT: Retrieve data from one or more tables
-- Select all columns from a table
SELECT * FROM employees;

-- Select specific columns
SELECT first_name, last_name, salary FROM employees;

-- WHERE: Filter rows based on a condition
SELECT * FROM employees
WHERE salary > 70000;

-- Using AND, OR, NOT
SELECT * FROM employees
WHERE department = 'Sales' AND salary > 60000;

-- ORDER BY: Sort the results
-- Sort by salary, highest first
SELECT * FROM employees
ORDER BY salary DESC;

-- Sort by department, then by last name
SELECT * FROM employees
ORDER BY department ASC, last_name ASC;

-- LIMIT: Restrict the number of rows returned
-- Get the top 5 highest-paid employees
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 5;

-- DISTINCT: Return only unique values
SELECT DISTINCT department FROM employees;
```


## Advanced SQL Queries

### Aggregate Functions

Aggregate functions perform a calculation on a set of values and return a single value.

```sql
-- COUNT(): Count the number of rows
SELECT COUNT(*) FROM employees; -- Total number of employees
SELECT COUNT(DISTINCT department) FROM employees; -- Number of unique departments

-- SUM(): Calculate the sum of a numeric column
SELECT SUM(salary) FROM employees; -- Total payroll

-- AVG(): Calculate the average value
SELECT AVG(salary) FROM employees; -- Average salary

-- MIN() and MAX(): Get the minimum and maximum values
SELECT MIN(salary) AS min_salary, MAX(salary) AS max_salary FROM employees;
```


### GROUP BY

The `GROUP BY` statement groups rows that have the same values into summary rows. It's often used with aggregate functions.

```sql
-- Find the number of employees in each department
SELECT department, COUNT(*) AS num_employees
FROM employees
GROUP BY department;

-- Find the average salary for each department
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;

-- HAVING: Filter groups based on a condition
-- Find departments with more than 10 employees
SELECT department, COUNT(*) AS num_employees
FROM employees
GROUP BY department
HAVING COUNT(*) > 10;
```


### JOINs

JOINs are used to combine rows from two or more tables based on a related column between them.

```sql
-- Sample tables for JOIN examples
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- INNER JOIN: Returns records that have matching values in both tables
SELECT employees.name, departments.name AS department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.id;

-- LEFT JOIN (or LEFT OUTER JOIN): Returns all records from the left table,
-- and the matched records from the right table. The result is NULL from the
-- right side if there is no match.
SELECT employees.name, departments.name AS department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id;

-- RIGHT JOIN (or RIGHT OUTER JOIN): Returns all records from the right table,
-- and the matched records from the left table.
SELECT employees.name, departments.name AS department_name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.id;

-- FULL OUTER JOIN: Returns all records when there is a match in either
-- left or right table. (Note: MySQL doesn't support FULL OUTER JOIN directly,
-- you can emulate it with a UNION of LEFT and RIGHT JOINs).
SELECT employees.name, departments.name AS department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id
UNION
SELECT employees.name, departments.name AS department_name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.id;
```


### Subqueries (Nested Queries)

A subquery is a query nested inside another query.

```sql
-- Find employees who have a salary above the company average
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Find departments that have at least one employee
SELECT name
FROM departments
WHERE id IN (SELECT DISTINCT department_id FROM employees);

-- Correlated Subquery: An inner query that depends on the outer query
-- Find employees whose salary is above the average for their department
SELECT name, salary, department_id
FROM employees e1
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);
```


### Window Functions

Window functions perform a calculation across a set of table rows that are somehow related to the current row.

```sql
-- ROW_NUMBER(), RANK(), DENSE_RANK()
-- Rank employees by salary within each department
SELECT
    name,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dense_salary_rank
FROM employees;

-- LAG() and LEAD()
-- Compare each employee's salary to the next employee's salary in the same department
SELECT
    name,
    department,
    salary,
    LEAD(salary, 1) OVER (PARTITION BY department ORDER BY salary DESC) as next_highest_salary
FROM employees;

-- Running Total
SELECT
    hire_date,
    COUNT(*) AS new_hires,
    SUM(COUNT(*)) OVER (ORDER BY hire_date) as running_total_hires
FROM employees
GROUP BY hire_date;
```


### Common Table Expressions (CTEs)

CTEs allow you to define a temporary, named result set that you can reference within another SQL statement.

```sql
-- Use a CTE to find departments with high average salaries
WITH DepartmentSalaries AS (
    SELECT
        department,
        AVG(salary) as avg_salary
    FROM employees
    GROUP BY department
)
SELECT department, avg_salary
FROM DepartmentSalaries
WHERE avg_salary > 60000;
```

