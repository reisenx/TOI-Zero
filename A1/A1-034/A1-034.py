# --------------------------------------------------
# File Name : A1-034.py
# Problem   : Minimum Value
# Author    : Worralop Srichainont
# Date      : 2026-03-13
# --------------------------------------------------

# Input amount of numbers
n_numbers = int(input().strip())

# Find the minimum numbers
min_number = int(input().strip())
for _ in range(n_numbers - 1):
    current_number = int(input().strip())
    min_number = min(min_number, current_number)

# Output the minimum number
print(min_number)
