# --------------------------------------------------
# File Name : A1-064.py
# Problem   : Game Score
# Author    : Worralop Srichainont
# Date      : 2026-01-03
# --------------------------------------------------

# Read commands from input
commands = input().strip().split()[1:]

# Calculate total score
total_score = 0
for command in commands:
    if command.strip() == "+":
        total_score += 10
    elif command.strip() == "-":
        total_score -= 5

# Output the total score
print(total_score)
