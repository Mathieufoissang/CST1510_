"""Handling Missing Data

Load students_missing.csv, report missing counts and rows, fill missing Grade
with the original column mean rounded to 1 dp, fill Scholarship and Course
with Unknown, drop rows missing Attendance or Age, verify no missing values,
and save DATA/students_clean.csv without an index.
"""
import pandas as pd

df = pd.read_csv("DATA/students_missing.csv")
print("Missing values per column:")
print(df.isnull().sum())
print("\nRows with at least one missing value:")
print(df[df.isnull().any(axis=1)])

grade_average = round(df["Grade"].mean(), 1)
df["Grade"] = df["Grade"].fillna(grade_average)
df["Scholarship"] = df["Scholarship"].fillna("Unknown")
df["Course"] = df["Course"].fillna("Unknown")
df = df.dropna(subset=["Attendance", "Age"])

print("\nMissing values after cleaning:")
print(df.isnull().sum())
df.to_csv("DATA/students_clean.csv", index=False)
print("\nSaved cleaned data to DATA/students_clean.csv")
