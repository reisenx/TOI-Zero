# --------------------------------------------------
# File Name : A1-060.py
# Problem   : Gift Paper
# Author    : Worralop Srichainont
# Date      : 2026-01-02
# --------------------------------------------------

# Read input values
radius, height, glue_section = map(float, input().split())

# Calculate gift paper dimensions
gift_paper_width = (2 * radius) + height
gift_paper_height = (2 * 3.14 * radius) + glue_section

# Print the result with two decimal places
print(f"{gift_paper_width:.2f} {gift_paper_height:.2f}")
