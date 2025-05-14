# Input trees height
n = int(input())
trees = list(map(int, input().split()))

# Count amount of trees that has no taller adjacent trees
ans = 0
if(trees[0] >= trees[1]):
    ans += 1
for i in range(1, n - 1):
    if(trees[i] >= trees[i - 1] and trees[i] >= trees[i + 1]):
        ans += 1
if(trees[n - 1] >= trees[n - 2]):
    ans += 1

# Output
print(ans)