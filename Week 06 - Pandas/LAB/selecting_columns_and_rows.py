"""Selecting Columns and Rows

Create grades_df from Name, Course, and Grade and show its first 8 rows. Use
iloc to display positions 5 through 9, and loc to show Name and City at index 3.
"""
import pandas as pd

df = pd.read_csv("DATA/students.csv")
grades_df = df[["Name", "Course", "Grade"]]
print("Grades (first 8 rows):")
print(grades_df.head(8))
print("\nRows at positions 5 to 9:")
print(df.iloc[5:10])
print("\nName and City at index 3:")
print(df.loc[3, ["Name", "City"]])
