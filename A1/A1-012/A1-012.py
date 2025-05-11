# Input
num01 = int(input())
operation = input()
# Reverse a number
num02 = int(str(num01)[::-1])
# Output
if(operation == '+'):
    print(num01, '+', num02, '=', num01 + num02)
elif(operation == '*'):
    print(num01, '*', num02, '=', num01 * num02)
