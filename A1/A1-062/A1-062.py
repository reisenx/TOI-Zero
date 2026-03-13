# --------------------------------------------------
# File Name : A1-062.py
# Problem   : Primes in Range
# Author    : Worralop Srichainont
# Date      : 2026-01-02
# --------------------------------------------------

# Read finding range
start, stop = map(int, input().strip().split())

# Sieve of Eratosthenes to find all primes in the range
is_prime = [True] * (stop + 1)
is_prime[:2] = [False, False]

for i in range(2, int(stop**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, stop + 1, i):
            is_prime[j] = False

# Collect all primes in the specified range
primes = []
for num in range(start, stop + 1):
    if is_prime[num]:
        primes.append(str(num))

# Output the primes and their count
print(" ".join(primes))
print(f"Total primes: {len(primes)}")
