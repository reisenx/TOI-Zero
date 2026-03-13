# --------------------------------------------------
# File Name : A1-044.py
# Problem   : Ticket
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Read input
data = input().strip().split()
age, day = int(data[0]), data[1].strip().lower()

# Calculate ticket price by age
ticket_price = 0
if 5 <= age <= 18:
    ticket_price = 100
elif age >= 19:
    ticket_price = 150

# Apply discount for Wednesday
if day == "wed":
    ticket_price //= 2

# Print the ticket price
print(ticket_price)
