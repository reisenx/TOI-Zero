# Input
N, K, T = map(int, input().split())

# Pass the box to next K person (starts at person number 1)
# Note that person number N is in index 0
received = [False] * N
received[1] = True
ans = 1
curr = (1 + K) % N
while(ans < N):
    # Current person has not received the box yet
    if(not received[curr]):
        received[curr] = True
        ans += 1
    # The box come back to person number 1
    if(curr == 1):
        break
    # The box is in the thief hands
    if(curr == (T % N)):
        break
    # Pass to the next person
    curr = (curr + K) % N

# Output
print(ans)