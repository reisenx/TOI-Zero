# Input
letter = input()
num = input()
# Output
if(letter == "H" and num == "4567"):
    print("safe unlocked")
elif(letter == "H"):
    print("safe locked - change digit")
elif(num == "4567"):
    print("safe locked - change char")
else:
    print("safe locked")