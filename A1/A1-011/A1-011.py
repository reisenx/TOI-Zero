# --------------------------------------------------
# File Name : A1-011.py
# Problem   : THEOS
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# Input text
text = input().strip()

# Initialize current letter and counts
curr_letter = text[0]
curr_count = 1

# Iterate each letter and count
for i in range(1, len(text)):
    # If the current letter is the same, just count
    if text[i] == curr_letter:
        curr_count += 1

    # Otherwise, output and change to the new letter
    else:
        # Output the current count
        print(f"{curr_count}{curr_letter}", end="")

        # Change to the new letter
        curr_letter = text[i]
        curr_count = 1

# Do not forget to output the last one
print(f"{curr_count}{curr_letter}")
