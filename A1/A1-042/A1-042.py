# --------------------------------------------------
# File Name : A1-042.py
# Problem   : Festival
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Define movement directions
DIRECTIONS = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

# Initialize starting position
position = [0, 0]

# Read walking path input
walking_path = input().strip().upper()

# Process each step in the walking path
for step in walking_path:
    # Update position based on direction
    position[0] += DIRECTIONS[step][0]
    position[1] += DIRECTIONS[step][1]

# Calculate Manhattan distance from origin
distance = abs(position[0]) + abs(position[1])

# Output final position and distance
print(position[0], position[1], distance)
