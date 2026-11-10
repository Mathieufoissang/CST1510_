"""Add New Columns

Add Result using apply() and a lambda (Pass for Grade >= 60, otherwise Fail),
add Combined_Score = Grade * 0.7 + Attendance * 0.3 rounded to 1 dp, display
the first 10 relevant rows, and print pass/fail counts.
"""
import pandas as pd

df = pd.read_csv("DATA/students.csv")
df["Result"] = df["Grade"].apply(lambda grade: "Pass" if grade >= 60 else "Fail")
df["Combined_Score"] = (df["Grade"] * 0.7 + df["Attendance"] * 0.3).round(1)
print(df[["Name", "Grade", "Attendance", "Result", "Combined_Score"]].head(10))
print("\nPass and fail counts:")
print(df["Result"].value_counts())
