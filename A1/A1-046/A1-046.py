# --------------------------------------------------
# File Name : A1-046.py
# Problem   : Product Export
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Input product types
product_types = int(input().strip())

# Input product quantities
products = [int(num) for num in input().strip().split()]

# Count products with even and odd quantities
even_amount = 0
odd_amount = 0
for quantity in products:
    if quantity % 2 == 0:
        even_amount += 1
    else:
        odd_amount += 1

# Output results
print(f"SUM {sum(products)}")
print(f"EVEN {even_amount}")
print(f"ODD {odd_amount}")
