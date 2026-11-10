"""Scholarship Deep Dive

Calculate scholarship participation, compare average grades and attendance
for scholarship and non-scholarship students, show scholarship counts and
rates by course, and include a 3-4 sentence findings summary as a comment.
"""
import pandas as pd

df = pd.read_csv("DATA/students.csv")
has_scholarship = df["Scholarship"] == "Yes"
scholarship_pct = has_scholarship.mean() * 100
print(f"Students with a scholarship: {scholarship_pct:.1f}%")

grade_by_scholarship = df.groupby("Scholarship")["Grade"].mean()
print("\nAverage grade by scholarship status:")
print(grade_by_scholarship.round(1))
if "Yes" in grade_by_scholarship.index and "No" in grade_by_scholarship.index:
    grade_difference = grade_by_scholarship["Yes"] - grade_by_scholarship["No"]
    print(f"Grade difference (Yes minus No): {grade_difference:.1f} points")

course_scholarships = df.assign(Has_Scholarship=has_scholarship).groupby("Course").agg(
    Total_Students=("Name", "count"),
    Scholarship_Students=("Has_Scholarship", "sum"),
)
course_scholarships["Scholarship_Rate_Pct"] = (
    course_scholarships["Scholarship_Students"] / course_scholarships["Total_Students"] * 100
).round(1)
print("\nScholarship rates by course:")
print(course_scholarships.sort_values("Scholarship_Rate_Pct", ascending=False))

attendance_by_scholarship = df.groupby("Scholarship")["Attendance"].mean()
print("\nAverage attendance by scholarship status:")
print(attendance_by_scholarship.round(1))
if "Yes" in attendance_by_scholarship.index and "No" in attendance_by_scholarship.index:
    attendance_difference = attendance_by_scholarship["Yes"] - attendance_by_scholarship["No"]
    print(f"Attendance difference (Yes minus No): {attendance_difference:.1f} points")

# Findings summary: 40% of students have a scholarship. Scholarship students
# average 86.1 in Grade and 90.1 in Attendance, compared with 69.5 and 75.5 for
# students without scholarships. Mathematics has the highest scholarship rate
# (66.7%), while Data Science has the lowest (16.7%). These sample associations
# do not show that scholarships cause higher grades or attendance.
