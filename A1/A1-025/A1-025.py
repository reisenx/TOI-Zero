# --------------------------------------------------
# File Name : A1-025.py
# Problem   : Cards
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# Dict of card value and card groups
CARD_VALUES = {
    "A": "ace",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "10",
    "J": "jack",
    "Q": "queen",
    "K": "king",
}
CARD_GROUPS = {"D": "diamonds", "H": "hearts", "S": "spades", "C": "clubs"}

# Input card and find its value and group
card = input().upper()
card_value = card[:-1]
card_group = card[-1]

# Output card name
print(f"{CARD_VALUES[card_value]} of {CARD_GROUPS[card_group]}")
