# --------------------------------------------------
# File Name : A1-048.py
# Problem   : Electricity Usage
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Initialize total price
total_price = 0.0

# Read the number of electricity units consumed
units = float(input().strip())

# Calculate FT charge
ft_charge = units * 0.5

# Calculate the price for units 1 to 10
total_price += min(units, 10) * 5.0
units -= min(units, 10)

# Calculate the price for units 11 to 50
total_price += min(units, 40) * 7.0
units -= min(units, 40)

# Calculate the price for units 51 to 100
total_price += min(units, 50) * 10.0
units -= min(units, 50)

# Calculate the price for units 101 to 200
total_price += min(units, 100) * 12.0
units -= min(units, 100)

# Calculate the price for units above 200
total_price += units * 15.0

# Calculate VAT
vat = total_price * 0.07

# Add FT charge and VAT to total price
total_price += ft_charge + vat

# Print the total price rounded to 2 decimal places
print(f"{total_price:.2f}")
