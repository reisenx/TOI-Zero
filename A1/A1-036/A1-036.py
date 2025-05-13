# Input
num = int(input())
# Output
for i in range(num - (num % 10), -1, -10):
    print(i, end = ' ')