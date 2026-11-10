"""Printing Objects with __str__

Add a __str__ method to the Student class from Task 1 (for example, "Alice
(age 19)"). Create a list of 5 students and print them with a loop using
print(student).
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} (age {self.age})"


students = [
    Student("Alice", 19),
    Student("Ben", 20),
    Student("Chloe", 18),
    Student("Daniel", 21),
    Student("Eva", 19),
]

for student in students:
    print(student)
