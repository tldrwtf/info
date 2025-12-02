-- ==========================================
-- SQL PRACTICE SOLUTIONS
-- Covers: DDL, Basic Queries, and Advanced Joins
-- ==========================================

-- ------------------------------------------
-- 1. Data Definition Language (DDL)
-- ------------------------------------------

-- Task: Create Students Table
CREATE TABLE Students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE
);

-- Task: Create Courses Table
CREATE TABLE Courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    instructor VARCHAR(100),
    credits INT DEFAULT 3
);

-- Task: Create Enrollment (Junction) Table
CREATE TABLE Enrollments (
    student_id INT,
    course_id INT,
    grade VARCHAR(2),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);

-- ------------------------------------------
-- 2. Basic Data Manipulation (DML)
-- ------------------------------------------

-- Insert Data
INSERT INTO Students (name, email) VALUES 
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com');

INSERT INTO Courses (title, instructor) VALUES 
('Math 101', 'Dr. Smith'),
('History 202', 'Prof. Jones');

-- Select All Students
SELECT * FROM Students;

-- Select Specific Student
SELECT * FROM Students WHERE name = 'Alice';

-- Update Data
UPDATE Courses SET instructor = 'Dr. Wilson' WHERE title = 'Math 101';

-- Delete Data
DELETE FROM Students WHERE name = 'Bob';

-- ------------------------------------------
-- 3. Advanced Queries
-- ------------------------------------------

-- JOIN: View Student Enrollments
SELECT s.name, c.title, e.grade
FROM Students s
JOIN Enrollments e ON s.id = e.student_id
JOIN Courses c ON c.id = e.course_id;

-- AGGREGATION: Count students per course
SELECT c.title, COUNT(e.student_id) as student_count
FROM Courses c
LEFT JOIN Enrollments e ON c.id = e.course_id
GROUP BY c.id, c.title;

-- FILTERING GROUPS: Courses with more than 10 students
SELECT c.title, COUNT(e.student_id) as student_count
FROM Courses c
JOIN Enrollments e ON c.id = e.course_id
GROUP BY c.id, c.title
HAVING COUNT(e.student_id) > 10;
