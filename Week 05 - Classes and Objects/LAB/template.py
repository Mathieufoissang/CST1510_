"""
RECORD CHECK  -  my version
===========================

Name  : Mathieu Foissang
Lane  :  AI Data Science
Date  : 23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

from pathlib import Path


class Record:

    over_limit_count = 0  # shared by all Record instances

    def __init__(self, label, value, limit):
        self.label = label
        self.value = float(value)
        self.limit = float(limit)
        if self.limit <= 0:
            raise ValueError("The total capacity (limit) must be positive.")

    def percent(self):
        return (self.value / self.limit) * 100

    def status(self):
        percentage = self.percent()
        if percentage >= 100:
            return "OVER LIMIT"
        if percentage >= 90:
            return "WARNING"
        return "OK"


def load_records(path):
    records = []
    with open(path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            parts = [part.strip() for part in line.split(",")]
            if len(parts) != 3:
                raise ValueError(f"Invalid record on line {line_number}: {line!r}")
            label, value, limit = parts
            records.append(Record(label, float(value), float(limit)))
    return records


def print_reports(records):
    Record.over_limit_count = 0 
    for record in records:
        result = record.status() 
        if result == "OVER LIMIT":
            Record.over_limit_count += 1
        print()
        print("=" * 38)
        print(f" RECORD CHECK - {record.label}")
        print("=" * 38)
        print(f" Used:    {record.value:g} GB")
        print(f" Total:   {record.limit:g} GB")
        print(f" Usage:   {record.percent():.1f}%")
        print(f" Status:  {result}")
        print("=" * 38)
    print(f"\n{Record.over_limit_count} of {len(records)} records are OVER LIMIT")


def main():
    path = Path(__file__).with_name("records_sample.txt")
    records = load_records(path)
    print_reports(records)


if __name__ == "__main__":
    main()

