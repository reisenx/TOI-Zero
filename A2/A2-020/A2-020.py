# Input amount of people
N = int(input())

# Input graph of items flows
graph = [-1] * N
for node_from in range(N):
    node_to = int(input())
    graph[node_from] = node_to - 1

# Find maximum node amount on cycle on a graph
# Every node has 1 in-degree and 1 out-degree
max_cycle_count = 0
is_visited = [False] * N
for start in range(N):
    # Find start node of a cycle
    if(is_visited[start]):
        continue
    
    # Count node on a cycle
    curr = start
    cycle_count = 0
    while(not is_visited[curr]):
        is_visited[curr] = True
        curr = graph[curr]
        cycle_count += 1
    # Find maximum node amount on a cycle
    max_cycle_count = max(max_cycle_count, cycle_count)

# Output maximum node amount on cycle on a graph
print(max_cycle_count)