# --------------------------------------------------
# File Name : A1-015.py
# Problem   : Password
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# Input name and age
first_name = input().strip()
last_name = input().strip()
age = input().strip()

# Output password
if len(first_name) > 5 and len(last_name) > 5:
    print(f"{first_name[:2]}{last_name[-1]}{age[-1]}")
else:
    print(f"{first_name[0]}{age}{last_name[-1]}")
