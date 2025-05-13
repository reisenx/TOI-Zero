# Fruits calories
CALORIES = [100, 120, 200, 60]

# Input orders until exits
total_calories = 0
order = int(input())
while(order != 5):
    total_calories += CALORIES[order - 1]
    order = int(input())

# Output
print("Bye Bye")
print("Total Calories:", total_calories)