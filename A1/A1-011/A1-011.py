# Input
text = input()
# Output
letter = text[0]
cnt = 1
for i in range(1, len(text)):
    # Count if it is the same letter
    if(text[i] == letter):
        cnt += 1
    # Otherwise, output and change to the new letter
    else:
        print(str(cnt) + letter, end = '')
        letter = text[i]
        cnt = 1
# Don't forget to output the last one
print(str(cnt) + letter)