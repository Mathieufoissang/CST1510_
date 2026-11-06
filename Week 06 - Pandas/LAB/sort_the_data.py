"""Sort the Data

Show the top 5 students by Grade, highest first. Then sort by City A-Z and
Grade lowest-first and display the first 10 rows.
"""
import pandas as pd

df = pd.read_csv("DATA/students.csv")
print("Top 5 grades:")
print(df.sort_values("Grade", ascending=False).head(5))
print("\nSorted by City, then Grade (first 10):")
print(df.sort_values(["City", "Grade"], ascending=[True, True]).head(10))
