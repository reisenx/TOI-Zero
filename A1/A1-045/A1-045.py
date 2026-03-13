# --------------------------------------------------
# File Name : A1-045.py
# Problem   : Taxi Fare Calculation
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Initialize total fare
total_fare = 35

# Read distance from input
distance = int(input().strip())

# Calculate fare based on distance
total_fare += (5 * min(9, max(0, distance - 1))) + (8 * max(0, distance - 10))

# Output the total fare
print(total_fare)
