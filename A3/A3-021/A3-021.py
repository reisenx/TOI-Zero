# Input
N, K = map(int, input().split())

# Input time per round of each athlete
runs = []
for _ in range(N):
    runs.append(int(input()))
fastest = min(runs)

# Calculate time delay of each athlete compared to the fastest
# Eliminate athlete by consider time delay when running K - 1 rounds
eliminated = 0
for i in range(N):
    delay = (runs[i] - fastest) * (K - 1)
    if(delay >= fastest):
        eliminated += 1

# Output
print(N - eliminated)