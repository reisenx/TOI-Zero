# Input task amount
N = int(input())
# Count normal work (<= 18 hours) and hard work (> 18 hours)
normal = 0
hard = 0
for _ in range(N):
    H = int(input())
    if(H <= 18):
        normal += 1
    else:
        hard += 1

# Do hard work, then normal work repeatedly
tasks = min(normal, hard)
ans = tasks * 2
# If normal work still remains
normal -= tasks
ans += normal
# If hard work still remains
hard -= tasks
ans += max(0, (2 * hard) - 1)
# Output
print(ans)