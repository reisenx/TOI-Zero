# --------------------------------------------------
# File Name : A1-038.py
# Problem   : Display Symbol
# Author    : Worralop Srichainont
# Date      : 2026-03-13
# --------------------------------------------------

# Symbol pattern
SYMBOL_PATTERN = "****X"

# Input length of the symbol sequence
n = int(input())

# Construct the symbol sequence
symbol_sequence = (
    SYMBOL_PATTERN * (n // len(SYMBOL_PATTERN))
    + SYMBOL_PATTERN[: n % len(SYMBOL_PATTERN)]
)

# Output
print(symbol_sequence)
