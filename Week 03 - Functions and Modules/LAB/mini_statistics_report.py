"""Report basic statistics for five numeric values."""

import statistics as stats

try:
    values = [float(value) for value in input("Enter five numbers separated by spaces: ").split()]
    if len(values) != 5:
        print("Please enter exactly five numbers.")
    else:
        print("Values: " + ", ".join(f"{value:g}" for value in values))
        print(f"Total = {sum(values):.2f}")
        print(f"Mean = {stats.mean(values):.2f}")
        print(f"Median = {stats.median(values):.2f}")
        print(f"Std Dev = {stats.stdev(values):.2f}")
except ValueError:
    print("Please enter numeric values separated by spaces.")
