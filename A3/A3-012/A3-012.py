# Input student amount and start point
N, S = map(int, input().split())
# Input message forward graph
to_who = []
for i in range(N):
    to_who.append(int(input()) - 1)

# Count student amount who get a message
received = [False] * N
curr = S - 1
ans = 0
while(True):
    # The previous student didn't forward a message
    if(curr == -1):
        break
    # The current student already got a message
    if(received[curr]):
        break
    # The current student received a message
    received[curr] = True
    ans += 1    # Counting...
    # Go to the next student
    curr = to_who[curr]

# Output
print(ans)