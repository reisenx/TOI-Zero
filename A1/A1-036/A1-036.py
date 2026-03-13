# --------------------------------------------------
# File Name : A1-036.py
# Problem   : Squared Sum
# Author    : Worralop Srichainont
# Date      : 2026-03-13
# --------------------------------------------------

# Input
num = int(input())

# Floor to nearest tens
num = (num // 10) * 10

# Output
for i in range(num, -1, -10):
    print(i, end=" ")
