"""Iris Dataset - Group Analysis

Calculate measurement means per target species, find largest mean petal length
and smallest mean sepal width, calculate petal_area and display its top 5
flowers, then calculate and interpret the petal measurement correlation.
"""
import pandas as pd

df = pd.read_csv("DATA/iris_dataset.csv")
measurement_columns = df.select_dtypes(include="number").columns
species_means = df.groupby("target")[measurement_columns].mean()
print("Measurement means by species:")
print(species_means)

largest_petal_length_species = species_means["petal length (cm)"].idxmax()
smallest_sepal_width_species = species_means["sepal width (cm)"].idxmin()
print(f"\nLargest average petal length: {largest_petal_length_species}")
print(f"Smallest average sepal width: {smallest_sepal_width_species}")

df["petal_area"] = df["petal length (cm)"] * df["petal width (cm)"]
print("\nFive flowers with the largest petal area:")
print(df.nlargest(5, "petal_area"))

correlation = df["petal length (cm)"].corr(df["petal width (cm)"])
print(f"\nPetal length/width correlation: {correlation:.3f}")
# A correlation close to 1 shows that petal length and width tend to increase
# together; this is an association, not evidence that one causes the other.
