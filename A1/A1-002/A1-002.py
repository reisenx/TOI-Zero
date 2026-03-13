# --------------------------------------------------
# File Name : A1-002.py
# Problem   : Money Exchange
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Input amount of money
money = int(input().strip())

# Output amount of coins
print(f"10 = {money // 10}")

money %= 10
print(f"5 = {money // 5}")

money %= 5
print(f"2 = {money // 2}")

money %= 2
print(f"1 = {money}")
