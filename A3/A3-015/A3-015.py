# Input pillar amount
N = int(input())
# Input pillar length
pillars = []
for _ in range(N):
    pillars.append(int(input()))

# Sort pillars length in ascending order
pillars.sort()
# Calculate total distance
curr = 0
dist = 0
for L in pillars:
    curr += L           # Calculate current total pillar length
    dist += curr * 2    # Calculate total distance
# Output
print(dist)