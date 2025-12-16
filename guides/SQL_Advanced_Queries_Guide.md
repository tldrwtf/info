# SQL Advanced Queries Guide

This guide delves into advanced SQL querying techniques, moving beyond basic `SELECT` statements to tackle complex data retrieval and manipulation scenarios. Mastering these concepts is crucial for efficient database management and data analysis.

---

## 1. Introduction to Advanced SQL Queries

While basic `SELECT`, `WHERE`, and `ORDER BY` clauses are fundamental, real-world data analysis and application development often require more sophisticated SQL. Advanced queries enable:
*   **Aggregated Reporting:** Summarizing data using `GROUP BY` and aggregate functions.
*   **Data Integration:** Combining data from multiple tables using various `JOIN` types.
*   **Complex Filtering:** Using subqueries and `HAVING` clauses for nuanced conditions.
*   **Analytical Operations:** Performing calculations across sets of table rows using window functions.
*   **Readability and Modularity:** Breaking down complex queries with Common Table Expressions (CTEs).

---

## 2. Aggregation with `GROUP BY` and `HAVING`

`GROUP BY` is used with aggregate functions to group rows that have the same values into summary rows. `HAVING` is then used to filter these grouped results.

### Aggregate Functions

| Function   | Description                                  | Example                 |
| :--------- | :------------------------------------------- | :---------------------- |
| `COUNT()`  | Number of rows / non-NULL values             | `COUNT(*)`, `COUNT(column)` |
| `SUM()`    | Total sum of a numeric column                | `SUM(amount)`           |
| `AVG()`    | Average value of a numeric column            | `AVG(price)`            |
| `MIN()`    | Minimum value in a column                    | `MIN(salary)`           |
| `MAX()`    | Maximum value in a column                    | `MAX(age)`              |

### `GROUP BY` Clause

```sql
-- Count the number of books in each category
SELECT category, COUNT(book_id) AS total_books
FROM Books
GROUP BY category;

-- Calculate the average salary for each department
SELECT department, AVG(salary) AS average_salary
FROM Employees
GROUP BY department;
```

### `HAVING` Clause

`HAVING` is used to filter the results of a `GROUP BY` clause, similar to how `WHERE` filters individual rows.

```sql
-- Find categories with more than 5 books
SELECT category, COUNT(book_id) AS total_books
FROM Books
GROUP BY category
HAVING COUNT(book_id) > 5;

-- Find departments where the average salary is above $60,000
SELECT department, AVG(salary) AS average_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > 60000;
```

---

## 3. Joins

Joins are used to combine rows from two or more tables based on a related column between them.

### `INNER JOIN`

Returns only the rows that have matching values in both tables.

```sql
-- Get book titles and their authors
SELECT B.title, A.author_name
FROM Books AS B
INNER JOIN Authors AS A
ON B.author_id = A.author_id;
```

### `LEFT JOIN` (or `LEFT OUTER JOIN`)

Returns all rows from the left table, and the matching rows from the right table. If there is no match, the right side will have `NULL` values.

```sql
-- Get all authors and their books (even if they have no books)
SELECT A.author_name, B.title
FROM Authors AS A
LEFT JOIN Books AS B
ON A.author_id = B.author_id;
```

### `RIGHT JOIN` (or `RIGHT OUTER JOIN`)

Returns all rows from the right table, and the matching rows from the left table. If there is no match, the left side will have `NULL` values.

```sql
-- Get all books and their authors (even if some books have no author assigned,
-- less common use case in practice as author_id is usually NOT NULL)
SELECT A.author_name, B.title
FROM Authors AS A
RIGHT JOIN Books AS B
ON A.author_id = B.author_id;
```

### `FULL JOIN` (or `FULL OUTER JOIN`)

Returns rows when there is a match in one of the tables. If no match, it returns `NULL` for the columns of the table without a match.

```sql
-- Get all authors and all books, matching where possible (NULLs otherwise)
SELECT A.author_name, B.title
FROM Authors AS A
FULL JOIN Books AS B
ON A.author_id = B.author_id;
```

### `CROSS JOIN`

Returns the Cartesian product of the rows of the joined tables (each row from the first table is combined with each row from the second table).

```sql
-- Combine every author with every book
SELECT A.author_name, B.title
FROM Authors AS A
CROSS JOIN Books AS B;
```

---

## 4. Subqueries

A subquery (or inner query) is a query nested inside another SQL query. It can be used in the `SELECT`, `FROM`, `WHERE`, or `HAVING` clauses.

### `IN` / `NOT IN` Subqueries

```sql
-- Find employees who work in the 'Sales' department
SELECT employee_name
FROM Employees
WHERE department_id IN (SELECT department_id FROM Departments WHERE department_name = 'Sales');

-- Find products that have never been ordered
SELECT product_name
FROM Products
WHERE product_id NOT IN (SELECT product_id FROM Order_Items);
```

### Scalar Subqueries (Returns a single value)

```sql
-- Find employees whose salary is greater than the average salary
SELECT employee_name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);
```

### `EXISTS` / `NOT EXISTS` Subqueries

Used to test for the existence of rows in a subquery. More efficient than `IN` for large subquery results.

```sql
-- Find departments that have at least one employee
SELECT department_name
FROM Departments
WHERE EXISTS (SELECT 1 FROM Employees WHERE Employees.department_id = Departments.department_id);
```

### Subqueries in `FROM` Clause (Derived Tables)

```sql
-- Find the average quantity ordered per product
SELECT product_name, avg_qty_ordered
FROM Products
JOIN (
    SELECT product_id, AVG(quantity) AS avg_qty_ordered
    FROM Order_Items
    GROUP BY product_id
) AS AvgOrders
ON Products.product_id = AvgOrders.product_id;
```

---

## 5. Window Functions

Window functions perform a calculation across a set of table rows that are somehow related to the current row. Unlike aggregate functions, window functions do not group rows; instead, they return a value for each row.

### Basic Syntax

```sql
FUNCTION_NAME(column) OVER ([PARTITION BY column] [ORDER BY column [ASC|DESC]])
```

### Ranking Functions

| Function      | Description                                  |
| :------------ | :------------------------------------------- |
| `ROW_NUMBER()`| Assigns a unique, sequential integer to each row within its partition. |
| `RANK()`      | Assigns a rank within its partition, with gaps for ties. |
| `DENSE_RANK()`| Assigns a rank within its partition, without gaps for ties. |
| `NTILE(n)`    | Divides rows into `n` groups.                |

```sql
-- Rank employees by salary within each department
SELECT
    employee_name,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank
FROM Employees;

-- Get the top 3 employees by salary in the entire company
SELECT * FROM (
    SELECT
        employee_name,
        salary,
        ROW_NUMBER() OVER (ORDER BY salary DESC) as rn
    FROM Employees
) AS RankedEmployees
WHERE rn <= 3;
```

### Value Functions

| Function   | Description                                  |
| :--------- | :------------------------------------------- |
| `LAG(col, offset, default)` | Access data from a previous row.        |
| `LEAD(col, offset, default)` | Access data from a subsequent row.      |

```sql
-- Calculate the difference in sales from the previous month
SELECT
    sale_month,
    monthly_sales,
    LAG(monthly_sales, 1, 0) OVER (ORDER BY sale_month) AS previous_month_sales,
    monthly_sales - LAG(monthly_sales, 1, 0) OVER (ORDER BY sale_month) AS sales_difference
FROM Monthly_Sales;
```

---

## 6. Common Table Expressions (CTEs)

A Common Table Expression (CTE) is a temporary, named result set that you can reference within a single SQL statement (SELECT, INSERT, UPDATE, or DELETE). It improves readability and reusability of complex queries.

### Basic Syntax

```sql
WITH CTE_Name (column1, column2, ...) AS (
    SELECT column1, column2, ...
    FROM another_table
    WHERE condition
)
SELECT *
FROM CTE_Name
WHERE another_condition;
```

### CTE Example

```sql
-- Find the top 3 highest-paid employees in each department using CTE
WITH DepartmentAvgSalary AS (
    SELECT
        department_id,
        AVG(salary) AS avg_dept_salary
    FROM Employees
    GROUP BY department_id
),
RankedEmployees AS (
    SELECT
        employee_name,
        department_id,
        salary,
        ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) as rn
    FROM Employees
)
SELECT
    re.employee_name,
    re.salary,
    das.avg_dept_salary
FROM RankedEmployees AS re
JOIN DepartmentAvgSalary AS das
ON re.department_id = das.department_id
WHERE re.rn <= 3;
```

---

## 7. Set Operators

Set operators combine the results of two or more `SELECT` statements into a single result set.

### `UNION` / `UNION ALL`

Combines the result sets of two or more `SELECT` statements. `UNION` removes duplicates, while `UNION ALL` retains them.

```sql
-- Get all names from two different tables
SELECT first_name FROM Customers
UNION
SELECT employee_name FROM Employees;

-- Get all first names, including duplicates
SELECT first_name FROM Customers
UNION ALL
SELECT employee_name FROM Employees;
```

### `INTERSECT`

Returns only the rows that are common to both `SELECT` statements. (Not supported in MySQL directly, often simulated with `INNER JOIN`).

```sql
-- Find customers who are also employees
SELECT email FROM Customers
INTERSECT
SELECT email FROM Employees;
```

### `EXCEPT` (or `MINUS` in Oracle)

Returns rows from the first `SELECT` statement that are not present in the second `SELECT` statement. (Not supported in MySQL directly, often simulated with `LEFT JOIN` and `WHERE IS NULL`).

```sql
-- Find employees who are not also customers
SELECT email FROM Employees
EXCEPT
SELECT email FROM Customers;
```

---

## 8. Practical Assignments (from new data)

Apply your knowledge of advanced SQL queries to solve the following problems.

### Assignment 1: Student Grades Analysis

Assume the following tables:

*   **`Students`**: `(student_id PK, name, major)`
*   **`Courses`**: `(course_id PK, course_name, department)`
*   **`Enrollments`**: `(student_id FK, course_id FK, grade)`

**Queries:**

1.  **List all students who have enrolled in 'Computer Science' courses.**
    *   *Hint:* Use a subquery or JOIN with `Courses`.

    ```sql
    -- Solution:
    SELECT DISTINCT S.name
    FROM Students S
    JOIN Enrollments E ON S.student_id = E.student_id
    JOIN Courses C ON E.course_id = C.course_id
    WHERE C.department = 'Computer Science';
    ```

2.  **Find the average grade for each course.**
    *   *Hint:* Use `GROUP BY` and `AVG()`.

    ```sql
    -- Solution:
    SELECT C.course_name, AVG(E.grade) AS average_grade
    FROM Courses C
    JOIN Enrollments E ON C.course_id = E.course_id
    GROUP BY C.course_name;
    ```

3.  **Identify students who have a grade of 'A' in at least one course.**
    *   *Hint:* Use `EXISTS` or `IN`.

    ```sql
    -- Solution:
    SELECT S.name
    FROM Students S
    WHERE EXISTS (
        SELECT 1
        FROM Enrollments E
        WHERE E.student_id = S.student_id AND E.grade = 'A'
    );
    ```

4.  **List students who have taken all courses offered by the 'Math' department.**
    *   *Hint:* Count distinct math courses and compare.

    ```sql
    -- Solution:
    WITH MathCoursesCount AS (
        SELECT COUNT(course_id) AS total_math_courses
        FROM Courses
        WHERE department = 'Math'
    )
    SELECT S.name
    FROM Students S
    JOIN Enrollments E ON S.student_id = E.student_id
    JOIN Courses C ON E.course_id = C.course_id
    WHERE C.department = 'Math'
    GROUP BY S.name
    HAVING COUNT(DISTINCT C.course_id) = (SELECT total_math_courses FROM MathCoursesCount);
    ```

### Assignment 2: Employee Department Analysis

Assume the following tables:

*   **`Employees`**: `(employee_id PK, name, salary, department_id FK)`
*   **`Departments`**: `(department_id PK, department_name, location)`

**Queries:**

1.  **Find the names of all employees who earn more than the average salary of their respective departments.**
    *   *Hint:* Use a correlated subquery or a window function.

    ```sql
    -- Solution using Correlated Subquery:
    SELECT E1.name, E1.salary, D.department_name
    FROM Employees E1
    JOIN Departments D ON E1.department_id = D.department_id
    WHERE E1.salary > (
        SELECT AVG(E2.salary)
        FROM Employees E2
        WHERE E2.department_id = E1.department_id
    );

    -- Solution using Window Function:
    SELECT name, salary, department_name
    FROM (
        SELECT
            E.name,
            E.salary,
            D.department_name,
            AVG(E.salary) OVER (PARTITION BY D.department_name) AS avg_dept_salary
        FROM Employees E
        JOIN Departments D ON E.department_id = D.department_id
    ) AS Subquery
    WHERE salary > avg_dept_salary;
    ```

2.  **List the top 2 highest-paid employees in each department.**
    *   *Hint:* Use a ranking window function.

    ```sql
    -- Solution:
    WITH RankedEmployees AS (
        SELECT
            E.name,
            D.department_name,
            E.salary,
            ROW_NUMBER() OVER (PARTITION BY D.department_name ORDER BY E.salary DESC) as rn
        FROM Employees E
        JOIN Departments D ON E.department_id = D.department_id
    )
    SELECT name, department_name, salary
    FROM RankedEmployees
    WHERE rn <= 2;
    ```

3.  **Calculate the running total of salaries for each department, ordered by employee ID.**
    *   *Hint:* Use a window function with `SUM()` and `ORDER BY`.

    ```sql
    -- Solution:
    SELECT
        E.name,
        D.department_name,
        E.salary,
        SUM(E.salary) OVER (PARTITION BY D.department_name ORDER BY E.employee_id) AS running_total_salary
    FROM Employees E
    JOIN Departments D ON E.department_id = D.department_id;
    ```

---

## See Also

-   **[SQL and SQLAlchemy Cheat Sheet](../cheatsheets/SQL_and_SQLAlchemy_Cheat_Sheet.md)** - Basic SQL syntax and ORM concepts.
-   **[SQL DDL Guide](../guides/SQL_DDL_Guide.md)** - For understanding how database structures are created and modified
-   **[Big O Notation Cheat Sheet](../cheatsheets/Big_O_Notation_Cheat_Sheet.md)** - Understanding the performance implications of complex queries.
