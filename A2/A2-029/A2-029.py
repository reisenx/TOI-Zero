# Input triangle height
N = int(input())

# Construct upper part of the triangle
triangle = ''
for i in range(1, N):
    # Left border
    line = '0 '
    # Middle part
    line += '1 ' * max(0, i - 2)
    # Right border
    if(i - 1 > 0):
        line += '0 '
    # Add to the triangle
    triangle += line + '\n'
# Construct base of the triangle
triangle += '0 ' * N

# Output
print(triangle)