# --------------------------------------------------
# File Name : A1-052.py
# Problem   : Basic ATM
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Read the amount of money to withdraw
amount = int(input())

# Calculate and print the number of each banknote
if amount % 100 == 0 and 100 <= amount <= 20000:
    thousands = amount // 1000
    amount %= 1000

    five_hundreds = amount // 500
    amount %= 500

    hundreds = amount // 100

    if thousands > 0:
        print(f"1000 = {thousands}")

    if five_hundreds > 0:
        print(f"500 = {five_hundreds}")

    if hundreds > 0:
        print(f"100 = {hundreds}")

# If the amount is invalid, print ERROR
else:
    print("ERROR")
