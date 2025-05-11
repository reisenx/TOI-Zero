# Input
age = int(input())
type = input()

# Output
if(age < 18 or type.lower() == 's'):
    print(20)
else:
    print(50)