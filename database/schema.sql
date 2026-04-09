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
