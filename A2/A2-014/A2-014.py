# Input names and lowercase them
name01 = input().strip().lower()
name02 = input().strip().lower()

# Initialize a talisman
talisman = ""
talisman_size = max(len(name01), len(name02))
w_count = 0
w_consecutive = 0
w_max_consecutive = 0

# Add '$' and 'w' to a talisman
for i in range(talisman_size):
    # Add 'w' when a letter contains 'l', 'o', 'v' or 'e'
    c1 = name01[i % len(name01)] in ['l', 'o', 'v', 'e']
    c2 = name02[i % len(name02)] in ['l', 'o', 'v', 'e']
    if(c1 or c2):
        talisman += 'w'
        # Count amount of 'w' and consecutive 'w'
        w_count += 1
        w_consecutive += 1
    # Otherwise, add '$'
    else:
        talisman += '$'
        # Find maximum consecutive 'w' and reset consecutive counter
        w_max_consecutive = max(w_max_consecutive, w_consecutive)
        w_consecutive = 0
# Don't forget to find maximum consecutive 'w' once again
w_max_consecutive = max(w_max_consecutive, w_consecutive)

# Add maximum consecutive 'w' at the end, if w amount is odd
if(w_count % 2 == 1):
    talisman += str(w_max_consecutive)
# Add '#' if maximum consecutive is less than 2 and w amount is even
elif(w_max_consecutive < 2):
    talisman += '#'

# Output
print(talisman)