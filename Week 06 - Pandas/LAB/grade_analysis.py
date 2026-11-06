"""Grade Analysis with Multiple Conditions

Show Computer Science or Data Science students with Grade > 75 and
Attendance > 80; list students at risk (Grade < 60) and count them; and show
Manchester scholarship students with Grade > 80.
"""
import pandas as pd

df = pd.read_csv("DATA/students.csv")
selected_courses = df["Course"].isin(["Computer Science", "Data Science"])
high_performers = df[selected_courses & (df["Grade"] > 75) & (df["Attendance"] > 80)]
print("Course, grade, and attendance criteria:")
print(high_performers[["Name", "Course", "Grade", "Attendance"]])

at_risk = df[df["Grade"] < 60]
print(f"\nStudents at risk of failing: {len(at_risk)}")
print(at_risk[["Name", "Grade"]])

scholarship_students = df[(df["City"] == "Manchester") & (df["Scholarship"] == "Yes") & (df["Grade"] > 80)]
print("\nManchester scholarship students with a grade above 80:")
print(scholarship_students[["Name", "Grade", "Scholarship"]])
