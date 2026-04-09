class Course:
    def __init__(self, course_code,course_name, credits,max_students=20):
        self.course_code = course_code
        self.course_name = course_name
        self.credits =credits
        self.max_students = max_students
        ##----
        self.enrolled_students = [] 

    def add_student(self, student_id):
        if student_id in self.enrolled_students:
            print("Student",student_id, "is existing in",self.course_name)
            return False
        if len(self.enrolled_students) >= self.max_students:
            print(self.course_name,"is full")
            return False

        self.enrolled_students.append(student_id)
        print("Student",student_id," is enrolled  in",self.course_name)
        return True
    
    def student_count(self):
        return len(self.enrolled_students)
    
    def remove_student(self, student_id):
        if student_id not in self.enrolled_students:
            print( "Student", student_id,"is not existing")
            return False
        self.enrolled_students.remove(student_id)
        print("Student",student_id,"is removed from", self.course_name)
        return True
    
    def display_info(self):
        print(
            "Course info",
            "Code:", self.course_code,
            "Name:", self.course_name,
            "Credits:", self.credits,
            "Students:", self.student_count(), "out of", self.max_students)
        
    def to_csv_row(self):
        return f"{self.course_code},{self.course_name},{self.credits},{self.max_students}"
    