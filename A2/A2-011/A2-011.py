# Input numbers
nums = list(map(int, input().split()))
# Output unique number
unique = set()
for num in nums:
    if(num not in unique):
        print(num, end = ' ')
        unique.add(num)