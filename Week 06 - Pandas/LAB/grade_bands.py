"""Grade Bands

Create Grade_Band using A for 90-100, B for 80-89, C for 70-79, D for 60-69,
and F below 60. Display students and band counts, then identify the course
with the most students in band A or B.
"""
import pandas as pd

df = pd.read_csv("DATA/students.csv")
df["Grade_Band"] = pd.cut(
    df["Grade"], bins=[-1, 60, 70, 80, 90, 101],
    labels=["F", "D", "C", "B", "A"], right=False,
)
print(df[["Name", "Grade", "Grade_Band"]])
print("\nStudents per grade band:")
print(df["Grade_Band"].value_counts().sort_index())

high_band_counts = df[df["Grade_Band"].isin(["A", "B"])].groupby("Course").size()
if not high_band_counts.empty:
    top_course = high_band_counts.idxmax()
    print(f"\nMost A/B students: {top_course} ({high_band_counts[top_course]})")
else:
    print("\nNo students have an A or B grade band.")
