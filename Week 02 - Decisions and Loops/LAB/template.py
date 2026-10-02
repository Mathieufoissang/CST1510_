"""
RECORD CHECK  -  AI / Data Science
==================================

Name  : Mathieu Foissang
Lane  : AI / Data Science
Date  : 02 October 2026

Run it: python template.py
"""

while True:
    label = input("Enter dataset name (or quit to finish): ")
    if label == "quit":
        break

dataset_name = input("Dataset_name: ")     
value = float(input("Enter rows loaded: "))
limit = float(input("Enter rows expected: "))


difference = limit - value
percent = (value / limit) * 100


if percent >= 100:
    status = "OVER LIMIT"
    over_limit_count += 1

elif percent >= 90:
    status = "WARNING"

else:
    status = "OK"


    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"  Rows loaded   : {value:>10.2f}")
    print(f"  Rows expected : {limit:>10.2f}")
    print(f"  Difference    : {difference:>10.2f}")
    print(f"  Percent       : {percent:>10.2f} %")
    print(f"  Status        : {status:>10}")

    print("=" * 34)
    print()







"""
RECORD CHECK  -  AI / Data Science
==================================

Name  : Mathieu Foissang
Lane  : AI / Data Science
Date  : 02 October 2026

Run it: python template.py
"""

while True:
    label = input("Enter dataset name (): ")
    if label == "Survey_123":
        break

dataset_name = input("Dataset_name: ")     
value = float(input("Enter rows loaded: "))
limit = float(input("Enter rows expected: "))


difference = limit - value
percent = (value / limit) * 100


if percent >= 100:
    status = "OVER LIMIT"
    over_limit_count += 1

elif percent >= 90:
    status = "WARNING"

else:
    status = "OK"


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Rows loaded   : {value:>10.2f}")
print(f"  Rows expected : {limit:>10.2f}")
print(f"  Difference    : {difference:>10.2f}")
print(f"  Percent       : {percent:>10.2f} %")
print(f"  Status        : {status:>10}")

print("=" * 34)
print()
