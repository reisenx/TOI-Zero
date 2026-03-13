# --------------------------------------------------
# File Name : A1-041.py
# Problem   : Multiplication Table
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Input a number
num = int(input().strip())

# Print multiplication table from 1 to 12
for i in range(1, 13):
    print(f"{num} * {i} = {num * i}")
