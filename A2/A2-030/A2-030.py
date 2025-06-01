# Input 5 x 5 array
arr = [[0, 0, 0, 0, 0] for _ in range(5)]
row = [0, 0, 0, 0, 0]
col = [0, 0, 0, 0, 0]
for i in range(5):
    j = 0
    for num in input().strip().split():
        arr[i][j] = int(num)
        # Calculate row and column sum
        row[i] += arr[i][j]
        col[j] += arr[i][j]
        j += 1

# Find row and column that has odd sum
r = -1
c = -1
for i in range(5):
    if(row[i] % 2 == 1):
        r = i
    if(col[i] % 2 == 1):
        c = i

# Output
print(r, c)