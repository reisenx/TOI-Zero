# --------------------------------------------------
# File Name : A1-061.py
# Problem   : Tiktok Filter
# Author    : Worralop Srichainont
# Date      : 2026-01-02
# --------------------------------------------------

# Read input values
radius, x, y = map(int, input().split())

# Determine the position of the point relative to the circle
if (x**2) + (y**2) < (radius**2):
    print("IN")
elif (x**2) + (y**2) == (radius**2):
    print("ON")
else:
    print("OUT")
