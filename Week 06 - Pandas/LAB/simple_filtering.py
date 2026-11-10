"""Simple Filtering

Show students in London and their count; show Name and Grade for students
whose Grade is below 65; and count students in each City with value_counts().
"""
import pandas as pd

df = pd.read_csv("DATA/students.csv")
london_students = df[df["City"] == "London"]
print("Students in London:")
print(london_students)
print(f"Students in London: {len(london_students)}")
print("\nStudents with a grade below 65:")
print(df.loc[df["Grade"] < 65, ["Name", "Grade"]])
print("\nStudents per city:")
print(df["City"].value_counts())
