# --------------------------------------------------
# File Name : A1-057.py
# Problem   : Dice
# Author    : Worralop Srichainont
# Date      : 2026-01-02
# --------------------------------------------------

# Read the guessed value and the actual value
guessed_value = int(input().strip())
actual_value = int(input().strip())

# Validate the input
if 1 <= guessed_value <= 6 and 1 <= actual_value <= 6:
    # Compare the guessed value with the actual value
    if guessed_value == actual_value:
        print("Correct!")
    else:
        print("Wrong!")

# If the input is invalid
else:
    print("Invalid")
