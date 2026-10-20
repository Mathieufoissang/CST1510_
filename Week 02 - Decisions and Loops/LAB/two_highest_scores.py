"""Read scores and display the highest and second-highest scores."""

student_count = int(input("Enter the number of students: "))

if student_count < 2:
    print("Enter at least two students.")
else:
    highest = float("-inf")
    second_highest = float("-inf")

    for student in range(student_count):
        score = float(input(f"Enter student {student + 1}'s score: "))
        if score > highest:
            second_highest = highest
            highest = score
        elif score > second_highest:
            second_highest = score

    print(f"Highest score: {highest:g}")
    print(f"Second-highest score: {second_highest:g}")
