# Input amount of money
money = int(input())
# Output amount of coins
print("10 =", money // 10)
money %= 10
print("5 =", money // 5)
money %= 5
print("2 =", money // 2)
money %= 2
print("1 =", money)