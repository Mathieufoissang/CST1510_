"""## Task 1: Questionnaire
Write a program that asks for name, interest, nationality, course, and programming experience, then prints a formatted summary using escape sequences (`\n`, `\t`).

**Example Output:**
```
User Information:
	Name: Alice
	Interest: Security
	Nationality: UK
	Course: Cyber
	Experience: Beginner
```"""

name = input("Name: ")
interest = input("Interest: ")
nationality = input("Nationality: ")
course = input("Course: ")
experience = input("Programming experience: ")

print("\nUser Information:")
print(f"\nName: {name}\nInterest: {interest}\nNationality: {nationality}\nCourse: {course}\nExperience:  {experience}")
