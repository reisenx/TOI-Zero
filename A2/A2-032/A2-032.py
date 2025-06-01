# Input dimension of a grid
R, C = map(int, input().split())

# Input position of pokemon
grid = [[0] * C for _ in range(R)]
dp = [[0] * C for _ in range(R)]

P = int(input())
for _ in range(P):
    r, c = map(int, input().split())
    # Update amount o pokemon on a grid
    grid[r][c] += 1
    # Mark position (r, c) as unavailable to catch
    dp[r][c] = -1
    # Update catch pokemon amount on adjacent grid
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            # Check out of bounds
            if(not (0 <= r + dr < R and 0 <= c + dc < C)):
                continue
            # Skip unavailable position
            if(dp[r + dr][c + dc] == -1):
                continue
            # Skip current grid
            if(dr == 0 and dc == 0):
                continue
            # Add catch pokemon amount
            dp[r + dr][c + dc] += 1

# Find maximum catch pokemon amount
ans = 0
for r in range(R):
    ans = max(ans, max(dp[r]))
print(ans)