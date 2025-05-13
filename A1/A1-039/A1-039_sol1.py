# Input
n = int(input())
# Calculate n!
ans = 1
for i in range(1, n + 1):
    ans *= i
# Output
print(ans)