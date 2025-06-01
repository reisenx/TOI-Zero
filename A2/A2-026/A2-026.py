# Input rabbit numbers
N = int(input())

# Input rabbit name and weight
rabbits = []
fat_count = 0
for _ in range(N):
    name, weight = input().strip().split()
    rabbit = [int(weight), name]
    rabbits.append(rabbit)
    # Count fat rabbits
    if(int(weight) > 15):
        fat_count += 1

# Sort rabbit by weights in descending order
rabbits.sort(reverse = True)

# Output
print(fat_count)
print(rabbits[0][1], rabbits[0][0])