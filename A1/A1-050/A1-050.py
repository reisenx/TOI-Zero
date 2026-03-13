# --------------------------------------------------
# File Name : A1-050.py
# Problem   : Hotel Customer
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Initialize counters
male_count = 0
female_count = 0

# Read list of card numbers
cards = [int(num) for num in input().strip().split()]
cards.pop()

# Count male and female from card numbers
for card in cards:
    if card % 2 == 0:
        female_count += 1
    else:
        male_count += 1

# Print the male customers, female customers, and total customers
print(f"{male_count} {female_count} {male_count + female_count}")
