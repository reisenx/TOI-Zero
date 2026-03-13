# --------------------------------------------------
# File Name : A1-018.py
# Problem   : Roman Numbers
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# List of Roman numbers
ROMAN_NUMS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

# Input an Arabic number
num = int(input())

# Output a Roman number
if 1 <= num <= 9:
    print(ROMAN_NUMS[num - 1])
elif num < 0:
    print("Error : Please input positive number")
else:
    print("Error : Out of range")
