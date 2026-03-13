# --------------------------------------------------
# File Name : A1-070.py
# Problem   : Smart Trash Collector
# Author    : Worralop Srichainont
# Date      : 2026-01-05
# --------------------------------------------------

# Read the number of trash bins
trash_bins = int(input().strip())

# Process each trash bin
for _ in range(trash_bins):
    # Read the amounts of plastic, can, and glass
    plastic, can, glass = map(float, input().strip().split())

    # Calculate total trash
    total_trash = plastic + can + glass

    # Construct the result string
    result = f"{total_trash:.1f}"

    # Check for overload trash
    if total_trash > 50.0:
        result += ",Overloaded"

    # Check for type-specific overloads
    if plastic > 20.0:
        result += ",Check Type Plastic"

    if can > 20.0:
        result += ",Check Type Can"

    if glass > 20.0:
        result += ",Check Type Glass"

    # Print the result for the current trash bin
    print(result)
