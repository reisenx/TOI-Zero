# Input
first_name = input()
last_name = input()
age = input()
# Output
if(len(first_name) > 5 and len(last_name) > 5):
    print(first_name[:2] + last_name[-1] + age[-1])
else:
    print(first_name[0] + age + last_name[-1])