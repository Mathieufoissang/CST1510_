"""Full EDA Report

Find the most popular course and top 3 students, compare average attendance
for Pass and Fail students, calculate and interpret Grade/Attendance
correlation, and export and print one summary row per course.
"""
import pandas as pd

df = pd.read_csv("DATA/students.csv")
course_counts = df["Course"].value_counts()
print(f"Most popular course: {course_counts.index[0]} ({course_counts.iloc[0]} students)")
print("\nTop 3 students by grade:")
print(df.nlargest(3, "Grade")[["Name", "Course", "Grade"]])

df["Result"] = df["Grade"].apply(lambda grade: "Pass" if grade >= 60 else "Fail")
print("\nAverage attendance by result:")
print(df.groupby("Result")["Attendance"].mean().round(1))

correlation = df["Attendance"].corr(df["Grade"])
print(f"\nAttendance/Grade correlation: {correlation:.3f}")
# Correlation near 1 indicates a strong positive relationship, near 0 little
# linear relationship, and near -1 a strong negative relationship. Correlation
# describes association and does not prove that attendance causes grades.

df["Has_Scholarship"] = df["Scholarship"] == "Yes"
course_report = df.groupby("Course").agg(
    Student_Count=("Name", "count"),
    Avg_Grade=("Grade", "mean"),
    Avg_Attendance=("Attendance", "mean"),
    Pass_Rate_Pct=("Result", lambda results: (results == "Pass").mean() * 100),
    Scholarship_Pct=("Has_Scholarship", "mean"),
).reset_index()
course_report["Avg_Grade"] = course_report["Avg_Grade"].round(1)
course_report["Avg_Attendance"] = course_report["Avg_Attendance"].round(1)
course_report["Pass_Rate_Pct"] = course_report["Pass_Rate_Pct"].round(1)
course_report["Scholarship_Pct"] = (course_report["Scholarship_Pct"] * 100).round(1)
course_report.to_csv("DATA/eda_report.csv", index=False)
print("\nCourse EDA report:")
print(course_report)
