
class Student:
    def __init__(self, name, course):
        self.course = course
        self.name = name
        self.classes = 0
        print("New student is created.")

    def get_student_details(self):
        return f"Your name is {self.name} and study {self.course}. "
    
    def add_class(self, name):
        self.classes += 1
