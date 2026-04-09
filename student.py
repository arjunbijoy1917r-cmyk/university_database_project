class Student:
    def __init__(self,student_id, name,age,email):
        self.student_id = student_id
        self.name = name
        self.age =age
        self.email =email
#--                          ---
        self.grades = {}      
        self.enrolled_courses = []

    def add_grade(self,course_name,grade):
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            return False
 
        self.grades[course_name] = grade
        print("Grade", grade, "added for student",self.name, "in",course_name)
        return True
    
    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0.0

        total = 0
        for g in self.grades.values():
            total = total+g
        average = total / len(self.grades)
        return round(average, 2)
    
    def display_info(self):
        avg = self.get_average_grade()
        print(
             
            "Student details"
            "ID:",self.student_id, 
            "Name:",self.name, 
            "Age:", self.age, 
            "Email:",self.email, 
            "Average GPA:", avg
        )   
        if len(self.grades) > 0:
                print("Grades:")
                for course in self.grades:
                    grade = self.grades[course]
                    print(course,grade)
        else:
                print("No grades")

    def check_pass(self):
        avg = self.get_average_grade()

        if avg >= 50:
            return "Pass"
        else:
            return "Fail"
    def for_csv_row(self):
        return f"{self.student_id},{self.name},{self.age},{self.email}"
 