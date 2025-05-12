# Input
text = input()
# Count vowel letters
cnt = 0
for char in text:
    if(char in ['a', 'e', 'i', 'o', 'u']):
        cnt += 1
# Output
print(cnt)