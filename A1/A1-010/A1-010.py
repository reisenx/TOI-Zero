# --------------------------------------------------
# File Name : A1-010.py
# Problem   : Ticket
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# Input
age = int(input())
ticket_type = input().strip()

# Output
if age < 18 or ticket_type.lower() == "s":
    print(20)
else:
    print(50)
