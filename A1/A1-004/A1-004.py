# --------------------------------------------------
# File Name : A1-004.py
# Problem   : Exam Result
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# Input scores
exercise = int(input())
midterm = int(input())
finals = int(input())

# Output
if exercise >= 5 and midterm >= 20 and finals >= 25:
    print("pass")
else:
    print("fail")
