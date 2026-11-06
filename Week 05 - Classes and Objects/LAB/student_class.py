"""Student Class

Create a class Student with attributes name and age set in __init__. Create
two student objects and print their attributes using dot notation.
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student_one = Student("Alice", 19)
student_two = Student("Ben", 21)

print(student_one.name, student_one.age)
print(student_two.name, student_two.age)
