# --------------------------------------------------
# File Name : A1-049.py
# Problem   : Hotel Room without 13th Floor
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Initial values of each part of the room number
part_01 = 13
part_02 = 0
part_03 = 0

# Read password input
password = input().strip()

# Determine part 1 based on password digits
if int(password[0]) > 5:
    part_01 = 9
elif int(password[1]) > 5:
    part_01 = 10
elif int(password[2]) > 5:
    part_01 = 11
elif int(password[3]) > 5:
    part_01 = 12
elif int(password[4]) > 5:
    part_01 = 14

# Determine part 2 based on password properties
if password == password[::-1]:
    if int(password[0]) + int(password[4]) > 5:
        part_02 = 1
    elif int(password[1]) * int(password[3]) > 5:
        part_02 = 2
else:
    if int(password[4]) > 0 and int(password[0]) % int(password[4]) > 5:
        part_02 = 1
    elif int(password[1]) - int(password[4]) > 5:
        part_02 = 2

# Determine part 3 based on password properties
sums = 0
product = 1
for digit in password:
    sums += int(digit)
    product *= int(digit)

if sums > 25:
    part_03 = 1
elif product > 55:
    part_03 = 2

# Output the room number
print(f"{part_01}{part_02}{part_03}")
