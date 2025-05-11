# Input
temp = int(input())
unit = input()
# Output
if(unit.upper() == 'C'):
    if(temp <= 0):
        print("solid")
    if(0 < temp < 100):
        print("liquid")
    if(temp >= 100):
        print("gas")
if(unit.upper() == 'F'):
    if(temp <= 32):
        print("solid")
    if(32 < temp < 212):
        print("liquid")
    if(temp > 212):
        print("gas")