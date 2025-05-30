PRICE = {'R':{'S':60, 'M':80, 'L':100},
         'T':{'S':80, 'M':100, 'L':120}}
TOPPING = {'P':15, 'E':10}

# Input ramen information
ramen_size, ramen_type = input().strip().split()
price = PRICE[ramen_type][ramen_size]

# Input topping information
topping = input().strip().split()
if(len(topping) == 2):
    topping_type, topping_amount = topping[0], int(topping[1])
    price += TOPPING[topping_type] * topping_amount

# Output
print(price)