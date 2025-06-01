# Input map dimension
R, C = map(int, input().split())

# Input bomb position
B = int(input())
bomb_count = [[0] * C for _ in range(R)]
for _ in range(B):
    # Mark bomb position as unavailable
    r, c = map(int, input().split())
    bomb_count[r][c] = -1
    # Add 1 to bomb counter in all adjacent grid
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            # Check out of bounds
            if(not(0 <= r + dr < R and 0 <= c + dc < C)):
                continue
            # Skip bomb position
            if(bomb_count[r + dr][c + dc] == -1):
                continue
            bomb_count[r + dr][c + dc] += 1
# Output
map = ''
for r in range(R):
    for c in range(C):
        if(bomb_count[r][c] == -1):
            map += 'x '
        else:
            map += str(bomb_count[r][c]) + ' '
    map += '\n'
print(map)