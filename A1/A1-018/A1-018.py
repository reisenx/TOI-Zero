# Input
num = int(input())

# Output
roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
if(1 <= num <= 9):
    print(roman[num - 1])
elif(num < 0):
    print("Error : Please input positive number")
else:
    print("Error : Out of range")