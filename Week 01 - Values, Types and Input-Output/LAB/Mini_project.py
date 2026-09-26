"""
RECORD CHECK  -  my version
===========================

Name  : Mathieu Foissang
Lane  :  AI 
Date  : 26/09/2026

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


#  Test 1 

# Dataset_name: Survey_2026
# Rows loaded: 1187
# Rows Expected 1200

# ==================================
# RECORD CHECK  -  Survey_2026
# ==================================
#  Loaded      :    1187.00
#  Expected    :    1200.00
#  Difference     :      13.00
#  Percent     :      98.92 %
# ==================================



#  Test 2 

#  Dataset_name: Survey_2026
#  Rows loaded: 2500
#  Rows Expected 3000

#  ==================================
#  RECORD CHECK  -  Survey_2026
#  ==================================
#  Loaded      :    2500.00
#  Expected    :    3000.00
#  Difference     :     500.00
#  Percent     :      83.33 %
#  ==================================


# Test 3 


#  Dataset_name: Survey_2026
#  Rows loaded: 500
#  Rows Expected 550

#  ==================================
#  RECORD CHECK  -  Survey_2026
#  ==================================
#  Loaded      :     500.00
#  Expected    :     550.00
#  Difference     :      50.00
#  Percent     :      90.91 %
# ==================================


# Test 4 

# Dataset_name: Survey_2026
# Rows loaded: 250
# Rows Expected 0
# Traceback (most recent call last):
#  File "j:\CST1510_\Week 01 - Values, Types and Input-Output\LAB\template.py", line 21, in <module>
#    percent = (rows_loaded / rows_expected) *100
#               ~~~~~~~~~~~~^~~~~~~~~~~~~~~
# ZeroDivisionError: division by zero