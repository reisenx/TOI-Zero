# --------------------------------------------------
# File Name : A1-033.py
# Problem   : Count Vowels
# Author    : Worralop Srichainont
# Date      : 2026-03-13
# --------------------------------------------------

# Vowel constants
VOWELS = ("A", "E", "I", "O", "U")

# Input number of letters
n_letters = int(input())

# Count vowels
vowel_count = 0
for _ in range(n_letters):
    letter = input().strip()
    if letter in VOWELS:
        vowel_count += 1

# Output
print(vowel_count)
