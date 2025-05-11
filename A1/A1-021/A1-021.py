# Input
year = int(input())
# Output
if(year < 1582):
    print("yes")
elif(year % 400 == 0):
    print("yes")
elif(year % 4 == 0 and year % 100 != 0):
    print("yes")
else:
    print("no")