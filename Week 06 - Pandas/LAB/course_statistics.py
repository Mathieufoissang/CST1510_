"""Course Statistics with Groupby

Group by Course and calculate student count, average Grade (1 dp), maximum
Grade, and average Attendance (1 dp), then sort by average Grade descending.
"""
import pandas as pd

df = pd.read_csv("DATA/students.csv")
course_stats = df.groupby("Course").agg(
    Count=("Name", "count"),
    Avg_Grade=("Grade", "mean"),
    Max_Grade=("Grade", "max"),
    Avg_Attendance=("Attendance", "mean"),
)
course_stats[["Avg_Grade", "Avg_Attendance"]] = course_stats[["Avg_Grade", "Avg_Attendance"]].round(1)
print(course_stats.sort_values("Avg_Grade", ascending=False))
