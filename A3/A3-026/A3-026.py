# Input images dimension
R, C = map(int, input().split())

# Input images
images = []
for i in range(2):
    img = []
    for r in range(R):
        row = []
        for char in input().strip():
            if(char == '-'):
                row.append(0)
            if(char == '+'):
                row.append(1)
            if(char == 'x'):
                row.append(2)
        img.append(row)
    images.append(img)

# Output overlapped images
overlapped_img = ''
SYMBOLS = ['-', '+', 'x', '*']
for r in range(R):
    for c in range(C):
        s1 = images[0][r][c]
        s2 = images[1][r][c]
        # Both image has the same symbol
        if(s1 == s2):
            overlapped_img += SYMBOLS[s1]
        # Both image has different symbol
        else:
            overlapped_img += SYMBOLS[s1 + s2]
    overlapped_img += '\n'
print(overlapped_img)