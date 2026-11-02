"""
AI / DATA SCIENCE DATASET CHECK
==============================

Name : Mathieu Foissang
Lane : AI Data Science
Date : 23/10/2026
Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


class Dataset:
    incomplete_count = 0

    def __init__(self, name, rows_loaded, rows_expected):
        self.name = name
        self.rows_loaded = int(rows_loaded)
        self.rows_expected = int(rows_expected)

        if self.rows_expected <= 0:
            raise ValueError("Rows expected must be positive.")

    def percent_loaded(self):
        return (self.rows_loaded / self.rows_expected) * 100

    def status(self):
        percentage = self.percent_loaded()

        if percentage >= 100:
            return "COMPLETE"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "INCOMPLETE"


def print_reports(datasets):
    Dataset.incomplete_count = 0

    for dataset in datasets:
        result = dataset.status()

        if result == "INCOMPLETE":
            Dataset.incomplete_count += 1

        print()
        print("=" * 40)
        print(f" AI / DATA SCIENCE - {dataset.name}")
        print("=" * 40)
        print(f" Rows Loaded:   {dataset.rows_loaded}")
        print(f" Rows Expected: {dataset.rows_expected}")
        print(f" Completion:    {dataset.percent_loaded():.1f}%")
        print(f" Status:        {result}")
        print("=" * 40)

    print(
        f"\n{Dataset.incomplete_count} of {len(datasets)} datasets are INCOMPLETE"
    )


def main():
    datasets = []

    number = int(input("How many datasets do you want to enter? "))

    for i in range(number):
        print(f"\nDataset {i + 1}")

        name = input("Dataset name: ")
        rows_loaded = int(input("Rows loaded: "))
        rows_expected = int(input("Rows expected: "))

        datasets.append(Dataset(name, rows_loaded, rows_expected))

    print_reports(datasets)


if __name__ == "__main__":
    main()
