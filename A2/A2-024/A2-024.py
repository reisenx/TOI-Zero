# Input track length and checkpoint
L, P = map(int, input().split())
# Input jump distance of rabbit, monkey and frog
jump = list(map(int, input().split()))
# Input checkpoints
points = [0] * (L + 1)
for _ in range(P):
    idx, value = map(int, input().split())
    points[idx] = value

# Each animal jump through the track
pos = [0, 0, 0]
total = [0, 0, 0]
for i in range(3):
    # Calculate total points of each animals
    while(pos[i] <= L):
        total[i] += points[pos[i]]
        pos[i] += jump[i]

# Output
ANIMAL = ['Rabbit', 'Monkey', 'Frog']
for i in range(3):
    if(total[i] == max(total)):
        print(ANIMAL[i], total[i])