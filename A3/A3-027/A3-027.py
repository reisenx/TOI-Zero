# Input map dimension
R, C = map(int, input().split())

# Input map
map = [[0] * C for _ in range(R)]
for r in range(R):
    temp = input().strip().split()
    for c in range(C):
        if(temp[c] == '*'):
            map[r][c] = 1

# Flood expands from above
for r in range(R - 1):
    for c in range(C):
        if(map[r][c] == 1 and map[r + 1][c] == 0):
            map[r + 1][c] = 2

# Output
map_after = ''
STATUS = ['- ', '* ', '* ']
for r in range(R):
    for c in range(C):
        map_after += STATUS[map[r][c]]
    map_after += '\n'
print(map_after)