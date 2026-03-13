# --------------------------------------------------
# File Name : A1-056.py
# Problem   : Distance in 3D Space
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

import math

# Read coordinates of the two points
x1, y1, z1 = map(int, input().strip().split())
x2, y2, z2 = map(int, input().strip().split())

# Calculate the Euclidean distance in 3D space
distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2))

# Output the distance rounded to two decimal places
print(f"{distance:.2f}")
