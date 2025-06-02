# Input
N, W, L = map(int, input().split())

# Input position of the hole
woods = [[False] * W for _ in range(N)]
for i in range(N):
    holes = list(map(int, input().split()))
    holes = holes[1:]
    # Mark [hole - L, hole + L] as a hole
    for hole in holes:
        for dl in range(-L, L + 1):
            if(0 <= hole + dl < W):
                woods[i][hole + dl] = True

# Check hold on all woods
hasAllHoles = True
for x in range(W):
    hasAllHoles = True
    for i in range(N):
        if(not woods[i][x]):
            hasAllHoles = False
            break
    if(hasAllHoles):
        break

# Output
if(hasAllHoles):
    print(1)
else:
    print(0)