# Input
width, height, level = map(int, input().split())
price_per_meter = int(input())
# Calculate total fence length and price
length = (2 * (width + height)) * level
price = length * price_per_meter
# Output
print(length)
print(price)