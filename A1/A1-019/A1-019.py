# --------------------------------------------------
# File Name : A1-019.py
# Problem   : All the Same
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# Input
a = int(input())
b = int(input())
c = int(input())

# Output
if a == b == c:
    print("all the same")
elif a != b and b != c and a != c:
    print("all different")
else:
    print("neither")
