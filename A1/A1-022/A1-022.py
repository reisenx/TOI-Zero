# Input
day = int(input())
month = int(input())
# Output
date = [month, day]
if(date <= [1, 19]):
    print("capricorn")
elif(date <= [2, 18]):
    print("aquarius")
elif(date <= [3, 20]):
    print("pisces")
elif(date <= [4, 19]):
    print("aries")
elif(date <= [5, 20]):
    print("taurus")
elif(date <= [6, 21]):
    print("gemini")
elif(date <= [7, 22]):
    print("cancer")
elif(date <= [8, 22]):
    print("leo")
elif(date <= [9, 22]):
    print("virgo")
elif(date <= [10, 23]):
    print("libra")
elif(date <= [11, 21]):
    print("scorpio")
elif(date <= [12, 21]):
    print("sagittarius")
else:
    print("capricorn")