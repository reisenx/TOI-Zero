# --------------------------------------------------
# File Name : A1-069.py
# Problem   : RYW Cinema
# Author    : Worralop Srichainont
# Date      : 2026-01-03
# --------------------------------------------------

import math

# Read number of rows and columns
rows = int(input().strip())
columns = int(input().strip())

# Print the adult seats
for _ in range(math.ceil(rows / 2)):
    print("A " * columns)

# Print the kids seats
for _ in range(math.floor(rows / 2)):
    print("K " * columns)
