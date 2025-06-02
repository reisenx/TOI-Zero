# Calculate oranges amount on each layer
oranges = [0]
for i in range(1, 101):
    oranges.append(oranges[-1] + (i ** 2))

# Get the layer number by orange amount using binary search
def get_orange_layer(N:int) -> int:
    low, high = 0, 100
    layer = -1
    while(low <= high):
        mid = (low + high) // 2
        if(oranges[mid] == N):
            layer = mid
            break
        elif(oranges[mid] < N):
            layer = mid
            low = mid + 1
        else:
            high = mid - 1
    return layer

# Input layer and orange amount
L, N = map(int, input().split())
# Output
# 1. Find layer number of oranges that taken off
# 2. Calculate [total layers - taken off layers]
print(L - get_orange_layer(N))