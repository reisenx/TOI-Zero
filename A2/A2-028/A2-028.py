# Input id and its length
N = int(input())
id01 = input().strip()
id02 = input().strip()
# Consider the sum of each digits
cnt = 0
for i in range(N):
    # Calculate sum of digits
    sum = int(id01[i]) + int(id02[i])
    # Count amount of digits which the sum is not 9
    if(sum != 9):
        cnt += 1
# Output
if(cnt > 0):
    print("NO", cnt)
else:
    print("YES")