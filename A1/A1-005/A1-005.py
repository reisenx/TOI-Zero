# Input date
month = int(input())
day = int(input())
# Output
date = [month, day]
if(date < [3, 21]):
    print("winter")
elif(date < [6, 21]):
    print("spring")
elif(date < [9, 21]):
    print("summer")
elif(date < [12, 21]):
    print("fall")
else:
    print("winter")