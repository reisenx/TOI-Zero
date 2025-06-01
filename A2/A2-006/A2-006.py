# Input map
N = int(input())
maps = [[0] * N for _ in range(N)]

for r in range(N):
    row = input().strip()
    for c in range(N):
        if(row[c] == 'X'):
            maps[r][c] = 1

# Depth First Search (DFS) algorithm on a 2D grid implemented by a stack.
# Starts at the bottom-right, and go up and right direction only.
DR = [-1, 0]
DC = [0, -1]
ans = 0

# Starts at the bottom-right of a map
grid = []
grid.append([N - 1, N - 1])
maps[N - 1][N - 1] = 1
ans += 1

# Traverse to adjacent grid
while(len(grid) > 0):
    # Get current grid information
    r, c = grid[-1]
    grid.pop()
    
    for i in range(2):
        # Check out of bounds
        if(not (0 <= r + DR[i] < N and 0 <= c + DC[i] < N)):
            continue
        # Check obstacle and already passed
        if(maps[r + DR[i]][c + DC[i]] != 0):
            continue
        # Go to that grid and add to a stack
        maps[r + DR[i]][c + DC[i]] = 1
        grid.append([r + DR[i], c + DC[i]])
        # Count possible start points
        ans += 1

# Output
print(ans)