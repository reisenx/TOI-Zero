# Input string and made it all lowercase
txt = input().strip().lower()

# Consider string
consecutive_a = 0
max_consecutive_a = 0
is_unknown = True
is_rabbit = True

for i in range(len(txt)):
    # A character that isn't 'i' and 't' detected
    if(is_unknown and txt[i] not in ['i', 't']):
        is_unknown = False

    # After 'r' must be 'a'
    if(txt[i] == 'r'):
        # 'r' is the last character or after 'r' is not 'a'
        if(i + 1 == len(txt) or txt[i + 1] != 'a'):
            if(i + 1 == len(txt)):
                print("no", i)
            else:
                print("no", i + 1)
            is_rabbit = False
            break

    # Before 'a' must be 'r' or 'a'
    if(txt[i] == 'a'):
        consecutive_a += 1  # Count consecutive 'a'
        # 'a' is the first character or before 'a' is not 'r' or 'a'
        if(i == 0 or txt[i - 1] not in ['r', 'a']):
            print("no", i)
            is_rabbit = False
            break
    # Reset consecutive 'a' counter
    else:
        max_consecutive_a = max(max_consecutive_a, consecutive_a)
        consecutive_a = 0

    # After 'b' must be 'i' or 't'
    if(txt[i] == 'b'):
        # 'b' is the last character or after 'b' is not 'i'
        if(i + 1 == len(txt) or txt[i + 1] not in ['i', 't']):
            if(i + 1 == len(txt)):
                print("no", i)
            else:
                print("no", i + 1)
            is_rabbit = False
            break

# Don't forget to find maximum consecutive once again
max_consecutive_a = max(max_consecutive_a, consecutive_a)

# Output
if(is_unknown):
    print("unknown", len(txt))
elif(is_rabbit):
    print("yes", max_consecutive_a)