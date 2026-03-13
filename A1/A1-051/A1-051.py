# --------------------------------------------------
# File Name : A1-051.py
# Problem   : Conan
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Define the alphabet
ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

# Read original message
message = input().strip().lower()

# Read shift value
k = int(input())

# Encrypt the message by using Caesar cipher
encrypted_message = ""
for char in message:
    if char in ALPHABETS:
        idx = ALPHABETS.index(char)
        encrypted_message += ALPHABETS[(idx + k) % len(ALPHABETS)]
    else:
        encrypted_message += char

# Print the encrypted message
print(encrypted_message)
