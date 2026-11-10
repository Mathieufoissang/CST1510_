"""Gradebook

Create a Course that stores a course name and Student objects, each with a
name and a list of marks. Add add_student(), average_mark(student_name), and
top_student() methods. Create a course with at least 4 students and print
each student's average and the top student.
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_mark(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def average_mark(self, student_name):
        for student in self.students:
            if student.name.casefold() == student_name.casefold():
                return student.average_mark()
        raise ValueError(f"No student named '{student_name}' is enrolled.")

    def top_student(self):
        students_with_marks = [student for student in self.students if student.marks]
        if not students_with_marks:
            return None
        return max(students_with_marks, key=lambda student: student.average_mark())


course = Course("Introduction to Programming")
course.add_student(Student("Alice", [82, 91, 87]))
course.add_student(Student("Ben", [75, 79, 84]))
course.add_student(Student("Chloe", [93, 89, 96]))
course.add_student(Student("Daniel", [68, 77, 73]))

print(f"{course.name} gradebook:")
for student in course.students:
    print(f"{student.name}: average mark = {course.average_mark(student.name):.1f}")

best_student = course.top_student()
if best_student is not None:
    print(
        f"Top student: {best_student.name} "
        f"(average {best_student.average_mark():.1f})"
    )
else:
    print("There are no marks to rank yet.")
