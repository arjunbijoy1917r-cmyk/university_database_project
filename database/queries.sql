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
