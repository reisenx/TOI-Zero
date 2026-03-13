# --------------------------------------------------
# File Name : A1-013.py
# Problem   : Safe Password
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# Input
letter = input().strip()
num = input().strip()

# Output
if letter == "H" and num == "4567":
    print("safe unlocked")
elif letter == "H":
    print("safe locked - change digit")
elif num == "4567":
    print("safe locked - change char")
else:
    print("safe locked")
