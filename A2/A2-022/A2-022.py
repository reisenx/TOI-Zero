# Input length of a road and bridge amount
L, N = map(int, input().split())

# Input bridge
K = 2
road = [0] * ((K * L) + 1)
for _ in range(N):
    # Input bridge interval
    start, stop = map(int, input().split())
    # Update road array (1 block = 1/K meters)
    for i in range((K * start) + 1, (K * stop)):
        road[i] += 1

# Output maximum bridge
print(max(road))