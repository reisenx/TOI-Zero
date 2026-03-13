# --------------------------------------------------
# File Name : A1-030.py
# Problem   : Sum of Max Value in Pairs
# Author    : Worralop Srichainont
# Date      : 2026-03-13
# --------------------------------------------------

# Input amount of pairs, and numbers
n_pairs = int(input())
nums = [int(num) for num in input().split()]

# Variables for displaying the result
sums = 0
max_values_str = []

# Iterate each pair and find the maximum
for i in range(n_pairs):
    # Find max value of the current pair
    max_value = max(nums[2 * i], nums[(2 * i) + 1])

    # Calculate the sum
    sums += max_value

    # Store a number as a string for display
    max_values_str.append(str(max_value))

# Construct the output string
output_str = ""
if n_pairs > 1:
    output_str += f"{' + '.join(max_values_str)} = "
output_str += str(sums)

# Display the output string
print(output_str)
