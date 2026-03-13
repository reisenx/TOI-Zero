# --------------------------------------------------
# File Name : A1-039_sol-01.py
# Problem   : Factorial
# Author    : Worralop Srichainont
# Date      : 2026-03-13
# --------------------------------------------------

# Input
n = int(input())

# Calculate the factorial
result = 1
for i in range(1, n + 1):
    result *= i

# Output result
print(result)
