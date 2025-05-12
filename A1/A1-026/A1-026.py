# Input
a = int(input())
b = int(input())
c = int(input())

# Count odd numbers
odd = (a % 2) + (b % 2) + (c % 2)

# Output
print("even", 3 - odd)
print("odd", odd)