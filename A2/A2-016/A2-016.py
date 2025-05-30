PRIZE = [[100000, 200, 100, 0],
         [1000000, 2000, 1000, 20]]
# Input lottery and its result
lottery = input().strip()
result = input().strip()

# Check letter part
type01 = int(lottery[0] == result[0])
# Check number part
type02 = 3
if(lottery[2:] == result[2:]):
    type02 = 0
elif(lottery[4:] == result[4:]):
    type02 = 1
elif(lottery[5:] == result[5:]):
    type02 = 2

# Output
print(PRIZE[type01][type02])