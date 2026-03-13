# --------------------------------------------------
# File Name : A1-067.py
# Problem   : Member Cost
# Author    : Worralop Srichainont
# Date      : 2026-01-03
# --------------------------------------------------

# Initialize membership status and total price
is_member = False
total_price = 0.0

# Read membership status from input
data = input().strip()
if data == "Y":
    is_member = True

# Read number of items and their prices
items_count = int(input().strip())
for _ in range(items_count):
    total_price += float(input().strip())

# Apply discounts based on membership status and total price
if is_member:
    total_price *= 0.95
elif not is_member and total_price >= 500:
    total_price *= 0.97

# Output the final total price rounded to two decimal places
print(f"{total_price:.2f}")
