BOBA_CALORIES = {'H':5, 'O':3, 'J':2}
TEA_CALORIES  = {'R':[12, 18, 25],
                 'T':[15, 20, 30],
                 'M':[10, 15, 20]}
total = 0

# Input boba details
data = input().split()
boba_type, boba_amount = data[0], int(data[1])
total += BOBA_CALORIES[boba_type] * boba_amount

# Input tea details
data = input().split()
tea_type, tea_sweet, tea_amount = data[0], int(data[1]), int(data[2])
total += TEA_CALORIES[tea_type][tea_sweet - 1] * tea_amount

# Output
print(total)