"""Cars Dataset

Load DATA/CARS.text. Show the best and worst 5 mpg cars, 4-cylinder cars with
hp > 90, cylinder group count/average mpg/average hp, and efficiency counts
(High >= 25 mpg, Medium >= 18 mpg, else Low). Save cars_clean.csv without index.
"""
import pandas as pd

df = pd.read_csv("DATA/CARS.text")
print("Five best mpg values:")
print(df.nlargest(5, "mpg"))
print("\nFive worst mpg values:")
print(df.nsmallest(5, "mpg"))

print("\n4-cylinder cars with horsepower above 90:")
print(df[(df["cyl"] == 4) & (df["hp"] > 90)])

print("\nStatistics by cylinder count:")
print(df.groupby("cyl").agg(
    Count=("model", "count"),
    Average_MPG=("mpg", "mean"),
    Average_HP=("hp", "mean"),
).round(1))

df["Efficiency"] = df["mpg"].apply(
    lambda mpg: "High" if mpg >= 25 else "Medium" if mpg >= 18 else "Low"
)
print("\nCars per efficiency category:")
print(df["Efficiency"].value_counts())
df.to_csv("cars_clean.csv", index=False)
print("\nSaved cars_clean.csv")
