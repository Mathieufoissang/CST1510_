"""
RECORD CHECK  -  my version
===========================

Name  : Mathieu Foissang
Lane  :  AI 
Date  : 26/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


dataset_name = input("Dataset_name: ")     
rows_loaded = float(input("Rows loaded: ")) 
rows_expected = float(input("Rows Expected "))

difference = rows_expected - rows_loaded
percent = (rows_loaded / rows_expected) *100

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {dataset_name}")
print("=" * 34)

print(f"  Loaded      : {rows_loaded:>10.2f}")
print(f"  Expected    : {rows_expected:>10.2f}")
print(f"  Difference     : {difference:>10.2f}")
print(f"  Percent     : {percent:>10.2f} %")


print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
