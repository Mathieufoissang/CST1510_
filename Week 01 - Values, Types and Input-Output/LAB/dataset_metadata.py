"""Print basic metadata and the number of cells in a dataset."""

dataset_name = input("Dataset name: ")
rows = int(input("Rows: "))
columns = int(input("Columns: "))

print(f'"{dataset_name}"')
print(f"Rows: {rows}")
print(f"Columns: {columns}")
print(f"Cells: {rows * columns}")
