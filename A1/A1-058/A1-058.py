# --------------------------------------------------
# File Name : A1-058.py
# Problem   : Coffee Shop
# Author    : Worralop Srichainont
# Date      : 2026-01-02
# --------------------------------------------------

# Initialize to store coffee sales
coffee_sales = []

# Read number of days
days = int(input().strip())

# Read coffee sales for each day
for _ in range(days):
    coffee_sales.append(int(input().strip()))

# Calculate minimum, maximum, total, and average sales
total_sales = sum(coffee_sales)
max_sales = max(coffee_sales)
min_sales = min(coffee_sales)
average_sales = total_sales / days

# Print results
print(total_sales)
print(max_sales)
print(min_sales)
print(f"{average_sales:.1f}")
