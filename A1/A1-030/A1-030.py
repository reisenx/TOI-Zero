# Input amount of pairs, and numbers
n = int(input())
nums = [int(num) for num in input().split()]

# Find maximum number of each pair
ans = []
for i in range(n):
    ans.append(max(nums[2 * i], nums[(2 * i) + 1]))

# Output
if(n == 1):
    print(ans[0])
else:    
    for i in range(n):
        # Output number
        print(ans[i], end = ' ')
        # Output operator
        if(i < n - 1):
            print('+', end = ' ')
        else:
            print('=', end = ' ')
    # Output sum
    print(sum(ans))