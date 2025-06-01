# Input dimension of a grid
row, col = map(int, input().split())
# Input rabbit position
pos = list(map(int, input().split()))

# Input infected points and mark on grid
grid = [[0] * col for _ in range(row)]
safe_points = row * col
N = int(input())
for _ in range(N):
    # Input infected points
    r, c = map(int, input().split())
    # Mark infected points
    for dr in range(-2, 3):
        for dc in range(-2, 3):
            # Check out of bounds
            if(not (0 <= r + dr < row and 0 <= c + dc < col)):
                continue
            # Decrease safe points
            if(grid[r + dr][c + dc] == 0):
                safe_points -= 1
            # Mark 100% infected points
            if(dr == 0 and dc == 0):
                grid[r + dr][c + dc] = 100
            # Mark 60% infected points
            elif(abs(dr) <= 1 and abs(dc) <= 1):
                grid[r + dr][c + dc] = max(grid[r + dr][c + dc], 60)
            # Mark 20% infected points
            else:
                grid[r + dr][c + dc] = max(grid[r + dr][c + dc], 20)
# Output
print(safe_points)
print(grid[pos[0]][pos[1]], end = '%\n')