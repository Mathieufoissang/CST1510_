"""City vs Scholarship Analysis

Using students.csv, count students per City, calculate average Grade by City
in descending order, compare average Grade by Scholarship, and count by City
and Scholarship to identify the city with the most scholarship students.
"""
import pandas as pd

df = pd.read_csv("DATA/students.csv")
print("Students per city:")
print(df.groupby("City").size().sort_values(ascending=False))
print("\nAverage grade by city:")
print(df.groupby("City")["Grade"].mean().sort_values(ascending=False).round(1))

scholarship_averages = df.groupby("Scholarship")["Grade"].mean()
print("\nAverage grade by scholarship status:")
print(scholarship_averages.round(1))
if "Yes" in scholarship_averages.index and "No" in scholarship_averages.index:
    difference = scholarship_averages["Yes"] - scholarship_averages["No"]
    print(f"Difference (Yes minus No): {difference:.1f} grade points")

city_scholarship_counts = df.groupby(["City", "Scholarship"]).size().unstack(fill_value=0)
print("\nStudents by city and scholarship status:")
print(city_scholarship_counts)
if "Yes" in city_scholarship_counts.columns:
    top_city = city_scholarship_counts["Yes"].idxmax()
    print(f"Most scholarship students: {top_city} ({city_scholarship_counts.loc[top_city, 'Yes']})")
