# Input dishes and find frequency of each dish size
freq = [0] * 305
maxFreq = 0
n = int(input())
for _ in range(n):
    dish = int(input())
    freq[dish] += 1
    maxFreq = max(maxFreq, freq[dish])
# Output
print(maxFreq)