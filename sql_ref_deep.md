# COMPLETE SQL DATABASE GUIDE

## PART 1: DDL - DATA DEFINITION LANGUAGE

### Database Fundamentals

```sql
-- ========== WHAT IS SQL? ==========
-- SQL: Structured Query Language
-- Used to communicate with relational databases
-- Four main categories:
--   DDL (Data Definition Language) - CREATE, ALTER, DROP
--   DML (Data Manipulation Language) - SELECT, INSERT, UPDATE, DELETE
--   DCL (Data Control Language) - GRANT, REVOKE
--   TCL (Transaction Control Language) - COMMIT, ROLLBACK

-- ========== CREATING DATABASES ==========
-- Create a new database
CREATE DATABASE company_db;

-- Use/select a database
USE company_db;

-- Delete a database (CAREFUL!)
DROP DATABASE company_db;

-- Check if database exists before creating
CREATE DATABASE IF NOT EXISTS company_db;

-- ========== CREATING TABLES ==========
-- Basic table creation
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10, 2)
);

-- Table with constraints
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    hire_date DATE DEFAULT CURRENT_DATE,
    salary DECIMAL(10, 2) CHECK (salary > 0),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- ========== DATA TYPES ==========
-- Numeric Types
INT                    -- Integer: -2147483648 to 2147483647
BIGINT                 -- Large integer
DECIMAL(10,2)         -- Fixed-point: 10 total digits, 2 after decimal
FLOAT                  -- Floating-point number
DOUBLE                 -- Double precision floating-point

-- String Types
CHAR(10)              -- Fixed length string (padded)
VARCHAR(255)          -- Variable length string (up to 255)
TEXT                  -- Large text (up to 65,535 characters)
LONGTEXT              -- Very large text (up to 4GB)

-- Date/Time Types
DATE                  -- YYYY-MM-DD
TIME                  -- HH:MM:SS
DATETIME              -- YYYY-MM-DD HH:MM:SS
TIMESTAMP             -- Unix timestamp
YEAR                  -- Year value

-- Boolean
BOOLEAN               -- TRUE/FALSE (stored as 1/0)

-- ========== CONSTRAINTS ==========
-- PRIMARY KEY - Unique identifier for each row
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50)
);

-- FOREIGN KEY - Links tables together
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- UNIQUE - No duplicate values
CREATE TABLE accounts (
    email VARCHAR(100) UNIQUE,
    username VARCHAR(50) UNIQUE
);

-- NOT NULL - Must have a value
CREATE TABLE products (
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

-- DEFAULT - Default value if none provided
CREATE TABLE posts (
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'active'
);

-- CHECK - Value must meet condition
CREATE TABLE employees (
    age INT CHECK (age >= 18),
    salary DECIMAL(10,2) CHECK (salary > 0)
);

-- ========== ALTER TABLE ==========
-- Add a column
ALTER TABLE employees
ADD COLUMN middle_name VARCHAR(50);

-- Modify column data type
ALTER TABLE employees
MODIFY COLUMN salary DECIMAL(12, 2);

-- Rename column
ALTER TABLE employees
CHANGE COLUMN middle_name middle_initial CHAR(1);

-- Drop a column
ALTER TABLE employees
DROP COLUMN middle_initial;

-- Add constraint
ALTER TABLE employees
ADD CONSTRAINT chk_salary CHECK (salary >= 30000);

-- Drop constraint
ALTER TABLE employees
DROP CONSTRAINT chk_salary;

-- ========== DROP vs TRUNCATE ==========
-- DROP - Deletes entire table structure
DROP TABLE employees;

-- TRUNCATE - Deletes all data, keeps structure
TRUNCATE TABLE employees;

-- DROP with safety check
DROP TABLE IF EXISTS employees;

-- ========== PRACTICAL EXAMPLE ==========
-- Complete database setup
CREATE DATABASE school_db;
USE school_db;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    gpa DECIMAL(3,2) CHECK (gpa >= 0.0 AND gpa <= 4.0),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    credits INT CHECK (credits > 0),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    grade CHAR(2),
    enrollment_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    UNIQUE(student_id, course_id)  -- Student can't enroll twice
);
```


***

## PART 2: BASIC SQL QUERIES

### SELECT Statement - Reading Data

```sql
-- ========== BASIC SELECT ==========
-- Select all columns
SELECT * FROM employees;

-- Select specific columns
SELECT first_name, last_name, salary FROM employees;

-- Select with alias (rename columns)
SELECT 
    first_name AS "First Name",
    last_name AS "Last Name",
    salary AS "Annual Salary"
FROM employees;

-- ========== WHERE CLAUSE - FILTERING ==========
-- Basic comparison operators
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE department_id = 3;
SELECT * FROM employees WHERE hire_date >= '2020-01-01';

-- String comparisons
SELECT * FROM employees WHERE first_name = 'John';
SELECT * FROM employees WHERE last_name != 'Smith';

-- LIKE - Pattern matching
SELECT * FROM employees WHERE first_name LIKE 'J%';      -- Starts with J
SELECT * FROM employees WHERE email LIKE '%@gmail.com';  -- Ends with @gmail.com
SELECT * FROM employees WHERE last_name LIKE '_mith';    -- Second char can be anything
SELECT * FROM employees WHERE phone LIKE '%555%';        -- Contains 555

-- IN - Multiple values
SELECT * FROM employees WHERE department_id IN (1, 3, 5);
SELECT * FROM employees WHERE city IN ('New York', 'Boston', 'Chicago');

-- BETWEEN - Range of values
SELECT * FROM employees WHERE salary BETWEEN 40000 AND 60000;
SELECT * FROM employees WHERE hire_date BETWEEN '2020-01-01' AND '2020-12-31';

-- IS NULL / IS NOT NULL
SELECT * FROM employees WHERE phone IS NULL;
SELECT * FROM employees WHERE manager_id IS NOT NULL;

-- ========== LOGICAL OPERATORS ==========
-- AND - All conditions must be true
SELECT * FROM employees 
WHERE salary > 50000 AND department_id = 3;

SELECT * FROM employees
WHERE hire_date >= '2020-01-01' AND city = 'New York' AND salary < 100000;

-- OR - At least one condition must be true
SELECT * FROM employees
WHERE department_id = 1 OR department_id = 2;

SELECT * FROM employees
WHERE city = 'New York' OR city = 'Boston';

-- NOT - Negates condition
SELECT * FROM employees WHERE NOT department_id = 3;
SELECT * FROM employees WHERE city NOT IN ('New York', 'LA');

-- Combining operators (use parentheses!)
SELECT * FROM employees
WHERE (city = 'New York' OR city = 'Boston')
  AND salary > 60000
  AND hire_date >= '2020-01-01';

-- ========== ORDER BY - SORTING ==========
-- Ascending order (default)
SELECT * FROM employees ORDER BY last_name;
SELECT * FROM employees ORDER BY salary ASC;

-- Descending order
SELECT * FROM employees ORDER BY salary DESC;

-- Multiple columns
SELECT * FROM employees 
ORDER BY department_id ASC, salary DESC;

-- Order by alias
SELECT first_name, salary * 12 AS annual_salary
FROM employees
ORDER BY annual_salary DESC;

-- ========== LIMIT - RESTRICT ROWS ==========
-- First 10 rows
SELECT * FROM employees LIMIT 10;

-- Top 5 highest salaries
SELECT * FROM employees 
ORDER BY salary DESC 
LIMIT 5;

-- Pagination: Skip 10, get next 10
SELECT * FROM employees 
LIMIT 10 OFFSET 10;

-- MySQL shorthand
SELECT * FROM employees LIMIT 10, 10;  -- (offset, count)

-- ========== DISTINCT - UNIQUE VALUES ==========
-- Remove duplicates
SELECT DISTINCT city FROM employees;
SELECT DISTINCT department_id FROM employees;

-- Distinct combinations
SELECT DISTINCT city, state FROM employees;

-- Count unique values
SELECT COUNT(DISTINCT city) AS unique_cities FROM employees;

-- ========== AGGREGATE FUNCTIONS ==========
-- COUNT - Number of rows
SELECT COUNT(*) FROM employees;
SELECT COUNT(phone) FROM employees;  -- Ignores NULL
SELECT COUNT(DISTINCT city) FROM employees;

-- SUM - Total of numeric column
SELECT SUM(salary) FROM employees;
SELECT SUM(salary) AS total_payroll FROM employees WHERE department_id = 3;

-- AVG - Average value
SELECT AVG(salary) FROM employees;
SELECT AVG(salary) AS average_salary FROM employees WHERE city = 'New York';

-- MIN/MAX - Minimum/Maximum
SELECT MIN(salary) FROM employees;
SELECT MAX(salary) FROM employees;
SELECT MIN(hire_date) AS first_hire FROM employees;

-- Multiple aggregates
SELECT 
    COUNT(*) AS total_employees,
    AVG(salary) AS avg_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary,
    SUM(salary) AS total_payroll
FROM employees;

-- ========== GROUP BY - GROUPING DATA ==========
-- Count employees per department
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;

-- Average salary per department
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id;

-- Multiple columns
SELECT city, state, COUNT(*) AS employee_count
FROM employees
GROUP BY city, state;

-- With ORDER BY
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
ORDER BY avg_salary DESC;

-- ========== HAVING - FILTER GROUPS ==========
-- WHERE filters rows BEFORE grouping
-- HAVING filters groups AFTER grouping

-- Departments with more than 5 employees
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;

-- Departments with average salary > $60,000
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 60000;

-- Combining WHERE and HAVING
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
WHERE hire_date >= '2020-01-01'  -- Filter rows first
GROUP BY department_id
HAVING AVG(salary) > 50000        -- Then filter groups
ORDER BY avg_salary DESC;
```


***

## PART 3: ADVANCED SQL QUERIES

### JOIN Operations - Combining Tables

```sql
-- ========== INNER JOIN - MATCHING ROWS ONLY ==========
-- Basic INNER JOIN
SELECT 
    employees.first_name,
    employees.last_name,
    departments.dept_name
FROM employees
INNER JOIN departments 
    ON employees.department_id = departments.dept_id;

-- Using table aliases
SELECT 
    e.first_name,
    e.last_name,
    d.dept_name,
    e.salary
FROM employees e
INNER JOIN departments d 
    ON e.department_id = d.dept_id;

-- Multiple JOINs
SELECT 
    e.first_name,
    e.last_name,
    d.dept_name,
    c.city_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.dept_id
INNER JOIN cities c ON e.city_id = c.city_id;

-- ========== LEFT JOIN - ALL FROM LEFT TABLE ==========
-- All employees, even without departments
SELECT 
    e.first_name,
    e.last_name,
    d.dept_name
FROM employees e
LEFT JOIN departments d 
    ON e.department_id = d.dept_id;

-- Find employees without departments
SELECT 
    e.first_name,
    e.last_name
FROM employees e
LEFT JOIN departments d 
    ON e.department_id = d.dept_id
WHERE d.dept_id IS NULL;

-- ========== RIGHT JOIN - ALL FROM RIGHT TABLE ==========
-- All departments, even without employees
SELECT 
    e.first_name,
    d.dept_name
FROM employees e
RIGHT JOIN departments d 
    ON e.department_id = d.dept_id;

-- ========== FULL OUTER JOIN - ALL FROM BOTH ==========
-- MySQL doesn't support FULL OUTER JOIN directly
-- Simulate with UNION
SELECT e.first_name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.dept_id
UNION
SELECT e.first_name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.dept_id;

-- ========== SELF JOIN - JOIN TABLE TO ITSELF ==========
-- Find employees and their managers
SELECT 
    e.first_name AS employee,
    m.first_name AS manager
FROM employees e
LEFT JOIN employees m 
    ON e.manager_id = m.employee_id;

-- ========== CROSS JOIN - CARTESIAN PRODUCT ==========
-- Every combination of rows
SELECT 
    products.product_name,
    colors.color_name
FROM products
CROSS JOIN colors;

-- ========== SUBQUERIES - QUERIES WITHIN QUERIES ==========
-- Employees earning above average
SELECT first_name, last_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- IN subquery
SELECT first_name, last_name
FROM employees
WHERE department_id IN (
    SELECT dept_id 
    FROM departments 
    WHERE location = 'New York'
);

-- EXISTS subquery
SELECT dept_name
FROM departments d
WHERE EXISTS (
    SELECT 1 
    FROM employees e 
    WHERE e.department_id = d.dept_id
);

-- Subquery in SELECT
SELECT 
    first_name,
    salary,
    (SELECT AVG(salary) FROM employees) AS avg_salary,
    salary - (SELECT AVG(salary) FROM employees) AS difference
FROM employees;

-- ========== UNION - COMBINE RESULTS ==========
-- Must have same number of columns and compatible types
SELECT first_name, last_name FROM employees WHERE city = 'New York'
UNION
SELECT first_name, last_name FROM contractors WHERE city = 'New York';

-- UNION ALL - Includes duplicates
SELECT city FROM employees
UNION ALL
SELECT city FROM offices;

-- ========== WINDOW FUNCTIONS (Advanced) ==========
-- ROW_NUMBER - Unique number per row
SELECT 
    first_name,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees;

-- RANK - With gaps for ties
SELECT 
    first_name,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees;

-- Partition by department
SELECT 
    first_name,
    department_id,
    salary,
    ROW_NUMBER() OVER (
        PARTITION BY department_id 
        ORDER BY salary DESC
    ) AS dept_rank
FROM employees;

-- Running total
SELECT 
    order_date,
    amount,
    SUM(amount) OVER (ORDER BY order_date) AS running_total
FROM orders;

-- ========== CASE STATEMENTS - CONDITIONAL LOGIC ==========
-- Simple CASE
SELECT 
    first_name,
    salary,
    CASE
        WHEN salary >= 100000 THEN 'High'
        WHEN salary >= 60000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category
FROM employees;

-- CASE in aggregate
SELECT 
    department_id,
    COUNT(*) AS total,
    SUM(CASE WHEN salary > 70000 THEN 1 ELSE 0 END) AS high_earners,
    SUM(CASE WHEN salary <= 70000 THEN 1 ELSE 0 END) AS low_earners
FROM employees
GROUP BY department_id;

-- ========== COMMON TABLE EXPRESSIONS (CTEs) ==========
-- Named temporary result set
WITH high_earners AS (
    SELECT * 
    FROM employees 
    WHERE salary > 80000
)
SELECT 
    he.first_name,
    he.salary,
    d.dept_name
FROM high_earners he
JOIN departments d ON he.department_id = d.dept_id;

-- Multiple CTEs
WITH 
dept_avg AS (
    SELECT department_id, AVG(salary) AS avg_sal
    FROM employees
    GROUP BY department_id
),
above_avg AS (
    SELECT e.*
    FROM employees e
    JOIN dept_avg da ON e.department_id = da.department_id
    WHERE e.salary > da.avg_sal
)
SELECT * FROM above_avg;
```


***

## PART 4: DATA MANIPULATION

```sql
-- ========== INSERT - ADD DATA ==========
-- Insert single row
INSERT INTO employees (first_name, last_name, email, salary)
VALUES ('John', 'Doe', 'john@email.com', 55000);

-- Insert multiple rows
INSERT INTO employees (first_name, last_name, email, salary)
VALUES 
    ('Jane', 'Smith', 'jane@email.com', 60000),
    ('Bob', 'Johnson', 'bob@email.com', 58000),
    ('Alice', 'Williams', 'alice@email.com', 62000);

-- Insert from SELECT
INSERT INTO archived_employees
SELECT * FROM employees WHERE hire_date < '2010-01-01';

-- ========== UPDATE - MODIFY DATA ==========
-- Update single row
UPDATE employees
SET salary = 65000
WHERE employee_id = 5;

-- Update multiple columns
UPDATE employees
SET 
    salary = salary * 1.10,
    last_modified = CURRENT_TIMESTAMP
WHERE department_id = 3;

-- Update with calculation
UPDATE products
SET price = price * 0.9  -- 10% discount
WHERE category = 'Electronics';

-- Update with JOIN
UPDATE employees e
JOIN departments d ON e.department_id = d.dept_id
SET e.salary = e.salary * 1.05
WHERE d.dept_name = 'Engineering';

-- ========== DELETE - REMOVE DATA ==========
-- Delete specific rows
DELETE FROM employees WHERE employee_id = 10;

-- Delete with condition
DELETE FROM employees WHERE hire_date < '2000-01-01';

-- Delete with JOIN
DELETE e
FROM employees e
JOIN departments d ON e.department_id = d.dept_id
WHERE d.dept_name = 'Closed Department';

-- Delete all rows (use TRUNCATE instead)
DELETE FROM temporary_table;
TRUNCATE TABLE temporary_table;  -- Faster
```


***

## SQL Best Practices \& Interview Tips

### Performance Optimization

- Always use **indexes** on columns used in WHERE, JOIN, ORDER BY
- Use **EXPLAIN** to analyze query performance
- Avoid SELECT * - specify only needed columns
- Use **LIMIT** when testing queries
- Index foreign keys for faster JOINs


### Common Patterns

- **Pagination:** `LIMIT 10 OFFSET 20`
- **Top N:** `ORDER BY column DESC LIMIT N`
- **Deduplication:** `DISTINCT` or `GROUP BY`
- **Pivot data:** Use CASE with GROUP BY


### Interview Questions Coverage

- Difference between WHERE and HAVING
- INNER vs OUTER JOINs
- Subquery vs JOIN performance
- PRIMARY KEY vs UNIQUE constraint
- DELETE vs TRUNCATE vs DROP

