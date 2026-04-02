class Student:
    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        return f"Student(name={self.name!r})"
    
class Course:
    def __init__(self,title):
        self.title = title
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def roster(self):
        names = []
        for s in self.students:
            names.append(s.name)
        return names
    
    def find_student(self, name):
        target = name.strip().lower()
        for s in self.students:
            if s.name.lower() == target:
                return s
        return None 
    
course = Course("Python101")
course.add_student(Student("Kelvin"))
course.add_student(Student("Madison"))
print(course.title)
print(course.roster())

found = course.find_student("    KELVIN ")
missing = course.find_student("    KEVIN ")