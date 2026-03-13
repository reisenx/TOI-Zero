# --------------------------------------------------
# File Name : A1-063.py
# Problem   : Movie Ticket
# Author    : Worralop Srichainont
# Date      : 2026-01-02
# --------------------------------------------------

import sys

remaining_seats = int(input().strip())

for line in sys.stdin:
    age, booked_seats = map(int, line.strip().split())

    if age < 15:
        print(-1)
        continue

    if booked_seats > remaining_seats:
        print(-2)
        continue

    remaining_seats -= booked_seats

    total_cost = 150 * booked_seats
    if 15 <= age <= 22:
        total_cost *= 0.8

    if age >= 60:
        total_cost *= 0.5

    print(f"{round(total_cost)} {remaining_seats}")
