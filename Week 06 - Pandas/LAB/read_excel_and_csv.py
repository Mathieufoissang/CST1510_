"""Reading Excel and CSV Files

Load DATA/data.xlsx and DATA/sample_data.csv. Compare their columns and rows,
combine and remove duplicates, then filter people older than 30 and sort by Age.
"""
import pandas as pd

# Excel support requires openpyxl; install it with: python -m pip install openpyxl
excel_df = pd.read_excel("DATA/data.xlsx")
csv_df = pd.read_csv("DATA/sample_data.csv")
print("Excel data:")
print(excel_df)
print("\nCSV data:")
print(csv_df)
print(f"\nSame columns: {excel_df.columns.tolist() == csv_df.columns.tolist()}")
print(f"Same rows: {excel_df.equals(csv_df)}")

combined = pd.concat([excel_df, csv_df], ignore_index=True).drop_duplicates().reset_index(drop=True)
print("\nCombined data without duplicate rows:")
print(combined)

older_than_30 = combined[combined["Age"] > 30].sort_values("Age")
print("\nPeople older than 30, sorted by Age:")
print(older_than_30)
