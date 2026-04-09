class Instructor:
    def __init__(self,instructor_id, name, department, email):
        self.instructor_id = instructor_id
        self.name = name
        self.department = department
        self.email = email
        self.courses_teaching = [] 

    def assign_course(self, course_code):
        if course_code in self.courses_teaching:
            print(self.name, "already teaching", course_code)
            return False
        self.courses_teaching.append(course_code)
        print(self.name, "is teaching",course_code)
        return True
    
    def display_info(self):
        print(
            "Instructor details",
            "ID:",self.instructor_id,
            "Name:",self.name,
            "Department:", self.department,
            "Email:",self.email,
            "Courses count:", self.get_total_courses()
    )

        if len(self.courses_teaching) > 0:
            for c in self.courses_teaching:
                print("-",c)
        else:
            print("No courses assigned")

    def remove_course(self, course_code):
        if course_code not in self.courses_teaching:
            print(self.name,"is not teaching", course_code)
            return False
        self.courses_teaching.remove(course_code)
        print(course_code, "removed from", self.name)
        return True
    def get_total_courses(self):
        return len(self.courses_teaching)
    
    def to_csv_row(self):
        return f"{self.instructor_id},{self.name},{self.department},{self.email}"