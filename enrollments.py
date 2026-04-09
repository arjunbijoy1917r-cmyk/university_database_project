import csv
import os
 
class Enrollment:
    def __init__(self, student_id,course_code, enrollment_date,status="active"):
        self.student_id =student_id
        self.course_code = course_code
        self.enrollment_date= enrollment_date
        self.status = status   

    def drop_enrollment(self):
        if self.status == "dropped":
            print("The  enrollment was already dropped")
            return False

        self.status = "dropped"
        print("Student" ,self.student_id, "dropped",self.course_code)
        return True  
    
    def is_active(self):
        return self.status == "active"
    
    def display_info(self):
        print(
            "Enrollment details",
            "Student ID:" , self.student_id,
            "Course Code:",self.course_code,
            "Date:",self.enrollment_date,
            "Status:", self.status
        )

    def to_csv_row(self):
        return f"{self.student_id},{self.course_code},{self.enrollment_date},{self.status}"

def save_students_to_file(students,filename="students.csv"):
    try:
        file = open(filename ,"w")
        file.write("student_id,name,age,email\n")
        for student in students:
            row = str(student.student_id) + ","+student.name + "," + str(student.age) + ","+ student.email  +"\n"
            file.write(row)
        file.close()
        print("Students are saved to",filename)

    except:
        print("Error saving the students file")

def load_students_from_file():
    students_data = []
    file = open("students.csv","r")
    file.readline()

    for line in file:
        line = line.strip()
        parts = line.split(",")
        students_data.append(parts)
    file.close()

    print("Loaded" , len(students_data),"students")
    return students_data

def save_courses_to_file(courses):
    file = open("courses.csv", "w")
    print("course_code,course_name,credits,max_students", file=file)
    for c in courses:
        print(c.course_code,c.course_name, c.credits, c.max_students,  sep=",", file=file)

    file.close()
    print("Courses saved")

def save_enrollments_to_file(enrollments):
    file = open("enrollments.csv", "w")
    print("student_id,course_code,date,status", file=file)
    for e in enrollments:
        print(e.student_id, e.course_code, e.enrollment_date, e.status, sep=",", file=file)

    file.close()

    print("enrollments are saved")

def load_enrollments_from_file():
    records = []
    file = open("enrollments.csv","r")
    file.readline()

    for line in file:
        line = line.strip()
        parts =line.split(",")
        records.append(parts)

    file.close()
    print( "Loaded",len(records), "enrollments")
    return records