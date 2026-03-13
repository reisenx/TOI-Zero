# --------------------------------------------------
# File Name : A1-026.py
# Problem   : Count odd even
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# Input numbers
a = int(input())
b = int(input())
c = int(input())

# Count odd numbers
odd = (a % 2) + (b % 2) + (c % 2)

# Output
print(f"even {3 - odd}")
print(f"odd {odd}")
