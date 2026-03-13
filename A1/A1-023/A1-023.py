# --------------------------------------------------
# File Name : A1-023.py
# Problem   : Water State
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# Input temperature
temperature = int(input())
unit = input().strip()

# Output the water state for Celsius unit
if unit.upper() == "C":
    if temperature <= 0:
        print("solid")
    elif temperature < 100:
        print("liquid")
    elif temperature >= 100:
        print("gas")

# Output the water state for Fahrenheit unit
if unit.upper() == "F":
    if temperature <= 32:
        print("solid")
    elif temperature < 212:
        print("liquid")
    elif temperature > 212:
        print("gas")
