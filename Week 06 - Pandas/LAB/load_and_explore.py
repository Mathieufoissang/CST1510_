"""Load and Explore

Load DATA/students.csv and print the first 5 rows, last 3 rows, shape, and
column names as a list.
"""
import pandas as pd

df = pd.read_csv("DATA/students.csv")
print("First 5 rows:")
print(df.head(5))
print("\nLast 3 rows:")
print(df.tail(3))
print(f"\nShape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
