# Input number of scores
N = int(input())
# Find maximum score and count them
max_score = 0
max_count = 0
for _ in range(N):
    score = int(input())
    if(score == max_score):
        max_count += 1
    elif(score > max_score):
        max_score = score
        max_count = 1
# Output
print(max_score)
print(max_count)