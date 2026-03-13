# --------------------------------------------------
# File Name : A1-053.py
# Problem   : RGB Mixed
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------


# Function to mix two color components
def mix_color(c1, c2):
    return (c1 + c2) // 2


# Function to mix two RGB colors
def mix_rgb(r1, g1, b1, r2, g2, b2):
    r = mix_color(r1, r2)
    g = mix_color(g1, g2)
    b = mix_color(b1, b2)
    return r, g, b


# Main function
def main():
    r1, g1, b1 = map(int, input().split())
    r2, g2, b2 = map(int, input().split())

    r, g, b = mix_rgb(r1, g1, b1, r2, g2, b2)
    print(r, g, b)


# Run the main function
main()
