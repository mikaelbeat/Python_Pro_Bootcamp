
from student import Student


student1 = Student("Test person", "testing")
print(student1.get_student_details())

student1.add_class("Art")
student1.add_class("Math")
print(student1.classes)