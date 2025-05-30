COLORS = ["Red", "Green", "Blue"]
INITIAL = {'R':0, 'G':1, 'B':2}

# Input initial color and length
letter, length = input().strip().split()
idx = INITIAL[letter]
# Output
for step in range(int(length)):
    print(COLORS[idx], end = ' ')
    idx = (idx + 1) % 3