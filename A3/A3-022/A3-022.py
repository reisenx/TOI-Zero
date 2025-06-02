# Input light interval and mark as lighted
N = int(input())

degree = [False] * 360
for _ in range(N):
    A, B = map(int, input().split())
    if(A > B):
        B += 360
    
    for i in range(A, B):
        if(not degree[i % 360]):
            degree[i % 360] = True

# Find maximum lighted interval
# Case 1: Maximum interval is [A, B] when A < B
degree_count = 0
max_degree_count = 0
for i in range(360):
    if(degree[i]):
        degree_count += 1
    else:
        max_degree_count = max(max_degree_count, degree_count)
        degree_count = 0
max_degree_count = max(max_degree_count, degree_count)

# Case 2: Maximum interval is [A, B] when A > B
if(max_degree_count < 360):
    A = 359
    while(degree[A]):
        A -= 1
    B = 0
    while(degree[B]):
        B += 1
    degree_count = (B + 360) - A - 1
max_degree_count = max(max_degree_count, degree_count)

# Output
print(max_degree_count)