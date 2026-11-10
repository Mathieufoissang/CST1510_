"""Data Types and Summary

Show each column's data type and describe() summary statistics. Print the
average grade, maximum attendance, and youngest student's age.
"""
import pandas as pd

df = pd.read_csv("DATA/students.csv")
print("Data types:")
print(df.dtypes)
print("\nSummary statistics:")
print(df.describe())
print(f"\nAverage grade: {df['Grade'].mean():.2f}")
print(f"Maximum attendance: {df['Attendance'].max()}")
print(f"Youngest student's age: {df['Age'].min()}")
