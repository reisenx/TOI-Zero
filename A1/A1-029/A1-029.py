# --------------------------------------------------
# File Name : A1-029.py
# Problem   : Count Vowels
# Author    : Worralop Srichainont
# Date      : 2026-03-13
# --------------------------------------------------

# Vowel constants
VOWELS = ("a", "e", "i", "o", "u")

# Input and converts all to lowercase
text = input().strip().lower()

# Count vowels
vowel_count = 0
for char in text:
    if char in VOWELS:
        vowel_count += 1

# Output
print(vowel_count)
