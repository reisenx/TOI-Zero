# --------------------------------------------------
# File Name : A1-054.py
# Problem   : Bonus
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Define bonus values
FIXED_BONUS = {"M": 1500, "B": 1000, "G": 500}

PERCENTAGE_BONUS = {
    "M": (0.06, 0.08, 0.10),
    "B": (0.05, 0.06, 0.07),
    "G": (0.04, 0.05, 0.06),
}

# Read employee data
data = input().strip().split()
position, work_age, salary = data[0].upper(), int(data[1]), int(data[2])

# Calculate bonus
bonus = 0
if position in FIXED_BONUS:
    bonus += FIXED_BONUS[position]
    if work_age < 5:
        bonus += salary * PERCENTAGE_BONUS[position][0]
    elif work_age <= 10:
        bonus += salary * PERCENTAGE_BONUS[position][1]
    else:
        bonus += salary * PERCENTAGE_BONUS[position][2]

# Output the rounded bonus
print(round(bonus))
