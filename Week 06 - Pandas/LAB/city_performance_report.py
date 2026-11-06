"""City Performance Report

Create a city summary containing student count, average Grade and Attendance,
Pass_Rate percentage, and Performance relative to the overall average Grade.
Save DATA/city_report.csv without an index and print it sorted by Avg_Grade.
"""
import pandas as pd

df = pd.read_csv("DATA/students.csv")
overall_average = df["Grade"].mean()
city_report = df.groupby("City").agg(
    Students=("Name", "count"),
    Avg_Grade=("Grade", "mean"),
    Avg_Attendance=("Attendance", "mean"),
    Pass_Rate=("Grade", lambda grades: (grades >= 60).mean() * 100),
)
city_report["Performance"] = city_report["Avg_Grade"].apply(
    lambda average: "Above Average" if average > overall_average else "Below Average"
)
city_report[["Avg_Grade", "Avg_Attendance", "Pass_Rate"]] = city_report[
    ["Avg_Grade", "Avg_Attendance", "Pass_Rate"]
].round(1)
city_report = city_report[["Students", "Avg_Grade", "Avg_Attendance", "Pass_Rate", "Performance"]]
city_report.to_csv("DATA/city_report.csv", index=False)
print(city_report.sort_values("Avg_Grade", ascending=False))
