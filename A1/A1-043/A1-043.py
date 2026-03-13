# --------------------------------------------------
# File Name : A1-043.py
# Problem   : Online Game Score
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Read a player details
base_score = int(input().strip())
bonus_score = int(input().strip())
consecutive_days = int(input().strip())

# Calculate total score with bonus
total_score = base_score + bonus_score
if consecutive_days > 3:
    total_score *= 1.5

# Determine ranking code
ranking_code = 1
if total_score >= 1500:
    ranking_code = 5
elif total_score >= 1000:
    ranking_code = 4
elif total_score >= 500:
    ranking_code = 3
elif total_score >= 200:
    ranking_code = 2

# Determine special code
special_code = 0
if ranking_code == 5 and consecutive_days >= 7:
    special_code = 99
elif ranking_code == 4 and bonus_score > 300:
    special_code = 88

# Output results
print(int(total_score))
print(ranking_code)
print(special_code)
