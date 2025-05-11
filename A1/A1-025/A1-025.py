# Data Preparation
NUMS = {'A':'ace', 'J':'jack', 'Q':'queen', 'K':'king'}
GROUPS = {'D':'diamonds', 'H':'hearts', 'S':'spades', 'C':'clubs'}

# Input
card = input()

# Find card name
card = card.upper()
num = card[:-1]
group = card[-1]

card_name = ""
if(num in NUMS):
    card_name += NUMS[num]
else:
    card_name += num
card_name += " of " + GROUPS[group]

# Output
print(card_name)