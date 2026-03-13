# --------------------------------------------------
# File Name : A1-009.py
# Problem   : Pass
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# Input score
midterm = int(input())
finals = int(input())

# Calculate total score
total = midterm + finals

# Output
print(total)
if total >= 50:
    print("pass")
else:
    print("fail")
