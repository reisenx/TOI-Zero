# --------------------------------------------------
# File Name : A1-024.py
# Problem   : Car Tax
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# List of car tax
CAR_TAX = [[1250, 1400, 2000], [1100, 1300, 1700], [1000, 1200, 1500]]

# Input
year = int(input())
motor_volume = int(input())

# Find index for year
year_idx = -1
if year <= 1990:
    year_idx = 0
elif year <= 2000:
    year_idx = 1
else:
    year_idx = 2

# Find index for motor
motor_idx = -1
if motor_volume <= 1500:
    motor_idx = 0
elif motor_volume <= 2000:
    motor_idx = 1
else:
    motor_idx = 2

# Output tax
print(CAR_TAX[year_idx][motor_idx])
