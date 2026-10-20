"""Read student names and scores, then display the highest scorer."""

student_count = int(input("Enter the number of students: "))

if student_count < 1:
    print("Enter at least one student.")
else:
    highest_name = ""
    highest_score = float("-inf")

    for student in range(student_count):
        name = input(f"Enter student {student + 1}'s name: ")
        score = float(input(f"Enter {name}'s score: "))
        if score > highest_score:
            highest_name = name
            highest_score = score

    print(f"Highest score: {highest_name} with {highest_score:g}")
