# --------------------------------------------------
# File Name : A1-021.py
# Problem   : Leap Year
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# Input
year = int(input())

# Output
if year < 1582 or year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("yes")
else:
    print("no")
