# --------------------------------------------------
# File Name : A1-012.py
# Problem   : Reverse a number
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# Input the number and the operation
num = int(input().strip())
operation = input().strip()

# Reverse a number
reversed_num = int(str(num)[::-1])

# Calculate result
result = 0
if operation == "+":
    result = num + reversed_num
elif operation == "*":
    result = num * reversed_num

# Output
print(f"{num} {operation} {reversed_num} = {result}")
