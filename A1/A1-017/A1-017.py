# --------------------------------------------------
# File Name : A1-017.py
# Problem   : Birthday
# Author    : Worralop Srichainont
# Date      : 2026-02-08
# --------------------------------------------------

# Input the first birth date
y1 = int(input())
m1 = int(input())
d1 = int(input())
birth_date_01 = [y1, m1, d1]

# Input the second birth date
y2 = int(input())
m2 = int(input())
d2 = int(input())
birth_date_02 = [y2, m2, d2]

# Output which person is older
if birth_date_01 < birth_date_02:
    print(1)
elif birth_date_02 < birth_date_01:
    print(2)
else:
    print(0)
