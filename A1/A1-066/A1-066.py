# --------------------------------------------------
# File Name : A1-066.py
# Problem   : Jumping Frog
# Author    : Worralop Srichainont
# Date      : 2026-01-03
# --------------------------------------------------

# Initialize position and jump count
current_position = 0
jump_amount = 0

# Read jump distance and goal position from input
jump_distance, goal = map(int, input().strip().split())

# Simulate jumps
while jump_distance > 0:
    # Stop if the goal is reached
    if current_position >= goal:
        break

    # Update position and jump count
    current_position += jump_distance
    jump_amount += 1

    # Decrease jump distance for the next jump
    jump_distance -= 2

# Output the result
if current_position >= goal:
    print(jump_amount)
else:
    print(-1)
