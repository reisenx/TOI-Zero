# Input flower layer and flower amount
L, N = map(int, input().split())

# Calculate total flower on each layer
total = 0
n = 0
while(total < N):
    # Add flower on the first n * L columns
    total += (n * L) * L
    # Add flower on the last L columns
    total += (L * (L + 1)) / 2
    # Go to the next layer
    n += 1

# Output
print(n)