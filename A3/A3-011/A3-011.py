# Input prices and calculate prefix sum
N = int(input())
P = list(map(int, input().split()))
sum = [0] * N
sum[0] = P[0]
for i in range(1, N):
    sum[i] = sum[i - 1] + P[i]

# Get the sum from P[a] to P[b]
def get_sum(a:int, b:int) -> int:
    if(a == 0):
        return sum[b]
    return sum[b] - sum[a - 1]

# Find all unique sum by using set
unique = set()
for i in range(N):
    for j in range(i, N):
        unique.add(get_sum(i, j))
# Output
print(len(unique))