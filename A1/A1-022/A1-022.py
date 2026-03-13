# --------------------------------------------------
# File Name : A1-022.py
# Problem   : Zodiac
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# List of zodiac name and its date range
ZODIACS_INFO = (
    ([12, 22], [12, 31], "capricorn"),
    ([1, 1], [1, 19], "capricorn"),
    ([1, 20], [2, 18], "aquarius"),
    ([2, 19], [3, 20], "pisces"),
    ([3, 21], [4, 21], "aries"),
    ([4, 22], [5, 20], "taurus"),
    ([5, 21], [6, 21], "gemini"),
    ([6, 22], [7, 22], "cancer"),
    ([7, 23], [8, 22], "leo"),
    ([8, 23], [9, 22], "virgo"),
    ([9, 23], [10, 23], "libra"),
    ([10, 24], [11, 21], "scorpio"),
    ([11, 22], [12, 21], "sagittarius"),
)

# Input date
day = int(input())
month = int(input())
date = [month, day]

# Find a zodiac for the input date
ans = ""
for start_date, stop_date, zodiac_name in ZODIACS_INFO:
    if start_date <= date <= stop_date:
        ans = zodiac_name
        break

# Output
print(ans)
