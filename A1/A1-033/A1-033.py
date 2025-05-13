# Input
n = int(input())
cnt = 0
for i in range(n):
    letter = input()
    # Count vowels
    if(letter in ['A', 'E', 'I', 'O', 'U']):
        cnt += 1
# Output
print(cnt)