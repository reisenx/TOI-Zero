# --------------------------------------------------
# File Name : A1-037.py
# Problem   : Roman Number
# Author    : Worralop Srichainont
# Date      : 2026-03-13
# --------------------------------------------------

# Roman number on each digits
THOUSANDS = ["", "M", "MM", "MMM"]
HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

# Input number and extract digits
digits = [0, 0, 0, 0]
for digit in input().strip():
    digits.append(int(digit))

# Construct roman number
roman_number = (
    THOUSANDS[digits[-4]] + HUNDREDS[digits[-3]] + TENS[digits[-2]] + ONES[digits[-1]]
)

# Output
print(roman_number)
