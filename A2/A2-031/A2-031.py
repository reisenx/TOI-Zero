# Input DNA
N = int(input())
DNA = []
DNA.append(input().strip().split())
DNA.append(input().strip().split())

# Change DNA lines
M = int(input())
for _ in range(M):
    line, pos, gene = input().strip().split()
    line, pos = int(line) - 1, int(pos)
    DNA[line][pos] = gene

# Output new DNA lines
print(' '.join(DNA[0]))
print(' '.join(DNA[1]))

# Count matched gene pair
cnt = 0
for i in range(N):
    if(DNA[0][i] == 'A' and DNA[1][i] == 'T'):
        cnt += 1
    if(DNA[0][i] == 'T' and DNA[1][i] == 'A'):
        cnt += 1
    if(DNA[0][i] == 'C' and DNA[1][i] == 'G'):
        cnt += 1
    if(DNA[0][i] == 'G' and DNA[1][i] == 'C'):
        cnt += 1

# Output unmatched gene pair
print(N - cnt)