from student import Student
from course import Course
from instructor import Instructor
from enrollments import (
    Enrollment,
    save_students_to_file,
    load_students_from_file,
    save_courses_to_file,
    save_enrollments_to_file,
    load_enrollments_from_file,
)
students = []
courses = []
instructors = []
enrollments = []


def find_student(student_id):
    for s in students:
        if s.student_id ==student_id:
            return s
    return None

def find_course(course_code):
    for c in courses:
        if c.course_code  == course_code:
            return c
    return None

def find_instructor(instructor_id):
    for i in instructors:
        if i.instructor_id == instructor_id:
            return i
    return None


def add_student():
    print("Add a student")
    sid = input("Enter student ID: ")

    if find_student(sid) != None:
        print("Student already exists")
        return

    name = input("Enter name: ")
    try:
        age = int(input("Enter age: "))
    except:
        print("Invalid age")
        return
    email = input("Enter email: ")

    new_student = Student(sid, name,age, email)
    students.append(new_student)
    print("student added successfully")

#details of every students..
def show_all_students():
    if students == []:
        print("No students")
    else:
        print("Total students:", len(students))

        for s in students:
            s.display_info()


def add_grade_to_student():
    print("Add Grade")

    sid = input("Enter student ID: ")
    student = find_student(sid)

    if student == None:
        print("Student not found")
        return
    course_name = input("enter course name: ")
    try:
        grade = float(input("Enter grade:(0-100)"))
    except:
        print("Invalid grade")
        return
    
    student.add_grade(course_name,grade)


def add_course():
    print("Add a Course")
    code =input("Enter course code: ")

    if find_course(code) != None:
        print("course already exists")
        return

    name = input("Enter course name: ")
    credits = int(input( "Enter credits: "))
    max_s = int(input("enter max students: "))
    new_course = Course(code, name, credits, max_s)
    courses.append(new_course)

    print("Course is added")

def show_all_courses():
    if len(courses) == 0:
        print("No courses")
        return
    print("Total courses:",len(courses))

    for c in courses:
        c.display_info()



def add_instructor():
    print("add Instructor")
    iid = input("Enter instructor ID: ")

    if find_instructor(iid) != None:
        print("Instructor already exists")
        return

    try:
        name = input("Enter name: ")
        dept = input("Enter department: ")
        email = input("enter email: ")
    except:
        print("Error")
        return

    new_instructor = Instructor(iid , name, dept,email)
    instructors.append(new_instructor)
    print("Instructor added")

def assign_instructor_to_course():
    print(" To assign Instructor")
    iid = input("Enter instructor ID: ")
    instructor = find_instructor(iid)

    if instructor == None:
        print("Instructor not found")
        return
    
    code = input("Enter course code: ")
    course =find_course(code)
    if course == None:
        print("Course not found")
        return
    instructor.assign_course(code)


def show_all_instructors():
    if not instructors:
        print("No instructors are found in the system.")
        return
    for i in instructors:
        i.display_info()


def enroll_student():
    print("\n Enroll Student")
    sid = input("enter student ID: ")
    student = find_student(sid)
    if student is None:
        print("student not found")
        return

    code = input("Enter course code: ")
    course = find_course(code)
    if course is None:
        print("course not found")
        return

    for e in enrollments:
        if e.student_id == sid and e.course_code == code and e.is_active():
            print("Student already enrolled in this course")
            return
        
    date = input("Enter enrollment date: ")
    new_enroll = Enrollment(sid,code, date)
    enrollments.append(new_enroll)
    course.add_student(sid)
    print("enrollment is added")


def show_all_enrollments():
    """Show every enrollment record."""
    if not enrollments:
        print("No enrollments recorded.")
        return

    print(f"\nTotal enrollments: {len(enrollments)}")
    for e in enrollments:
        e.display_info()


def save_all_data():
    print("\n data is saving...")
    save_students_to_file(students)
    save_courses_to_file(courses)
    save_enrollments_to_file(enrollments)
    print("Data saved.")

def load_saved_data():
    print("\nLoading data...")

    raw_students = load_students_from_file()
    for row in raw_students:
        sid = row[0]
        name = row[1]
        age = int(row[2])
        email = row[3]
        s = Student(sid , name,age, email)
        students.append(s)

    raw_enrollments = load_enrollments_from_file()

    for row in raw_enrollments:
        sid = row[0]
        code = row[1] 
        date = row[2]
        status = row[3]
        e = Enrollment(sid , code, date, status)
        enrollments.append(e)

    print("Data is here")
#menu list----------

def show_menu():
    print("\n==========================")
    print("  University Management System")
    print("=============================")
    print("1. Add Student")
    print("2. Show All Students")
    print("3.Add Grade to Student")
    print("4. Add Course")
    print("5. Show All Courses")
    print("6. Add Instructor")
    print("7. Assign Instructor to Course")
    print("8.Show All Instructors")
    print("9. Enroll Student in Course")
    print("10. Show All Enrollments")
    print("11.Save All Data")
    print("0. Exit")
   


def run():

    load_saved_data()
    while True:
        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            add_grade_to_student()
        elif choice == "4":
            add_course()
        elif choice == "5":
            show_all_courses()
        elif choice == "6":
            add_instructor()
        elif choice == "7":
            assign_instructor_to_course()
        elif choice == "8":
            show_all_instructors()
        elif choice == "9":
            enroll_student()
        elif choice == "10":
            show_all_enrollments()
        elif choice == "11":
            save_all_data()
        elif choice == "0":
            save_all_data()
            print("End,Data saved")
            break
        else:
            print("the option doesn't exist, please try again.")


#if file executed directly
if __name__ == "__main__":
    run()