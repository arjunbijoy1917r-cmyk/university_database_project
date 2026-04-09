CREATE DATABASE university_db;
USE university_db; 

CREATE TABLE students(
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100)NOT NULL,
    last_name VARCHAR(100 ) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    Gender VARCHAR(50),
    date_of_birth DATE
);
CREATE TABLE instructors(
    instructor_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100)NOT NULL,
    email VARCHAR(100) UNIQUE
);
CREATE TABLE courses(
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL
);
CREATE TABLE modules(
    module_id INT PRIMARY KEY AUTO_INCREMENT,
    module_name VARCHAR(100) NOT NULL,
    instructor_id INT NOT NULL,
    course_id INT NOT NULL
);
CREATE TABLE enrollments(
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE
);

ALTER TABLE modules
ADD CONSTRAINT fk_modules_course
FOREIGN KEY (course_id ) REFERENCES courses(course_id);
ALTER TABLE modules
ADD CONSTRAINT fk_modules_instructor
FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id);

ALTER TABLE enrollments
ADD CONSTRAINT fk_enrollments_student
FOREIGN KEY (student_id) REFERENCES students(student_id);
ALTER TABLE enrollments
ADD CONSTRAINT fk_enrollments_course
FOREIGN KEY (course_id) REFERENCES courses(course_id);

-- sample_data
INSERT INTO instructors (first_name, last_name, email) VALUES
('Arjun', 'Smith', 'arjun.452@gmail.com'),
('Carlsen', 'Brown', 'emily.brown@yahoo.com'),
('Jackson', 'Clark', 'michael.123@uni.com'),
('Fredrick','Dannis', 'fdrick@gmail.com');

INSERT INTO courses (course_name, credits) VALUES
('Business Management', 8),
('Foreign Language', 3),
('Database Systems', 4),
('Data Science', 3),
('Software Engineering', 5);

INSERT INTO students (first_name, last_name, email, gender, date_of_birth) VALUES
('Arjun', 'Bijoy', 'arj234@gmail.com', 'male', '2006-05-10'),
('Pinky', 'Gandhi', 'rahul@gmail.com', 'female', '2005-08-15'),
('Muhammed', 'Singh', 'priya@yahoo.com', 'male', '2003-02-20'),
('David', 'Verma', 'vd828@gmail.com', 'male', '2005-11-25');

INSERT INTO modules (module_name, instructor_id, course_id) VALUES
('AI', 1, 1),
('Mathematics', 2, 2),
('Machine Learning', 3, 4),
('Foreign Language', 2, 2);

INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES
(1, 1, '2026-01-10'),
(2, 2, '2026-01-12'),
(3, 3, '2026-01-15'),
(4, 4, '2026-01-18'),
(1, 2, '2026-01-20'),
(2, 3, '2026-01-22');


-- JOIN
SELECT 
    s.first_name,
    s.last_name,
    c.course_name,
    e.enrollment_date
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id;
-- Aggregation
SELECT 
    c.course_name,
    COUNT(e.student_id) AS total_students
FROM enrollments e
JOIN courses c ON e.course_id = c.course_id
GROUP BY c.course_name;

-- order
SELECT course_name, credits
FROM courses
ORDER BY credits DESC;

-- delete
DELETE FROM enrollments
WHERE enrollment_id = 3;
-- 
SELECT * FROM students;