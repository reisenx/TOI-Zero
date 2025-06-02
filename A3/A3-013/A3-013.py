# Input mountain amount and road length
N, S = map(int, input().split())

# Calculate distance on a road
min_dist = S
max_dist = S
for _ in range(N):
    # Input mountain height
    H = int(input())
    # Can be either type 1 or 2 mountain
    if(H % 12 == 0):
        min_dist -= (H // 3) * 10
        max_dist -= (H // 4) * 10
    elif(H % 3 == 0):
        min_dist -= (H // 3) * 10
        max_dist -= (H // 3) * 10
    elif(H % 4 == 0):
        min_dist -= (H // 4) * 10
        max_dist -= (H // 4) * 10

# Output
print(min_dist, max_dist)