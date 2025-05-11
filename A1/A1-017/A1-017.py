# Input
y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

# Output
date01 = [y1, m1, d1]
date02 = [y2, m2, d2]
if(date01 < date02):
    print(1)
elif(date02 < date01):
    print(2)
else:
    print(0)