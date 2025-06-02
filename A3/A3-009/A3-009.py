# Input amount of customer of pods
N, K = map(int, input().split())

# Input queue line of each customer
total_customer = 0
has_customer = 0
queue = [0] * K
for _ in range(N):
    # Input queue line
    line = int(input()) - 1
    # Update total customer
    total_customer += 1
    # Update queue line amount that has customer
    if(queue[line] == 0):
        has_customer += 1
    # Assign a customer to a queue
    queue[line] += 1
    
    # Check if the customer are ready to get into a pod
    if(has_customer == K):
        # Update all queue lines
        for i in range(K):
            queue[i] -= 1       # Remove a customer from a queue
            total_customer -= 1 # Update total customer
            # Update queue line amount that has customer
            if(queue[i] == 0):
                has_customer -= 1
# Output
print(total_customer)