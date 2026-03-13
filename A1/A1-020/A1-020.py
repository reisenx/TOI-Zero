# --------------------------------------------------
# File Name : A1-020.py
# Problem   : Increasing Decreasing
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# Input numbers
a = int(input())
b = int(input())
c = int(input())

# Output
if a < b < c:
    print("increasing")
elif a > b > c:
    print("decreasing")
else:
    print("neither")
