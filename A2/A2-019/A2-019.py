# Input string
txt = input().strip()

# Find first appearance of 'B'
firstB = txt.upper().find('B')

# Find the most consecutive 'U' in a string
idx = 0
consecutive_u = 0
max_consecutive_u = 0
while(True):
    # Find appearance of 'BUU' start at idx + 3
    idx = txt.upper().find('BUU', idx)
    # 'BUU' not found, stop the process
    if(idx == -1):
        break
    # 'BUU' found, count consecutive 'U'
    for i in range(idx + 1, len(txt)):
        if(txt[i].upper() == 'U'):
            consecutive_u += 1
        else:
            break
    # Find maximum consecutive 'U'
    max_consecutive_u = max(max_consecutive_u, consecutive_u)
    consecutive_u = 0
    # Shift idx by 3
    idx += 3

# Output (Has 'BUU')
if(max_consecutive_u > 1):
    print('Yes', max_consecutive_u)
# Output (Has no 'BUU', but has 'B')
elif(firstB != -1):
    # Output same letter until the first 'B', then spams 'U'
    print(txt[:firstB + 1] + ('U' * (len(txt) - firstB - 1)))
# Output (Has no 'BUU' nor 'B')
else:
    # Output 'BUU' in loop
    print(('BUU' * ((len(txt) // 3) + 1))[:len(txt)])