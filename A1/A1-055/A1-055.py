# --------------------------------------------------
# File Name : A1-055.py
# Problem   : Promotion Price
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Define item prices
ITEM_PRICES = (25, 40, 55)

# Read item amounts
item_amounts = list(map(int, input().strip().split()))

# Calculate total price
total_price = 0
for i in range(3):
    total_price += ITEM_PRICES[i] * item_amounts[i]

# Apply discount if total items are 3 or more
if sum(item_amounts) >= 3:
    total_price *= 0.9

# Output the total price as an integer
print(int(total_price))
