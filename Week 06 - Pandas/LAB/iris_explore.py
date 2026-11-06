"""Iris Dataset - Explore

Load DATA/iris_dataset.csv. Show the first 5 rows, shape, dtypes, describe(),
species counts by target, missing values, and duplicated row count.
"""
import pandas as pd

df = pd.read_csv("DATA/iris_dataset.csv")
print("First 5 rows:")
print(df.head())
print(f"\nShape: {df.shape}")
print("\nData types:")
print(df.dtypes)
print("\nSummary statistics:")
print(df.describe())
print("\nFlowers per target species:")
print(df["target"].value_counts())
print("\nMissing values by column:")
print(df.isnull().sum())
print(f"\nDuplicated rows: {df.duplicated().sum()}")
