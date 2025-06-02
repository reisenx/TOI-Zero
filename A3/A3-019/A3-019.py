# Input customer amount and extra customer amount
N, L = map(int, input().split())
# Input height of each customer
heights = list(map(int, input().split()))
# Input index of extra customer
extra = [int(idx) - 1 for idx in input().split()]

# Output
max_height = 0
idx = 0
for i in range(N):
    # Skip, if no more extra customer
    if(idx >= L):
        continue
    # Current customer is the tallest
    if(heights[i] > max_height):
        max_height = heights[i]
        # The extra customer is the tallest
        if(i == extra[idx]):
            print(0)
            idx += 1
    # The extra customer is not the tallest
    elif(i == extra[idx]):
        print((max_height + 1) - heights[i])
        idx += 1